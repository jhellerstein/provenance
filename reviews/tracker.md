# Review Tracker

## P0: Structural (must fix before submission)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 1 | Datalog theorem must be in body (before page 15) | All three | **TODO** | Need named theorem + proof sketch for filtration/negation-semantics correspondence |
| 2 | Page budget: rebalance transactions vs. Datalog | All three | **TODO** | Currently 15.5pp. Compress transactions, move SI details to appendix |

## P1: Formal (fix to avoid rejection)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 3 | Theorem 2.1 too strong / underspecified | ChatGPT, Claude | **TODO** | Add clarifying sentence: "classical provenance" = single K-relation over one resolved instance |
| 4 | History-invariance scope unclear | ChatGPT, Claude | **TODO** | Add quiescent-history interpretation: holds when all environment events have occurred |
| 5 | Semiring framing: filtration should be headline | All three | **Partial** | Added "filtration is the content" sentence. Reviews say go further — consider restructuring Section 3 |
| 6 | "Minimal resolving determination" undefined | ChatGPT | **TODO** | Add definition: minimal = no proper subsequence resolves |
| 7 | Foata normal form / canonical layering unjustified | ChatGPT | **TODO** | Either prove uniqueness or weaken to "given a chosen valid layering" |
| 8 | Transaction model non-standard / vulnerable | ChatGPT, Claude | **Deferred** | Will compress transactions; Datalog becomes primary. Transactions as motivating instantiation |

## P2: Presentation (fix to strengthen)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 9 | Complexity result is validation, not headline | All three | **Done** | Reframed in Section 6 opening |
| 10 | Two algebraic objects conflated (D→K vs 2^D) | Claude | **TODO** | Clarify which is "determination provenance" vs "support semiring" |
| 11 | Notation clash: ▷ for layers and join | Claude | **TODO** | Check — may be a false alarm (▷ is only for layers; ⋈ for join) |
| 12 | "Three forces" taxonomy formally underused | Claude | **Acceptable** | Conceptual scaffolding; not every concept needs a theorem |
| 13 | Why-not claim needs more formal development | Claude | **Acceptable** | Remark 3.1 (symmetry) + Datalog appendix cover this adequately |
| 14 | Figure 1 appears before all cases developed | Claude | **Acceptable** | Standard for summary figures; forward pointers are fine |
| 15 | Example 1.1 formalism not yet established when it appears | Claude | **Acceptable** | Intro examples are always informal; formalism comes in Section 2-3 |

## P3: Already addressed (validate)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 16 | Boolean algebra is trivial | All three | **Done** | "Filtration is the content" sentence in Section 3.1 |
| 17 | CQA connection underdeveloped | ChatGPT, Claude | **Done** | Expanded paragraph with disanalogy (flat repairs vs layered) |
| 18 | Persistence: what breaks without it | Claude | **Done** | Expanded in open directions |
| 19 | Persistence for FCW informal | Claude | **Done** | Added justification in Section 2.3 |
| 20 | Filtration under negation in queries | Koutris (simulated) | **Done** | Proposition 3.8 (difference increases depth) |
| 21 | Filtration reachability | Bienvenu (simulated) | **Done** | Proposition 3.9 (every level realized) |
| 22 | coNP result thin | Livshits (simulated) | **Done** | FPT corollary + validation framing |
| 23 | No algorithms | Livshits (simulated) | **Done** | FPT corollary + semantic index framing in appendix |
| 24 | Transactions section too long | Koutris (simulated) | **Done** | Compressed isolation levels, SI subsection |

## Notes

- ChatGPT suggests demoting transactions to motivating example, making Datalog primary. We agree with rebalancing but keep both instantiations.
- ChatGPT suggests renaming "determination semiring" to "support semiring." Consider.
- Claude suggests promoting scheduling-basis (Section 4.6) since complexity result depends on it. Already integrated.
- Gemini suggests condensing protocol comparisons to appendix. Already done (Appendix E).
