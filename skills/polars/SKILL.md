---

name: polars-guide
description: Example-driven Polars DataFrame operations
languages: python,rust
---

## Purpose

Provide concise, idiomatic Polars examples for common DataFrame workflows.

Focus areas:

* Creating DataFrames and reading and writing common formats
* Core expression-based contexts:

  * `select`
  * `with_columns`
  * `filter`
  * `group_by().agg()`
* Chaining contexts into multi-step queries
* Combining DataFrames via joins and concatenation

## When to use

Use for practical Polars examples or for translating pandas-style logic into idiomatic Polars.

When relevant, show both eager and lazy execution and prefer lazy for multi-step pipelines.

## Conventions

* Prefer expressions like `pl.col` and `pl.lit` over Python row-wise logic
* Explicitly name derived columns with `.alias(...)`
* Use readable chained transformations for multi-step logic
* Call out ordering implications in `group_by`
* For joins, always specify keys, join type, and key uniqueness assumptions

## Reference patterns

* Expressions are abstract until used in a context
* Primary contexts:

  * `select`
  * `with_columns`
  * `filter`
  * `group_by().agg()`
* Combine DataFrames with:

  * `join`
  * `pl.concat`
* Apply expressions to multiple columns with name expansion
* Build complex queries by chaining `with_columns`, `select`, and `group_by().agg()`

---
