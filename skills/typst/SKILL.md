---
name: typst
description: Comprehensive Typst document creation, compilation, and styling system. Use when creating academic papers, reports, books, or presentations; converting documents to Typst format; implementing custom layouts; styling with set/show rules; integrating math, tables, and figures; debugging compilation issues; or optimizing performance. Includes 8 production templates, 20+ patterns, solutions for 20+ issues, 100+ code examples, and Python utilities.
---

# Typst

Typst is a modern markup-based typesetting system designed as an alternative to LaTeX that combines power, simplicity, and performance. This skill helps create and optimize Typst documents efficiently.

## Core Concepts

Typst operates in three syntactical modes that can be switched anywhere:

- **Markup mode** (default): Write content with `= Headings`, `*bold*`, `-` lists
- **Math mode** (`$...$`): Typeset equations with LaTeX-like syntax
- **Code mode** (`#...`): Execute expressions and logic

Key design principles: (1) Simplicity through consistency—if you know one thing, transfer that knowledge to similar tasks; (2) Power through composability—combine simple systems in flexible ways; (3) Performance through incrementality—documents compile in milliseconds with live preview.

## Document Basics

### Project Structure for Large Documents

For complex documents, organize files hierarchically:

```
project/
├── main.typ              # Entry point
├── template.typ          # Shared functions and styling
├── chapters/
│   ├── introduction.typ
│   ├── methodology.typ
│   └── conclusion.typ
├── figures/              # Images and diagrams
├── references.bib        # Bibliography in BibLaTeX format
```

Use `#include "path/to/file.typ"` to include files and `#import "template.typ": function_name` to import specific functions.

### Styling Hierarchy

Always apply global styling at the document start before content:

```typst
#set page(paper: "a4", margin: 2.5cm)
#set text(font: "Times New Roman", size: 12pt, lang: "en")
#set par(justify: true, leading: 0.65em, first-line-indent: 1.2em)
#set heading(numbering: "1.")
```

This ensures consistent styling across all elements. Scoped styling with `#[...]` blocks restricts rules to specific sections.

## Element Styling: Set vs. Show Rules

### Set Rules

Configure basic properties—use for 90% of styling needs:

```typst
#set text(size: 12pt, font: "Helvetica")
#set list(marker: [--])              // Change list markers
#set heading(numbering: "1.")        // Number headings
#set par(first-line-indent: 1.2em)  // Indent paragraphs
```

### Show Rules

Completely customize appearance—use when set rules are insufficient:

```typst
// Centered, italic headings
#show heading: it => [
  #set align(center)
  #set text(style: "italic")
  #it.body
]

// Highlight all "important" text
#show "important": text(red, weight: "bold")
```

Advanced selectors: `#show heading.where(level: 1)` targets specific elements, `#show <label>` targets labeled content, `#show regex("pattern")` uses pattern matching.

## Mathematical Typesetting

Inline math: `$x^2 + y^2 = z^2$`

Display math (space before/after):
```typst
$ sum_(i=1)^n i = (n(n+1))/2 $
```

Multi-line equations with alignment:
```typst
$ (3x + y) / 7 &= 9 && "given" \
  3x + y &= 63 & "multiply by 7" \
  x &= 21 - y/3 & "divide by 3" $
```

Vectors and matrices:
```typst
$ vec(a, b, c) + vec(1, 2, 3) = vec(a+1, b+2, c+3) $

$ mat(1, 2, 3; 4, 5, 6; 7, 8, 9) $
```

## Tables and Grids

### Basic Tables

Use markdown-style for simple tables:

```typst
| Name  | Age | City    |
|-------|-----|---------|
| Alice | 25  | Berlin  |
| Bob   | 30  | London  |
```

### Advanced Table Styling

```typst
#table(
  columns: (1fr, auto, 2fr),
  fill: (x, y) => if y == 0 { gray.lighten(50%) },
  stroke: 0.5pt,
  [Header 1], [Header 2], [Header 3],
  [Data 1],   [Data 2],   [Data 3]
)
```

## Images and Figures

### Basic Images

```typst
#image("path/to/image.png", width: 50%)
#image("diagram.svg", height: 200pt)
```

### Figures with Captions and Labels

```typst
#figure(
  image("architecture.png", width: 80%),
  caption: [System Architecture Diagram]
) <fig:architecture>

// Reference: See @fig:architecture
```

## Scripting and Programming

### Expressions and Blocks

Embed code with `#`:
```typst
#emph[Hello]
#(1 + 2)
#"hello".len()

// Complex expressions
#{
  let x = 1
  let y = 2
  x + y
}
```

### Functions and Variables

```typst
#let add(x, y) = x + y
#let greet(name) = [Hello #name!]

#let person = (name: "Alice", age: 30)
#person.name  // Access: "Alice"
```

## Templates and Reusable Components

### Template Pattern

Store shared styling in `template.typ`:

```typst
#let report(title, author, body) = {
  set page(margin: 2.5cm)
  set text(font: "Times New Roman", size: 12pt)
  set par(justify: true)
  
  align(center)[
    #text(size: 18pt, weight: "bold")[#title]
    #v(1em)
    #author
  ]
  
  body
}
```

Use in main document:
```typst
#import "template.typ": report

#show: report.with(
  title: "My Report",
  author: "John Doe"
)

Your document content here...
```

## Bibliography

Typst supports both BibLaTeX and Hayagriva formats.

### BibLaTeX (.bib files)

```typst
#bibliography("references.bib", style: "ieee")
```

Cite with: `@key1 @key2`

## Common Document Types

### Academic Paper

```typst
#set page(paper: "a4", margin: 2.5cm)
#set text(font: "Times New Roman", size: 12pt)
#set par(justify: true, first-line-indent: 1.2em)

#align(center)[
  #text(size: 18pt, weight: "bold")[Paper Title]
  Author Name
  Institution
  #datetime.today().display()
]

= Introduction
Your content...

#bibliography("references.bib")
```

### Report with Headers and Footers

```typst
#set page(
  header: align(right)[Company Name],
  footer: align(center)[#context counter(page).display()]
)
```

## Performance Optimization

### Best Practices

1. **Structure**: Break large documents into multiple files with `#include`
2. **Styling**: Apply global `#set` rules at document start
3. **Reuse**: Extract repeated patterns into functions
4. **Conditionals**: Use conditional set rules to apply styling based on state
5. **Scope styling**: Restrict styling with `#[...]` blocks
6. **Avoid**: Don't use show rules for every element

### Compilation

- CLI: `typst compile document.typ` generates PDF
- Live preview available in Typst web app
- Incremental compilation keeps preview snappy

## Tips and Tricks

1. **Page break**: `#pagebreak()`
2. **Placeholder text**: `#lorem(n)` generates n words
3. **References**: Label with `<label>`, cite with `@label`
4. **Comments**: `// single line` and `/* multi-line */`
5. **Alignment**: `#align(center)[content]`

## References

For detailed information, see:

- **templates.md** - 8 production-ready templates
- **advanced-patterns.md** - 20+ expert patterns
- **troubleshooting.md** - Solutions and FAQ

## Utilities

Python utilities in `scripts/typst-utils.py`:

- **Validate**: Check documents for errors
- **Generate**: Create templates
- **Structure**: Extract document structure

Usage:
```bash
python3 scripts/typst-utils.py validate document.typ
python3 scripts/typst-utils.py generate article my-paper.typ
python3 scripts/typst-utils.py structure document.typ
```
