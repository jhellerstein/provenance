# Determination Provenance — modular paper sources

This directory builds the paper **“Determination Provenance: From Ambiguity to
Algebra”** from modular LaTeX sources, recast into the determination-framework
formalism (self-contained; the framework is not cited as external work).

## Variants (drivers)

| Driver | Lead instantiation in body | Deferred to appendix |
|---|---|---|
| `main-datalog.tex` | Datalog with negation | transactions |
| `main-txn.tex`     | transactional isolation | Datalog |
| `main-both.tex`    | both | — |

`main-datalog.tex` is the intended arXiv / PODS-facing paper. The variant is
selected by the `\ifleaddatalog` flag set at the top of each driver, which the
shared `sec-abstract.tex` and `sec-intro.tex` branch on.

## Shared, instantiation-agnostic modules

- `preamble.tex` — packages, foundation-matching macros (`\OrdI`,`\OrdO`,
  `\Basis`,`\Dets`,`\Rho`,`\Spec`, adequacy/consumer macros), theorem envs,
  title metadata.
- `sec-abstract.tex`, `sec-intro.tex`
- `sec-prelim.tex` — the determination model (specification, residual state,
  commitment vs. exposure/entailment, parallel steps/layers, complete
  determinations, result map).
- `sec-algebra.tex` — adequate consumer + adequacy law, product semiring
  `K^𝒟`, support homomorphism, canonical layer-prefix filtration,
  `sdepth`/`cdepth`, why/why-not certificates, result-extensional (GKT)
  specialization.
- `sec-consequences.tex` — work regret / semantic shift, responsibility value,
  bounded-treewidth support/robustness algorithm, PDB connection.
- `sec-related.tex`, `sec-conclusion.tex`

## Instantiation modules (swappable)

- `inst-datalog-body.tex` / (proofs in) `app-datalog-proofs.tex`
- `inst-txn-body.tex` / `inst-txn-appendix.tex`

## Appendix modules

- `app-algebra.tex` — within-determination structure, support propagation,
  depth-reachability construction.
- `app-robustness.tex` — robustness coNP-completeness; bounded-treewidth
  tractability and the locality condition.
- `app-responsibility.tex` — Shapley refinement of the responsibility value
  (hardness, FPT, approximation, multi-layer).
- `app-datalog-proofs.tex`, `app-open-questions.tex`

## Building

Offline build via the bundled tectonic (works around the read-only sandbox
cache):

```
./build.sh main-datalog.tex      # or main-txn.tex / main-both.tex
```

The script redirects the tectonic/XDG/HOME caches to a writable scratch
location, builds in a unique temp dir, copies the PDF back when the working
directory is writable, and reports the page count. The legacy single-file
source is preserved as `main.tex` for reference.
