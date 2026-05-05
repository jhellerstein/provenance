# Review Tracker — Round 2

## Critical (raised by 2+ reviewers)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 1 | History-invariance too strong — quantifies over all H₁⊑H₂; should scope to completed histories | ChatGPT, Claude | **TODO** | Restate lemma: equality over prefixes of a closed history, or define "covered extension" |
| 2 | Dynamic layering needs recursive definition — define ≡ₖ inductively, prove equivalence relation | ChatGPT, Claude | **TODO** | D ≡₀ D' always; D ≡ₖ₊₁ D' iff ≡ₖ and next maximal commuting layer is same multiset. ~half page |
| 3 | Transaction model: use ordering commitments as primary basis in body (not commit/abort) | ChatGPT | **TODO** | Body example uses commit order as serialization order — inconsistent. Appendix already uses scheduling basis. Align. |
| 4 | Theorem 5.1 too broad — state exact program class | ChatGPT, Claude | **TODO** | Add: "programs whose negative SCCs form a final independent choice layer over a stratified sealing prefix" |
| 5 | Persistence canonicalization overclaims "WLOG" — outcome equivalence under stabilization, not full provenance equivalence | ChatGPT | **TODO** | Soften: "preserves resolved outcomes once dependencies stabilize; may change determination structure" |

## Moderate (raised by 1 reviewer, worth fixing)

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 6 | Theorem 5.1 proof sketch: WFS correspondence needs 1 more sentence | Claude | **TODO** | Explain why alternating fixpoint computes exactly the support classification at level k |
| 7 | Why-not claim underdeveloped — no formal "determination why-not" definition | Claude | **TODO** | Consider adding a brief definition parallel to Def 3.1 for the absent case |
| 8 | Finiteness of D: justify via bounded length (each commitment strictly shrinks), not "each applied at most once" | Claude | **TODO** | Fix the parenthetical in Section 3.1 |
| 9 | Notation ⊲ vs ⊲⊳ visual similarity | Claude | **False alarm** | ⊲ = \triangleright (layers); ⊲⊳ = \bowtie (join). Different symbols, but Claude finds them visually similar. Consider if worth changing. |
| 10 | Non-commutativity explanation dropped from Def 2.5 — restore | Claude | **TODO** | Was moved to prose but Claude says it should be more prominent |
| 11 | Abstract overclaims: "longstanding gaps," "recovering Green et al." | ChatGPT | **TODO** | Soften or remove |
| 12 | Complexity: "the right parameter" → "a natural parameter" | ChatGPT | **TODO** | Already partially addressed; check current wording |
| 13 | Tail-bound assumes uniform distribution — acknowledge | Claude | **TODO** | Add "under a uniform distribution over admissible serializations" |
| 14 | Corollary 3.1 should state union case explicitly | Claude | **TODO** | Minor |

## Low priority / acceptable

| # | Issue | Source | Status | Notes |
|---|-------|--------|--------|-------|
| 15 | Prop 3.5 (Reachability) proof is circular — needs existence construction | Claude | **Acceptable** | The "non-trivial choices at each layer" assumption is the existence condition |
| 16 | Relationship between minimal and non-minimal determinations | Claude | **TODO** | Add 1 sentence: any resolving determination reduces to a minimal one by dropping redundant commitments |
| 17 | Appendix H Prop H.1(c) "stabilized" is informal | Claude | **Acceptable** | Closing paragraph already appeals to quiescent-history assumption |
| 18 | "Three forces" taxonomy formally underused | Claude | **Acceptable** | Conceptual scaffolding; not every concept needs a theorem |

## Gemini's constructive suggestions for additional results

| # | Suggestion | Notes |
|---|-----------|-------|
| A | **Tractability frontiers / dichotomy**: Are there "safe queries" or restricted topologies where robustness drops to PTIME? (Analogous to safe queries in probabilistic DBs) | Interesting open question. Could add to Open Questions or develop if tractable cases exist beyond bounded width. |
| B | **Idempotence for Datalog fixpoints**: Does the determination semiring require idempotence for recursive queries with negation? State explicitly. | The determination semiring (2^D, ∪, ∩) IS idempotent (Boolean algebra). Worth noting explicitly. |
| C | **Where does complexity live?** Stable models are Π₂ᴾ-hard; WFS is PTIME. If the semiring captures stable models, where does the Π₂ᴾ hardness emerge — in constructing the semiring or in reading a filtration level? | Good question. Answer: constructing D (enumerating stable models) is the hard part; reading supports from a given D is polynomial. Worth a sentence. |

## Summary of priorities

**Before submission (in order):**
1. Fix history-invariance lemma (#1)
2. Narrow Theorem 5.1 (#4)
3. Soften persistence WLOG (#5)
4. Recursive filtration definition (#2)
5. Recast transactions as ordering commitments (#3)
6. Quick fixes: #6, #8, #10, #11, #12, #13, #14, #16
7. Consider Gemini suggestions B and C (1 sentence each)

**After submission / camera-ready:**
- Formal why-not definition (#7)
- Tractability frontiers (Gemini A)
- Notation change if needed (#9)
