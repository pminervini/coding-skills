#!/usr/bin/env python3
"""
Typst Document Utility Script
Provides common operations for Typst documents: validation, conversion, template generation
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Optional, List, Dict


class TypstValidator:
    """Validates Typst document structure and syntax."""
    
    @staticmethod
    def validate_document(filepath: str) -> Dict[str, any]:
        """Validate a Typst document and return issues found."""
        issues = {
            "errors": [],
            "warnings": [],
            "info": []
        }
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            issues["errors"].append(f"File not found: {filepath}")
            return issues
        
        # Check for common issues
        TypstValidator._check_syntax(content, issues)
        TypstValidator._check_structure(content, issues)
        TypstValidator._check_references(content, issues)
        TypstValidator._check_math_mode(content, issues)
        
        return issues
    
    @staticmethod
    def _check_syntax(content: str, issues: Dict) -> None:
        """Check for syntax issues."""
        lines = content.split('\n')
        
        # Check for unclosed brackets
        bracket_pairs = {'[': ']', '{': '}', '(': ')'}
        for open_char, close_char in bracket_pairs.items():
            opens = content.count(open_char)
            closes = content.count(close_char)
            if opens != closes:
                issues["warnings"].append(
                    f"Mismatched brackets: {opens} '{open_char}' vs {closes} '{close_char}'"
                )
        
        # Check for unclosed math mode
        math_opens = len(re.findall(r'(?<!\\)\$(?!\$)', content)) // 2
        if len(re.findall(r'(?<!\\)\$(?!\$)', content)) % 2 != 0:
            issues["warnings"].append("Unclosed math mode ($)")
        
        # Check for common typos in functions
        suspicious_patterns = [
            (r'#let\s+(\w+)\s*=\s*$', "Incomplete #let statement"),
            (r'#set\s+(\w+)\((?!.*\))', "Unclosed #set statement"),
            (r'#if\s+(?!.*\[)', "Conditional without content block"),
        ]
        
        for pattern, message in suspicious_patterns:
            if re.search(pattern, content, re.MULTILINE):
                issues["warnings"].append(message)
    
    @staticmethod
    def _check_structure(content: str, issues: Dict) -> None:
        """Check document structure."""
        # Check for heading hierarchy violations
        headings = re.findall(r'^(=+)\s+(.+)$', content, re.MULTILINE)
        if headings:
            prev_level = 0
            for level_str, heading_text in headings:
                level = len(level_str)
                if level > prev_level + 1:
                    issues["warnings"].append(
                        f"Heading hierarchy skip: from level {prev_level} to {level} "
                        f"at '{heading_text}'"
                    )
                prev_level = level
        
        # Check for orphaned labels
        labels = re.findall(r'<(\w+)>', content)
        references = re.findall(r'@(\w+)', content)
        
        orphaned = set(labels) - set(references)
        if orphaned:
            issues["info"].append(f"Unused labels: {', '.join(orphaned)}")
        
        missing = set(references) - set(labels)
        if missing:
            issues["errors"].append(f"Missing labels: {', '.join(missing)}")
    
    @staticmethod
    def _check_references(content: str, issues: Dict) -> None:
        """Check bibliography and references."""
        # Look for bibliography function
        if re.search(r'#bibliography\(', content):
            bib_match = re.search(r'#bibliography\("([^"]+)"', content)
            if bib_match:
                bib_file = bib_match.group(1)
                if not os.path.exists(bib_file):
                    issues["errors"].append(f"Bibliography file not found: {bib_file}")
        
        # Check for unused citations
        citations = re.findall(r'@(\w+)', content)
        if not re.search(r'#bibliography', content) and citations:
            issues["warnings"].append(
                f"Citations found ({', '.join(set(citations))}) but no #bibliography() call"
            )
    
    @staticmethod
    def _check_math_mode(content: str, issues: Dict) -> None:
        """Check mathematics mode syntax."""
        math_blocks = re.findall(r'\$(.+?)\$', content, re.DOTALL)
        
        for math_expr in math_blocks:
            # Check for common LaTeX mistakes in Typst
            if '\\' in math_expr and not any(cmd in math_expr for cmd in ['frac', 'sqrt', 'sum']):
                issues["warnings"].append(
                    f"LaTeX syntax in math mode: {math_expr[:30]}... "
                    "(Typst uses different syntax than LaTeX)"
                )


class TypstTemplateGenerator:
    """Generate template documents for common use cases."""
    
    TEMPLATES = {
        "blank": """#set page(paper: "a4", margin: 2cm)
#set text(font: "Times New Roman", size: 12pt)

= Title

Your content here...
""",
        "article": """#set page(paper: "a4", margin: 2.5cm)
#set text(font: "Times New Roman", size: 12pt, lang: "en")
#set par(justify: true, first-line-indent: 1.2em)

#align(center)[
  #text(size: 18pt, weight: "bold")[Article Title]
  
  Author Name
  
  #datetime.today().display()
]

= Introduction

Introduction content...

= Main Section

Main section content...

= Conclusion

Conclusion...

#bibliography("references.bib")
""",
        "report": """#set page(
  paper: "a4",
  margin: (top: 2cm, bottom: 2cm, left: 2.5cm, right: 2.5cm),
  header: align(right)[Company],
  footer: align(center)[#context counter(page).display()]
)
#set text(font: "Times New Roman", size: 11pt)
#set par(justify: true)
#set heading(numbering: "1.")

#align(center)[
  #text(size: 18pt, weight: "bold")[Report Title]
  
  #v(0.5em)
  
  Prepared by: Your Name
  
  Date: #datetime.today().display()
]

#pagebreak()

= Executive Summary

Summary content...

#pagebreak()

#outline()

#pagebreak()

= Introduction

Content...

= Findings

Content...

= Recommendations

Content...
""",
        "thesis": """#set page(paper: "a4", margin: 2.5cm, numbering: "1")
#set text(font: "Times New Roman", size: 12pt, lang: "en")
#set par(justify: true, leading: 0.65em, first-line-indent: 1.2em)
#set heading(numbering: "1.")

#align(center + horizon)[
  #text(size: 18pt, weight: "bold")[Thesis Title]
  
  #v(1em)
  
  Your Name
  
  #v(2em)
  
  Institution Name
  
  Year
]

#pagebreak()

= Abstract

Your abstract...

#pagebreak()

#outline()

#pagebreak()

= Introduction

Introduction content...

= Literature Review

Literature review...

= Methodology

Methods...

= Results

Results...

= Discussion

Discussion...

= Conclusion

Conclusion...

#bibliography("references.bib", style: "ieee")
"""
    }
    
    @staticmethod
    def generate(template_name: str, output_file: str) -> bool:
        """Generate a template document."""
        if template_name not in TypstTemplateGenerator.TEMPLATES:
            print(f"Unknown template: {template_name}")
            print(f"Available: {', '.join(TypstTemplateGenerator.TEMPLATES.keys())}")
            return False
        
        template_content = TypstTemplateGenerator.TEMPLATES[template_name]
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(template_content)
            print(f"✓ Generated template: {output_file}")
            return True
        except IOError as e:
            print(f"✗ Error writing file: {e}")
            return False


class TypstConverter:
    """Convert between formats and Typst."""
    
    @staticmethod
    def extract_structure(filepath: str) -> Dict:
        """Extract document structure (headings, sections, labels)."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            return {}
        
        structure = {
            "headings": [],
            "labels": [],
            "references": [],
            "figures": [],
            "tables": [],
            "code_blocks": []
        }
        
        # Extract headings with levels
        headings = re.findall(r'^(=+)\s+(.+)$', content, re.MULTILINE)
        for level_str, heading_text in headings:
            structure["headings"].append({
                "level": len(level_str),
                "text": heading_text.strip()
            })
        
        # Extract labels
        structure["labels"] = re.findall(r'<(\w+)>', content)
        
        # Extract references
        structure["references"] = re.findall(r'@(\w+)', content)
        
        # Extract figures
        figures = re.findall(r'#figure\([^)]+caption:\s*\[([^\]]+)\]', content)
        structure["figures"] = figures
        
        # Extract code blocks
        code_blocks = re.findall(r'```(\w+)?\n(.*?)\n```', content, re.DOTALL)
        structure["code_blocks"] = [(lang or "plain", code[:50]) for lang, code in code_blocks]
        
        return structure


def main():
    """Command-line interface for Typst utilities."""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "validate":
        if len(sys.argv) < 3:
            print("Usage: typst-utils validate <document.typ>")
            sys.exit(1)
        
        filepath = sys.argv[2]
        issues = TypstValidator.validate_document(filepath)
        
        if issues["errors"]:
            print(f"❌ Errors ({len(issues['errors'])}):")
            for error in issues["errors"]:
                print(f"   - {error}")
        
        if issues["warnings"]:
            print(f"⚠️  Warnings ({len(issues['warnings'])}):")
            for warning in issues["warnings"]:
                print(f"   - {warning}")
        
        if issues["info"]:
            print(f"ℹ️  Info ({len(issues['info'])}):")
            for info in issues["info"]:
                print(f"   - {info}")
        
        if not any([issues["errors"], issues["warnings"], issues["info"]]):
            print("✓ Document looks good!")
    
    elif command == "generate":
        if len(sys.argv) < 4:
            print("Usage: typst-utils generate <template-name> <output.typ>")
            print(f"Available templates: {', '.join(TypstTemplateGenerator.TEMPLATES.keys())}")
            sys.exit(1)
        
        template = sys.argv[2]
        output = sys.argv[3]
        TypstTemplateGenerator.generate(template, output)
    
    elif command == "structure":
        if len(sys.argv) < 3:
            print("Usage: typst-utils structure <document.typ>")
            sys.exit(1)
        
        filepath = sys.argv[2]
        struct = TypstConverter.extract_structure(filepath)
        
        print(f"\n📄 Document Structure: {filepath}")
        print(f"\nHeadings ({len(struct['headings'])}):")
        for h in struct["headings"]:
            indent = "  " * (h["level"] - 1)
            print(f"{indent}• {h['text']}")
        
        if struct["figures"]:
            print(f"\nFigures ({len(struct['figures'])}):")
            for fig in struct["figures"][:5]:
                print(f"  • {fig}")
        
        if struct["references"]:
            print(f"\nReferences ({len(struct['references'])}):")
            print(f"  • {', '.join(set(struct['references']))}")
        
        print()
    
    else:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)


def print_usage():
    """Print command usage."""
    print("""Typst Document Utilities

Usage:
  typst-utils validate <document.typ>     - Validate document for issues
  typst-utils generate <template> <file>  - Generate template document
  typst-utils structure <document.typ>    - Extract document structure

Templates: blank, article, report, thesis

Examples:
  python typst-utils.py validate paper.typ
  python typst-utils.py generate article my-article.typ
  python typst-utils.py structure thesis.typ
""")


if __name__ == "__main__":
    main()
