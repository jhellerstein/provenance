## Simulated PODS Review — Paraschos Koutris (Round 5)

### Summary

This paper introduces *determination provenance*, extending classical semiring provenance to settings with semantic ambiguity. The key idea is that non-monotone operations (negation, conflict resolution, aggregation) require completeness guarantees that are externalized as "sealing commitments," decomposing non-monotone provenance into layers of monotone computation. The supports of determination provenance form a Boolean semiring equipped with a filtration induced by commitment layers. The paper instantiates the framework for transactions and Datalog with negation, proves a monus-elimination theorem showing layered monotone semirings subsume semirings-with-monus at the support level, and defines determination responsibility (Shapley values over commitments) with #P-hardness and FPT tractability results.

---

### Strengths

- **The "non-monotonicity as commitment" framing is excellent.** This is the paper's most distinctive conceptual contribution. The observation that monus, complement, and aggregation all require completeness guarantees—and that these guarantees are exactly sealing commitments—gives the framework a unified rationale that goes beyond "provenance for ambiguous specs." It connects naturally to the CALM/coordination literature without overlapping with it.

- **The filtration is a genuine algebraic contribution.** The inductive definition of ≡_k, the proof that each F_k is a sub-semiring, and the non-expansiveness of positive RA (Corollary 3.1) are clean and correct. The characterization of query-relative depth is useful.

- **Theorem 5.1 (negation semantics as filtration levels) is striking.** The restricted class is clearly stated, the proof sketch is adequate, and the general case is proved in the appendix (Theorem G.2). The connection between stratification and determination layering is well-articulated.

- **Monus elimination (Theorem 5.2) is correctly scoped.** Stating it at the support level avoids the N[X] issue. The zero-divisor-free condition is noted. The proof is convincing for the claimed scope.

- **The responsibility section is well-structured.** The presence game is cleanly defined, the #P-hardness reduction via weighted voting games is correct, and the treewidth tractability theorem is appropriately stated in terms of support-formula treewidth (with conflict treewidth as a sufficient condition for local predicates).

- **The SLA example (Example 6.1) is effective.** It demonstrates the responsibility budget clearly and shows why robustness alone is insufficient.

---

### Weaknesses

**1. The support semiring (2^D, ∪, ∩) is still the Boolean algebra, and the paper should be more upfront about this.**

The paper acknowledges this ("elementary and idempotent") but the abstract and introduction still frame the "determination semiring" as if it were a novel algebraic object. The novelty is the *filtration*, not the semiring. A reviewer familiar with possible-worlds semantics will note that supports-as-sets-of-worlds is standard; what's new is the layered equivalence structure. The paper would be stronger if it said explicitly in Section 3.1: "The determination semiring is the powerset Boolean algebra; the contribution is the filtration it carries."

**2. The relationship between Theorem 5.2 (monus elimination) and Dannert et al. needs more precision.**

The theorem claims support equivalence for "any naturally ordered semiring K." But Dannert et al. define their LFP provenance specifically for ω-continuous semirings with a natural order satisfying certain properties (e.g., the existence of infinite sums for fixpoint computation). The paper should either (a) state the exact class of semirings for which the theorem holds (ω-continuous, zero-divisor-free, naturally ordered), or (b) note that the theorem applies to all semirings in which Dannert et al.'s construction is defined. As written, "any naturally ordered semiring K" is slightly broader than what the proof establishes.

**3. The treewidth tractability theorem (Theorem 6.2) has a gap between the theorem statement and the sufficient condition.**

The theorem is stated for "support formula with primal-graph treewidth w." The sufficient condition says conflict treewidth bounds this for "predicates that depend only on pairwise ordering relationships." But the paper doesn't formally define what "pairwise ordering relationships" means, and the SLA example (abort ratio ≤ k) is a threshold function over individual commitments—which is indeed local. A more complex query (e.g., "the serialization order is consistent with a given partial order") might not be local. The paper should either formalize the locality condition or give a counterexample showing when conflict treewidth is insufficient.

**4. The paper claims "aggregation" fits the framework but provides no formal instantiation.**

The abstract and introduction list "aggregation" alongside negation and conflict resolution. The intro adds "all contributing tuples accumulated before an aggregate is computed." But no section develops this. The claim that it "follows from stratified aggregation (Ross & Sagiv 1992)" is plausible but unstated as a theorem. Either develop a brief aggregation example (even 3-4 lines showing how a GROUP BY with a threshold becomes a sealing commitment + monotone evaluation) or remove aggregation from the headline claims.

**5. Proposition 3.3 (Characterization of qdepth) part (b) proof is too terse.**

The proof says "Minimality of k means some level-(k-1) class is split." This is correct but the reader must verify that "split" means "contains both elements in S and elements not in S." A one-sentence expansion would help.

---

### Questions for the Authors

1. Is there a natural example where the filtration has non-trivial intermediate levels (i.e., F_k ≠ {∅, D} for some 0 < k < d)? The Datalog example has trivial intermediate levels; the transaction example has depth 1 (no intermediate levels). A depth-2 example with genuinely interesting F_1 would strengthen the paper.

2. For the monus elimination theorem: does the support equivalence extend to *provenance equivalence* (same K-values, not just same zero/nonzero status) for specific semirings like the Boolean semiring or the why-provenance semiring? If so, that would be a stronger result worth stating.

3. The paper defines determination responsibility for a *realized* determination D*. Is there a natural "unconditional" version that doesn't condition on a specific realization? (E.g., the expected responsibility over all D* ∈ D.)

---

### Minor Comments

- The % NOTE comments should be removed before submission (lines 143-146, 1256-1260, 1433-1435, 1474-1477).
- Definition 2.5 allows Spec(H·φ) ⊆ Spec(H) (non-strict). The finiteness argument at line 569 assumes strict shrinkage. Either make the definition strict or add "non-redundant" to the finiteness claim.
- The Valiant reference [29] appears in the bibliography but is no longer cited in the text. Remove it.
- "Seqencing" typo if present (flagged in earlier reviews).
- The contribution list item (iii) is long (5 lines). Consider splitting monus elimination into its own item (v).

---

### Overall Recommendation

**Accept (weak).**

The paper makes a genuine and well-articulated contribution. The "non-monotonicity as commitment" framing is memorable and connects to important themes in database theory. The filtration is a real algebraic structure (not just bookkeeping), the Datalog correspondence is striking, the monus elimination theorem is correctly scoped and interesting, and the responsibility section provides algorithmic depth. The main weaknesses are: (1) the aggregation claim is unsupported, (2) the treewidth locality condition needs formalization, and (3) the support semiring's novelty should be more carefully distinguished from the filtration's novelty. These are addressable in revision. The paper is above the PODS acceptance threshold.
