# Simulated PODS Review — Paraschos Koutris (Wisconsin-Madison)

## Summary

This paper introduces *determination provenance*, extending classical semiring provenance to settings where multiple admissible outcomes exist for the same input. The space of resolving determinations forms a Boolean algebra on supports, equipped with a filtration induced by non-commuting commitment layers. The framework is instantiated for transactional concurrency and Datalog with negation (where the classical negation semantics correspond to filtration levels). A new Section 6 defines *determination responsibility* via Shapley values, proves #P-hardness, and identifies a tractable frontier parameterized by conflict treewidth.

## Strengths

- **The filtration is a genuine algebraic contribution.** The observation that non-commuting commitment layers induce a chain of sub-semirings, and that positive relational algebra is non-expansive with respect to this chain (Corollary 3.1), is clean and non-trivial. This is the paper's strongest structural result.
- **Theorem 5.1 is striking.** Recovering stratified, well-founded, and stable-model semantics as different readings of the same filtration is a beautiful unification. The restriction to programs with independent final negative SCCs is appropriate and clearly stated.
- **Section 6 adds real depth.** The determination responsibility measure is well-motivated by the SLA example, and the tractability result (Theorem 6.2) connects the algebraic structure to algorithmic consequences. The paper is significantly stronger with this section than without it.
- **The recursive definition of ≡_k (Section 3.3)** is the right formalization. It makes the filtration well-defined under dynamic commutativity without requiring a global canonical form.
- **Good positioning against related work.** The possible-worlds paragraph and the Livshits et al. citation correctly distinguish this work from probabilistic provenance and tuple-level Shapley values.

## Weaknesses

**1. Theorem 6.1 (#P-hardness): the citation does not support the claim.**

The proof cites Deng and Papadimitriou [8] for the claim that computing marginal contributions in a DNF-support presence game is #P-hard. Deng and Papadimitriou's 1994 paper proves that computing Shapley values for *weighted voting games* is #P-hard. The presence game defined here is not a weighted voting game — it is a game whose value function is defined by model counting over a Boolean formula. The hardness of Shapley values for such games is established in later work (e.g., Aziz et al. 2009 for general Boolean games, or the connection to #P-hardness of reliability polynomials). The proof needs either a direct reduction or a more precise citation.

**2. Theorem 6.2: the assumption "support predicate definable as a monotone Boolean formula over commitment variables" is doing heavy lifting.**

The theorem statement includes the parenthetical "(as holds for SLA predicates over ordering commitments)." This is an important restriction that limits the theorem's applicability. For a general query Q evaluated over a transactional history, the support of Q(t) may not be a monotone formula over the ordering commitments — it depends on the query structure. The paper should either:
(a) prove that for a specified class of queries (e.g., monotone queries over the resolved instance), the support is always monotone in the commitments, or
(b) state the theorem with the monotonicity assumption as a hypothesis and discuss when it holds.

Currently the parenthetical makes it unclear whether this is a theorem about all supports or only about a subclass.

**3. The support semiring (2^D, ∪, ∩) is elementary; the paper should not oversell it.**

The paper correctly notes (Section 3.1) that "the Boolean algebra on supports is elementary" and that the filtration is the real content. However, the abstract and introduction still frame the "determination semiring" as a primary contribution. For a PODS audience, the semiring itself is just the powerset lattice. The contribution is the filtration + the fact that query evaluation respects it. I would recommend the abstract lead with the filtration rather than the semiring.

**4. Definition 2.5 allows ⊆ (not strict ⊊), but the finiteness argument requires strict shrinkage.**

The definition says "applying φ produces a nonempty subset Spec(H·φ) ⊆ Spec(H)." The finiteness argument (Section 3.1) says "each commitment strictly shrinks the admissible set." If a commitment can leave the admissible set unchanged (⊆ allows equality), then a minimal determination could have unbounded length. This is a minor formal gap — either require ⊊ in the definition or add "non-redundant" to the minimality condition.

**5. Proposition 3.2 (Single-layer case / PosBool) is stated without connecting to the responsibility section.**

Proposition 3.2 shows that for single-layer determinations, the determination semiring coincides with PosBool(Φ). Section 6 then defines responsibility for single-layer determinations. The connection should be made explicit: the support formula in Theorem 6.2 is exactly the PosBool formula from Proposition 3.2, and the treewidth of its primal graph is the conflict treewidth. This would make the tractability result feel less ad hoc and more like a structural consequence of the algebra.

## Questions for the Authors

1. **Theorem 6.2:** Can you give an example of a non-monotone query whose support is *not* a monotone formula over the ordering commitments? This would clarify the scope of the restriction.

2. **Filtration depth in practice:** For the transactional instantiation, what is the typical depth of real workloads? If most workloads have depth 1 (no overlapping cycles), the filtration is trivial (F_0 ⊂ F_1 = 2^D). Is there empirical evidence that depth > 1 arises in practice?

3. **Relationship to probabilistic provenance:** The possible-worlds paragraph says determination provenance "adds two layers absent from the probabilistic setting: the filtration and the independence structure." But probabilistic databases also have independence assumptions (tuple-independent, block-independent). How does your independence structure differ from block-independence in probabilistic DBs?

4. **Approximation guarantee:** Proposition 6.3 gives an additive ε-approximation. For small responsibility values (e.g., ρ ≈ 0.001), an additive error of ε = 0.05 is meaningless. Is there a regime where relative approximation is achievable?

## Minor Comments

- The proof of Lemma 2.1 (history-invariance) argues that exclusions at H* transfer to prefix H via persistence. But persistence says exclusions propagate *forward* (from earlier to later histories). The proof needs the exclusion to hold at H (earlier) and persist to H* (later), not the reverse. The argument is correct if read carefully (the commitment is *applied* at H, and persistence ensures the exclusion persists to H*), but the wording "the same exclusion holds at the corresponding prefix of H" is confusing. Consider rephrasing.

- Section 3.1 says |Spec(H)| − 1 bounds the length of a minimal determination. This should be |Spec(H₀)| − 1 for the initial history H₀, since Spec(H) changes as commitments are applied.

- The paper uses "determination semiring" for the support structure and "determination provenance" for the D → K function. This distinction is important and well-handled in Section 3.1, but the abstract uses "determination semiring" in a way that could be confused with the full D → K object.

## Overall Recommendation

**Weak Accept.**

The paper makes a genuine contribution: the filtration is algebraically interesting, the Datalog correspondence (Theorem 5.1) is the strongest result, and the responsibility section adds real technical content. The main concerns are: (1) the #P-hardness proof needs repair, (2) the treewidth theorem's scope needs clarification, and (3) the support semiring should not be oversold. These are fixable issues. The paper is above the acceptance threshold for PODS — it introduces a new algebraic framework with non-trivial structural theorems and a compelling application to negation semantics. The responsibility section, while newer and less polished, adds algorithmic depth that the paper previously lacked.
