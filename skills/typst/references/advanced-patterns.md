# Advanced Typst Patterns

## Set vs. Show Rules Decision Tree

Use this to determine which styling approach to use:

**Use SET rules when:**
- You want to configure basic properties (most common)
- Styling is straightforward and properties are simple
- You need scoped styling for specific sections
- You want readable, maintainable code

**Use SHOW rules when:**
- You need to transform element structure
- You need to add custom content around elements
- Properties alone can't achieve the desired appearance
- You need pattern matching (regex, selectors)

## Common Styling Patterns

### Centered, Numbered Headings

```typst
#set heading(numbering: "1.")
#show heading: it => [
  #set align(center)
  #set text(font: "serif", weight: "bold", size: 14pt)
  #it.body
]
```

### Boxed Code Blocks

```typst
#show raw.where(block: true): it => box(
  width: 100%,
  fill: rgb("#f5f5f5"),
  inset: 10pt,
  stroke: 1pt + rgb("#ccc"),
  radius: 4pt,
  it
)
```

### Custom Link Styling

```typst
#show link: it => text(blue, underline)[#it]

// Or with color on hover (in interactive contexts)
#show link.where(destination: regex("external.*")): 
  text(rgb("#0066cc"))
```

### Emphasized Blocks

```typst
#show <note>: it => box(
  width: 100%,
  fill: rgb("#fffacd"),
  stroke: 1pt + rgb("#daa520"),
  inset: 10pt,
  radius: 4pt,
  it.body
)

#[This is a note] <note>
```

### First-Letter Drop Caps

```typst
#let dropcap(text, body) = {
  let first = text.first
  let rest = text.slice(1)
  
  [
    #box(
      width: 1.2em,
      height: 1.2em,
      fill: gray,
      align(center + horizon)[
        #text(size: 2.5em, weight: "bold")[#first]
      ]
    )
    #rest
  ] + body
}

#dropcap("T", [his paragraph demonstrates drop caps...])
```

### Alternating Row Colors in Tables

```typst
#table(
  columns: 3,
  fill: (x, y) => if calc.even(y) { rgb("#f0f0f0") } else { white },
  stroke: 0.5pt,
  [Header 1], [Header 2], [Header 3],
  [Data 1], [Data 2], [Data 3],
  [Data 4], [Data 5], [Data 6],
)
```

### Conditional Styling Based on State

```typst
#let in-draft = state("draft", false)

#show heading.where(level: 1): it => {
  in-draft.update(false)
  if context in-draft.get() {
    text(red, weight: "bold")[DRAFT: #it.body]
  } else {
    it
  }
}
```

### Bibliography Customization

```typst
// Custom citation format
#show bibliography: set text(size: 10pt)

// Custom bibliography styling
#show <references>: set text(size: 10pt)
```

## Layout Composition Patterns

### Multi-Column Layout with Sidebar

```typst
#grid(
  columns: (3fr, 1fr),
  gutter: 1em,
  [
    Main content area with full text...
  ],
  [
    #box(
      width: 100%,
      fill: rgb("#f0f0f0"),
      inset: 10pt,
      [
        *Sidebar*
        
        Key points or supplementary info
      ]
    )
  ]
)
```

### Two-Column Document

```typst
#set page(columns: 2, column-gutter: 1em)
#set text(size: 11pt)

= Document Title

Content flows across two columns automatically...
```

### Hanging Indent List

```typst
#let hanging-list(items) = [
  #set par(first-line-indent: -1.5em, left: 1.5em)
  #for item in items [- #item]
]

#hanging-list((
  [First item with a long description that wraps to multiple lines],
  [Second item],
))
```

### Image Gallery with Captions

```typst
#grid(
  columns: 3,
  gutter: 0.5em,
  
  [
    #figure(
      image("image1.jpg", width: 100%),
      caption: [Figure 1]
    )
  ],
  
  [
    #figure(
      image("image2.jpg", width: 100%),
      caption: [Figure 2]
    )
  ],
  
  [
    #figure(
      image("image3.jpg", width: 100%),
      caption: [Figure 3]
    )
  ],
)
```

## Template Functions for DRY Code

### Reusable Components

```typst
// Info box
#let info-box(title, content) = box(
  width: 100%,
  fill: rgb("#e3f2fd"),
  stroke: 1pt + rgb("#1976d2"),
  inset: 10pt,
  radius: 4pt,
)[
  *#title*
  #content
]

// Warning box
#let warning-box(content) = box(
  width: 100%,
  fill: rgb("#fff3e0"),
  stroke: 1pt + rgb("#f57c00"),
  inset: 10pt,
  radius: 4pt,
)[
  ⚠️ #content
]

// Code snippet with language label
#let code-snippet(lang, code) = [
  #text(size: 9pt, fill: gray)[*#lang*]
  #box(width: 100%, fill: rgb("#f5f5f5"), inset: 8pt)[
    #raw(code, lang: lang)
  ]
]

// Usage
#info-box("Tip", [Remember to save your work regularly])
#warning-box([This is an experimental feature])
#code-snippet("python", "print('Hello, World!')")
```

### Hierarchical Page Headers

```typst
#let chapter-page(number, title, body) = {
  set page(
    header: align(right)[
      #text(fill: gray)[Chapter #number]
    ],
    footer: align(center)[#context counter(page).display()],
  )
  
  [
    #text(size: 32pt, weight: "bold")[
      Chapter #number
    ]
    
    #text(size: 18pt, style: "italic")[#title]
    
    #v(1em)
    
    #body
  ]
}

#chapter-page(1, "Introduction", [Your chapter content...])
```

### Bibliography with Custom Formatting

```typst
#let format-citation(authors, year, title, journal) = {
  text(weight: "bold")[#authors (#year).] 
  " " + title + ". " + 
  text(style: "italic")[#journal] + "."
}

#format-citation("Smith et al.", "2023", 
  "Important Research", "Nature Journal")
```

## Performance-Optimized Patterns

### Large Document with Incremental Compilation

Structure for best performance:

```typst
// main.typ
#set page(margin: 2.5cm)
#set text(font: "Times New Roman", size: 12pt)

#include "chapters/intro.typ"
#include "chapters/chapter1.typ"
#include "chapters/chapter2.typ"
// Typst compiles each file incrementally
```

### Lazy-Loaded Figures

```typst
#let lazy-figure(image-path, caption, label) = {
  figure(
    image(image-path, width: 80%),
    caption: caption
  )
  <{label}>
}

// Reference: See @fig:important
```

### Conditional Content Compilation

```typst
#let show-draft-notes = false

#let note(content) = {
  if show-draft-notes {
    box(fill: yellow, inset: 5pt)[*NOTE:* #content]
  }
}

#note("This section needs more research")
```

## Debugging and Troubleshooting

### Reveal Layout Boundaries

```typst
// Temporarily show element boundaries
#set rect(stroke: 1pt + red)

#rect[This box has visible boundaries]
```

### Function Tracing

```typst
#let debug(label, value) = {
  // Output for debugging
  label + ": " + str(value)
}

#let result = 42
Debug output: #debug("Result", result)
```

### Conditional Logging

```typst
#let log-if(condition, message) = {
  if condition {
    text(fill: gray, size: 8pt)[LOG: #message]
  }
}

#log-if(true, "This variable was computed")
```

## Integration Patterns

### Combining Multiple Content Sources

```typst
#let main-document = "content.md"  // External markdown
#let external-bib = "refs.bib"     // External bibliography

#include "template.typ"
#include "chapters/"

#bibliography(external-bib)
```

### Programmatic Content Generation

```typst
#let generate-toc(items) = {
  [= Table of Contents]
  
  #for (num, item) in items.enumerate() [
    #(num + 1). #link(<{item}>)[#item]
  ]
}

#generate-toc(("Introduction", "Methods", "Results"))
```

### Dynamic Styling Based on Context

```typst
#let responsive-layout() = {
  context if page.width > 21cm [
    // Wide layout
    #set columns(2)
  ] else [
    // Narrow layout
    #set columns(1)
  ]
}
```

## Export and Output Patterns

### Document with Multiple Output Targets

```typst
// Configure for different outputs
#let output-format = "pdf"  // or "web", "print"

#if output-format == "print" {
  set page(margin: 2.5cm, fill: white)
} else if output-format == "web" {
  set page(width: auto, height: auto)
}

// Document content...
```

### Print-Optimized Styling

```typst
#set page(fill: white, paper: "a4")
#set text(fill: black, font: "Times New Roman")
#show link: text(blue, underline)

// Remove colors that don't print well
#show heading: it => text(fill: black)[#it.body]
```
