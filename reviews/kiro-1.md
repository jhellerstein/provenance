Let me continue reading the rest of the paper.

I've now read the full paper. Here's my review, written from the perspective of a PODS reviewer.

---

## PODS Review: "Determination Provenance: From Ambiguity to Algebra"

### Summary

The paper introduces *determination provenance*, a new dimension of provenance that captures the semantic commitments (e.g., serialization orders, negation-cycle resolutions) that must be made before classical derivational provenance is even well-defined. The supports of determination provenance form a Boolean algebra with a filtration of sub-semirings reflecting the layered commitment structure. The framework is instantiated for transactions (across isolation levels) and Datalog with negation (recovering stratified, well-founded, and stable-model semantics as filtration levels). A Shapley-value responsibility measure is defined and shown #P-hard in general but FPT in support treewidth.

---

### Strengths

1. **Genuinely novel conceptual contribution.** The observation that provenance has a "semantic resolution" dimension orthogonal to derivation is clean and well-motivated. The paper identifies a real gap: classical provenance presupposes a resolved semantics, but many systems operate under ambiguity.

2. **Unifying power.** The filtration theorem for Datalog negation (Theorem 5) is elegant—recovering three classical semantics as prefixes of a single algebraic object is a satisfying result that reframes well-known material.

3. **Monus elimination (Theorem 6)** is a nice structural insight: layered monotone semirings are support-equivalent to semirings-with-monus, giving a cleaner decomposition of non-monotone provenance.

4. **The responsibility section** connects to a well-studied game-theoretic framework and gives a clear tractability frontier (treewidth of the conflict graph).

5. **Writing quality** is generally high. The paper is well-structured and the running example is carried through effectively.

---

### Weaknesses and Suggestions

#### Major Issues

**M1. The determination semiring is trivial (Boolean algebra on subsets of D).**
The paper acknowledges this ("The Boolean algebra on supports is elementary (and idempotent)") and argues the non-trivial content is the filtration. But a PODS reviewer will ask: what algebraic work is the semiring actually doing that you couldn't do with plain set-membership tracking? The filtration is a partition-refinement structure on a finite set—it's combinatorially interesting but algebraically thin. The paper needs to make a stronger case for why calling this a "semiring" adds value beyond the vocabulary. Specifically:
- Is there a universality result (analogous to N[X] for positive RA)? You flag this as open but it's the result that would justify the algebraic framing.
- Does the semiring structure enable new *algorithms* (not just new *vocabulary*) for computing provenance?

**M2. The transactional instantiation is underdeveloped relative to its prominence.**
The paper devotes significant space to transactions but the formal results are thin: Proposition 3.5 (depth by isolation level) is stated without proof, and the "expressive power beyond classical provenance" paragraph lists capabilities (robustness, counterfactuals, tail bounds) without demonstrating any of them algorithmically. The reader is told determination provenance *enables* these queries but not *how* to compute them efficiently. For a PODS submission, at least one of these should be developed into a concrete algorithm with complexity bounds.

**M3. The Datalog negation theorem (Theorem 5) has restrictive assumptions.**
The theorem requires "independent final negative SCCs resolved by binary choice predicates." The generalization to nested cycles (Appendix, Theorem A.4) is more realistic but is relegated to the appendix. For PODS, the main-body theorem should state the general result (or at least acknowledge the restriction more prominently and explain why it's not merely a toy case).

**M4. Relationship to probabilistic databases is underexplored.**
The paper notes that determination provenance "shares the support-set structure" with possible-worlds models but "adds the filtration." This distinction needs sharper formalization. Specifically: is there a formal sense in which the determination semiring is *not* a special case of the lineage semiring over possible worlds? The filtration adds structure, but is it structure that couldn't be encoded as a constraint on the world-set? A PODS reviewer familiar with Suciu et al. will want this boundary drawn precisely.

**M5. No experimental or algorithmic evaluation.**
The paper is purely theoretical, which is fine for PODS, but the responsibility section promises tractability "when contention is narrow" without any concrete evidence that real workloads have bounded conflict treewidth. Even a brief analysis of treewidth in TPC-C or similar benchmarks would strengthen the practical relevance claim.

#### Minor Issues

**m1. Definition 2.3 (Commitment) requires the result to be a "proper subset."** This means a commitment must always exclude at least one outcome. But what about vacuous commitments (e.g., sealing a stratum that's already complete)? The persistence canonicalization (Appendix G) explicitly constructs non-filtering seals. The definition should either allow non-filtering commitments or clarify that seals are not commitments in the formal sense (they're guards that enable entailments).

**m2. The notation $H \cdot \varphi$ (appending a commitment after all maximal events) conflates the commitment with its position in the history.** This works for the retrospective setting but would break down for online/streaming determination. The paper should note this limitation explicitly.

**m3. Theorem 3.1 (Resolution is necessary and sufficient for provenance) is somewhat tautological.** The "necessity" direction says that if outcomes disagree on a fact, no single annotation works—but this is just restating the definition of ambiguity. The "sufficiency" direction is immediate from Green et al. The theorem's value is as a framing device, not a technical contribution; it should be presented as such (perhaps as an observation or remark).

**m4. The filtration definition (Section 3.2) uses "agreement at level k" defined inductively, but the base case ($D \equiv_0 D'$ always) means $\mathcal{F}_0 = \{\emptyset, \mathcal{D}\}$ regardless of the specification.** This is correct but worth noting: the filtration's content comes entirely from levels $\geq 1$. Level 0 is vacuous.

**m5. Corollary 3.8 (query evaluation respects filtration) is stated for positive RA only.** The paper notes that difference can increase depth (Proposition in appendix) but doesn't discuss what happens under semi-join, anti-join, or aggregation—operations central to the transactional and Datalog settings the paper targets.

**m6. The "three forces" paragraph (Section 2.3) references [hellerstein2026complexity] but doesn't give enough context for a reader unfamiliar with that paper.** The distinction between commitments (operating on $2^O$) and entailments (operating on $O$ via $\preceq$) is crucial to the entire framework but is introduced in a single paragraph without a formal definition of "entailment."

**m7. Several forward references to appendix material are never fully discharged in the body.** For example, "Proposition~\ref{prop:persistence-canon}" is referenced in Section 2 but the proposition appears only in Appendix G. For a PODS submission with page limits, the body should be self-contained for the main claims.

**m8. The related work on consistent query answering (Arenas et al.) deserves more depth.** Certain answers = robustness under repairs; your robustness = certain answers under determinations. The structural difference (flat repairs vs. layered determinations) is noted but the *algorithmic* relationship is not: are there reductions between the two problems? CQA has a rich complexity landscape that could inform your tractability results.

---

### Questions for the Authors

1. Can you give a concrete example where the filtration enables an algorithm that a flat possible-worlds model cannot support efficiently?
2. For the transactional setting: what is the complexity of computing the support of a tuple given a conflict graph and a UCQ? (This seems like the natural computational problem but is never stated.)
3. The monus elimination theorem (Theorem 6) claims support equivalence. Does it extend to full provenance equivalence (not just supports) for semirings beyond the Boolean case?

---

### Overall Assessment

The paper identifies a genuine and important gap in provenance theory and proposes a clean conceptual framework to fill it. The unification of negation semantics via the filtration is the strongest technical result. However, the algebraic contribution is thinner than the framing suggests (the semiring is just a Boolean algebra; the real content is the filtration), the transactional instantiation lacks algorithmic depth, and the restrictive assumptions on the Datalog theorem weaken the generality claim. The paper reads more as a "foundations and framework" contribution than a paper with deep technical results—which is valuable, but needs to be positioned honestly.

**Recommendation:** Borderline accept. The conceptual contribution is strong enough for PODS if the authors can (a) sharpen the distinction from probabilistic databases, (b) develop at least one algorithmic result for the transactional setting, and (c) state the Datalog theorem in its general form in the body.

---

Here's what I'd prioritize in 10 days, ordered by impact-per-hour:

## Days 1–3: One concrete algorithm for the transactional setting

This is the biggest gap. Pick the most natural computational problem—I'd go with:

**Problem:** Given a conflict graph $G$, a UCQ $Q$, and a tuple $t$, compute $\mathrm{supp}(P(t))$ (or decide robustness).

You already have the coNP-completeness of robustness. What's missing is the positive side: an algorithm that exploits structure. The conflict-treewidth parameter is already there (Theorem 5.4), but it's stated only for responsibility. Write a dedicated theorem that says:

> For single-layer determinations where the conflict graph has treewidth $w$ and the query is a UCQ of size $q$, the support of any output tuple can be computed in time $O(2^w \cdot \mathrm{poly}(n, q))$.

This is likely straightforward (it's weighted model counting on a bounded-treewidth formula), but stating it explicitly and working through the reduction from "support computation" to "model counting on the primal graph" gives the paper a real algorithmic result in the body. It also lets you say something concrete about TPC-C: the conflict graph of a partitioned OLTP workload has treewidth bounded by the number of cross-partition transactions, which is small by design.

## Days 3–5: Sharpen the probabilistic-databases distinction

This is the question a knowledgeable reviewer will fixate on. The answer is already implicit in the paper but needs to be made explicit. I'd add a subsection (or a remark + proposition) in Section 3 that says:

1. **Syntactically**, the determination semiring on supports is isomorphic to the lineage semiring over a world-set $\mathcal{D}$. No claim otherwise.

2. **The filtration is additional structure that world-sets don't carry.** Formally: two specifications can have identical world-sets (same $\mathcal{D}$, same supports for every tuple) but different filtrations—because the filtrations encode the *causal layering* of commitments, not just which worlds support which tuples.

3. **Algorithmically, the filtration enables early termination.** If $\mathrm{qdepth}(t) = k$, you can decide robustness by examining only the first $k$ layers—exponentially fewer worlds when $k \ll d$. In a flat possible-worlds model, you'd have to enumerate all of $\mathcal{D}$.

State this as a proposition with a concrete separation example (e.g., two specifications with $|\mathcal{D}| = 2^n$ but one has depth 1 and the other has depth $n$; robustness is decidable in poly time for the first but requires exponential enumeration without the filtration for the second).

## Days 5–7: Promote the general Datalog theorem into the body

Move Theorem A.4 (nested negative cycles, depth $k+d$) into Section 4 as the main theorem. Demote the current Theorem 5 to a corollary for the restricted case. The general statement is only slightly harder to parse and it eliminates the "toy case" objection. The proof sketch can stay short—point to the appendix for details—but the *statement* should be in the body.

## Days 7–8: Fix Definition 2.3 and the "entailment" gap

Two surgical fixes:

- Weaken Definition 2.3 to allow non-filtering commitments (or split into "strict commitment" and "guard/seal"), then note that the persistence canonicalization produces a non-filtering seal followed by a strict commitment. This removes the internal inconsistency.

- Add a formal definition of "entailment" (a refinement $o \mapsto o'$ with $o \preceq o'$ that does not exclude alternatives). Right now the three-forces framework is load-bearing but entailment is never defined. Two sentences and a definition environment fix this.

## Days 8–9: Trim and rebalance

The appendices are long (protocols, worked examples, systems lineage). For PODS page limits, I'd:

- Keep Appendices A (robustness proofs), C (det-semiring details), and D (Datalog worked example)—these support the main theorems.
- Condense Appendix E (protocols) to a single page summarizing the depth comparison table. The 2PL/MVTO details are interesting but not essential for acceptance.
- Condense Appendix F (systems lineage) to a half-page "discussion" paragraph in the conclusion. The Dapper example is nice motivation but doesn't carry formal weight.

Use the recovered space for the algorithm (days 1–3) and the PDB distinction (days 3–5).

## Day 10: Polish

- Downgrade Theorem 3.1 to an "Observation" (it's a framing device, not a technical contribution—own that).
- Add a one-paragraph discussion of CQA reductions after the related work on Arenas et al.
- Make sure every forward reference to an appendix proposition is either proved in the body or clearly flagged as "proof in appendix."

---

**Net effect:** The paper goes from "clean framework, thin results" to "framework + one real algorithm + one formal separation from PDB + general Datalog theorem in the body." That's enough to move it from borderline to solid accept territory at PODS.