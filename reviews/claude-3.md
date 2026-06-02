## Review: "Determination Provenance: From Ambiguity to Algebra"

This paper extends algebraic semiring provenance to settings with semantic ambiguity by introducing *determinations* — sequences of irrevocable commitments that narrow a relational specification to a function — and building a commutative semiring over the space of resolving determinations. The framework is instantiated for transactional systems and Datalog with negation, and a new Section 6 introduces *determination responsibility*, a Shapley-value measure of each commitment's contribution, with a tractability frontier in conflict treewidth. The paper is well-motivated, the core algebraic machinery is clean, and the filtration's recovery of classical negation semantics is genuinely striking. The addition of determination responsibility substantially improves the paper's technical depth. Several issues remain that a PODS reviewer is likely to flag.

---

### Major Issues

**1. Theorem 5.1 is stated for a restricted class that is not disclosed in the abstract or introduction.**

The theorem requires that the program's negative SCCs "are mutually independent and form a *single final choice layer*." This means all negation cycles must be in the last stratum — a significant restriction that rules out programs with multiple strata of negation-in-cycle, or programs where cycles at one stratum feed into the stratification of a later one. Such programs would yield determinations of depth k+2 or more, and the correspondence claimed in the theorem table (stable/WFS/stratified as exactly layers k+1, k, k respectively) would not hold.

The abstract says "the classical negation semantics differ only in which filtration level they read" without qualification. The introduction similarly presents this as a general result. A PODS reviewer will find this overclaimed if the theorem's scope is limited to a subclass that excludes, for example, the simple program: `a ← ¬b. b ← ¬a. c ← ¬d. d ← ¬c. e ← a, c.` The abstract and Section 5 should scope the claim to the class covered by the theorem, or the theorem should be generalized.

**2. Theorem 6.1's proof cites the wrong source for the key hardness step.**

The proof says "#DNF problem under random restriction, which is #P-hard by reduction from #SAT [29]." Reference [29] is Valiant's 1979 paper on the permanent, not a result about #DNF counting. The specific hardness of computing Shapley values for Boolean formulas is non-trivial and has its own literature; in particular, the claim that marginal contributions in a DNF-support presence game are #P-hard requires either a careful direct reduction or a citation to results on Shapley values for monotone Boolean functions (e.g., Deng and Papadimitriou, or the Bachrach et al. line of work on Shapley values in weighted voting games). The current proof sketch is too compressed to verify and the citation does not support the claim as written.

**3. Theorem 6.2's proof assumes an unproven relationship between conflict treewidth and formula treewidth.**

The proof says "The support is a positive Boolean formula with primal-graph treewidth ≤ w." Conflict treewidth (Definition 6.3) is the treewidth of the graph connecting commitments that *share a transaction*. The primal graph of the support formula connects variables that *co-appear in a clause*. These graphs are related — shared-transaction commitments produce correlated support clauses — but they are not in general the same graph, and the treewidth bound does not follow immediately. If the support formula can encode interactions between commitments beyond their pairwise conflict structure, the formula's primal treewidth could exceed the conflict treewidth. This gap needs either a formal lemma or a more careful construction showing that the support formula's structure is controlled by conflict adjacency.

**4. Proposition D.4 (Reachability) has no proof.**

This proposition claims every filtration level 0 ≤ k ≤ d is realized as the query-relative depth of some tuple. No proof or proof sketch is given. The existence of a tuple at each depth is non-trivial: it requires constructing, for each k, a base fact or query whose support is a union of level-k classes but not of any level-(k−1) class. The proposition should be proved (the construction is not difficult — a base fact present in exactly the determinations that agree on a specific layer-k choice suffices) or clearly labeled as a claim awaiting proof.

**5. The "why-not under ambiguity" claim lacks formal grounding.**

The abstract and Section 5 claim that determination provenance "explains why-not under ambiguity: an atom can be absent not because of a blocked derivation but because of a semantic commitment." The example is correct — s(c) is absent under D^(r) because of φ_{r(c)=t}, a commitment rather than a derivational failure. But there is no definition of *why-not determination provenance* and no formal theorem distinguishing semantic absence from derivational absence. For a PODS audience familiar with Buneman et al. [6] and Köhler et al. [16], the claim needs either (a) a definition of the absent case of determination provenance parallel to Definition 3.1, or (b) a precise statement of what the framework provides for absent tuples beyond the support structure. As written, the claim amounts to an observation, not a contribution.

---

### Moderate Issues

**6. The related work treatment of Shapley values in provenance is insufficient given Section 6.**

Section 6 is an entire new technical section on determination responsibility as a Shapley value. The related work section compares to Meliou et al. [20] in one sentence. This omits relevant recent work: Livshits et al. (PODS 2021, "Shapley decomposition of query answers") and Deutch et al. on responsibility in provenance. These papers compute Shapley values for *data tuples*; determination responsibility computes them for *semantic commitments*. The distinction is real and worth making explicitly, but the comparison needs to be more substantive than a single contrast sentence.

**7. Lemma 2.1 (History-invariance) uses an undefined term in the main body.**

The lemma hypothesis refers to "a prefix H ⊑ H* containing the dependency set of D." "Dependency set" is defined only in Appendix I (Definition I.1), which is not required reading. A reader of the main body cannot evaluate the lemma's hypothesis. Either define dependency set in Section 2 or rephrase the lemma to avoid the term (e.g., "for any H ⊑ H* such that all events relevant to D's commitments have occurred in H").

**8. The abstract's framing of the contributions has shifted in a way that undersells robustness.**

The coNP-completeness of robustness is now in a parenthetical in contribution (iv): "Robustness is coNP-complete (Appendix A)." This was a main contribution in earlier versions and is still the primary complexity result. Demoting it to a parenthetical while promoting determination responsibility to top billing creates an asymmetry: the hardness result is in an appendix but is more fundamental (it bounds what any algorithm can do), while responsibility is in the body but is a follow-on result that presupposes the support structure. Consider either restoring robustness to a named contribution or noting that it is in Appendix A by design rather than apparent demotion.

**9. The uniform-distribution assumption in Definition 6.1 is too quietly handled.**

The presence game assumes "the remaining commitments are resolved uniformly at random." The parenthetical note that "the definition extends to an arbitrary product distribution μ...with the same tractability boundary" is important enough to deserve a proposition statement, not a parenthetical. In the SLA-diagnostic application (Example 6.1 and Appendix H), actual schedulers have strong non-uniform biases (FIFO, priority, load-based). A user applying determination responsibility to a real system will want to know whether the tractability result holds for their actual distribution. If it does for all product distributions, say so formally.

**10. "Normal" Datalog program is undefined in the main text.**

Theorem 5.1 applies to "finite normal Datalog programs." In logic programming, "normal" typically means at most one negative literal per rule body. This assumption should be stated explicitly, and its role in the theorem should be explained (it ensures the choice predicates are binary, supporting the single-final-layer structure).

---

### Minor Issues

**11.** The finiteness argument for D in Section 3.1 says "length at most |Spec(H)| − 1." The intended bound is |Spec(H₀)| − 1 where H₀ is the initial history; the phrasing "Spec(H)" is ambiguous since H changes as commitments are applied. Tighten to reference the initial admissible set.

**12.** Proposition 4.1 proves commutativity for independent transactions but Remark 4.1 only informally asserts non-commutativity under shared conflicts. Since depth > 1 is the paper's main structural parameter, consider adding a one-line formal corollary: "If T_i and T_j share a conflict cycle, φ_commit(Ti) and φ_commit(Tj) do not commute."

**13.** Definition 6.3 (conflict treewidth) defines the treewidth of the graph connecting commitments that "share a transaction." The phrase "share a transaction" is slightly ambiguous — it presumably means the two commitments each involve a transaction that participates in the same conflict edge, but this should be made precise given that Theorem 6.2's tractability result depends on it.

**14.** In Appendix I, Proposition I.1(b) says "the seal is non-filtering at H: Spec(H · φ_seal(S)) = Spec(H)." This is the key step that makes the canonicalization "invisible," but it relies on H being a prefix of H* where S has stabilized. The proposition statement should make explicit that this is a property of the specific history H, not of the seal predicate in general — otherwise a reader might conclude that seals never filter, which is false.

**15.** The paper uses ⊲⊳ for join and ⊲ for layer sequencing consistently throughout — a clear improvement over earlier versions. However, in Appendix D.1 (Proposition D.1), the join is written as "t₁ ⊲⊳ t₂" in the proof but the relation algebra statement uses "supp(P(t₁ ⊲⊳ t₂))" — given the similarity to ⊲, a brief reminder in a footnote or notation section that ⊲⊳ denotes join would help readers who encounter the appendix without reading through the body carefully.

---

### Overall Assessment

This is a substantially improved paper with a genuine and novel contribution. The determination semiring, the filtration, and the recovery of negation semantics are the core results and they are well-developed. Section 6 adds real technical content. The most important fixes before submission are: (1) scoping Theorem 5.1's claim in the abstract and introduction to match its actual hypothesis; (2) repairing the hardness proof for Theorem 6.1 with a precise citation or argument; (3) addressing the treewidth gap in Theorem 6.2; and (4) adding a proof of Proposition D.4. The why-not claim should either be formalized or modestly restated. These are real issues but not fundamental obstacles; the paper's core contribution is solid.