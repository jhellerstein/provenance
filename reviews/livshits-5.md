# Simulated PODS Review — Ester Livshits (Technion)

**Paper:** Determination Provenance: From Ambiguity to Algebra

## Summary

The paper introduces determination provenance, a framework that extends classical semiring provenance to settings with semantic ambiguity by making the commitments that resolve ambiguity explicit. The space of resolving determinations forms a filtered semiring. The paper instantiates the framework for transactions and Datalog with negation, and introduces "determination responsibility" — a Shapley-value measure of each commitment's contribution to a tuple's presence. The responsibility measure is shown to be #P-hard in general and FPT in support-formula treewidth.

## Strengths

- **Novel game-theoretic formulation.** The presence game (Definition 6.1) is well-defined and genuinely different from existing Shapley-value formulations in databases. Where Livshits et al. and Meliou et al. define games over *data tuples* (which tuples contribute to a query answer), this paper defines a game over *semantic commitments* (which resolution choices contribute to a tuple's presence). The players are fundamentally different objects, and the resulting complexity landscape is different.

- **Correct #P-hardness proof.** The reduction from weighted voting games is clean and correct. Deng & Papadimitriou [8] is the right citation. The embedding is immediate: a weighted threshold function is a special case of a monotone support predicate.

- **The treewidth tractability result is the right structural insight.** Stating the theorem in terms of support-formula treewidth (rather than conflict treewidth directly) is the correct move — it avoids the locality issue that plagued earlier versions. The sufficient condition (conflict treewidth bounds formula treewidth for local predicates) is clearly stated.

- **The "non-monotone as commitment" framing connects responsibility to the broader framework.** The paper argues that the same sealing mechanism that decomposes non-monotone provenance also determines the game structure for responsibility. This is a genuine conceptual contribution — it means the tractability frontier for responsibility is not ad hoc but follows from the framework's algebraic structure.

- **The SLA example (Example 6.1) is effective.** It shows concretely how responsibility distinguishes sensitivity to SLA tightening — something robustness alone cannot do.

## Weaknesses

**1. The relationship between the presence game and existing Shapley formulations is underdeveloped.**

The related work says "Livshits et al. compute Shapley values for data tuples in query answers under a fixed semantics; determination responsibility uses the same axioms but over semantic commitments." This is correct but insufficient. A reader familiar with the Shapley-for-databases literature will want to know:

- Is there a formal reduction between the two? (Probably not — different player sets.)
- Do the tractability boundaries align? (Livshits et al. show dichotomies based on query structure; this paper shows FPT in treewidth of the commitment graph. Are these related?)
- Can determination responsibility be used to *compute* tuple-level Shapley values as a special case? (If the "commitments" are tuple insertions and the "determination" is the database instance, does the presence game reduce to the tuple-contribution game?)

The last question is particularly interesting: if determination responsibility subsumes tuple-level responsibility as a special case (with trivial depth-0 determinations), that would be a strong unification claim. If it doesn't, the two are genuinely orthogonal and the paper should say so.

**2. The additive approximation (Appendix) has a subtle issue with the sampling procedure.**

The proof says: "Sample a random permutation π; let C precede i. Estimate the marginal by sampling a random completion of uncommitted variables and evaluating the query."

This gives an unbiased estimate of the marginal contribution for a *specific* permutation π. But the Shapley value is the *expectation* over all permutations. To get an additive ε-approximation of the Shapley value, you need O(1/ε²) permutation samples (outer loop), and for each you need the marginal contribution. If you estimate each marginal by a single random completion (inner loop), you get an unbiased but noisy estimate of each marginal, and the overall estimator has variance from both loops.

The stated bound O(n/ε² · log(1/δ) · p(n)) appears to assume that a single sample per permutation suffices. This is correct if the marginal contribution is deterministic given the permutation and the coalition (i.e., if you can evaluate v(C∪{i}) - v(C) exactly by checking whether the tuple holds under two specific determinations). But v(C) is defined as a *probability* over random completions of uncommitted variables — it's not the value under a single completion.

The correct sampling procedure is: for each permutation π, sample a random completion of all uncommitted variables, then check whether the tuple holds with and without φ_i's D*-value. The difference (0 or ±1) is an unbiased estimate of the marginal. This works because the expectation over both the permutation and the completion equals the Shapley value. The bound then follows from Hoeffding over the combined samples. The proof should make this two-level sampling explicit.

**3. The budget compositionality result (Appendix) is correct but trivial.**

Proposition B.2 says B(t₁⋈t₂) ≥ max(B(t₁), B(t₂)) where B(t) = 1 - |supp(t)|/2^n. This follows immediately from |S₁∩S₂| ≤ min(|S₁|, |S₂|). It's a statement about support sizes, not about Shapley values. Calling it "responsibility budget compositionality" oversells it — it's really "support-size monotonicity under intersection," which is a set-theoretic triviality. The paper should be more modest about this result.

**4. No dichotomy theorem.**

The paper shows #P-hardness (general) and FPT (bounded treewidth). But there is no dichotomy: is bounded support-formula treewidth the *only* tractable case, or are there other structural conditions that yield polynomial-time computation? For tuple-level Shapley values, recent work has identified dichotomies based on query structure (self-join-free CQs, hierarchical queries). Does a similar dichotomy exist for determination responsibility? Even a conjecture would be valuable.

**5. The multi-layer extension (Appendix) is informal.**

The appendix says responsibility for depth d>1 is "defined per layer, conditioned on discharged prefixes." But no formal definition is given — no game is defined for the conditional case, no theorem states its properties, and no complexity result is proved. For a paper that claims determination responsibility as a main contribution, the multi-layer case should be at least formally defined (even if complexity results are deferred).

## Questions for the Authors

1. Does the presence game reduce to the tuple-contribution game of Livshits et al. when determinations are trivial (depth 0, single determination)?

2. The treewidth theorem requires a *monotone* support formula. What fraction of natural SLA predicates are monotone? Is there a characterization of which predicates yield monotone supports?

3. For the approximation: is the correct interpretation that each "sample" is a (permutation, completion) pair, giving a ±1 estimate of the marginal? If so, the proof should say this explicitly.

4. Is there a natural notion of "safe" support predicates (analogous to safe queries in probabilistic databases) for which responsibility is polynomial without treewidth restrictions?

## Minor Comments

- The paper correctly notes that the definition extends to arbitrary product distributions μ. It would be worth noting that for non-product distributions (correlated commitments), the game structure changes and the treewidth result may not apply.

- The "self-disqualifying" argument for bounded treewidth is pragmatic but not formal. A reviewer might ask: is there a formal sense in which high-treewidth workloads are "rare" or "degenerate"?

- The contribution list says "efficient additive approximation for the general case" but this is in the appendix, not the body. The contribution list should reflect what's in the first 15 pages.

## Overall Recommendation

**Accept.**

The paper makes a genuine contribution at the intersection of provenance theory and game-theoretic explanation. The presence game is novel, the #P-hardness is correct, and the treewidth tractability result identifies the right structural parameter. The "non-monotone as commitment" framing gives the responsibility section a principled foundation rather than making it feel ad hoc. The main weaknesses (no dichotomy, informal multi-layer, trivial budget result) are limitations rather than errors. The combination of the filtered semiring, the Datalog correspondence, the monus elimination theorem, and the responsibility measure constitutes a substantial and coherent contribution to PODS.
