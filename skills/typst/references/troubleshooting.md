# Typst Troubleshooting and FAQ

## Common Issues and Solutions

### Styling Not Applied

**Problem:** Set or show rules don't affect content

**Solutions:**
1. Ensure `#set` rules appear *before* content they should affect
2. Scoped styling with `#[...]` blocks only affects content within brackets
3. Check for conflicting rules—later rules override earlier ones
4. For show rules, verify the element selector is correct

```typst
// ❌ Wrong: Set rule after content
Content here
#set text(size: 14pt)

// ✅ Correct: Set rule before content
#set text(size: 14pt)
Content here

// ✅ Scoped: Only affects content in brackets
#[
  #set text(red)
  Red text
]
Default text
```

### Math Mode Symbols Not Rendering

**Problem:** Greek letters or special symbols appear as text instead of symbols

**Solutions:**
1. In math mode, use multi-letter names: `$alpha$` not `$a$`
2. Single letters stay verbatim: `$x$` renders as x
3. Use correct symbol names: `$infinity$` not `$inf$`
4. For markup mode, prefix with `#sym.`: `#sym.alpha`

```typst
// ❌ Wrong
$alpha + beta = gamma$  // Renders as letters

// ✅ Correct
$ alpha + beta = gamma $

// ✅ In markup mode
#sym.alpha + #sym.beta
```

### Tables Look Misaligned or Ugly

**Problem:** Column widths, borders, or alignment are wrong

**Solutions:**
1. Specify explicit column widths: `columns: (1fr, 2fr, auto)`
2. Use `fill` function for row/column shading: `fill: (x, y) => ...`
3. Add `stroke` for borders: `stroke: 0.5pt`
4. Use `align()` function for cell content alignment
5. For complex tables, consider using `#grid()` instead

```typst
// ❌ Simple markdown tables have limited control
| A | B |
|---|---|
| 1 | 2 |

// ✅ Better: Use table() function with options
#table(
  columns: (1fr, 2fr),
  stroke: 0.5pt,
  fill: (x, y) => if y == 0 { gray.lighten(50%) },
  align: (left, center),
  [Col 1], [Col 2],
  [Data 1], [Data 2],
)
```

### Page Breaks in Wrong Places

**Problem:** Content splits awkwardly across pages

**Solutions:**
1. Use `#pagebreak()` to force breaks at specific locations
2. Adjust page margins to fit more content
3. Reduce spacing with `#set par(leading: 0.6em)`
4. For figures, place before or after paragraphs
5. Use `#page(columns: 2)` for column layouts

```typst
= Section
Content...

#pagebreak()

= New Section on New Page
```

### Images Not Showing or Wrong Size

**Problem:** Images don't appear or appear too large/small

**Solutions:**
1. Verify file path is correct (relative to .typ file location)
2. Use absolute paths for clarity: `/absolute/path/to/image.png`
3. Specify dimensions explicitly: `width: 80%` or `height: 200pt`
4. For responsive sizing, use percentages instead of fixed sizes
5. Supported formats: PNG, JPEG, SVG, GIF

```typst
// ❌ May fail with relative paths
#image("diagram.png")

// ✅ Explicit dimensions
#image("figures/diagram.png", width: 80%)

// ✅ Responsive sizing
#figure(
  image("diagram.svg", width: 100%),
  caption: [Responsive diagram]
)
```

### Text Overflow or Doesn't Wrap

**Problem:** Text extends beyond page margins

**Solutions:**
1. Check page margins are reasonable: `margin: 2.5cm`
2. Ensure text size isn't too large: `size: 12pt`
3. For inline code, use smaller font: `size: 9pt`
4. Enable justified text: `#set par(justify: true)`
5. Use `#h(1fr)` for flexible horizontal spacing

```typst
// ❌ May overflow
#set text(size: 16pt)
#set page(margin: 0.5cm)

// ✅ Better
#set text(size: 12pt)
#set page(margin: 2.5cm)
#set par(justify: true)
```

### Headings Won't Number

**Problem:** Numbering appears but doesn't follow outline

**Solutions:**
1. Use `#set heading(numbering: "1.")` for automatic numbering
2. Numbering applies to all headings; adjust selector if needed
3. For specific heading levels: `#show heading.where(level: 1): ...`
4. Reset numbering at document sections with appropriate `#set` blocks

```typst
// ❌ No numbering
= Heading 1
== Heading 2

// ✅ Automatic numbering
#set heading(numbering: "1.")

= Heading 1        // Becomes "1 Heading 1"
== Heading 2       // Becomes "1.1 Heading 2"

// ✅ Custom numbering format
#set heading(numbering: "I.A.1.")  // I.A.1 style
```

### Bibliography Not Showing

**Problem:** `#bibliography()` function doesn't generate citations

**Solutions:**
1. Ensure .bib file exists and path is correct
2. Verify bibliography file format (BibLaTeX .bib or Hayagriva .yml)
3. Use citation syntax in text: `@key` or `[see @key]`
4. Without citations in text, nothing appears
5. For custom styles: `#bibliography("refs.bib", style: "ieee")`

```typst
// ❌ Bibliography appears empty—no citations in text
#bibliography("refs.bib")

// ✅ Citations in text trigger bibliography
This was shown by @author2020.

#bibliography("refs.bib")
```

### Functions or Imports Not Working

**Problem:** `#import` statements fail or functions undefined

**Solutions:**
1. Check file paths are relative to main document
2. Use correct import syntax: `#import "file.typ": function_name`
3. For multiple functions: `#import "file.typ": func1, func2, func3`
4. Import all with: `#import "file.typ": *`
5. Namespace with: `#import "file.typ" as module_name`

```typst
// ❌ Wrong—typo or wrong path
#import "template.typ": my_function

// ✅ Correct
#import "template.typ": my_function

// ✅ Import multiple
#import "utils.typ": add, multiply, divide

// ✅ Namespace to avoid conflicts
#import "utils.typ" as utils
#utils.add(1, 2)
```

### Performance: Compilation Too Slow

**Problem:** Document takes long to compile or live preview lags

**Solutions:**
1. Break large documents into files with `#include` for incremental compilation
2. Reduce justified text paragraphs (justified layout is slower than ragged)
3. Simplify complex show rules—avoid redundant transformations
4. Minimize use of loops and dynamic content generation
5. Use `#context` efficiently—don't call repeatedly
6. Upgrade to Typst 0.12+ for 6x performance on justified paragraphs

```typst
// ❌ Single file—recompiles everything
[Entire 200-page document in one file]

// ✅ Structured files—incremental compilation
#include "chapters/intro.typ"
#include "chapters/ch1.typ"
[Each file compiles independently]
```

### Spacing Issues Between Elements

**Problem:** Too much or too little space between paragraphs, headings, lists

**Solutions:**
1. Adjust paragraph spacing: `#set par(leading: 0.65em)`
2. Add explicit spacing: `#v(1em)` for vertical, `#h(1em)` horizontal
3. Control paragraph breaks: `#block(spacing: 1em)[content]`
4. For lists, use `#list()` function for more control
5. Between sections, use `#pagebreak()` or `#v(2em)`

```typst
// Adjust global paragraph spacing
#set par(leading: 0.75em)

// Add explicit spacing
Text before
#v(1.5em)
Text after

// Between sections
#heading[New Section]
#v(1em)
Content starts here...
```

## FAQ

### Q: How do I create a table of contents?

A: Use the `#outline()` function after enabling heading numbering:

```typst
#set heading(numbering: "1.")

#outline()

= Chapter 1
Content...

= Chapter 2
Content...
```

### Q: Can I use colors in my document?

A: Yes, use `#text(fill: rgb("#FF0000"))[Red text]` or named colors:

```typst
#text(fill: red)[Red]
#text(fill: blue)[Blue]
#text(fill: rgb("#FFA500"))[Orange using hex]
#text(fill: luma(128))[Gray using luminance]
```

### Q: How do I make a landscape page?

A: Use `#set page(width: 11in, height: 8.5in)` or adjust during rotation:

```typst
// Single landscape page
#set page(width: 11in, height: 8.5in)
Landscape content...

#set page(width: 8.5in, height: 11in)
Back to portrait...
```

### Q: Can I add notes or TODO comments?

A: Yes, use `// comment` for single-line and `/* */` for multi-line:

```typst
// TODO: Add more references here

/* This section needs
   to be expanded and
   reviewed by the team */
```

### Q: How do I control page numbering?

A: Use `#set page(numbering: "1")` for numeric or other formats:

```typst
#set page(numbering: "1")           // 1, 2, 3, ...
#set page(numbering: "i")           // i, ii, iii, ...
#set page(numbering: "I")           // I, II, III, ...
#set page(numbering: "(1)")         // (1), (2), (3), ...

// Access current page
Page #context counter(page).display()
```

### Q: How do I add a watermark?

A: Use `set page(background: ...)`:

```typst
#set page(background: 
  text(90deg, fill: gray.lighten(70%), size: 80pt, weight: "bold")[DRAFT]
)
```

### Q: Can I mix left and right alignment?

A: Yes, use `#align()` with positioning:

```typst
#align(left + top)[Top left]
#align(center + horizon)[Center]
#align(right + bottom)[Bottom right]

// Justify between elements
Left text #h(1fr) Right text
```

### Q: How do I create multi-column layout?

A: Use either `#set page(columns: 2)` or `#grid()`:

```typst
// Page-level two columns
#set page(columns: 2)

// Or use grid for more control
#grid(
  columns: 2,
  gutter: 1em,
  [Left column content],
  [Right column content]
)
```

### Q: Can I include external files in different formats?

A: Typst primarily works with `.typ` files. For other formats:
- Images: `#image("file.png")`
- Raw text: `#include "data.txt"` (converts to text)
- Structured data: Read `.json` or `.yml` manually or use plugins

### Q: How do I handle long references or citations?

A: Use `#bibliography()` and cite with `@key`. For custom formatting:

```typst
#let cite-custom(author, year) = {
  text(blue)[[#author, #year]]
}

#cite-custom("Smith", 2023) demonstrated...

#bibliography("refs.bib", style: "apa")
```

### Q: Is there a way to generate PDFs programmatically?

A: Yes, use the Typst CLI:
```bash
typst compile document.typ output.pdf
typst watch document.typ        # Live preview
typst query document.typ        # Query structure
```

Or use the JavaScript API via npm package `typst`.
