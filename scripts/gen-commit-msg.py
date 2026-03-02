#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import subprocess
import sys
from typing import Any


def fail(message: str, *, details: str | None = None, code: int = 1) -> None:
    print(message, file=sys.stderr)
    if details:
        print(details, file=sys.stderr)
    raise SystemExit(code)


def run_cmd(
    args: list[str], *, input_text: str | None = None
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, input=input_text, capture_output=True, text=True)


def normalize_commit_message(text: str) -> str:
    lines = text.splitlines()

    first_non_empty_index = None
    for index, line in enumerate(lines):
        if line.strip():
            first_non_empty_index = index
            break

    if first_non_empty_index is None:
        return ""

    subject = lines[first_non_empty_index].strip()
    if (
        (subject.startswith('"') and subject.endswith('"'))
        or (subject.startswith("'") and subject.endswith("'"))
    ) and len(subject) >= 2:
        subject = subject[1:-1].strip()

    remaining_lines = lines[first_non_empty_index + 1 :]
    while remaining_lines and not remaining_lines[-1].strip():
        remaining_lines.pop()

    return "\n".join([subject, *remaining_lines]).strip()


def pick_error_message(err_obj: Any) -> str | None:
    if not isinstance(err_obj, dict):
        return None

    message = err_obj.get("message")
    if isinstance(message, str) and message.strip():
        return message.strip()

    data = err_obj.get("data")
    if isinstance(data, dict):
        data_message = data.get("message")
        if isinstance(data_message, str) and data_message.strip():
            return data_message.strip()

        response_body = data.get("responseBody")
        if isinstance(response_body, str) and response_body.strip():
            try:
                nested = json.loads(response_body)
            except Exception:
                nested = None

            if isinstance(nested, dict):
                nested_error = nested.get("error")
                if isinstance(nested_error, dict):
                    nested_message = nested_error.get("message")
                    if isinstance(nested_message, str) and nested_message.strip():
                        return nested_message.strip()

            return response_body.strip()

    return None


def parse_opencode_json(raw_text: str) -> tuple[str, list[str]]:
    parts: list[str] = []
    errors: list[str] = []

    for raw_line in raw_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        try:
            obj = json.loads(line)
        except Exception:
            continue

        event_type = obj.get("type")
        if event_type == "text":
            text = (obj.get("part") or {}).get("text")
            if isinstance(text, str) and text:
                parts.append(text)
        elif event_type == "error":
            msg = pick_error_message(obj.get("error"))
            if msg:
                errors.append(msg)

    return "\n".join(parts), errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a commit message from staged changes and optionally commit."
    )
    parser.set_defaults(create_commit=True)

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--create-commit",
        dest="create_commit",
        action="store_true",
        help="Create a git commit after generating the message (default).",
    )
    group.add_argument(
        "--no-create-commit",
        dest="create_commit",
        action="store_false",
        help="Only print the generated commit message.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    opencode_bin = os.environ.get("OPENCODE_BIN", "opencode")
    opencode_model = os.environ.get("OPENCODE_MODEL", "openai/gpt-5.1-codex-mini")

    git_check = run_cmd(["git", "rev-parse", "--git-dir"])
    if git_check.returncode != 0:
        fail("Error: not inside a git repository.")

    if shutil.which(opencode_bin) is None:
        fail(f"Error: '{opencode_bin}' not found in PATH.")

    staged_check = run_cmd(["git", "diff", "--cached", "--quiet"])
    if staged_check.returncode == 0:
        fail("Error: no staged changes found.")
    if staged_check.returncode not in (0, 1):
        details = (staged_check.stderr or staged_check.stdout).strip() or None
        fail("Error: failed to inspect staged changes.", details=details)

    staged_files = run_cmd(["git", "diff", "--cached", "--name-only"])
    if staged_files.returncode != 0:
        details = (staged_files.stderr or staged_files.stdout).strip() or None
        fail("Error: failed to list staged files.", details=details)

    staged_patch = run_cmd(["git", "diff", "--cached", "--no-color", "--minimal"])
    if staged_patch.returncode != 0:
        details = (staged_patch.stderr or staged_patch.stdout).strip() or None
        fail("Error: failed to read staged diff.", details=details)

    prompt = f"""Generate a concise git commit message for these staged changes.

Rules:
- Output ONLY the commit message text.
- No markdown, no quotes, no code fences.
- Prefer conventional commit style when appropriate. Do not add scope.
- Keep subject <= 72 chars.
- If useful, include a blank line and short body (max 2 bullets).

Staged files:
{staged_files.stdout}

Staged diff:
{staged_patch.stdout}
"""

    cmd = [opencode_bin, "run", "--format", "json"]
    if opencode_model:
        cmd.extend(["--model", opencode_model])
    cmd.append(prompt)

    opencode = run_cmd(cmd)
    raw_output = "\n".join(part for part in (opencode.stdout, opencode.stderr) if part)

    parsed_text, errors = parse_opencode_json(raw_output)

    if errors:
        fail("Error: opencode returned an error.", details="\n".join(errors))

    if opencode.returncode != 0:
        details = raw_output.strip() or None
        fail("Error: opencode failed to generate a commit message.", details=details)

    commit_message = normalize_commit_message(parsed_text)
    if not commit_message:
        fail("Error: model returned empty commit message.")

    if args.create_commit:
        commit = run_cmd(["git", "commit", "--file", "-"], input_text=commit_message)
        if commit.returncode != 0:
            details = (commit.stderr or commit.stdout).strip() or None
            fail("Error: failed to create commit.", details=details)
        output = commit.stdout.strip() or commit_message.splitlines()[0]
        print(output)
        return

    print(commit_message)


if __name__ == "__main__":
    main()
