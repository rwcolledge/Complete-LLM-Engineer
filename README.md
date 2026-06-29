# The Complete LLM Engineer

A multi-volume Overleaf/LaTeX curriculum for becoming an LLM engineer from zero background using free tools, including Databricks Community Edition where feasible.

## Current scaffold

- 16 volume folders
- Volume I expanded through Chapter 10
- Initial overview chapters for later volumes
- Shared LaTeX preamble
- Bibliography, appendices, templates, dataset catalog
- GitHub Actions LaTeX workflow

## Build locally

Install a TeX distribution with `latexmk` and `biber`, then run:

```bash
latexmk -pdf main.tex
biber main
latexmk -pdf main.tex
```

## Overleaf

Upload this repository as a ZIP to Overleaf and compile `main.tex`.

## Recommended writing workflow

1. Draft one chapter at a time.
2. Compile the project.
3. Commit the chapter.
4. Add matching code/notebooks/datasets.
5. Tag releases after each finished volume.

## Structure

- `main.tex` — master book entry point
- `preamble/` — shared packages, commands, environments
- `volumes/` — one folder per volume
- `templates/` — reusable chapter templates
- `bibliography/` — BibLaTeX references
- `notebooks/` — Jupyter notebooks
- `databricks/` — Databricks notebook exports
- `code/` — production code examples
- `datasets/` — dataset catalog and notes
- `exercises/` and `solutions/` — companion materials
