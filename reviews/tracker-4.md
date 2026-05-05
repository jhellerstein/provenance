# Review Tracker — Round 4

## Verdict: 3× Weak Accept

All three reviewers recommend acceptance with fixes. No structural objections to the framework, the Datalog result, or the responsibility section. Issues are localized and fixable.

## Must-fix (raised by 2+ reviewers)

| # | Issue | Source | Notes |
|---|-------|--------|-------|
| 1 | #P-hardness proof: wrong citation (Deng & Papadimitriou is about complexity of solution concepts, not about #P-hardness of Shapley for DNF games). Need either a direct reduction or cite Aziz et al. 2009 / Bachrach & Elkind 2008 on Shapley for weighted voting/Boolean games. | All three | Livshits most detailed: "the reduction from weighted model counting to Shapley computation is not immediate and requires showing that the marginal-contribution function encodes a #P-hard counting problem" |
| 2 | Treewidth theorem: monotonicity assumption ("support predicate definable as a monotone Boolean formula") needs justification — why are SLA predicates monotone? What about non-monotone queries? | Koutris, Livshits | Livshits: "monotone threshold predicates (abort ratio ≤ k) are monotone in the ordering variables, but a general query result need not be." Scope the theorem explicitly to monotone support predicates. |
| 3 | Approximation: gap in how v(C) is computed during permutation sampling. Computing v(C) exactly requires counting support elements — itself a #P-hard problem. The FPRAS claim implicitly assumes v(C) can be estimated, not computed exactly. | Livshits | Need to clarify: sample a random completion of uncommitted variables (not enumerate), evaluate query, average. Each sample gives an unbiased estimate of v(C). |

## Should-fix (raised by 1 reviewer, important)

| # | Issue | Source | Notes |
|---|-------|--------|-------|
| 4 | WFS correspondence: cite Van Gelder–Ross–Schlipf or Przymusinski for the result that WFS = skeptical/credulous classification over stable models (for the restricted class). Without this, the proof sketch's key step is unsupported. | Bienvenu | |
| 5 | Filtration degeneracy: for the class in Theorem 5.1, F₀=F₁=...=Fₖ={∅,D} (trivial until last layer). The filtration only becomes interesting at layer k+1. Acknowledge this — the theorem's value is the *correspondence*, not the filtration's richness for this class. | Bienvenu | |
| 6 | Related work on Shapley in DBs: cite Livshits et al. ICDT 2021 more substantively. Current one-sentence mention is insufficient given Section 6's prominence. Explain: they compute Shapley for data tuples in query answers; we compute Shapley for semantic commitments in the determination game. Different players, different game, same axiomatic foundation. | Livshits | |
| 7 | Support semiring: don't oversell. The Boolean algebra (2^D, ∪, ∩) is standard; the contribution is the filtration + responsibility, not the semiring itself. | Koutris | Already partially addressed in body ("elementary and idempotent... the non-trivial structure is the filtration") but could be even more explicit. |

## Low priority / nice-to-have

| # | Issue | Source | Notes |
|---|-------|--------|-------|
| 8 | Multi-layer responsibility: formalize the conditional game (currently only described in prose + appendix example). | Livshits | Could add a 2-line definition in the body. |
| 9 | Theorem 2.1: still somewhat philosophical as an iff. | Koutris | Not flagged as blocking by any reviewer this round. Leave as-is. |
| 10 | Proposition 3.3 (qdepth characterization): proof of (b) could be more explicit. | Koutris | Minor. |

## What's working

- **Filtration**: all three see it as the core algebraic contribution
- **Datalog Theorem 5.1**: all three find it striking, appropriately scoped
- **Responsibility (Section 6)**: all three see it as adding real depth; the SLA example lands well
- **Page budget**: 15 pages, no complaints about length or missing content
- **Persistence WLOG**: not flagged this round (retrospective scoping resolved it)
- **History-invariance**: not flagged this round
- **Transaction section**: not flagged as problematic (commit/abort + ordering framing works)

## Action plan

1. Fix #P citation: replace Deng & Papadimitriou with a proper reference (Aziz et al. "Computational aspects of cooperative game theory" or direct reduction showing marginal contribution in a DNF presence game encodes #DNF)
2. Treewidth theorem: add explicit "for monotone support predicates" scope + one sentence explaining why SLA predicates are monotone
3. Approximation: clarify that each permutation sample estimates v(C) by sampling a single random completion and evaluating the query (no exact counting needed)
4. Add Van Gelder et al. citation to Theorem 5.1 proof sketch
5. Acknowledge filtration degeneracy in Section 5 (one sentence)
6. Expand Livshits et al. comparison in related work (2-3 sentences)
