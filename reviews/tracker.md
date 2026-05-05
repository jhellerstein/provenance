# Review Tracker

## P0: Structural (must fix before submission)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 1 | Datalog theorem must be in body (before page 15) | All three | **Done** | Theorem 5.1 (negation semantics as filtration levels) + proof sketch |
| 2 | Page budget: rebalance transactions vs. Datalog | All three | **Done** | Section 4 compressed from 327 to 255 lines; Datalog theorem added |

## P1: Formal (fix to avoid rejection)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 3 | Theorem 2.1 too strong / underspecified | ChatGPT, Claude | **Done** | Added "a single K-relation consistent with all admissible outcomes" |
| 4 | History-invariance scope unclear | ChatGPT, Claude | **Done** | Added quiescent-history interpretation |
| 5 | Semiring framing: filtration should be headline | All three | **Done** | Added filtration-is-content sentence + distinguished two objects |
| 6 | "Minimal resolving determination" undefined | ChatGPT | **Done** | Defined: no proper subsequence resolves |
| 7 | Foata normal form / canonical layering unjustified | ChatGPT | **Done** | Clarified: canonical per-determination given prefix commutativity; filtration well-defined via shared-prefix comparison |
| 8 | Transaction model non-standard / vulnerable | ChatGPT, Claude | **Acceptable** | Compressed transactions; Datalog has the theorem. Transactions are motivating instantiation |

## P2: Presentation (fix to strengthen)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 9 | Complexity result is validation, not headline | All three | **Done** | Reframed in Section 6 opening |
| 10 | Two algebraic objects conflated (D→K vs 2^D) | Claude | **Done** | Added parenthetical distinguishing determination semiring (supports) from determination provenance (D→K) |
| 11 | Notation clash: ▷ for layers and join | Claude | **False alarm** | ▷ = \seq (layers); ⋈ = \bowtie (join). Different symbols. |
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
