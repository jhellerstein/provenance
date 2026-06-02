## Review: "Determination Provenance: From Ambiguity to Algebra"

This is an ambitious paper tackling a genuine gap in provenance theory. The core insight — that classical semiring provenance presupposes a resolved semantics, and that many practically important systems operate under semantic ambiguity — is well-motivated and the algebraic development is largely clean. Here is detailed criticism aimed at strengthening the submission.

---

### Summary Assessment

The paper makes a real contribution but has a structural problem that a PODS reviewer will likely flag immediately: **the main body (≤15 pages) does not contain enough technically developed results to stand alone.** The abstract promises four contributions; most of the interesting technical content (Datalog instantiation, protocol comparison, systems lineage) lives in appendices that reviewers are not required to read. A reviewer who reads only pages 1–15 will encounter the framework, the transactional instantiation sketched at a fairly high level, and coNP-completeness — and may reasonably wonder whether the paper earns its claims.

---

### Major Issues

**1. The main body undersells the Datalog contribution.**

Section 5 is the paper's most striking result — the classical negation semantics (stratified, well-founded, stable) emerging as filtration levels of a single determination semiring is genuinely beautiful. But it is presented in under two pages, with no formal theorem statement and a brief worked example. The claim "the three classical negation semantics differ only in which filtration level they read" deserves a named theorem. As written, it reads as a sketch with a forward pointer to Appendix F, which reviewers need not read. Either compress something else in the main body to give this space, or promote a formal theorem from the appendix.

**2. The framework introduction (Section 2) is dense without adequate payoff visible early.**

The sequence Histories → Extensions → Outcomes → Specifications → Commitments → Determinations → Resolution is conceptually well-ordered but operationally opaque to a reader who does not yet know what kind of object the paper is building toward. A reader finishing Section 2 has absorbed six definitions and two theorems without yet seeing a worked example. Example 1.1 appears in the introduction but the formalism it uses (D_in, D_out, provenance notation) is not established until Section 3. Consider restructuring so that Example 1.1 is re-encountered *after* Section 2 gives the formal grounding — or add a small running example directly in Section 2 to make definitions concrete as they appear.

**3. Persistence is load-bearing but its necessity is insufficiently argued.**

Persistence (Definition 2.6) is described as "the paper's main structural assumption" and the examples of persistent bases are stated but not proven. More importantly, Theorem 2.1 (resolution is necessary and sufficient for provenance) and Lemma 2.1 (history-invariance) both depend on it, but the reader is not shown what goes wrong without it — beyond the brief "majority vote" counterexample. A reviewer will ask: is persistence necessary, or merely sufficient? Could you identify a weaker condition? Section 8 mentions eventual persistence as a candidate; this feels like it belongs in the body, not the conclusion, as it would justify that persistence is the right assumption rather than a convenient one.

**4. The determination semiring construction (Section 3.1) conflates two different objects.**

The paper defines determination provenance as a function D → K (pairing each determination with a classical provenance value), then separately identifies the *supports* as forming the Boolean algebra (2^D, ∪, ∩). The determination semiring is identified as this Boolean algebra on supports. But then the filtration is defined as a chain of sub-semirings of this Boolean algebra.

This creates a notational tension: sometimes "determination semiring" refers to (2^D, ∪, ∩) and sometimes to the K-valued function together with the support structure. Proposition 3.1 says each F_k is a sub-semiring of "the determination semiring," but F_k consists of *sets of determinations*, not K-valued functions. The two algebraic structures — the K-valued provenance function and the Boolean algebra on supports — need to be more carefully distinguished. A reader trying to formalize the composition laws in Proposition C.1 will run into this.

**5. Robustness complexity (Section 6) is correct but the reduction is too compressed.**

Theorem 6.1 is stated and proved, but the proof relies entirely on the enriched scheduling basis from Section 4.6, which is itself somewhat briefly treated. The three "polynomial conditions" in the proof sketch are asserted rather than verified. Condition (ii) in particular — "checking validity amounts to verifying that the conflict graph is acyclic (trivially true here, since no cycles exist)" — holds only because the construction guarantees no cycles, but this follows from the construction rather than being a general property of scheduling determinations. This should be stated explicitly to avoid giving the impression that validity checking is always trivial.

---

### Moderate Issues

**6. The comparison to consistent query answering (Section 7) undersells the difference.**

The paper notes correctly that repairs are "typically defined by minimal symmetric difference, yielding a flat (single-layer) structure." But the deeper difference — that CQA repairs arise from *data* inconsistency while determinations resolve *semantic* ambiguity in the *specification* — is worth emphasizing more. This distinction would help a reader understand why determination provenance cannot simply be seen as CQA with a different repair notion.

**7. The "why-not" claim needs more formal development.**

The abstract and introduction promise that determination provenance "addresses longstanding gaps in provenance for queries with negation and why-not explanations." This is a strong claim. Section 5 gives one example where an atom is absent due to a semantic commitment rather than a blocked derivation. But the paper does not give a formal account of *why-not determination provenance* analogous to Buneman et al.'s why-not provenance — it shows that the framework can distinguish semantic absence from derivational absence, but does not develop the explanation structure for the absent case. A PODS reviewer familiar with [6] will notice this gap.

**8. Figure 1 is useful but appears before all its cases are developed.**

Figure 1 appears at the end of Section 5 but references "Appendix F for Datalog negation," and the snapshot isolation row references Section 4.4 and Appendix D. For a figure that is meant to summarize the paper's two main instantiations, having most of its rows point to optional appendices is a liability. Consider either expanding the figure after Section 6 once all main-body content is established, or restricting the figure to cases fully developed in the body.

**9. The "three forces on a history" taxonomy (Section 2.3) is conceptually useful but formally underused.**

The environment/commitment/entailment trichotomy appears in Section 2.3 and is illustrated in Example 2.1. It reappears in Section 5 to distinguish the alternating fixpoint (an entailment) from a commitment. But it plays no role in the formal results — no theorem references it, it does not appear in any proof, and it does not appear in the robustness theorem. Either make it formally load-bearing (e.g., show that the depth characterization changes if entailments are misclassified as commitments) or trim it to a remark.

---

### Minor Issues

**10.** The phrase "the determination of a history D(H) is the subsequence of commitment events in H" (Definition 2.7) uses "determination" to mean both a sequence of commitments *applied to a spec* and a subsequence *extracted from a history*. These are the same object operationally, but the dual usage creates momentary confusion.

**11.** Proposition 3.4 (difference can increase depth) is proved with a correct but abstract argument. A concrete example — parallel to Example 3.2 — would help readers see why negation/difference is the culprit, rather than just verifying the algebra.

**12.** The claim "Classical provenance is the degenerate case where no commitments are needed" appears in both the abstract and Section 3.1. Since this is a key selling point, it deserves a brief formal corollary: when |D| = 1, the determination semiring is the trivial Boolean algebra and determination provenance coincides with Green et al.

**13.** Section 4.6 ("Scheduling as Commitment") introduces ordering commitments that significantly enrich the framework and are used in the hardness reduction. But the section is presented as an optional enrichment rather than a core part of the transactional instantiation. Since the complexity result requires it, consider integrating it into Section 4.3 rather than treating it as an afterthought.

**14.** The related work treatment of Köhler et al. [16] is slightly dismissive ("all three approaches assume a resolved semantics; our framework is complementary"). The paper would benefit from a more precise statement of what determination provenance gives you for the specific programs and queries studied in [16], rather than a purely structural comparison.

---

### Presentation

The writing is generally precise, which is appropriate for the venue. A few passages in Section 2 (particularly the paragraph on "three forces") read more like a conceptual essay than a technical paper; tightening these would improve the overall rhythm. The use of ⊲ for both layer sequencing in determinations (Definition 2.8) and join in relational algebra (Corollary 3.1, Proposition C.1) is a notation clash that should be fixed.

---

### Summary of Recommendations

The core algebraic framework is sound and the contributions are real. The most important revisions are: (1) promote the Datalog/filtration result to a named theorem in the main body; (2) clarify the relationship between the K-valued provenance function and the Boolean algebra on supports; (3) give a more formal treatment of the why-not claim; and (4) ensure the main body (pages 1–15) can be evaluated on its own merits. The appendices are rich and the paper will be stronger for the PODS audience if the best results there are surfaced into the body.