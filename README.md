This repository contains agent skills in the `skills/` directory, it's compatible with Claude and Opencode.

## Skills Summary

- `skills/convex`: Convex development guidelines covering schema design, validators, queries, mutations, actions, and HTTP endpoints.
- `skills/polars`: Example-driven Polars DataFrame workflows for eager and lazy pipelines, expressions, joins, and aggregation.
- `skills/frontend-design`: High-quality frontend design playbook for building distinctive, production-ready interfaces.
- `skills/typst`: Comprehensive Typst guide for document creation, styling, templates, troubleshooting, and utilities.
- `skills/webapp-testing`: Playwright-based toolkit for local web app testing, server orchestration, and debugging workflows.

## Install

From the repository root:

```bash
./scripts/install-skills.sh
```

Optional custom target directory:

```bash
./scripts/install-skills.sh ~/.opencode/skills
```


## Verify links

```bash
ls -la ~/.claude/skills
```

You should see each entry pointing to the corresponding directory in this repository.

## Notes

- `ln -sfn` safely replaces existing links.
- Reference: https://opencode.ai/docs/skills/
