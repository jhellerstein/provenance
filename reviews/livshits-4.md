# Simulated PODS Review — Ester Livshits (Technion)

## Summary

This paper introduces *determination provenance*, extending classical semiring provenance to settings with semantic ambiguity by indexing provenance over a space of resolving determinations. The supports of this indexed provenance form a Boolean semiring equipped with a filtration reflecting the layered commitment structure. The paper instantiates the framework for transactions and Datalog with negation, and introduces *determination responsibility*—a Shapley-value measure quantifying each commitment's contribution to a tuple's presence—with #P-hardness, FPT tractability under bounded conflict treewidth, and an additive approximation algorithm.

## Strengths

- **Novel game-theoretic formulation.** The presence game (Definition 6.1) is a clean and well-motivated cooperative game. The players are semantic commitments rather than data tuples, which is a genuinely new object compared to existing work on Shapley values in databases (Livshits et al. ICDT 2021, Deutch et al.). The distinction is meaningful: data-tuple Shapley asks "which input is most responsible for the output?"; determination responsibility asks "which semantic resolution is most responsible for the output holding under this execution?"

- **Structural tractability result.** Theorem 6.2 identifies conflict treewidth as the parameter governing tractability. The argument that the support formula's primal graph is a subgraph of the conflict graph (for monotone SLA predicates over ordering commitments) is the right kind of structural insight. This connects the algebraic framework to algorithmic utility.

- **The filtration as a stopping criterion.** The observation that qdepth(t) = k means layers beyond k contribute zero responsibility is elegant and practically useful—it tells you which layers of the determination to analyze and which to ignore.

- **The SLA example (Example 6.1) is effective.** It concretely shows how responsibility distinguishes "any one commitment suffices" (low individual responsibility) from "all are needed" (high individual responsibility), which robustness alone cannot.

## Weaknesses

**1. The #P-hardness proof (Theorem 6.1) is inadequate.**

The proof says computing the marginal v(C ∪ {i}) − v(C) "is a weighted model-counting problem over a DNF formula under partial assignment, which is #P-hard [12]." Reference [12] is Deng and Papadimitriou (1994), which proves #P-hardness of computing Shapley values for *weighted voting games*, not for arbitrary DNF model-counting under partial assignment.

The gap: the presence game is not a weighted voting game. It is a game whose value function is defined by the fraction of support elements consistent with a coalition. To apply Deng & Papadimitriou, you would need to show that the presence game with DNF support *encodes* a weighted voting game, or you need a different reduction.

The correct citation for #P-hardness of Shapley values in Boolean games with DNF representation would be closer to Bachrach et al. (2009, "Approximating power indices: theoretical and empirical analysis") or the more recent Arenas et al. (PODS 2023) results on Shapley values for Boolean classifiers. Alternatively, a direct reduction from #DNF (which is #P-complete by Provan & Ball 1983) to the marginal-contribution computation would work but needs to be spelled out.

**2. Theorem 6.2's assumption is restrictive and not fully justified.**

The theorem requires the support predicate to be "definable as a monotone Boolean formula over the commitment variables (as holds for SLA predicates over ordering commitments)." This is a significant restriction:

- Not all query-derived supports are monotone. A tuple derived via difference (Section 3.3 notes difference can increase depth) may have a non-monotone support formula.
- The claim "as holds for SLA predicates over ordering commitments" is asserted without proof. An SLA predicate like "abort ratio ≤ 25%" is a threshold function (at most k of n variables are true), which is indeed monotone. But more complex SLA predicates (involving latency, which depends on the *order* of operations, not just which commitments are made) may not be monotone over the commitment variables.

The theorem should either (a) explicitly restrict to monotone support predicates and discuss when this holds, or (b) prove that the class of predicates arising from positive queries over the ordering basis is always monotone.

**3. The additive approximation (Proposition 6.3) is correct but the complexity claim needs qualification.**

The proposition states O(n/ε² · log(1/δ) · p(n)) time. This is correct for additive ε-approximation via the permutation-sampling estimator (standard from Shapley-value approximation literature). However:

- The proof says "compute the marginal contribution of i by evaluating the query under two determinations." This is correct only if v(C) can be computed exactly for any given C. But v(C) = |{D ∈ S : D agrees with D* on C}| / 2^{n−|C|}, which requires counting support elements consistent with a partial assignment—itself a #P-hard problem in general. The sampling approach actually requires *sampling* from the conditional distribution, not computing v(C) exactly.

- The correct argument is: sample a random permutation π, sample a random completion of the uncommitted variables (uniform over {0,1}^{n−|C|−1}), and check whether the resulting determination is in S (one query evaluation). This gives an unbiased estimate of the marginal. The paper should clarify this.

**4. The relationship to existing Shapley-value-in-databases work is too thin.**

The related work mentions Livshits et al. [18] in one sentence and Meliou et al. [20] in a comparison sentence. Given that Section 6 is an entire technical section on Shapley values, the related work should discuss:

- How determination responsibility relates to the *Shapley value of a fact* in query answering (Livshits et al. ICDT 2021): both define cooperative games over a space of "possible inputs," but the players differ (tuples vs. commitments) and the value functions differ (query output vs. conditional probability of tuple presence).
- Whether the tractability boundary (conflict treewidth) relates to known tractability boundaries for Shapley values in databases (e.g., hierarchical queries, bounded hypertreewidth).
- Whether the multi-layer conditioning (Section 6, multi-layer paragraph) has analogs in the causal-responsibility literature (e.g., Halpern-Pearl structural equations with sequential interventions).

**5. The multi-layer responsibility definition is informal.**

The multi-layer paragraph says responsibility at layer k is "the Shapley value in the presence game conditioned on layers 1,...,k−1 being discharged." But what does "conditioned on" mean formally? Is the game at layer k defined over the residual specification Spec | (L₁ ▷ ... ▷ L_{k-1}), with the support being the set of layer-k completions that produce the tuple? This should be a definition, not a paragraph.

## Questions for the Authors

1. Can you give a concrete example where the support formula is *not* monotone over commitment variables? Does this arise for natural queries, or only for contrived ones?

2. For the approximation: do you sample v(C) or compute it exactly? If sampling, what is the variance bound?

3. Is there a relationship between conflict treewidth and the hypertreewidth of the query? In the Shapley-for-tuples setting, query structure governs tractability; here it seems to be the commitment structure instead. Is that a fundamental difference or an artifact of the formulation?

4. For multi-layer responsibility: does the efficiency axiom still hold per-layer? That is, do the layer-k responsibilities sum to v_k(N_k) − v_k(∅) for the layer-k game?

## Minor Comments

- The label `prop:fpras` should be renamed since it is no longer an FPRAS.
- Definition 6.3 says "commitments that share a transaction" — this should be more precise: two ordering commitments φ_{Ti≺Tj} and φ_{Tk≺Tl} share a transaction iff {Ti,Tj} ∩ {Tk,Tl} ≠ ∅.
- The efficiency property "∑ᵢ ρ(φᵢ,t) = v(N) − v(∅)" should note that v(N) − v(∅) can be negative (if D* ∉ S but |S|/2^n > 0, then v(N) = 0 < v(∅)). In that case responsibilities can be negative, which is fine for Shapley values but should be acknowledged.
- Example 6.1 computes responsibility ≈ 0.08 for the 25% SLA case. It would strengthen the example to show the actual Shapley computation for at least one commitment (even informally) rather than just stating the result.

## Overall Recommendation

**Weak Accept.**

The paper introduces a well-motivated framework with a genuine contribution in Section 6. The presence game is novel, the treewidth tractability result is the right kind of structural insight, and the connection between the filtration and the stopping criterion for responsibility is elegant. However, the #P-hardness proof needs repair (wrong citation, missing reduction details), the treewidth theorem's monotonicity assumption needs explicit justification, and the approximation argument has a gap (sampling vs. exact computation of v(C)). The multi-layer definition should be formalized. The related work on Shapley values in databases needs expansion given the prominence of Section 6.

Despite these issues, the conceptual contribution is solid: lifting responsibility from data tuples to semantic commitments is a meaningful generalization, and the structural parameter (conflict treewidth) is natural and practically motivated. With the technical fixes, this would be a good PODS paper.
