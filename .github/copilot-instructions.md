# Copilot instructions for this repo

This repo is a *single-paper LaTeX project*.
The “application” is `main.tex`, which builds to `main.pdf` using `acmart` + BibTeX.

## Big picture

- Primary source: `main.tex` (all sections, macros, theorem envs, and prose live here).
- Bibliography database: `references.bib`; generated output: `main.bbl` (don’t hand-edit).

## Build + local workflow

- Preferred build is `latexmk -pdf main.tex` (runs `pdflatex` and `bibtex` as needed).
- VS Code is configured for LaTeX Workshop in `.vscode/settings.json`:
  - auto-build on save
  - SyncTeX enabled
  - recipe: `pdflatex → bibtex → pdflatex × 2` and `latexmk`

Notes from a real build:
- Build artifacts (including `*.pdf`, `*.bbl`, `*.aux`, `*.synctex.gz`) are ignored via `.gitignore`.
- Current document references `fig:interp-tables`, but that label isn’t defined in `main.tex` (expect “undefined references” until added/fixed).

## Editing conventions in `main.tex`

- Macros and theorem environments are defined at the top of `main.tex` (e.g., `\Hist`, `\Spec`, `\Prov`, and theorem counters `\numberwithin{theorem}{section}`); reuse these instead of introducing near-duplicates.
- Environments used for exposition include `commentary` and `bracketlines`.
- Citations use BibTeX (`natbib` via `acmart`), so update `references.bib` and cite with `\cite{...}`.

## What not to do

- Don’t edit `main.bbl` directly; regenerate by running the LaTeX/BibTeX toolchain.
- Don’t commit build outputs (`*.pdf` is intentionally ignored).
