New PODS-style review

This draft is substantially improved. It now has a clearer central thesis, a better explanation of why the support semiring alone is not the novelty, a main-body Datalog theorem, a more explicit distinction between determination provenance and the support semiring, and a better “reviewer-visible” related-work section. The paper is much closer to something a PODS reviewer could understand and evaluate from the first 15 pages.

My current simulated review would be:

Weak accept / borderline accept if the authors narrow the claims and repair the formal weak spots; weak reject if submitted as-is.
The idea is interesting and plausibly PODS-worthy, but several statements in the first 15 pages are still too strong relative to the definitions. The biggest remaining risks are: history-invariance, persistence canonicalization, dynamic layering/filtration well-definedness, and the transactional instantiation.

The positive news: the problems are now much more localized. The paper no longer feels like it needs a wholesale reframing. It needs a defensive pass: remove overclaims, formalize the key quotient/layering choices, and stop asking the transaction model to carry too much.

⸻

What has improved

The introduction is better. The revised paper now states the key observation cleanly: ambiguous specifications are relations, classical provenance wants a function, and a determination narrows the relation to a function. That is the right first-principles pitch.  ￼

The filtration is also better positioned. The intro now explicitly says that the filtration gives the framework “genuine algebraic depth beyond the support structure alone.”  ￼ That directly addresses the likely reviewer reaction that (2^D, ∪, ∩) is just a powerset semiring.

You also improved the main-body Datalog section. Theorem 5.1 now appears before the page-15 boundary and states the intended correspondence among stable-model, well-founded, and stratified semantics.  ￼ This is important: before, the abstract depended too heavily on Appendix F.

The related-work section is much stronger. In particular, the comparison to consistent query answering is now useful and appropriately scoped: both robustness and CQA certain answers quantify over admissible completions, but the multiplicity comes from different sources, and your layered/non-commutative structure has no direct CQA analog.  ￼

⸻

Remaining major concern 1: History-invariance is still the biggest formal hazard

Lemma 2.1 still says that if D resolves Spec, then (Spec | D)(H1) = (Spec | D)(H2) for all H1 ⊑ H2.  ￼ You added a note that this is a “retrospective guarantee” over prefixes of a completed history, and that new environment events may introduce ambiguity requiring additional commitments.  ￼ That helps rhetorically, but it does not fully fix the formal statement.

The problem is that the lemma still quantifies over all H1 ⊑ H2, while the note says the intended interpretation is only over prefixes of a completed history where the determination already covers all relevant environment events. Those are not the same. As written, a reviewer can still construct H2 with a new input fact, transaction, message, or EDB atom that changes the resolved outcome. Persistence prevents excluded outcomes from being rehabilitated; it does not prevent new outcomes from appearing unless the outcome universe and history class are frozen in a special way.

I would change the lemma rather than explain around it.

Possible replacement:

Lemma 2.1′ (Retrospective invariance over a closed history). Fix a completed history H* and a resolving determination D for the ambiguity present in H*. For any prefix H ⊑ H* containing the dependency set of D, applying D yields the same resolved outcome as applying D at H*.

Or, more generally:

Persistence implies stability of exclusions, not equality of outcomes. If o ∉ Spec(H · D), then o ∉ Spec(H′ · D) for any covered extension H′; additional environment events may require additional commitments.

That version aligns with your “new messages disturb convergence” intuition and avoids an obviously false-looking equality claim.

⸻

Remaining major concern 2: Theorem 2.1 is improved but still over-assertive

You narrowed Theorem 2.1 to “classical semiring provenance over Spec—a single K-relation assigning each tuple a provenance value consistent with all admissible outcomes.”  ￼ That is better. But the necessity proof is still too hand-wavy for a theorem in a PODS paper. It says semiring provenance expresses only positive dependence on base facts, so if two admissible outcomes differ on a fact, no annotation can simultaneously explain both.  ￼

A reviewer may ask: what if all admissible outcomes agree on the queried tuple? What if the single K-relation is allowed to assign a value in a product semiring, a powerset semiring, or a function space? Your later construction is precisely a function D → K, so a skeptical reviewer can say “you just defined a single semiring-ish object after all.”

I recommend demoting this from theorem to proposition/observation unless you want to formalize the class of allowed “classical” provenance semantics.

Suggested wording:

Classical Green-style semiring provenance is defined for a fixed instance or model. For an ambiguous specification, one must either choose a determination first or lift provenance pointwise across determinations. The latter is the construction of this paper.

This avoids an unnecessary impossibility claim. You do not need Theorem 2.1 to carry the paper.

⸻

Remaining major concern 3: Persistence canonicalization is not “without loss of generality”

The draft now says every basis can be canonicalized to an equivalent persistent one, with a reference to Proposition H.1.  ￼ Appendix H defines a dependency set, sealing commitment, and claims that sealing plus deterministic entailment gives the same resolved outcome once the dependency set has stabilized.  ￼

This is useful, but it is not enough to justify “without loss of generality” as a blanket statement.

Why? Because sealing the dependency set is itself a semantic commitment. It may change:

* the depth of the determination,
* the explanatory vocabulary,
* which commitments count as independent,
* the provenance support structure,
* and possibly the intended operational interpretation.

The proposition says that at histories where S has stabilized, the sealed basis produces the same resolved outcome as the original.  ￼ That is outcome equivalence under a stabilization condition, not full provenance equivalence.

I would weaken the claim in Section 2.3:

Current spirit:

Every basis can be canonicalized to an equivalent persistent one.

Safer version:

Non-persistent commitments can often be represented by first sealing their dependency set and then treating the original predicate as deterministic entailment. This preserves resolved outcomes once the relevant dependency set has stabilized, but may change the determination structure; throughout the main development we assume a persistent basis.

That is much harder to attack.

⸻

Remaining major concern 4: The filtration still depends on a not-yet-formal dynamic layering

You improved the Foata discussion by acknowledging that commutativity may depend on the prefix and that different determinations may have different layerings.  ￼ But the paper still defines level agreement and claims it is an equivalence relation.  ￼ This is a key place where a PODS reviewer may slow down and ask for a proof.

Dynamic commutativity makes “same commitments in layers 1 through k” delicate. If two determinations diverge in layer 1, then their layer-2 commutativity relation may differ. If layer boundaries are prefix-dependent, agreement-at-level-k may be well-defined only for determinations that have already agreed through level k-1. That is probably what you intend, but the equivalence-relation claim should be spelled out recursively.

A more robust definition:

D ≡0 D′ always.
D ≡k+1 D′ iff D ≡k D′ and, after the common prefix of k layers, their next maximal commuting layer is the same multiset.

Then prove ≡k is an equivalence relation by induction. That would make Definitions 3.2–3.3 feel much safer.

Also, Appendix H/Open Questions still notes “dynamic Foata normal form” as open: characterizing equivalence of determinations under dynamic commutation remains unresolved.  ￼ That is fine, but then the main body should not sound as if canonical layering is fully settled. I would replace “the filtration is well-defined because…” with a short recursive definition and say equivalence of different determinations producing the same resolved specification is left open.

⸻

Remaining major concern 5: The transaction section is still risky

The transaction section is shorter and less over-proved, which helps. But the basic model remains vulnerable.

You define the conflict graph over active transactions and say that when Ti commits, all adjacent edges are removed because Ti’s position in the serial order is finalized.  ￼ Then commit is valid if, after removing Ti, the isolation invariant is not violated.  ￼ This is not a standard presentation of conflict serializability. Standard serialization graphs are about committed transactions and dependencies among them; removing committed vertices from an active graph is at best an operational model that needs justification.

Even worse, the running example still uses commit order as if it directly determines visibility/serialization order:

Din = commit(T2) · commit(TQ) · commit(T3) and Dout = commit(T2) · commit(T3) · commit(TQ).  ￼ But in real systems, commit order and serialization order need not coincide. If your commitment is actually “serialize TQ before T3,” call it an ordering/serialization commitment, not a commit commitment.

The appendix partially acknowledges this: for the running example, the enriched scheduling basis is used for expository clarity, and the determination consists of ordering commitments rather than commit/abort commitments.  ￼ That is a red flag: the main body says commit/abort; the appendix says scheduling commitments.

My recommendation is strong: make the transaction section explicitly about ordering commitments, not commit/abort, in the main body.

A clean version:

* A transaction history induces a partial order of observed conflicts.
* A determination chooses a linear extension / serialization order / visibility order consistent with the history.
* Commit/abort are one possible operational implementation, but not the formal basis used in the example.
* Scheduling commitments φTi≺Tj are the formal commitments for Section 4 and for the robustness reduction.

This would eliminate most of the concurrency-control objections. You can still discuss commit/abort as an alternative basis, but don’t make it the primary one.

⸻

Remaining major concern 6: Datalog theorem is now visible, but probably too broad

Theorem 5.1 states that for a finite normal Datalog program with k stratification layers and negation cycles resolved by choice predicates, the determination semiring has depth k+1; stable semantics reads the full filtration, well-founded reads Fk, and stratified reads Fk only when the sealing prefix resolves all atoms.  ￼

This is a good addition, but it may overgeneralize. In arbitrary normal programs, negation cycles can be nested, mutually dependent, or interact through positive recursion. A single choice layer after all sealing layers may not capture the structure unless you restrict the program class or define the transformation very carefully. “k stratification layers and ¬-cycles resolved by choice predicates” sounds like a special class, not all finite normal Datalog.

Two fixes:

1. State the syntactic restriction precisely. For example: locally stratified prefix plus a final independent collection of negative SCCs; or normal programs after SCC condensation with choice predicates per unresolved SCC.
2. Avoid saying “the classical negation semantics differ only in which filtration level they read” without qualification. That is a striking slogan, but reviewers may interpret it as all normal Datalog.

Possible wording:

For the class of finite normal Datalog programs whose negative SCCs are represented as a final choice layer over a stratified sealing prefix, stable, well-founded, and stratified readings correspond to the following filtration levels…

This still gives you the conceptual win without inviting a reviewer to find a pathological normal program.

⸻

Remaining major concern 7: The complexity theorem is still generic and slightly rhetorically inflated

Theorem 6.1 is fine as a general schema: independent binary commitments plus polynomial validity/evaluation gives coNP-complete robustness via DNF validity.  ￼ The appendix instantiation for Datalog is also straightforward and useful.  ￼

But the main text still says this confirms that width is “the right complexity parameter.”  ￼ That is too strong. It confirms width is a natural source of hardness for this representation. “The right parameter” would require more: lower/upper bounds under compact representations, interaction with depth, validity constraints, and maybe structural parameters of the query/program.

Suggested wording:

This validates width as a natural complexity parameter for explicit determination enumeration.

Also, the bound O(2^{wd} · p(n)) assumes every layer has width w and choices combine freely across depth. That is fine as a brute-force upper bound, but it is not the same as saying width alone controls complexity once depth grows. Be precise.

⸻

Review-score style summary

Strengths

* Nice conceptual problem: provenance under ambiguity rather than only under fixed semantics.
* The relation-to-function/determination framing is now clear.
* The filtered support semiring is a plausible algebraic contribution.
* Datalog with negation is a compelling database-theory application.
* The related work now does useful positioning against provenance for negation, systems lineage, and CQA.
* The first 15 pages are much more self-contained than before.

Weaknesses

* Several central formal claims are still too strong: history-invariance, persistence canonicalization, and generality of the Datalog theorem.
* Dynamic layering is not formal enough for the filtration to feel completely well-defined.
* The transaction model still mixes commit/abort, serialization order, and scheduling order.
* The abstract still overclaims: “longstanding gaps,” “no analog in classical provenance,” and “recovering Green et al.’s framework at a new level” may annoy reviewers.
* The complexity result is useful but should not be sold as a major independent technical theorem.

⸻

Recommended revision plan

1. Make the core paper safer

Change Theorem 2.1 and Lemma 2.1 from broad claims to scoped observations/lemmas. In particular, do not claim equality across arbitrary history extensions. Claim stability of exclusions, or equality only over closed/completed histories with covered dependency sets.

2. Formalize dynamic filtration recursively

Define ≡k by induction over common prefixes. Prove it is an equivalence relation. Then define Fk as unions of ≡k classes. This is probably a half-page change that will significantly improve reviewer confidence.

3. Recast transactions around ordering commitments

Move commit/abort into a “basis choices” discussion. Use ordering/serialization commitments as the formal basis for Example 1.1 and Section 4. The paper’s own appendix already leans this way.  ￼

4. Narrow Theorem 5.1

State the exact class of Datalog programs covered by the theorem. Keep the broader idea as discussion, not theorem.

5. Tone down the abstract

I would remove or soften:

* “recovering Green et al.’s framework at a new level”
* “longstanding gaps”
* “no analog in classical provenance”

The paper is stronger when it sounds precise, not grand.

A safer abstract sentence:

Determination provenance complements classical provenance by indexing ordinary semiring annotations by semantic resolutions and organizing their supports through a filtration induced by commitment depth.

That is credible and sharp.

⸻

My current bottom line

This draft is now within striking distance. The core idea is clear, the first 15 pages carry more of the burden, and the Datalog application gives PODS reviewers something native to grab onto.

The main thing that could still sink it is a reviewer deciding that the formal framework is “too loose”: persistence is assumed but canonicalization is not really equivalence; layering is dynamic but treated as canonical; transactions use a nonstandard active-graph model; and the Datalog theorem is broader than justified. These are fixable, but they need to be fixed before submission.

If I were revising under time pressure, I would prioritize:

1. Fix Lemma 2.1/history-invariance.
2. Give a recursive definition of filtration under dynamic commutativity.
3. Recast transactions as ordering commitments.
4. Narrow Theorem 5.1.
5. De-hype the abstract and intro.

Do those, and I would be much more comfortable imagining a PODS reviewer saying: “I don’t buy every application yet, but the algebraic framework is interesting and the Datalog connection is worth accepting.”