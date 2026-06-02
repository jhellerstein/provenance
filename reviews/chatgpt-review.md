Overall PODS-style reaction

This is a promising paper with a real idea: provenance should explain not only derivations under a fixed semantics, but also the semantic commitments that make a particular semantics/execution/model determinate. The introduction sells that well: the bank-account example makes clear why ordinary provenance cannot explain “why this schedule/model rather than another,” and the paper’s stated move from ambiguity to determinations to a support semiring is attractive.  ￼

My likely PODS-reviewer stance would be: borderline-to-weak accept if the core formalism is repaired and the transactional instantiation is made more precise; weak reject if submitted in current form. The idea is good enough for PODS, but the first 15 pages currently contain several claims that feel too strong, underdefined, or vulnerable to counterexample. Since material after page 15 is optional, the main body has to carry all definitional and correctness burden; right now it doesn’t.

The most important fixes are not cosmetic. They are:

1. Narrow and harden the formal claims.
2. Make the “determination semiring” feel less like just powerset bookkeeping.
3. Repair the transaction model or demote it to a motivating example.
4. Move enough proof/definition from the appendix into the first 15 pages that a reviewer can verify the paper’s central theorems without optional reading.

⸻

What is strong

The paper’s conceptual wedge is compelling. The distinction between derivational provenance and “which commitments made this derivation possible” is crisp, and the introduction uses it well. The paper explicitly positions a determination as a sequence of irrevocable commitments after which classical provenance applies, and then separates structure within a determination from structure across determinations.  ￼

The best contribution, rhetorically, is the filtration story. The support semiring itself is unsurprising—powersets under union/intersection—but the claim that non-commuting layered commitments induce a filtration that query evaluation respects is the part that feels genuinely paper-worthy. The text already recognizes this, saying the Boolean algebra on supports is elementary and that the nontrivial structure is the filtration.  ￼ Lean harder into that.

The Datalog-with-negation instantiation is also the strongest application. It connects naturally to stable models, well-founded semantics, stratification, skeptical reasoning, and why-not provenance. The example on pages 13–14 is understandable, and the “same semiring, different filtration levels” line is attractive.  ￼

⸻

Major concern 1: Theorem 2.1 is too strong and will draw fire

Theorem 2.1 says classical semiring provenance over Spec is well-defined iff Spec is determined. The proof of necessity says semiring provenance expresses only positive dependence on base facts, and if two admissible outcomes differ on a fact, “no annotation can simultaneously explain both.”  ￼

A PODS reviewer is likely to object that this is not a theorem as stated. It depends on what “classical semiring provenance over Spec” means. There are several possible readings:

* Provenance of a tuple under each admissible outcome is well-defined.
* A single provenance value aggregating all admissible outcomes is desired.
* A provenance semantics must distinguish why/why-not across outcomes.
* A provenance semantics must be Green-style positive provenance over one resolved instance.

Only the last reading makes the theorem plausible, and even then the necessity proof is currently a position statement, not a proof. A relational spec with multiple admissible outcomes could still have a tuple whose provenance is identical across all outcomes, or one could define a set-valued/function-valued provenance object—which is exactly what the paper later does. So “if and only if Spec is determined” looks false unless you carefully define the target notion of “classical provenance over Spec.”

Suggested fix: Replace Theorem 2.1 with a narrower lemma:

Classical Green-style provenance is directly applicable to a resolved instance/outcome. For an ambiguous specification, applying it requires either selecting a determination or lifting provenance pointwise over determinations.

Then your new framework is not justified by a dubious impossibility theorem; it is justified by a clean semantic mismatch.

⸻

Major concern 2: History-invariance seems false or at least badly underspecified

Lemma 2.1 says that if a persistent basis and a determination resolve Spec, then (Spec | D)(H1) = (Spec | D)(H2) for all H1 ⊑ H2, and the paper then says the resolved outcome does not depend on which history prefix we start from—only on the determination.  ￼

This is a very strong claim. In most database and systems settings, extending the history with new environment events changes the outcome. If H2 has new input facts, new transactions, or new messages not present in H1, why should the same determination yield the same outcome? Persistence can preserve exclusions; it does not obviously prevent new admissible outcomes from appearing unless the outcome universe is fixed and all future environment events are already represented somehow.

This also sits uneasily with the earlier story that histories are incomplete and can be extended by new events.  ￼ If histories can acquire new facts/events, then resolved outcomes should normally vary with the history.

Suggested fix: Decide which of these you mean:

1. Fixed completed history: determinations resolve ambiguity within a fixed observed history. Then delete or sharply limit history-invariance.
2. Prefix-invariant semantic commitments: commitments made at a prefix remain valid under extensions, but the resolved outcome may refine upward under ⪯. Then change equality to refinement/compatibility.
3. Outcome space already includes all future events: then state this explicitly, because it is not how readers will parse “history extension.”

I would probably replace equality with something like:

If D resolves Spec at H, then for any extension H′, either D remains valid and the resolved outcome at H′ refines the resolved outcome at H, or the framework records the additional commitments needed to resolve newly introduced ambiguity.

That is more consistent with your broader coordination/future-monotonicity worldview.

⸻

Major concern 3: “Minimal resolving determinations” and finiteness are doing hidden work

Section 3 fixes the set D of minimal resolving determinations and states that this set is finite.  ￼ But “minimal” is not formally defined in the main body. Minimal by prefix? By multiset inclusion? By no redundant commitment? By no proper subsequence resolving? These differ when commitments do not commute.

This matters because the semiring is built over D. If D changes under equivalent presentations of the same commitments, or includes redundant determinations, then supports, robustness, and qdepth change. That makes the core object look basis- and normalization-dependent in a way reviewers will worry about.

Suggested fix: Add a definition before Definition 3.1:

A resolving determination D is minimal if no proper prefix/subsequence/commutation-equivalent reduction of D resolves Spec.

Pick one and explain why. Then state whether the results depend on this choice. If they do, say so openly: provenance is relative not only to Spec but also to a commitment basis and minimality policy. That is acceptable, but it must be explicit.

⸻

Major concern 4: The semiring contribution may be perceived as too easy

The determination provenance object is a function D → K, and its support is a subset of D. Supports form (2^D, ∪, ∩, ∅, D).  ￼ A skeptical reviewer may say: “Of course subsets of worlds form a Boolean algebra. What is the theorem?”

You already have the answer: the filtration. But right now the paper spends substantial rhetorical energy on the semiring itself. I would invert the emphasis:

* The support semiring is the baseline.
* The real contribution is: commitment dependence induces a canonical filtration; query evaluation is non-expansive over that filtration; negation/difference can increase depth; classical negation semantics can be read as stopping levels.

The paper’s strongest algebraic section is 3.3, not 3.1. The text defines level-k supports, the nested sub-semirings, and qdepth, and proves positive relational algebra cannot increase qdepth.  ￼ That should be the centerpiece.

Suggested title-level reframing: Instead of “the space of resolving determinations forms a commutative semiring,” lead with “semantic commitments induce a filtered provenance semiring.” That sounds less trivial and more PODS.

⸻

Major concern 5: Foata normal form / canonical layering is not justified

The filtration relies on a “canonical layering” of each determination, described as its Foata normal form, grouping commitments into maximal commuting batches.  ￼ This is dangerous as written. Foata normal forms are canonical under a fixed trace monoid/independence relation. But your commutativity seems semantic and state-dependent: two commitments may commute in one context but not another, and validity of later commitments can depend on earlier commitments.

A reviewer may ask:

* What is the independence relation?
* Is it static over the commitment basis, or history-dependent?
* Does every determination have a unique Foata normal form?
* If different but equivalent layerings exist, is qdepth invariant?

Suggested fix: Either prove a canonical-layering theorem in the main body, or weaken the claim:

Given a chosen valid layering of determinations, we obtain a filtration…

Then the filtration is relative to a layering discipline. That is less grand, but much safer. If you want canonicity, move the relevant appendix material before page 15.

⸻

Major concern 6: The transaction section is the weakest instantiation

The transaction application is appealing as motivation, but the formalization is likely to be attacked by concurrency-control readers.

The paper models isolation levels as invariants on the active conflict graph, where commit/abort removes vertices from the active graph.  ￼ Then commit is valid if, after removing the transaction, the acyclicity invariant is not violated.  ￼ This is not the usual serialization-graph account, where committed transactions and their dependencies matter; simply removing committed vertices from an active graph risks losing precisely the dependencies that define serializability.

There is also an internal tension: Proposition 4.1 says commit/abort on transactions sharing no conflict edges commute, but Proposition 4.3 says that when the active conflict graph is acyclic, every active transaction can be committed independently and “all commit decisions commute,” citing Proposition 4.1.  ￼  ￼ An acyclic graph can have many conflict edges. “No cycles” does not imply “no shared conflict edges.” So the proof sketch appears invalid as written.

Example 1.1 also creates a conceptual issue: it says all four transactions are concurrent and “any serialization is possible,” and then uses different commit orders to explain presence/absence of d.  ￼ But in real serializability, commit order is not generally the serialization order; a system may commit transactions in an order different from the equivalent serial order. If your commitments are serialization-order choices rather than commit events, say that. If they are actual commits, the example needs a CC model where commit order determines visibility.

Suggested fix: For PODS, I would either:

* Replace the transaction section with a cleaner abstract serialization-order model: histories induce a partial order; determinations choose a linear extension; provenance is computed under that linear extension.
* Or keep transactions, but use a standard Adya serialization graph model and make commitments be serialization-order / dependency-resolution choices, not commit events.
* Or demote transactions to motivation and make Datalog the formal main instantiation.

Right now, the transaction section may cost you more than it helps.

⸻

Major concern 7: The Datalog claim is strong but under-supported before page 15

The paper claims that stratified, well-founded, and stable semantics differ only by which filtration level they read, sharing one underlying determination semiring.  ￼ The page-13 example is nice, but the general claim is largely deferred to Appendix F. Since page 15 is the optional-reading boundary, a PODS reviewer may treat the general Datalog claim as unproven in the submitted paper.

For acceptance, I think you need at least one precise theorem in the main body:

For finite normal Datalog programs under [specified restrictions], the determination construction yields a filtration such that stable models correspond to full determinations, WFS corresponds to the sealing prefix plus ambiguity classification, and stratified semantics corresponds to the case where the sealing prefix resolves all atoms.

Then give proof sketch in the main body. The example alone is not enough for the breadth of the abstract’s claim.

Also, be careful with “stratified semantics discharges the same sealing layers but is defined only when they resolve everything; ¬-cycle atoms remain ⊥.”  ￼ Classical stratified negation is not usually described as a partial semantics that leaves unstratified programs at ⊥; rather, the program is outside the stratified fragment. Your enriched-domain presentation can define such a partial reading, but you should make clear it is your embedding of stratified evaluation, not the standard semantics itself.

⸻

Major concern 8: The complexity theorem is too generic to count as a major result

Theorem 6.1 says that for any instantiation with n independent binary commitments, polynomial validity checking, and polynomial query evaluation, robustness is coNP-complete.  ￼ This is correct-looking but may feel tautological: if determinations encode truth assignments and UCQs encode DNF, then robustness is DNF validity.

That is fine as validation, but it should not be overclaimed. The paper says this “confirms that width is the right complexity parameter.”  ￼ A reviewer may ask: right for what class of representations? What about compact support representations? What about deeper determinations with constrained validity? What about FPT in width but exponential in depth? The corollary gives a brute-force bound, but the theory of representation is explicitly left open.  ￼

Suggested fix: Present the complexity theorem as a sanity check and unifying explanation, not as the main technical payload. The main payload should be the filtered provenance construction and the Datalog correspondence.

⸻

Page-15 strategy

Because PODS reviewers need not read after page 15, I would restructure the first 15 pages around a smaller number of claims that are fully defensible.

A stronger first-15-page structure might be:

1. Introduction: same story, but sharpened around “filtered provenance under ambiguity.”
2. Core model: histories, outcomes, commitments, determinations. Remove or weaken Theorem 2.1 and history-invariance.
3. Determination provenance: define D → K, supports, robustness.
4. Filtered semiring: main theorem: valid layerings induce sub-semirings; positive RA is non-expansive; difference can increase depth.
5. Datalog instantiation: one theorem plus example. Make this the primary application.
6. Transactions: either shortened to a motivation/example or rebuilt as a clean serialization-order model.
7. Complexity: short theorem as validation, not headline.

I would not spend precious first-15-page space on the current transaction conflict-graph depth claims unless you can make them airtight.

⸻

Concrete edits I would make before submission

1. Change the abstract

Current abstract overclaims in three places: “recovering Green et al.’s framework at a new level,” “longstanding gaps,” and “compact algebraic foundation for systems settings… previously eluded formal provenance treatment.”  ￼ These are reviewer-bait.

A safer abstract shape:

We introduce determination provenance, a provenance model for specifications that admit multiple semantic resolutions. For each resolving determination, provenance is ordinary semiring provenance; across determinations, supports form a Boolean semiring equipped with a filtration induced by commitment layers. Positive relational algebra is non-expansive with respect to this filtration, while difference can increase depth. We instantiate the construction for Datalog with negation, showing how stable, well-founded, and stratified readings arise as different levels or restrictions of the same filtered object. We also discuss transactional ambiguity and show that robustness is coNP-complete in the width of independent commitments.

This sounds less revolutionary but more credible.

2. Rename “determination semiring” or qualify it

“Determination semiring” for (2^D, ∪, ∩) may disappoint. Consider “support semiring” for the Boolean algebra and reserve “determination provenance” for the richer D → K object plus filtration. Then the novelty is not “sets form a semiring,” but “semantic resolution induces a filtered support structure.”

3. Define all dependence on basis explicitly

Say early:

Determination provenance is relative to a specification, a commitment basis, and a normalization/minimality criterion for resolving determinations.

This disarms a lot of objections. It is analogous to provenance being relative to a query plan or query expression unless quotienting/equivalence is proved.

4. Replace equality with refinement wherever histories grow

The framework already has ⪯. Use it. Equality across history extensions is too brittle.

5. Make one running example do all the work

The paper currently has a transaction example first and Datalog later. Since Datalog is cleaner for PODS, consider opening with a tiny Datalog-negation example or pairing the examples earlier. The transaction example is intuitive, but it drags in lots of concurrency-control commitments before the algebra is stable.

6. Move a real theorem for Datalog into the main body

Do not leave the general Datalog correspondence in Appendix F. The abstract and contribution list depend on it.  ￼

7. Tighten related work against CQA and possible-worlds provenance

The CQA comparison is useful and should move earlier or become more pointed. The analogy is direct: robustness resembles certain answers over repairs, but your multiplicity arises from semantic commitments rather than database repairs, and you track the support set rather than only universal truth.  ￼ I would also explicitly discuss possible-worlds/probabilistic DB provenance, because reviewers will reach for that analogy immediately.

⸻

Likely reviewer objections and how to preempt them

Objection: “This is just possible-worlds provenance over a set of models/executions.”

Preempt with: possible-worlds gives the support set; your contribution is the commitment-generated filtration and query-relative depth. Make the filtration the headline.

Objection: “The Boolean semiring is trivial.”

Agree in the paper: yes, the unfiltered support semiring is elementary; the contribution is how a noncommutative commitment process induces a compositional filtered algebra.

Objection: “Transactions are modeled nonstandardly.”

Either fix with a standard model or make the transaction section illustrative. Do not let an avoidable systems-model fight sink the theory.

Objection: “The formalism is too broad; anything can be encoded as commitments.”

Concede relativity to basis, then show why that is a feature: different bases correspond to different explanatory vocabularies. But also identify a canonical basis for each instantiation.

Objection: “Main claims depend on appendix.”

Move the Datalog theorem and enough proof of layering/canonicity before page 15.

⸻

Bottom line

I think there is a PODS paper here, but the current draft is trying to win on too many fronts: provenance, transactions, Datalog negation, systems lineage, complexity, and a general semantic theory. For submission, I would make the paper narrower and more formal:

Main claim: ambiguity-aware provenance is ordinary semiring provenance indexed by determinations, and commitment structure induces a filtration that is respected by positive query evaluation.

Main application: Datalog with negation.

Secondary application: transactions, only if the model is repaired.

Validation: robustness coNP-completeness via width.

That version feels much more acceptable to PODS reviewers: precise, algebraic, connected to known provenance and negation literature, and not overexposed to concurrency-control objections.