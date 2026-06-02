# Simulated PODS Review — Meghyn Bienvenu (CNRS, University of Bordeaux)

**Paper:** Determination Provenance: From Ambiguity to Algebra

## Summary

The paper introduces "determination provenance," extending classical semiring provenance to settings where multiple admissible outcomes exist for the same input. The key construction is a "determination semiring" on supports (subsets of resolving determinations) equipped with a filtration reflecting the layered commitment structure. The framework is instantiated for transactional concurrency and Datalog with negation, with the latter yielding the claim that stratified, well-founded, and stable-model semantics correspond to different filtration levels of a single algebraic object.

## Strengths

- **Conceptually appealing unification.** The idea that the three classical negation semantics for Datalog can be viewed as reading different levels of a single filtered algebraic structure is elegant and, if correct, provides a genuinely new perspective on the relationship between these semantics.

- **Clean separation of concerns.** The distinction between "which commitments were made" (determination) and "how was the result derived given those commitments" (classical provenance) is well-motivated and clearly articulated.

- **The filtration is the right contribution.** The paper correctly identifies that the support semiring (2^D, ∪, ∩) is elementary, and positions the filtration—and its interaction with query evaluation—as the novel algebraic content. This is honest and appropriate.

- **Robustness = skeptical reasoning.** The observation that robustness in the determination semiring coincides with skeptical reasoning under stable models, and that the coNP-completeness follows from the same width-based mechanism, is a satisfying validation.

- **The WFS correspondence via the alternating fixpoint** (proof sketch of Theorem 5.1 and Appendix F) is the most interesting technical claim. The idea that the alternating fixpoint is an *entailment* (operating on the outcome order) rather than a *commitment* (operating on the admissible set) is a useful conceptual distinction.

## Weaknesses

**1. Theorem 5.1 restricts to a narrow class but the presentation suggests generality.**

The theorem applies to "finite normal Datalog programs whose negative SCCs are mutually independent and form a single final choice layer." This is a significant restriction. Programs with nested negative cycles, or where negative SCCs interact through positive recursion, are excluded. The paper should be more explicit about what fraction of "interesting" normal programs this covers. In particular:

- Programs like `p ← ¬q`, `q ← ¬r`, `r ← ¬p` (an odd cycle) have a single negative SCC but it is not binary—it requires ternary choice predicates. Does the theorem apply?
- Programs where a negative SCC feeds into another negative SCC (nested cycles) are excluded. This is a common pattern in answer set programming.

The abstract says "the classical negation semantics differ only in which filtration level they read" without qualification. This is misleading for the general case.

**2. The relationship between WFS and the filtration is stated but not proved in the body.**

The proof sketch says: "WFS computes the same sealing prefix and then applies the alternating fixpoint—an entailment that classifies each atom by whether it holds in all stable models (robust, t), none (robustly absent, f), or some but not all (contingent, u). This classification is exactly the support structure at filtration level k."

This is the key claim and it is asserted, not argued. The identification of WFS truth values with support classifications relies on a non-trivial fact: that the well-founded model of a program (in the restricted class) assigns **t** to an atom iff it is true in every stable model, and **f** iff it is false in every stable model. This is known to hold for "normal programs with stable models" (a result going back to Van Gelder, Ross, and Schlipf), but:

(a) The paper does not cite this result explicitly.
(b) The result requires that the program *has* stable models. Programs without stable models (e.g., `p ← ¬p` alone) have a well-founded model but no stable models. What does the determination semiring look like in this case? Is D empty?
(c) The restricted class in Theorem 5.1 guarantees stable models exist (binary choice on independent cycles always yields models), but this should be stated as a lemma.

**3. The comparison to consistent query answering is too brief and misses key distinctions.**

The related work says repairs are "flat, single-layer" while determinations are "layered, non-commutative." This is true but superficial. A deeper comparison would note:

- In CQA, the set of repairs is defined *extensionally* (all maximal consistent subsets, or all subsets at minimal symmetric difference). In determination provenance, the set D is defined *intensionally* via a commitment basis. This means D depends on the choice of basis—a point the paper acknowledges but does not explore for the Datalog case.
- CQA has a rich complexity landscape (FO-rewritability for certain primary-key constraints, coNP-completeness for general denial constraints, etc.). The paper's coNP result for robustness is analogous to the coNP-completeness of certain-answer computation for general CQA, but the tractability landscape is unexplored. Are there "safe" commitment structures (analogous to primary keys) where robustness is in PTIME?

**4. The enriched outcome domain (⊥, u, t, f) is non-standard and its relationship to Belnap's four-valued logic or Fitting's bilattice is not discussed.**

The outcome order ⊥ ⪯ u ⪯ {t, f} is essentially the knowledge ordering of Belnap's FOUR. The paper uses this without acknowledgment. For a PODS audience familiar with Fitting's work on logic programming semantics over bilattices, this omission is notable. It also raises the question: is the enriched domain necessary, or could the framework work with standard two-valued outcomes plus a separate "undetermined" status at the meta-level?

**5. The "sealing" commitment for Datalog is not formally defined in the body.**

Section 5 says: "sealing predicates φ_seal(S_i) (stratum S_i is complete—excludes outcomes where additional atoms in S_i are true)." But what does "additional atoms" mean formally? In a Datalog program, the set of derivable atoms in a stratum is determined by the least fixpoint of the stratum's rules given the sealed strata below. The sealing commitment should be: "exclude all outcomes where any atom in S_i is true beyond those derivable by the least fixpoint of stratum i's rules." This is the standard stratified evaluation, but calling it a "commitment" is a modeling choice that should be justified—why is it a commitment rather than a deterministic entailment? The answer (I think) is that sealing declares the stratum *complete* before the fixpoint is computed, and the fixpoint computation is the subsequent entailment. But this is not clearly separated in the body.

**6. The provenance annotation for negation-cycle atoms is trivial (value 1).**

In the running example, P(r(c)) = {(D^(r), 1)}. The provenance value is just 1—there is no derivational structure to explain. This is because r(c) ← ¬s(c) has a single rule with a single negated body atom. For more complex programs, what would the K-valued annotation look like for atoms derived through negation? The paper does not address this. Under a fixed stable model, derivational provenance for atoms derived through stratified negation is handled by Dannert et al. But for atoms in negative cycles (which are resolved by choice predicates), what is the "derivation"? The paper assigns them provenance value 1, which is essentially saying "this atom holds by fiat (choice)." This is honest but limits the explanatory power of the framework for precisely the atoms where explanation is most needed.

## Questions for the Authors

1. What happens when a program has no stable models? Is D empty? If so, every atom is "robustly absent" (vacuously), which seems uninformative.

2. For programs with nested negative SCCs (e.g., SCC A feeds negatively into SCC B, which feeds negatively into SCC C), would the determination have depth k+3 (one choice layer per SCC)? If so, the "single final choice layer" restriction in Theorem 5.1 seems unnecessarily limiting—the theorem should generalize to multiple choice layers with appropriate independence conditions.

3. The paper claims the alternating fixpoint is an entailment (not a commitment). But the alternating fixpoint can assign **f** to atoms that were previously **u**—this *excludes* the outcome where that atom is **t**. How is this not a commitment? The answer seems to be that the outcome order ⪯ makes this an upward move (u ⪯ f), but this depends on the specific choice of ⪯. If ⪯ were flat, the same operation would be a commitment. This suggests the commitment/entailment distinction is not intrinsic but depends on the choice of outcome order—which should be acknowledged.

4. Is there a formal relationship between the determination semiring for Datalog and the "possible models" semantics of Sakama and Inoue? Their work on abductive logic programming considers sets of possible models and queries over them, which seems closely related.

## Minor Comments

- Line 1248: The citation [gelfond1988stable] is for the stable model semantics definition, but the specification Spec_P is described as admitting "all assignments consistent with the program rules and EDB." This is vague—does it mean all supported models? All stable models? All three-valued models extending the EDB? The formal definition matters for the framework.

- The filtration F_0 = F_1 = F_2 = {∅, D} in the running example (line 1262) follows because the sealing prefix is shared. But this means the filtration is trivial at all levels below the choice layer. For the restricted class of programs in Theorem 5.1, the filtration always has this degenerate structure (trivial until the last layer). This limits the filtration's usefulness for Datalog—it only distinguishes "robust/absent" from "contingent," which is just the WFS classification. The filtration becomes interesting only when there are multiple non-commuting choice layers, which the theorem excludes.

- The paper should note that for the Datalog instantiation, the determination semiring is always a product of Boolean algebras (one per independent negative SCC), which is itself a Boolean algebra. This is a much more specific structure than the general framework suggests.

## Overall Recommendation

**Weak Accept.** The conceptual contribution—viewing negation semantics as filtration levels—is appealing and novel. However, the Datalog instantiation is restricted to a narrow class of programs, the key theorem's proof sketch elides the most important step (the WFS correspondence), and the framework provides limited explanatory power for the atoms that most need explanation (those in negative cycles get provenance value 1). The paper would be strengthened by: (a) explicitly stating and citing the Van Gelder–Ross–Schlipf result that underpins the WFS correspondence; (b) discussing what happens beyond the restricted class; and (c) acknowledging that the filtration is degenerate (trivial until the last layer) for the class covered by Theorem 5.1.
