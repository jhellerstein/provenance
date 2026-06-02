# Simulated PODS Review — Paraschos Koutris (Wisconsin)

## Summary

The paper introduces "determination provenance," extending classical semiring provenance to settings where a specification admits multiple outcomes (semantic ambiguity). The key construction is a "determination semiring" on supports (subsets of resolving determinations) equipped with a filtration of sub-semirings induced by the layered commitment structure. The framework is instantiated for transactional concurrency and Datalog with negation, and robustness is shown coNP-complete in the width of independent commitments.

## Strengths

- **Conceptually clean separation.** The decomposition into "which commitments resolve ambiguity" (the determination) and "how is the result derived under that resolution" (classical provenance) is well-motivated and clearly articulated. The observation that classical provenance requires a function, while ambiguous specs are relations, is the right starting point.

- **The filtration is the real contribution.** The paper correctly identifies that the support semiring (2^D, ∪, ∩) is elementary. The non-trivial content is the filtration: the chain F_0 ⊆ F_1 ⊆ ... ⊆ F_d = 2^D of sub-semirings induced by the layered commitment structure, and the fact that positive relational algebra is non-expansive with respect to this filtration (Corollary 3.1). This is a genuine algebraic observation.

- **Datalog instantiation is compelling.** Theorem 5.1—that stratified, well-founded, and stable-model semantics correspond to different filtration levels of the same determination semiring—is the paper's strongest result. It gives a clean algebraic explanation of a phenomenon that is usually described operationally.

- **Tightness results.** Proposition 3.4 (difference can increase depth) and Proposition 3.5 (every level is realized) together show the filtration is tight. This is the kind of structural completeness result that PODS values.

## Weaknesses

**1. The support semiring composition laws require a zero-divisor-free assumption that is not stated in the body.**

The claim that join maps to intersection of supports (Section 3.1, line 642) relies on the provenance semiring K being zero-divisor-free: supp(P(t₁ ⋈ t₂)) = supp(P(t₁)) ∩ supp(P(t₂)) holds only if a·b = 0 implies a = 0 or b = 0 in K. This is true for N[X] and all standard provenance semirings, but it is an assumption. The appendix (Proposition C.1) states it explicitly, but the body does not. Since the entire filtration theory rests on this composition law, the assumption should be stated in Section 3.1.

**2. Theorem 2.1 (Resolution is necessary and sufficient) is not a theorem in the usual sense.**

The "necessity" proof (lines 499–504) is an informal argument: "semiring provenance expresses only positive dependence on base facts; when two outcomes differ on a fact, no annotation can simultaneously explain both." This is a plausibility argument, not a proof. What is the formal statement being proved? What is the class of "classical semiring provenance" semantics being excluded? Without a precise definition of the target class, the "if and only if" is not well-defined. I would accept this as a proposition or observation, but not as a theorem with a proof.

**3. The complexity result (Theorem 6.1) does not advance the state of the art.**

The coNP-completeness of robustness via DNF-Validity is a straightforward encoding: n independent binary commitments biject with truth assignments, UCQs encode DNF, robustness = validity. The paper acknowledges this is "unsurprising" and frames it as "validation." I agree with the framing, but then the theorem should not occupy a full section. The FPT corollary (Corollary 6.1) is more interesting but is stated without proof and the bound O(2^{wd} · p(n)) is brute-force enumeration—not an algorithm. Are there better algorithms for restricted query classes? The paper leaves this entirely open.

**4. The filtration definition relies on "maximal commuting batches" whose canonicity is not proved.**

The paper defines ≡_k inductively (lines 778–791) and claims it is an equivalence relation "by multiset equality at each layer." But the layers themselves are defined as "maximal commuting batches given the semantic commutativity induced by the determination's prefix." This is a dynamic notion: commutativity depends on the current admissible set, which depends on the prefix. The paper acknowledges this (lines 772–776) but does not prove that the resulting layering is unique for each determination. If two valid layerings of the same determination exist, ≡_k may not be well-defined. The paper should either prove uniqueness of the maximal commuting decomposition (analogous to Foata normal form for a fixed independence relation) or explicitly state that the filtration is relative to a chosen layering discipline.

**5. Proposition 3.5 (Reachability) has a non-constructive proof.**

The proof says "a tuple whose presence depends on the choice at layer k but not on layers k+1,...,d has support that is a union of level-k classes but not of level-(k-1) classes." This describes what such a tuple would look like but does not construct one. The existence claim requires showing that for any determination structure with non-trivial choices at each layer, one can find (or construct via a query) a tuple at each depth level. This is plausible but the proof as written is incomplete.

**6. The transactional instantiation is underdeveloped relative to its page budget.**

Section 4 occupies roughly 3 pages but contains no theorem beyond Proposition 4.2 (depth by isolation level), which is stated without proof. The running example is helpful but the section does not establish any non-trivial property of the transactional determination semiring that does not follow immediately from the general framework. Compare with Section 5 (Datalog), which proves a genuine theorem (Theorem 5.1) connecting the framework to known semantics. Section 4 would benefit from a comparable result—e.g., a characterization of which transaction workloads have bounded determination width, or a connection to known results on the complexity of checking serializability.

## Questions for the Authors

1. **Zero-divisor-free assumption.** Is the composition law supp(t₁ ⋈ t₂) = supp(t₁) ∩ supp(t₂) essential to the filtration theory, or can the filtration be defined without it (e.g., using ⊆ rather than =)?

2. **Uniqueness of layering.** Can you give an example where two valid layerings of the same determination yield different ≡_k relations? If so, how does this affect the filtration?

3. **Compact representations.** You note (line 742–748) that for single-layer determinations, supports admit compact representation as PosBool(Φ). For deeper determinations, you say this "remains open." Can you characterize the class of supports that arise at each filtration level? Are they always representable as Boolean formulas with restricted quantifier depth?

4. **Tractability.** Beyond bounded width, are there structural restrictions on the commitment basis or the query that make robustness tractable? For instance, is robustness in PTIME for acyclic conjunctive queries over single-layer determinations?

5. **Relationship to possible-worlds provenance.** The determination semiring on supports is isomorphic to the powerset semiring over possible worlds. How does this relate to the lineage semiring in probabilistic databases (Suciu et al.)? The connection seems direct but is not discussed.

## Minor Comments

- Line 607–608: "a minimal resolving determination has length at most |Spec(H)| - 1." This bound is loose. In practice, minimal determinations have length equal to the number of independent choices needed, which may be much smaller than |Spec(H)| - 1. Is there a tighter characterization?

- Proposition 3.2 (Single-layer case): The identification with PosBool(Φ) is nice but the proof assumes each determination corresponds to a conjunction of commitment variables. This is true only when each commitment is binary (applied or not). If commitments have multiple alternatives (k_i > 2), the correspondence is with a multi-valued positive Boolean formula. Please clarify.

- The paper uses "determination semiring" for (2^D, ∪, ∩) and "determination provenance" for the D → K function. This is clear once established but the terminology is initially confusing because "determination semiring" sounds like it should be the richer object. Consider "support semiring" for the former.

- Corollary 3.1: The proof appeals to Proposition 3.1 but does not verify that ∪ and ∩ of level-k supports remain level-k supports when the two inputs have different depths. This follows from the definition (level-k supports are closed under ≡_k agreement regardless of deeper structure) but should be stated.

## Overall Recommendation

**Weak Accept.** The paper introduces a well-motivated framework with a genuine algebraic contribution (the filtration and its interaction with query evaluation). The Datalog instantiation is the strongest result and connects cleanly to known semantics. The main weaknesses are: (1) the complexity result is routine, (2) the transactional instantiation lacks a comparable theorem, (3) several formal claims in the body are stated without adequate proof (Theorem 2.1, Proposition 3.5, uniqueness of layering). The paper would be strengthened by either proving the layering canonicity or explicitly relativizing the filtration, and by replacing Theorem 2.1 with a more precisely scoped statement. Despite these issues, the conceptual contribution is solid and the Datalog result alone is interesting enough for PODS.
