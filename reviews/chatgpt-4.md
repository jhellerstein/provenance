Fresh PODS-style review

My overall read is that this is now a much stronger and more coherent paper. The central idea has snapped into focus:

A tuple’s provenance has two dimensions: how it is derived once semantics is fixed, and which semantic resolutions make that semantics possible.

That sentence, now in the abstract, is doing real work. It gives the paper a memorable identity and distinguishes it from “yet another provenance semiring.”  ￼

My simulated PODS review would now be:

Weak accept, leaning accept, subject to tightening a few formal claims.
The paper proposes a compelling algebraic framework for provenance under semantic ambiguity. Its strongest contribution is the filtered determination semiring, with Datalog negation as the most convincing database-theoretic application. The responsibility section is interesting and gives the paper an appealing quantitative payoff. Remaining concerns are mostly about over-strong claims in the general framework and transaction instantiation, not about the core idea.

This is the first version where I would say the paper has a clear “there” there for PODS.

⸻

What is now working very well

1. The paper has a sharp conceptual thesis

The new framing around non-monotone operations requiring completeness guarantees is excellent. It turns the paper from a broad “ambiguity provenance” proposal into a more precise thesis:

Classical approaches internalize completeness guarantees algebraically; determination provenance externalizes them as sealing commitments, after which the non-monotone operation becomes monotone entailment.  ￼

That is a powerful move. It makes negation, conflict resolution, aggregation, and distributed ordering feel like instances of the same pattern rather than a bag of examples.

This also helps the title. “From Ambiguity to Algebra” now feels earned.

2. The Datalog section has become a serious main application

Section 5 is much stronger. It now explicitly says negation-as-failure requires knowing all derivations of p have been exhausted, and that determination provenance decomposes this into stratum sealing plus monotone evaluation.  ￼

Theorem 5.1 is also appropriately restricted: finite normal Datalog, at most one negated body literal, independent final negative SCCs, binary choice predicates.  ￼ This is the right kind of reviewer-safe theorem. It is not trying to claim the whole universe of normal logic programming.

The addition of Theorem 5.2, monus elimination, is a major improvement. It gives the paper a much more concrete connection to prior provenance-for-negation work: rather than just saying “we handle ambiguity too,” it says that for stratified cases, monus can be replaced by sealing plus ordinary monotone semiring computation.  ￼ That is a crisp technical contribution.

3. The responsibility section now feels less bolted-on

Determination responsibility is now framed as a refinement of robustness: robustness asks whether a tuple holds under every determination; responsibility asks which commitments matter for contingent tuples.  ￼

The presence game is intuitive, the SLA example is useful, and the move from #P-hardness to bounded-treewidth tractability to additive approximation is a plausible PODS-style arc.  ￼

I especially like the line that robustness sees only “contingent” in both SLA examples, while responsibility distinguishes loose versus tight SLAs.  ￼ That makes the measure feel operationally meaningful.

4. Related work is now mostly in the right posture

The paper positions itself well against semiring provenance, stratified negation provenance, fixed-execution systems provenance, causal responsibility, and consistent query answering. The CQA comparison is useful: certain answers quantify over repairs, whereas determinations resolve semantic ambiguity and have layered structure.  ￼

I would still add possible-worlds/probabilistic provenance explicitly, but the related-work posture is no longer a major weakness.

⸻

Remaining major concerns

Concern 1: Theorem 2.1 is still too strong for the value it provides

Theorem 2.1 says classical semiring provenance over an ambiguous spec is well-defined iff the spec is determined.  ￼ I understand the intended contrast, but I still think this theorem invites unnecessary objections.

The issue is that “well-defined” depends on what class of provenance objects is allowed. A single K-relation cannot represent all admissible outcomes, but a product semiring, powerset semiring, possible-world annotation, or a function D → K can. Indeed, the paper’s own construction is exactly a lifted object.

I would demote this from theorem to observation:

Classical Green-style semiring provenance is defined for a resolved instance/model. For an ambiguous specification, one must either choose a determination first or lift provenance pointwise over determinations. This paper develops the latter.

You lose little and remove a review target.

Concern 2: Lemma 2.1 still has a proof-direction problem

The revised history-invariance lemma is much better scoped: completed history, prefixes containing the relevant events, no future environment events.  ￼ But the proof still appears to use persistence backwards.

Persistence says: if a commitment excludes an outcome at earlier history H1, then it also excludes it at later history H2.

The proof needs: if a commitment excludes an outcome at completed history H*, it also excludes it at prefix H, assuming H contains all dependency events.

That does not follow from persistence alone. It follows from a locality/dependency sufficiency property:

If two histories agree on the dependency set of a commitment, then applying that commitment excludes the same outcomes in both histories.

You are gesturing at this with “containing all events on which D’s commitments depend,” but the lemma statement and proof should name that property. Otherwise a formal reviewer will notice the direction mismatch.

This is fixable. Add a definition:

A commitment φ is local to dependency set dep(φ) if histories agreeing on dep(φ) induce the same filter.

Then Lemma 2.1 follows from locality plus persistence, or perhaps from locality alone over completed-history prefixes.

Concern 3: Persistent canonicalization still overclaims

The paper says that in completed histories, every basis can be canonicalized to an equivalent persistent one without changing the determination structure.  ￼ This is still risky.

Sealing the dependency set plus applying a deterministic entailment may preserve final outcomes, but it plausibly changes:

* the number of layers,
* whether an operation is a commitment or entailment,
* the dependency graph,
* responsibility values,
* the explanatory vocabulary.

The paper says the seal is non-filtering in the retrospective setting and leaves the remainder unchanged, which helps. But “without changing the determination structure” is a very strong phrase. I would weaken it to:

In the retrospective setting, non-persistent commitments can be represented by persistent seals plus deterministic entailments that preserve resolved outcomes; we assume a persistent basis in the main development.

Unless Appendix I proves a precise structure-preserving isomorphism over layers and supports, avoid the stronger claim.

Concern 4: Minimal determination finiteness still needs assumptions

Section 3 says minimal resolving determinations are finite because each commitment strictly shrinks the admissible set, so length is at most |Spec(H)| − 1.  ￼

But Definition 2.5 allows Spec(H · φ) ⊆ Spec(H), not necessarily a proper subset.  ￼ Later prose says commitments are proper subsets, but the formal definition does not.

Also, Spec(H) may be infinite unless finite outcome domains or finite relevant support are assumed.

Simple fix:

We assume throughout that the set of minimal resolving determinations is finite. In the finite settings considered here, every nonredundant commitment strictly shrinks a finite admissible set, so minimal determinations have bounded length.

This is safer than deriving finiteness from current definitions.

Concern 5: The filtration depends on unique “next maximal commuting layer”

The inductive definition of level agreement is much better than earlier versions. It is clear and intuitive.  ￼

But it still assumes that, given a prefix, “the next maximal commuting layer” is uniquely defined. If maximal commuting batches are not unique, then ≡_k depends on a choice of layering policy.

This may be okay! But the paper should say one of:

1. The next maximal layer is canonical under the semantic commutativity relation.
2. The filtration is relative to a deterministic layering policy.
3. Different valid layerings yield equivalent filtrations under some quotient.

Right now it says the filtration is well-defined because agreement compares determinations sharing the same prefix.  ￼ That does not fully address non-unique maximal layers.

Given that dynamic Foata normal form appears as an open structural issue in the appendix, I would be conservative. Say:

We fix a canonical layering policy; the resulting filtration is relative to that policy.

That is acceptable and honest.

⸻

Transactions: useful, but still the weakest formal instantiation

The transaction section is much more readable now, and the ordering-commitment version of the running example is correct in spirit.  ￼

However, as a formal instantiation, it remains fragile.

The model uses an active conflict graph and removes committed transactions, saying the transaction’s serial position is finalized.  ￼ This is not a standard enough treatment of serializability to carry formal weight without proof. Proposition 4.2 also packs a lot into one unproved statement: RC depth 0, SER depth conditions, SI O(n) depth.  ￼

I would either prove Proposition 4.2 in the main body or soften it. A safer framing:

The following examples illustrate how different isolation mechanisms induce different determination depths.

Then leave the formal transaction-depth taxonomy to Appendix F. For PODS, the Datalog section is the stronger formal application. Do not let a transaction-model debate distract from the provenance contribution.

Also, “read committed is already determined” may not read right to database people unless you define the outcome carefully. RC permits many executions; it may be monotone under some observation order, but “determined” in your Definition 2.4 means exactly one outcome per history. If RC has multiple possible committed states or read results under different interleavings, depth 0 is not obvious.

⸻

Datalog and monus: likely the strongest technical story

The Datalog section is now the best candidate for the paper’s impact.

Theorem 5.1 is appropriately limited and gives a convincing filtration interpretation.  ￼ The proof sketch is readable. The table comparing stable, well-founded, stratified, and monotone readings is useful.  ￼

Theorem 5.2 is especially interesting but needs more care. It currently says:

For any naturally ordered semiring with monus and any finite normal Datalog program, LFP provenance over (K, monus) equals conditioned provenance with sealing commitments at each stratum.  ￼

This sounds too broad because “each stratum” presupposes stratification or at least a stratified evaluation order. The theorem later says monus is undefined for unstratified negation, while determination provenance remains defined across stable models. That suggests the theorem should be scoped to stratified or stratifiable programs, not “any finite normal Datalog program.”

Suggested theorem title and statement:

Monus elimination for stratified negation. For any stratified finite normal Datalog program and naturally ordered semiring with monus, the LFP provenance computed using monus equals conditioned provenance computed over ordinary K after sealing each stratum.

Then add:

For unstratified programs, the monus construction lacks a unique model to complement against; determination provenance instead ranges over stable-model determinations.

That would be clean and hard to attack.

⸻

Responsibility: interesting, but tighten two technical claims

1. The bounded-treewidth theorem needs the right hypothesis

Theorem 6.2 now says bounded conflict treewidth plus a monotone support predicate gives FPT responsibility.  ￼ This is improved, but the proof sketch still needs one extra assumption: that the support formula’s primal graph is bounded by the conflict graph.

Monotonicity alone does not imply locality. A monotone predicate can mention variables from far-apart parts of the conflict graph in one clause. The proof says clauses involve only commitments sharing a transaction, but that is not guaranteed by “monotone support predicate.” It is a separate locality condition.

Fix the theorem statement:

For a single-layer determination whose support predicate is represented by a monotone Boolean formula whose primal graph has treewidth w—in particular, for local predicates whose clauses involve only commitments sharing a transaction—responsibility is computable in …

Then define conflict treewidth as a useful sufficient condition, not the whole theorem.

2. Additive approximation is now correctly stated

This is much improved. The paper no longer says FPRAS; it says additive approximation, with sampling over permutations and random completions.  ￼ That is the right claim. I would just ensure the proof sketch explicitly says the samples are bounded, so Hoeffding/Chernoff gives the stated O(n/ε² log(1/δ)) bound. It looks like the text is going there, but the page excerpt cuts off mid-proof.

⸻

Related work: add one paragraph

The paper should explicitly address possible-worlds and probabilistic databases. A likely reviewer question is:

Is determination provenance just possible-worlds provenance over a set of resolutions?

The answer is:

The support set resembles possible-worlds semantics, but determinations are structured by semantic commitments, layers, and independence. The filtration and responsibility are over the resolution process, not merely over possible outcomes.

A paragraph in related work would preempt this.

You may also want to mention knowledge compilation / lineage circuits near the responsibility section, since your tractability story is essentially weighted model counting over support formulas. That will make Theorem 6.2 feel connected to existing PODS themes.

⸻

Smaller but important presentation issues

“No analog in classical provenance”

The introduction says some questions have no analog in the classical setting.  ￼ This is rhetorically effective, but maybe too strong. Some analogs exist in probabilistic provenance, CQA, why-not, or causal responsibility. The real claim is that they have no analog inside a single resolved execution/model. I would phrase it that way.

“Conflict resolution, aggregation”

The abstract mentions aggregation alongside negation and conflict resolution.  ￼ Aggregation is not really developed in the first 15 pages. Either add a one-sentence example or remove aggregation from the abstract to avoid opening a new obligation.

Typos

Definition 2.8 says “Seqencing” rather than “Sequencing.”  ￼

⸻

What I would prioritize before submission

If you have limited time, I would do these in order:

1. Scope Theorem 5.2 to stratified/stratifiable negation. This is now one of the paper’s most interesting claims, so make it precise.
2. Fix Lemma 2.1 by adding a locality/dependency-set assumption. Persistence alone does not prove the stated direction.
3. Weaken persistent canonicalization. Avoid “without changing determination structure” unless fully formalized.
4. Restate Theorem 6.2 in terms of support-formula treewidth, with conflict treewidth as a sufficient condition.
5. Demote transaction depth claims or move their proof into the main body.
6. Add possible-worlds/probabilistic provenance to related work.
7. Demote Theorem 2.1 to an observation, or define its terms more tightly.

⸻

Verdict

This is now a credible PODS submission. The paper has a real thesis, an algebraic construction, a meaningful Datalog application, and a quantitative extension. I would expect reviewers to find it interesting.

The main acceptance risk is that it still occasionally states framework-level claims more broadly than the current formal apparatus supports. If you tighten those statements, the paper’s strongest contribution becomes much clearer:

Determination provenance decomposes non-monotone provenance into explicit sealing commitments plus monotone derivation, yielding a filtered semiring over semantic resolutions.

That is a good PODS idea.