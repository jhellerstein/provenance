Here is an independent review of the current draft, evaluated strictly on its own merits as a submission to the PODS (Principles of Database Systems) conference.

***

### **Reviewer: PODS Program Committee**

**Paper:** Determination Provenance: From Ambiguity to Algebra

#### **1. Summary of the Contribution**
This paper extends classical algebraic provenance to environments characterized by *semantic ambiguity*, where a single history can lead to multiple admissible outcomes (e.g., due to transactional concurrency or Datalog negation). The core conceptual innovation is the separation of "sealing commitments" (decisions that irrevocably shrink the space of admissible outcomes) from monotone entailments (standard query evaluation). The paper shows that the space of resolutions forms a commutative semiring—the determination semiring—whose layered structure yields a filtration. The framework is applied to transactional isolation levels and Datalog with negation. Furthermore, the paper introduces "determination responsibility," a Shapley-value-based metric for quantifying a commitment's contribution, showing it is #P-hard in general but Fixed-Parameter Tractable (FPT) with respect to conflict treewidth.

#### **2. Strengths**
* **Elegant Conceptual Ontology:** The classification of database transitions into "three forces" (environment events, commitments, and entailments) is a beautiful and clarifying framework. Decomposing non-monotone provenance into "sealing commitments" followed by monotone computation perfectly bridges the gap between systems-level non-determinism and classical monotone semiring theory.
* **Mathematical Sophistication:** Modeling non-commuting resolutions as a filtration of sub-semirings is a highly original approach in provenance theory. It provides a rigorous algebraic vocabulary for concepts (like stratification) that are usually treated purely logically or algorithmically. 
* **State-of-the-Art Complexity Analysis:** The introduction of determination responsibility and the subsequent parameterized complexity result (FPT bounded by conflict treewidth) is exactly the kind of deep algorithmic analysis PODS values. It elegantly connects provenance to the rich literature on probabilistic databases and query evaluation bounded by treewidth.
* **Strong Motivating Examples:** The running transactional example (Example 1.1) cleanly demonstrates why standard provenance fails under ambiguity and why capturing "why-not" explanations requires internalizing the schedule's semantic commitments.

#### **3. Weaknesses & Areas for Improvement (Constructive Criticism)**
While the theoretical core is exceptionally strong, a few structural and expositional choices pose risks given the strict rules and expectations of the PODS venue.

**A. The 15-Page Boundary and Datalog (Appendix G)**
* **The Issue:** The abstract and introduction heavily promise a unification of transactional ambiguity and Datalog negation (stratified, well-founded, stable models). However, the detailed treatment of Datalog semantics—specifically how WFS and Stable Models map to the determination structure—appears to be deferred to Appendix G. 
* **Why it matters for PODS:** PODS reviewers are explicitly instructed that material beyond page 15 is optional. Because the database theory community is deeply invested in Datalog semantics, reviewers will want to see the formal translation of logic programs into your algebraic filtration in the main text. 
* **Recommendation:** You must ensure that the core theorems equating the classical negation semantics to your filtration layers appear before page 15. It is acceptable to leave the long proofs or the "Nontrivial examples" in Appendix G, but the formal mapping and theorem statements are critical main-text material.

**B. Robustness and Parameterized Complexity**
* **The Issue:** The abstract notes that robustness (deciding if an outcome holds under every resolution) is coNP-complete (deferred to Appendix A). Later, you brilliantly show that the Shapley-value metric is FPT in conflict treewidth.
* **Recommendation:** It would vastly strengthen the paper to explicitly state how robustness behaves under the treewidth parameterization. Since computing Shapley values (#P-hard) is generally strictly harder than robustness (coNP-complete), does bounded conflict treewidth also make the robustness check PTIME/FPT? Explicitly connecting the tractability of robustness to your treewidth metric would perfectly round out the theoretical story.

**C. Clarifying the $K$-relation over Determinations**
* **The Issue:** Section 2 lays down a rigorous foundation for commitments, persistence, and resolving determinations. Theorem 2.1 establishes that resolution is necessary and sufficient for semiring provenance. 
* **Recommendation:** Ensure the main text explicitly defines the algebraic operations ($\oplus, \otimes$) of the determination semiring itself, and how it formally interacts with the underlying data semiring $K$. A brief, formal definition of the polynomials over the determination space will help theorists verify the algebraic claims without having to extrapolate from the text. 

#### **4. Summary Recommendation**
**Strong Accept.** This is a mathematically mature, conceptually ambitious paper that tackles a major blind spot in provenance theory. The framing of "sealing commitments" and the parameterized complexity results for Shapley-based responsibility are outstanding. To ensure the smoothest possible path through the PC, the authors should verify that the Datalog theorems and the formal definitions of the semiring operations do not spill past the 15-page limit, as these are exactly the elements the PODS audience will scrutinize most closely.