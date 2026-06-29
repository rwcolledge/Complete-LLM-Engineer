# The Complete LLM Engineer

A multi-volume Overleaf/LaTeX curriculum for becoming an LLM engineer from zero background using free tools, including Databricks Community Edition where feasible.

## Build locally

Install a TeX distribution with `latexmk` and `biber`, then run:

```bash
latexmk -pdf main.tex
biber main
latexmk -pdf main.tex
```

## Overleaf

Upload this repository as a ZIP to Overleaf and compile `main.tex`.

## Structure

- `main.tex` — master book entry point
- `preamble/` — shared packages, commands, environments
- `volumes/` — one folder per volume
- `bibliography/` — BibLaTeX references
- `notebooks/` — Jupyter notebooks
- `databricks/` — Databricks notebook exports
- `code/` — production code examples
- `exercises/` and `solutions/` — companion materials

## Writing workflow

Each chapter should be created as a separate `.tex` file and included from its volume file.
