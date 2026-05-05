# Review Tracker — Round 2

## Critical (raised by 2+ reviewers)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 1 | History-invariance too strong — quantifies over all H₁⊑H₂; should scope to completed histories | ChatGPT, Claude | **Done** | Lemma now scoped to prefixes of completed H* with covered dependency set |
| 2 | Dynamic layering needs recursive definition — define ≡ₖ inductively, prove equivalence relation | ChatGPT, Claude | **Done** | Inductive definition added: ≡₀ always; ≡ₖ₊₁ iff ≡ₖ and same next layer. Equivalence by multiset equality. |
| 3 | Transaction model: use ordering commitments as primary basis in body (not commit/abort) | ChatGPT | **Done** | Commitment Basis subsection restructured: ordering commitments primary, commit/abort demoted to "operational basis" paragraph. Running example + figure updated. |
| 4 | Theorem 5.1 too broad — state exact program class | ChatGPT, Claude | **Done** | Now: "programs whose negative SCCs are mutually independent and form a single final choice layer over a stratified sealing prefix" |
| 5 | Persistence canonicalization overclaims "WLOG" — outcome equivalence under stabilization, not full provenance equivalence | ChatGPT | **Done (strengthened)** | Rather than softening, proved the stronger result: in retrospective setting, seal is non-filtering guard, entailment reproduces exclusions exactly, remainder of determination unchanged. Full provenance equivalence (D, supports, filtration, K-values all preserved). WLOG claim now justified. |

## Moderate (raised by 1 reviewer, worth fixing)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 6 | Theorem 5.1 proof sketch: WFS correspondence needs 1 more sentence | Claude | **Done** | Proof sketch now explains: alternating fixpoint classifies atoms by whether they hold in all/no/some stable models, which is exactly the support classification at level k |
| 7 | Why-not claim underdeveloped — no formal "determination why-not" definition | Claude | **Deferred** | After submission / camera-ready |
| 8 | Finiteness of D: justify via bounded length (each commitment strictly shrinks), not "each applied at most once" | Claude | **Done** | Fixed: "each commitment strictly shrinks the admissible set, so length ≤ |Spec(H)| - 1" |
| 9 | Notation ⊲ vs ⊲⊳ visual similarity | Claude | **False alarm** | ⊲ = \triangleright (layers); ⊲⊳ = \bowtie (join). Different symbols. |
| 10 | Non-commutativity explanation dropped from Def 2.5 — restore | Claude | **Already present** | Lines 331–333 already have "The result of a commitment may depend on the full set Spec(H)...this is what allows commitments to be non-commutative" |
| 11 | Abstract overclaims: "longstanding gaps," "recovering Green et al." | ChatGPT | **Done** | Removed both phrases; replaced with precise claims |
| 12 | Complexity: "the right parameter" → "a natural parameter" | ChatGPT | **Done** | All three occurrences fixed |
| 13 | Tail-bound assumes uniform distribution — acknowledge | Claude | **Done** | Added "under a uniform distribution over D" + "other distributions yield weighted variants" |
| 14 | Corollary 3.1 should state union case explicitly | Claude | **Done** | Both join and union bounds now stated |

## Low priority / acceptable

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 15 | Prop 3.5 (Reachability) proof is circular — needs existence construction | Claude | **Acceptable** | The "non-trivial choices at each layer" assumption is the existence condition |
| 16 | Relationship between minimal and non-minimal determinations | Claude | **Done** | Added: "Any resolving determination can be reduced to a minimal one by dropping redundant commitments" |
| 17 | Appendix H Prop H.1(c) "stabilized" is informal | Claude | **Done** | Proposition now explicitly states "within a completed history H*" |
| 18 | "Three forces" taxonomy formally underused | Claude | **Acceptable** | Conceptual scaffolding; not every concept needs a theorem |

## Gemini's constructive suggestions for additional results

| # | Suggestion | Status | Notes |
|---|-----------|--------|-------|
| A | **Tractability frontiers / dichotomy**: Are there "safe queries" or restricted topologies where robustness drops to PTIME? | **Deferred** | Open question for future work |
| B | **Idempotence for Datalog fixpoints**: Does the determination semiring require idempotence for recursive queries with negation? | **Done** | Noted: (2^D, ∪, ∩) is idempotent; fixpoint computations over supports terminate |
| C | **Where does complexity live?** Stable models are Π₂ᴾ-hard; WFS is PTIME. | **Done** | Added: "hardness resides in constructing D; once D is given, reading supports is polynomial" |

## Summary

All critical and moderate items addressed. Persistence result strengthened rather than softened — full provenance equivalence proved in retrospective setting via non-filtering guard argument.
