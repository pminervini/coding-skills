# Typst Templates Reference

## Academic Paper Template

```typst
#set page(paper: "a4", margin: 2.5cm, numbering: "1")
#set text(font: "Times New Roman", size: 12pt, lang: "en")
#set par(justify: true, leading: 0.65em, first-line-indent: 1.2em)
#set heading(numbering: "1.")

// Title and metadata
#align(center)[
  #text(size: 18pt, weight: "bold")[Your Paper Title]
  
  #v(0.5em)
  
  Author Name$^1$, Co-Author$^2$
  
  #text(size: 10pt)[
    $^1$ Department, University A
    #linebreak()
    $^2$ Department, University B
  ]
  
  #v(0.5em)
  
  #text(size: 10pt, style: "italic")[
    #datetime.today().display("[day] [month repr] [year]")
  ]
]

#v(1.5em)

== Abstract

Your abstract here. Keep it under 150 words and summarize the main contributions, methods, and findings.

#v(1em)

= Introduction

Introduction content...

= Related Work

Related work...

= Methodology

Methods...

= Results

Results...

= Discussion

Discussion...

= Conclusion

Conclusion...

#bibliography("references.bib", style: "ieee")
```

## Business Report Template

```typst
#set page(
  paper: "a4",
  margin: (top: 2cm, bottom: 2cm, left: 2.5cm, right: 2.5cm),
  header: align(right)[Confidential],
  footer: align(center)[Page #context counter(page).display()]
)
#set text(font: "Helvetica", size: 11pt)
#set par(justify: false, leading: 0.75em)
#set heading(numbering: "1.")

// Cover page
#align(center + horizon)[
  #text(size: 28pt, weight: "bold")[Report Title]
  #v(1em)
  #text(size: 14pt, style: "italic")[Subtitle]
  #v(3em)
  #text(size: 12pt)[
    Prepared by: Your Name
    #linebreak()
    Date: #datetime.today().display()
  ]
]

#pagebreak()

// Table of contents
#outline(indent: 1em)

#pagebreak()

// Executive Summary
= Executive Summary

High-level overview of findings and recommendations.

#pagebreak()

= Introduction

Project scope and objectives.

= Key Findings

#list(
  [Finding 1: Description],
  [Finding 2: Description],
  [Finding 3: Description],
)

= Recommendations

#numbered-list(
  [Recommendation 1],
  [Recommendation 2],
  [Recommendation 3],
)

= Appendix <appendix>

Additional details and data tables.
```

## Presentation Slides Template

```typst
#let slide(title: "", body) = {
  set page(width: 16cm, height: 9cm, margin: 1em)
  set text(size: 16pt)
  
  [
    #box(width: 100%, height: 100%, fill: rgb("#f0f0f0"))[
      #align(top + left)[
        #text(size: 24pt, weight: "bold", fill: rgb("#003366"))[#title]
      ]
      #align(left + horizon)[
        #body
      ]
    ]
  ]
}

#slide(title: "Title Slide")[
  Presenter Name
  
  Institution/Company
  
  Today's Date
]

#slide(title: "Key Points")[
  - Point 1: Explanation
  - Point 2: Explanation
  - Point 3: Explanation
]

#slide(title: "Data Visualization")[
  #table(
    columns: 2,
    [Metric], [Value],
    [Item A], [87%],
    [Item B], [63%],
    [Item C], [95%],
  )
]

#slide(title: "Conclusion")[
  Main takeaway message
]
```

## Book Chapter Template

```typst
#set text(font: "Garamond", size: 12pt)
#set par(justify: true, leading: 0.8em, first-line-indent: 1.5em)

= Chapter 1: Introduction

First paragraph of chapter.

== Section 1.1

Content here...

=== Subsection 1.1.1

Details...

#figure(
  image("chapter1-diagram.png", width: 80%),
  caption: [Diagram caption explaining the visualization]
) <fig:chapter1-diagram>

As shown in @fig:chapter1-diagram, the relationship is clear.

== Section 1.2

More content...

#pagebreak()
```

## Newsletter/Magazine Template

```typst
#set page(columns: 2, margin: 1.5cm)
#set text(font: "Source Sans Pro", size: 11pt)

#align(center)[
  #text(size: 32pt, weight: "bold")[Newsletter Title]
  
  #text(size: 14pt, fill: gray)[
    Issue #12 | December 2024
  ]
]

#v(1em)

= Featured Story

Article lead and first section...

#v(0.5em)

== Subsection

More details...

#v(1em)

= News Roundup

- Breaking news 1: Details about item 1
- Breaking news 2: Details about item 2
- Breaking news 3: Details about item 3

#v(1em)

= Featured Resource

#box(
  width: 100%,
  fill: rgb("#e8f4f8"),
  inset: 0.5em,
  stroke: rgb("#0066cc")
)[
  *Resource Title*: Description and relevance to readers
]

#v(1em)

= Upcoming Events

- January 15: Event name and location
- February 3: Event name and location
- March 10: Event name and location
```

## Lab Report Template

```typst
#set page(paper: "a4", margin: 2cm)
#set text(font: "Times New Roman", size: 11pt)
#set heading(numbering: "1.")

#align(center)[
  #text(size: 14pt, weight: "bold")[Laboratory Report]
  
  Experiment: Name of Experiment
  
  Date: #datetime.today().display()
  
  Student: Name | Lab Partners: Names
]

#v(1em)

= Objective

State what you aimed to achieve and the scientific principle being tested.

= Materials and Methods

List equipment and describe the experimental procedure step by step.

= Results

Present data in tables and figures with captions:

#figure(
  table(
    columns: 3,
    [Trial], [Temperature °C], [Measurement],
    [1], [25], [5.2],
    [2], [50], [8.7],
    [3], [75], [12.3],
  ),
  caption: [Experimental measurements]
) <tbl:results>

= Analysis

Interpret results. Include calculations:

$ Q = m c Delta T $

where $m$ is mass, $c$ is specific heat, and $Delta T$ is temperature change.

= Conclusion

Summarize findings and discuss any sources of error.

= References

#bibliography("references.bib")
```

## Resume/CV Template

```typst
#set page(margin: 1.5cm)
#set text(font: "Calibri", size: 10pt)
#set par(leading: 0.5em)

#align(center)[
  #text(size: 16pt, weight: "bold")[Your Name]
  #v(0.2em)
  city@email.com | +1-555-1234 | linkedin.com/in/yourprofile
]

#v(0.5em)

== Professional Summary

Brief summary of qualifications and career objectives (2-3 sentences).

== Experience

*Senior Developer* — Company A | Jan 2022 – Present
- Achievement or responsibility
- Key project or contribution
- Quantifiable result or impact

*Developer* — Company B | Jun 2019 – Dec 2021
- Implemented feature X with Y result
- Led team of Z people
- Technologies: Python, React, PostgreSQL

== Education

*Bachelor of Science* — Computer Science | University Name | 2019

== Skills

#grid(
  columns: 2,
  [*Languages:* Python, JavaScript, Rust],
  [*Databases:* PostgreSQL, MongoDB],
  [*Tools:* Git, Docker, AWS],
  [*Frameworks:* React, FastAPI, Django],
)

== Certifications

- AWS Solutions Architect Associate (2023)
- Kubernetes Fundamentals (2022)
```

## Proposal Template

```typst
#set page(margin: 2cm)
#set text(font: "Times New Roman", size: 12pt)
#set par(justify: true)

#align(center)[
  #text(size: 18pt, weight: "bold")[Project Proposal]
  
  #v(0.5em)
  
  Submitted to: Organization Name
  
  Submitted by: Your Organization
  
  Date: #datetime.today().display()
]

#v(1.5em)

= Executive Summary

Brief overview of proposal (half page maximum).

= Problem Statement

Describe the current situation, challenges, and why action is needed.

= Proposed Solution

Detail your approach, methodology, and how it addresses the problem.

= Timeline

#table(
  columns: 2,
  [Phase], [Timeline],
  [Planning], [Weeks 1-2],
  [Development], [Weeks 3-6],
  [Testing], [Weeks 7-8],
  [Deployment], [Week 9],
)

= Budget

#table(
  columns: 3,
  [Item], [Cost], [Qty],
  [Personnel], [$50,000], [1],
  [Equipment], [$10,000], [1],
  [Software], [$5,000], [1],
  table.cell(fill: gray)[*Total*], table.cell(fill: gray)[*$65,000*], table.cell(fill: gray)[]
)

= Qualifications

Explain why your team is equipped to execute this project successfully.

= Next Steps

- Stakeholder review: March 1
- Approval: March 8
- Project kickoff: March 15
```
