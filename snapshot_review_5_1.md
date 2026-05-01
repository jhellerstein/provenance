# Review: "Provenance of Determinations: From Ambiguity to Algebra"
## Snapshot Review — May 1, 2026

### Overall Assessment

The paper introduces two algebraic objects—conditioned provenance and determination provenance—that extend semiring provenance to settings with semantic ambiguity. The commitment tower and determination semiring are clean constructions, and the instantiations in transactions and Datalog with negation are well-chosen. The paper fills a genuine gap: provenance theory has never handled the case where the *semantics itself* is ambiguous.

The paper is publishable at PODS with revision. The main issues are: (1) the algebraic contribution is thinner than it first appears, (2) the transactional instantiation is underdeveloped relative to the Datalog one, and (3) several claims are made without sufficient formal backing.

---

### Major Issues

**1. The commitment tower is described but not algebraically developed.**

Section 3.2 introduces the commitment tower as "a sequence of commutative monoids resting on a provenance semiring." But the paper never formally defines the tower as an algebraic object with operations, never proves any algebraic properties about it (e.g., associativity of discharge, functoriality), and never shows how to *compute* with it. The paragraph "Why the two algebras do not flatten" gestures at the issue but doesn't resolve it.

Compare with Green et al., who gave a universal construction (the provenance semiring N[X]) and proved that it was the most general semiring for positive relational algebra. Here, the tower is presented descriptively—"each layer is a monoid, they compose sequentially"—but there's no universal property, no free construction, no algebraic characterization of what makes a valid tower. This makes the "algebraic" claim in the title somewhat oversold.

**Suggestion:** Either develop the tower algebraically (define it as a graded algebraic structure with explicit composition laws and prove a universality result), or be more modest in the claims—say it's a *structural description* of how provenance decomposes under semantic ambiguity, not a new algebra per se.

**2. The determination semiring is just the Boolean algebra 2^I.**

Section 3.3 identifies the determination semiring as $(2^{\mathcal{I}}, \cup, \cap, \emptyset, \mathcal{I})$. This is a known object—it's a finite Boolean algebra. The paper acknowledges the connection to PosBool(B) from Green et al. but doesn't develop what's *new* about using it in this context beyond the observation that "determinations play the role of tuple annotations."

The novelty is in the *interpretation* (supports track which resolutions support a tuple), not in the algebra itself. That's fine, but the paper should be more explicit that the algebraic machinery is inherited from Green et al. and the contribution is the semantic framework that makes it applicable.

**3. The transactional instantiation (Section 4) is sketchy.**

The running example (Example 1) is good, but Section 4 doesn't formally define the commitment basis for serializability. It says "ordering commitments $\varphi_{T_i \prec T_j}$" and "abort commitments" but never gives a precise definition of when these are valid, when they commute, or how determination depth is computed for a given conflict graph. The claim "depth arises from overlapping abort decisions" (Example 4.2) is stated but not proved.

By contrast, the Datalog instantiation (Section 5) is much more carefully developed—Proposition 5.1 is stated and proved, the three semantics are compared precisely, and the determination structures are explicit.

**Suggestion:** Bring Section 4 up to the level of Section 5. Define the commitment basis formally. State and prove a proposition about when ordering commitments commute. Give a precise characterization of determination depth in terms of conflict-graph structure (e.g., "depth equals the maximum number of overlapping cycles in the conflict graph" or whatever the correct statement is).

**4. Theorem 2.1 (resolved specs are history-monotone) is central but the proof is deferred.**

The paper says "Full proof in Appendix A" but the appendix proof sketch (Proposition A.1) is only two sentences. This theorem is load-bearing—it's what justifies the entire framework (classical provenance applies once the tower is discharged). A PODS reviewer will want to see the proof, and it should be straightforward enough to include in the body or at least give a complete proof in the appendix.

**5. Layer certificates (Section 3, paragraph + Appendix B) feel underdeveloped.**

The query monotonicity theorem (Appendix B) is trivial—it's just "if you need to preserve more queries, you need more information." The certificate framework is introduced as a contribution but doesn't have enough depth to justify that claim. Either develop it further (give non-trivial sufficient conditions for when a certificate exists, or show a complexity result about finding minimal certificates) or demote it from a listed contribution to a remark/discussion.

---

### Minor Issues

**6. The abstract lists four contributions but the paper delivers them unevenly.**

Contribution (i) (conditioned provenance / commitment tower) is described but not algebraically developed. Contribution (ii) (determination semiring) is clean but inherits its algebra from Green et al. Contribution (iii) (layer certificates) is underdeveloped. Contribution (iv) (instantiations) is solid for Datalog, sketchy for transactions. Consider either developing (i) and (iii) further or reducing the claimed contributions to match what's delivered.

**7. Definition 2.5 (Persistent commitment basis) — the relationship to irrevocability is unclear.**

Persistence says: once $\varphi$ excludes $o$ at $H_1$, it continues to exclude $o$ at $H_2 \sqsupseteq H_1$. But Definition 2.3 already says commitments satisfy "shrinkage": $\Spec(H') \subseteq \Spec(H)$ for every $H' \sqsupseteq H \cdot \varphi$. How are these different? Shrinkage says the admissible set can only shrink after a commitment. Persistence says individual exclusions are preserved under history extension. Are these not the same thing? If they differ, an example distinguishing them would help.

**8. Section 2.4 (Resolution Induces Monotonicity) — the CALM comparison is confusing.**

The paragraph distinguishing history-monotonicity from CALM monotonicity is important but hard to follow. The key distinction (containment *within* O vs. containment *in* 2^O) is stated but could use a concrete example showing a specification that is history-monotone but not CALM-monotone, and vice versa.

**9. Figure 1 — the table is hard to parse.**

Panel (B) mixes notation inconsistently. The SER rows use set notation $\{\varphi_{T_1 \prec T_Q}, ...\}$ (suggesting a single commuting layer), while the SI row uses $\seq$ notation (suggesting multiple layers). But the depth column says "1" for SER and "O(|H|)" for SI. The visual presentation doesn't make the depth distinction clear. Consider separating the layers visually (e.g., using | or explicit "Layer 1: ..., Layer 2: ...").

**10. The "TODO" comment in Figure 1.**

There's a `% TODO: Redesign panel (B)` comment on line 973. Remove before submission.

**11. Section 6 (Robustness) is too brief.**

The definitions of robustness and preservation are clean, but there's no theorem here—just definitions and examples. A natural result would be: "Robustness is decidable/computable given the determination semiring" or "Preservation from Spec to Spec' is coNP-complete" or something that gives the section teeth beyond definitions.

**12. Appendix D (Systems Lineage) is explicitly informal.**

The paper says "The treatment below is deliberately illustrative rather than fully formal." This is fine for an appendix, but it weakens the claim that determination provenance provides a "semantic foundation for systems lineage." Either formalize it or remove it from the contributions list and present it purely as motivation/future work.

**13. Notation: $\Spec | I$ vs $\Spec \mid I$.**

The paper uses both `\mid` and `|` for conditioning. Pick one and be consistent.

**14. The connection to the complexity paper is one-directional.**

The paper cites [hellerstein2026complexity] for determination depth but doesn't use any of its results beyond the definition. The exponential separation and conservation law from that paper have implications for provenance (e.g., the tower height is irreducible—you can't flatten it by enriching the basis). Mentioning this would strengthen the connection.

---

### Questions for the Author

1. Is there a universal property for the commitment tower? (i.e., is it the "most general" structure that decomposes provenance under semantic ambiguity, in the way N[X] is the most general provenance semiring?)

2. Can you give a non-trivial example where the determination semiring provides information that a simpler "robust/contingent" binary classification does not?

3. What is the computational complexity of computing determination provenance for the transactional instantiation? (The paper acknowledges |I| may be exponential but doesn't discuss tractable fragments.)

---

### Summary

The paper identifies a real gap (provenance under semantic ambiguity), proposes a clean conceptual framework (commitment tower + determination semiring), and instantiates it in two relevant domains. The Datalog instantiation is strong. The main weaknesses are: the algebraic development is shallower than the framing suggests, the transactional instantiation needs more formal development, and several claimed contributions (certificates, systems lineage) are underdeveloped. With revision to either deepen the algebra or moderate the claims, this is a solid PODS paper.
