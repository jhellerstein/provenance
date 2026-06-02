## Review: "Determination Provenance: From Ambiguity to Algebra"

This revision introduces two substantial conceptual additions: a reframing of the entire contribution around *non-monotone operations requiring completeness guarantees* (the "sealing commitment" unification), and Theorem 5.2 (monus elimination), which claims that layered monotone semirings subsume semirings-with-monus. The determination responsibility section is also better developed with compositionality results and a corrected hardness proof. These are meaningful improvements. Several new issues have been introduced alongside the old ones.

---

### What Has Genuinely Improved

**The "non-monotone as commitment" framing is the paper's most important conceptual advance.** The abstract's opening — "non-monotone operations require completeness guarantees before evaluation; determination provenance externalizes each such guarantee as a sealing commitment" — is a crisp, memorable thesis that was absent before. It gives the framework a unified rationale rather than presenting it as a collection of instantiations. This framing should be emphasized even more aggressively.

**The hardness proof for Theorem 6.1 is now correct.** Citing Deng and Papadimitriou for #P-completeness of Shapley values in weighted voting games is appropriate, and the embedding of presence games into weighted voting games is the right construction. This closes the most embarrassing technical error from the previous version.

**Proposition 6.4 (compositionality of responsibility under join and union) is new and conceptually useful.** The qualitative claim — joins concentrate responsibility, unions dilute it — is intuitive and has operational implications for scheduler design. The appendix on multi-layer responsibility is also well-motivated.

**The appendix on the general Datalog case (Appendix G.4) acknowledges the theorem's scope restriction** and sketches the extension. This is better than silence, though see below.

---

### Major Issues

**1. Theorem 5.2 (monus elimination) is overclaimed and the proof is incorrect for non-Boolean semirings.**

The theorem asserts equality between LFP provenance over $(K, \dot{-})$ and conditioned provenance over $(K, +, \cdot)$ with sealing, for *any* naturally ordered semiring $K$. The proof says the sealed-negation annotation is "t → 0_K, f → 1_K — a monotone lookup, not a monus" and that this equals the monus because "1_K ⊖ v = 0_K when v > 0_K."

This is only correct for Boolean-valued semirings. For $K = \mathbb{N}[X]$, the monus of a provenance polynomial is not simply "0 if nonzero, 1 if zero." The annotation $x_a$ (recording that atom $a$ was derived from base fact $x_a$) does not equal $0_K$ or $1_K$ — it is a polynomial. The monus $1_K \dot{-} x_a$ is not well-defined in $\mathbb{N}[X]$ as a polynomial (it would require subtraction), which is precisely why Dannert et al. work with the why-provenance semiring rather than $\mathbb{N}[X]$. The claim that determination provenance with sealing reproduces monus computation for arbitrary naturally ordered semirings appears to be false outside the Boolean case.

The contribution claimed — "monus elimination shows that layered monotone semirings subsume semirings-with-monus" — would be a significant result if true. As written, the proof does not establish it.

**2. Proposition 6.4 (responsibility under join and union) has an unconvincing proof.**

For joins, the claim is $\rho(\varphi_i, t_1 \bowtie t_2) \geq \max(\rho(\varphi_i, t_1), \rho(\varphi_i, t_2))$. The proof says "the join's support is $S_1 \cap S_2 \subseteq S_j$; removing $\varphi_i$ from the coalition can only make membership in the smaller set less likely, so marginal contributions are at least as large."

This argument is incorrect as stated. Shapley values don't behave monotonically under support set containment in general — the marginal contribution of player $i$ depends on the entire structure of the coalition function $v$, not just the size of the support. A correct proof would need to go through the game-theoretic definition and show that the presence game for the join stochastically dominates those for $t_1$ and $t_2$ in the right sense. The inequality may be true but the given argument doesn't establish it. This is a claimed proposition with a flawed proof in the main body — a PODS reviewer will notice.

**3. Theorem 6.2 (tractability at bounded conflict treewidth) still has the treewidth gap.**

The proof now says "the support is a monotone formula whose clauses involve only commitments sharing a transaction (a conflict edge). The primal graph of this formula is therefore a subgraph of the conflict graph."

This claim requires that the support formula only has "local" clauses — interactions between commitments that are directly conflict-adjacent. But a tuple's presence can depend on transitive ordering constraints: if $T_Q$ must see $T_i$'s write but not $T_j$'s delete, and $T_i$, $T_j$, $T_Q$ form a path in the conflict graph (not a triangle), then the support formula involves all three pairwise orderings, and the corresponding clause in the formula involves commitments $\varphi_{T_i \prec T_Q}$ and $\varphi_{T_j \prec T_Q}$ which share $T_Q$ but may not share a direct conflict edge with each other. The primal graph of the formula could have edges not present in the conflict graph. The claim needs a lemma establishing that the support formula's interaction structure is bounded by conflict adjacency.

**4. The general Datalog case (Appendix G.4) is insufficiently developed to constitute a contribution.**

Theorem 5.1 is restricted to programs where negative SCCs "form a single final choice layer." Appendix G.4 claims to extend this to nested cycles, asserting the determination has depth $k+d$ where $d$ is the DAG's longest path. But there are no theorems, no proofs, and no worked examples in this section — only bullet points. The most important claim — "WFS may access intermediate filtration levels when some cycle resolutions are entailed by others" — is stated without any formal support.

Given that this was the central criticism in prior reviews, and given that the paper's most striking result (Theorem 5.1) depends on a structural restriction that excludes many practical programs, the two-paragraph sketch in an appendix does not resolve the issue. Either prove the general case or be explicit in the main body that the theorem covers only a restricted class, and present the general structure as the primary open problem.

**5. Aggregation is mentioned in abstract and introduction but never developed.**

The abstract says "non-monotone operations—negation, conflict resolution, aggregation." The introduction repeats this. Aggregation provenance (e.g., Senellart's work, cited in related work as "operating at depth 0") is never shown to fit the determination framework. If aggregation requires sealing commitments, what are they? What is the commitment basis for an aggregation-over-negation program? Either develop this instantiation or remove "aggregation" from the claims.

---

### Moderate Issues

**6. Proposition D.4 (Reachability) still has no proof.**

The proposition that every filtration level $0 \leq k \leq d$ is realized as the query-relative depth of some tuple appears without proof for the third consecutive version. This should either be proved (the construction is not difficult: a base fact present in exactly the determinations that choose a specific value at layer $k$ has depth exactly $k$) or labeled as a claim.

**7. The note "(trivial until the choice layer; the theorem's value is the correspondence, not intermediate richness)" in Section 5 is editorially defensive.**

Authors should not preemptively argue against their own examples. If the filtration is trivial until the choice layer, simply state the filtration and move on. The parenthetical reads as though the authors are aware the example is thin and are trying to head off the criticism — which draws more attention to it.

**8. The monotonicity condition added to Theorem 6.2 is not adequately justified for the stated examples.**

The theorem now requires "a monotone support predicate over the commitment variables." The proof then claims "Monotonicity holds for threshold predicates ('at most k aborts'), upward-closed SLA conditions ('latency ≤ τ' when earlier serialization implies lower latency)." The parenthetical "when earlier serialization implies lower latency" is doing significant work — this is a non-trivial property of the workload that doesn't hold in general (a serialization that prioritizes a long analytics scan over short OLTP transactions may have lower abort rate but higher tail latency). This assumption should be stated explicitly as a condition on the workload, not absorbed into a parenthetical.

**9. The framing "subsumes semirings-with-monus" is a strong claim requiring a formal reduction.**

Contribution (iii) says monus elimination shows "layered monotone semirings subsume semirings-with-monus for provenance under negation." "Subsume" in a formal context means there is a simulation or embedding — every computation expressible with monus is also expressible (with the same result) using layered monotone semirings. As noted above, this is not established for $K = \mathbb{N}[X]$. If the result holds only for the Boolean semiring, say so.

---

### Minor Issues

**10.** The proof of Theorem 5.1 now says stratified evaluation is unique because "each stratum's least fixpoint is determined by the sealed strata below it, so no alternative sealing sequence exists." This is correct but should note that uniqueness of the sealing sequence is what makes the stratified prefix *shared* by all resolving determinations — without this uniqueness, different determinations might use different sealing prefixes, and $\mathcal{F}_k$ would not equal $\{\emptyset, \mathcal{D}\}$.

**11.** The paragraph on "Non-monotonicity as commitment" at the end of Section 3.3 reads as a preview rather than a result. It would read better as the opening paragraph of the Transactions section or as a bridging remark.

**12.** Lemma 2.1 (History-invariance) refers to "all events on which D's commitments depend" but this phrase is defined only in the persistence canonicalization appendix. A forward reference or brief inline definition would help readers of the main body.

**13.** The Additive Approximation (Proposition 6.3) changed from an FPRAS to an "additive approximation" between the previous and current versions. An additive ε-approximation for a value in [0,1] is weaker than a multiplicative FPRAS when the true value is small. For small responsibility values — precisely the case of a robust-near tuple where individual commitments matter little — an additive ε error could be larger than the true value. This limitation should be noted.

---

### Overall Assessment

The "non-monotone as commitment" reframing is a genuine conceptual advance that makes the paper's thesis more coherent and memorable. The hardness proof is now correct. The compositionality results for responsibility are new and useful.

The most urgent problems are Theorem 5.2 (monus elimination, which is overclaimed and likely wrong for $\mathbb{N}[X]$) and Proposition 6.4 (the join-responsibility inequality, whose proof is invalid). Both appear in the main body as named results and will not survive referee scrutiny. The treewidth gap in Theorem 6.2 also remains open. If the monus elimination theorem can be established correctly for an appropriate class of semirings, it would be a strong result worth featuring prominently; if not, the claim should be significantly narrowed.