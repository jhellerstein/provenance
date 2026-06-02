## Review: "Determination Provenance: From Ambiguity to Algebra"

### Summary

This paper introduces determination provenance, extending classical semiring provenance to settings where multiple admissible outcomes exist for the same input. The space of resolving determinations forms a commutative semiring with a filtration that query evaluation respects. The framework is instantiated for transactional systems and Datalog with negation, where the classical negation semantics (stratified, well-founded, stable-model) are shown to correspond to different filtration levels for a restricted class of programs. A new Section 6 introduces determination responsibility (Shapley values over commitments) with hardness and tractability results.

---

### Strengths

- **The filtration-recovers-semantics observation is genuinely novel.** The idea that stratified, well-founded, and stable-model semantics differ only in how much of the determination they discharge — and that this is reflected as a chain of sub-semirings — is a beautiful structural insight. It provides a new algebraic lens on a classical topic.

- **The framework is well-motivated and cleanly presented.** The progression from histories to specifications to commitments to determinations is natural. The key definitions are crisp.

- **Theorem 5.1 is now appropriately scoped.** The restriction to programs with mutually independent final negative SCCs is stated explicitly in the theorem, and the abstract says "for a natural class." This is honest and defensible.

- **The comparison to CQA is well-drawn.** The distinction between flat repairs (CQA) and layered determinations is precisely the right point to make.

- **The possible-worlds paragraph in related work is a welcome addition.** It directly addresses the obvious question and gives a clear answer (filtration + independence structure are the novelty beyond support sets).

---

### Weaknesses

**1. The WFS correspondence in the proof sketch remains the weakest link.**

The proof sketch for Theorem 5.1 says: "WFS computes the same sealing prefix and then applies the alternating fixpoint — an entailment that classifies each atom by whether it holds in all stable models (robust, t), none (robustly absent, f), or some but not all (contingent, u). This classification is exactly the support structure at filtration level k."

This is the key claim and it is stated without justification. The identification of WFS with "skeptical/credulous stable-model intersection" is a known result (Van Gelder, Ross, Schlipf 1991), but it holds only for specific program classes — in general, WFS can assign u to atoms that are true in all stable models (when the alternating fixpoint does not converge to the stable-model intersection). For the restricted class in Theorem 5.1 (independent final negative SCCs), the identification likely holds, but this should be stated as a lemma with a citation, not asserted in passing.

**2. The provenance values for negation-cycle atoms are uninformative.**

The determination provenance of r(c) is {(D^(r), 1)} — the provenance value is just the constant 1. This means that within a given stable model, the derivational provenance of a cycle atom carries no information beyond "it holds." This is inherent (cycle atoms are not derived from base facts via positive rules), but it limits the framework's explanatory power for exactly the atoms that most need explanation. The paper should acknowledge this limitation explicitly: determination provenance tells you *which* model supports the atom, but not *why* within that model (because there is no positive derivation to trace).

**3. The "why-not under ambiguity" claim is still observational, not formal.**

Section 5 says: "s(c) is absent because of the commitment φ_{r(c)=t} itself — not a blocked derivation but a semantic choice." This is a correct observation, but it is not formalized. There is no definition of "why-not determination provenance" and no theorem characterizing what the framework provides for absent tuples. The abstract's claim that the framework "explains why-not under ambiguity" is therefore somewhat overstated. A brief definition — even just "the why-not explanation for t under D is the complement of supp(P(t)), annotated with the commitments that exclude t" — would ground this claim.

**4. The relationship to Dannert et al. deserves more precision.**

The related work says "for stratifiable programs, our within-determination provenance coincides with theirs once the layers of sealing commitments are discharged." This is plausible but not proved. Dannert et al. work with a specific semiring construction for LFP; the paper should state precisely what "coincides" means (same semiring values? same support? same polynomial?) or weaken to "is analogous."

**5. The restriction in Theorem 5.1 makes the filtration degenerate for the covered class.**

For programs with k stratification layers and a single final choice layer, the filtration is F_0 = F_1 = ... = F_k = {∅, D} and F_{k+1} = 2^D. This means the filtration has only two non-trivial levels: the trivial one and the full powerset. The "chain of sub-semirings" is just {∅, D} ⊂ 2^D — a two-element chain. The filtration becomes interesting only for programs with multiple interacting choice layers (depth > k+1), which are outside the theorem's scope. The paper should acknowledge that for the class covered by Theorem 5.1, the filtration is structurally simple, and that richer filtrations arise for more complex programs (left to future work).

---

### Questions for the Authors

1. For programs with nested negative cycles (e.g., a cycle at stratum 2 whose resolution affects a cycle at stratum 4), would the determination have depth k+2 or more? If so, does the correspondence to WFS still hold at the intermediate levels?

2. The choice predicates φ_{a=v} are binary. For negative SCCs of length > 2 (e.g., a ← ¬b, b ← ¬c, c ← ¬a), the stable models are not simply binary choices on individual atoms. How does the commitment basis handle this? Is each stable model encoded as a conjunction of binary choices, or is a different commitment structure needed?

3. Does the framework say anything about programs with no stable models (e.g., a ← ¬a with no other rules)? The specification would have no resolving determination, making D empty. Is this a degenerate case or does it require special treatment?

---

### Minor Comments

- The definition of "normal" as "at most one negated body literal per rule" is non-standard. In logic programming, "normal" typically means rules may have any number of negated body literals (as opposed to "definite" which has none). The restriction to at most one negated literal per rule is sometimes called "simple" programs. Please verify the intended restriction and use standard terminology.

- The notation φ_seal(S_i) is used without a formal definition in the body (it is defined in the appendix). A one-line definition in Section 5 would help.

- The proof sketch says "stratified evaluation is unique (each stratum's least fixpoint is determined by the sealed strata below it)." This is correct but should cite the standard reference (Apt, Blair, Walker 1988 or similar).

---

### Overall Recommendation

**Weak Accept.** The paper presents a genuinely interesting algebraic framework with a striking application to Datalog negation. The filtration-as-semantics observation is novel and well-presented. The main weaknesses are: (1) the WFS correspondence needs a proper citation and justification for the restricted class; (2) the filtration is degenerate for the class covered by the theorem; and (3) the why-not claim remains informal. These are addressable in revision. The paper's conceptual contribution is strong enough for PODS, and the addition of determination responsibility gives it technical depth beyond the framework alone.
