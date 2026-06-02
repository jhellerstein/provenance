I reviewed the attached main.tex directly. This version is much more coherent than the previous stale file I mistakenly reviewed: the body changes are mostly integrated, the appendix ordering is sensible, and the theorem scoping is much improved.

My overall pre-submission take:

This is close to submission-ready, but I would fix a handful of technical trust issues before sending.
The biggest remaining issues are not global architecture. They are precise statements that a careful PODS reviewer could catch.

Executive summary

The body reads smoothly overall. The abstract is more engaging, the intro flow is better, and the contributions now match the paper’s shape. The related-work additions help, especially the Ameloot/Anonymous/this-paper ladder. The conclusion’s probability-space paragraph is potentially nice, but one sentence should be softened.

The most important remaining problems are:

1. Corollary 3.5’s proof has a false selection/projection sentence.
2. The “difference may increase depth” appendix proposition is false as stated.
3. The monus lemma remains mathematically risky.
4. Proposition 4.2 still contains a classification-style converse despite the title being weakened.
5. The abstract/conclusion still slightly overstate Datalog generality.
6. The probability-space paragraph should say “probability-one event,” not “hypothesis test.”
7. Line 303 still says “maximal element”; use “maximum element.”

Everything else is mostly polish.

Body review

Abstract

The rewritten abstract is much better. It starts with the problem rather than the machinery, and it makes the contribution legible quickly.

Two tweaks:

First, this sentence is still a little too broad:

We instantiate the framework for transactional isolation and for
$\mbox{Datalog}^\neg$; in both, classical semantic variants
(isolation levels; negation semantics) correspond to different views
of a single shared filtration.

For Datalog, your theorem is conditional on the layered-choice decomposition. I would change it to:

We instantiate the framework for transactional isolation and for a
representative class of $\mbox{Datalog}^\neg$ programs; in both,
classical semantic variants (isolation levels; negation semantics)
correspond to different views of a single shared filtration.

Second, “Classical data provenance cannot even pose its question” is rhetorically strong. It is defensible if “classical” means ordinary single-instance semiring provenance, but possible-worlds/probabilistic provenance reviewers may bristle. Safer:

Ordinary single-instance provenance cannot pose its question in such
settings...

Not essential, but lower-risk.

Introduction

The intro is much smoother. The banking bridge works, the example now handles the delete-before-insert no-op case, and the filtration preview is digestible.

One small terminology tweak: line 119 says:

A determination is a layered sequence of irrevocable, history-indexed
commitment events...

I would prefer:

A determination is a history-indexed, layered sequence of irrevocable
commitment events...

This better matches the later formal definition.

Definition 2.3

The “maximum element” fix is good. But line 303 still says:

the maximal element of $\Spec(H)$

Change maximal to maximum there too. In this context, “maximum” is the right word because the resolved outcome must be unique/greatest, not merely undominated.

The line-311 shorthand is fine:

we write $\Spec(H)$ as shorthand for $\max_\Ord \Spec(H)$

That addresses the earlier resolved-spec-as-function issue well enough.

Theorem 2.1

This is now much safer. The softening to “any sound representation must distinguish” is exactly right.

One wording nit: the theorem statement says:

Classical semiring provenance (a single $K$-relation) correctly
represents a specification $\Spec$ iff...

That is good, but I might say “a single ordinary K-relation” to make clear that richer possible-worlds representations are not being ruled out.

Filtration / algebra

Corollary 3.5 proof: selection/projection issue

This is the most important body-level technical fix.

The added sentence says:

Selection can only shrink supports (a subset of a level-$k$ support
is level-$k$); projection unions supports over matching tuples
(a union of level-$k$ supports is level-$k$).

The projection part is fine. The selection sentence is not generally correct: an arbitrary subset of a union of equivalence classes need not itself be a union of equivalence classes.

For ordinary selection by a fixed predicate on tuple values, the support of a selected tuple is either unchanged or removed; it is not an arbitrary subset. So rewrite as:

Selection by a determination-independent predicate either preserves a
tuple's support or removes the tuple entirely; hence it preserves
filtration membership. Projection unions supports over preimages; since
$\mathcal{F}_k$ is closed under union, projection preserves filtration
membership.

This fixes both the proof and the appendix version.

Appendix proposition: “Difference may increase depth”

The appendix proposition currently says:

Relational difference does not preserve filtration level: there exist
inputs of depth~$0$ whose difference has depth~$> 0$.

But the proof uses t_2 contingent, so t_2 is not depth 0. More importantly, in the support algebra, if both inputs are in \mathcal F_k, then set difference also stays in \mathcal F_k, because \mathcal F_k is a Boolean algebra over equivalence classes. So the proposition is not just misstated; the intended claim seems false at the support level.

I would cut this proposition and the body sentence:

Conversely, relational difference can strictly increase depth...

or replace it with a more careful claim about why-not provenance / complement dependence if you really need it. But as written, it is a reviewer trap.

Single-layer/PDB proposition

This is mostly fine, but I would slightly weaken:

A depth-$1$ determination semiring over $n$ binary commitments is
isomorphic to a tuple-independent PDB...

to:

A depth-$1$ determination semiring over $n$ binary commitments is
support-isomorphic to tuple-independent PDB lineage...

Tuple-independent PDBs include probabilities; your object is the support/lineage algebra unless a measure is added.

Transactions

The transaction section is much improved and now reads as a real contribution.

RC depth 0

The theorem says RC depth 0 because no conflict resolution is required to satisfy the isolation spec. That is now stated reasonably.

One potential nit remains: your transaction outcomes are decision traces with conflict edges and \(\Ord\) as sub-trace inclusion. If RC does not care about some conflict ordering distinctions, the order should quotient them away. Add one sentence near the transaction specification:

For each isolation level $L$, $\Ord_L$ quotients distinctions not
observable to $L$: under RC, conflict orderings that do not affect
committed-read validity are compatible; under SER and SI, orderings
needed to rule out forbidden cycles remain observable.

This makes the depth-0 RC claim airtight.

Theorem 4.1

The “repeatably generable” caveat is now in the theorem statement. Good.

The lower-bound witness with the rw-rw cycle is much clearer. I would only add one explicit phrase to avoid ambiguity:

with the reads ordered before the corresponding writes so that both
edges are anti-dependencies.

Something like:

$T_\infty$ reads $x$ before $T_i$ writes $x$, and $T_i$ reads $y$
before $T_\infty$ writes $y$.

That makes the two rw edges undeniable.

Proposition 4.2

Renaming it to “SER/SI qdepth incomparability” is good. But the last sentence still reads like a classification theorem:

Transactions not matching either pattern have the same qdepth under
both levels.

And the proof has a “Conversely…” paragraph. This partially reintroduces the earlier iff problem.

I would delete the last sentence and the converse paragraph unless you want to prove a full classification. The witness result is enough and much safer:

The following two patterns witness the two directions of SER/SI qdepth
incomparability...

Then stop after the two witness proofs.

Figure 1

The visible/absent rows list representative determinations. Since the running text now says representative members, the table should too. Change row labels to:

SER, $d$ visible representative
SER, $d$ absent representative

or mention in the caption that displayed determinations are representatives of query-outcome equivalence classes.

Datalog and monus

Body theorem

The Datalog theorem is now properly conditional:

whose negative SCCs admit a layered choice basis sound and complete...

Good.

However, the abstract and conclusion still say “Datalog{}^\neg” broadly. Qualify those as “a representative class” or “the Datalog class we study.”

Truth-value order

The body still writes:

ordered $\bot \Ord \mathbf{u} \Ord \{\mathbf{t}, \mathbf{f}\}$
(with $\mathbf{t}$ and $\mathbf{f}$ incomparable)

This is understandable, but for pre-submission I would make it explicit:

ordered by $\bot \Ord \mathbf{u} \Ord \mathbf{t}$ and
$\bot \Ord \mathbf{u} \Ord \mathbf{f}$, with
$\mathbf{t}$ and $\mathbf{f}$ incomparable.

Appendix Theorem 6.1

The conditionalization is now present:

satisfying the layered-choice decomposition of Proposition...

Good.

The remaining WFS discussion still has a slightly procedural tone:

WFS stops discharging further layers...

I would soften:

In filtration terms, layers depending on that unresolved SCC remain unread.

This is not a blocker.

Monus theorem and lemma

This remains the riskiest mathematical point in the paper.

The theorem assumes naturally ordered, zero-divisor-free, \omega-continuous commutative semirings. The lemma then argues:

By $\omega$-continuity this chain has an infimum...

Standard \omega-continuity gives directed suprema / increasing-chain behavior, not arbitrary descending infima. The repeated-squaring proof is not something I would want to defend unless the exact order-theoretic assumptions are nailed down.

Given that your theorem only needs support equivalence, I strongly recommend weakening the theorem to an explicit support-test assumption:

For any finite stratified $\mbox{Datalog}^\neg$ program and any
commutative semiring with monus satisfying
\[
1_K \dot{-} v \neq 0_K \iff v = 0_K,
\]
sealing and monus compute the same supports.

Then the proof is straightforward and the risky lemma disappears or becomes a remark:

This condition holds immediately for the Boolean support abstraction
$\mathrm{PosBool}$; identifying broader algebraic classes where it holds
is left open.

If you keep the stronger lemma, it is a real reviewer-risk item.

Also, line 2627 says:

$\omega$-continuity ... ensures that infinite descending chains in $K$
stabilize

That is not generally what \omega-continuity means. I would remove or rewrite that sentence.

Consequences / quantitative measures

This section is now much cleaner than the old bypass version.

Work regret / semantic shift

These concepts read well and are worth keeping. The section is concise and now functions as a synthesis rather than a third application.

One small issue: “semantic shift” says:

Tuples whose support differs between $I$ and $I'$ --- robust under
one, contingent under the other ---

Support can differ in more ways than robust-vs-contingent. I would say:

Tuples whose support differs between $I$ and $I'$—for example, robust
under one and contingent under the other—represent...

Responsibility

The body definition is now intentionally informal and points to the appendix. Fine.

The multi-layer responsibility appendix is coherent but still long. If appendix length matters, this is one of the easiest cuts or compressions.

Related work

The new citations are integrated well overall.

The Ameloot → Anonymous → this paper positioning makes sense:

* Ameloot et al.: when resolution/coordination is needed.
* Anonymous complexity paper: cost/depth of semantic resolution.
* This paper: algebraic consequences for provenance once determinations exist.

One issue: you removed “coordination” elsewhere, but Related Work still says:

coordination-free evaluation

That is fine because it is the standard term in CALM/Ameloot, not your undefined jargon. I would leave it.

The PDB paragraph is now better, but the first related-work paragraph still says probabilistic provenance is depth 0, then the PDB paragraph says tuple-independent PDB is depth 1. You can reconcile by changing the first paragraph to:

Semiring provenance and its extensions operate after the semantic model
is fixed. Probabilistic and possible-worlds provenance add flat
uncertainty over worlds or tuple-existence events, but not
non-commuting commitment layers.

This avoids the depth-0/depth-1 tension.

Conclusion

The conclusion reads well. The new probability-space paragraph is appropriate for PODS as a forward-looking note, but one phrase is too strong/vague:

robustness becomes a hypothesis test

Robustness under a measure is more directly a probability-one event, not a hypothesis test unless you introduce sampling and statistical decision procedures.

I would change that sentence to:

Under a probability measure on $\mathcal{D}$, support ratios become
probabilities, robustness becomes a probability-one property, and work
regret becomes expected regret.

That keeps the stochastic-process connection without overclaiming.

Also qualify the Datalog sentence in the conclusion:

Transactions and the $\mbox{Datalog}^\neg$ class we study instantiate
the framework...

Appendix ordering and consistency

The appendix ordering is now good. Algebraic details first, then robustness/responsibility, then transaction/Datalog details, then systems/depth/open questions. That is much easier to navigate.

Heredity canonicalization

The H^*-conditioned notation is now present. Good.

One subtle issue remains: the proposition says canonicalization preserves the same set of resolving determinations and the same filtration. Since the replacement inserts a sealing commitment, the literal commitment sequence changes. It preserves the resolved outcomes/supports and likely an isomorphic determination structure, but “same set” is too literal.

Safer:

preserves the resolving determinations up to the natural isomorphism
that replaces $\varphi$ by $\varphi_{\seal(S)}$ followed by the
entailment $f_\varphi$...

And:

preserves the filtration up to this isomorphism.

Not urgent, but it avoids a technical nit.

Systems directions

The condensed systems appendix is now the right length. I would keep it.

Depth reduction

Good as future/design material. No major issue.

LaTeX / mechanical check

I compiled the attached file successfully with pdflatex. It produced 33 pages total in this sandbox, with the body ending on page 15. The .bib was not attached, so citation warnings are expected here.

Mechanical issues:

* ACM metadata still has fake ISBN:

\acmISBN{978-x-xxxx-xxxx-x}

* ACM warnings:
    * CCS concepts mandatory.
    * keywords mandatory.
* Overfull boxes:
    * lines 845–847: the sentence about relational difference;
    * lines 1458–1464: provenance query complexity paragraph;
    * lines 2169–2177: appendix transaction/SI section.
* \vspace warnings around conclusion/related work due to manual spacing. Not fatal, but acmart complains.
* wrapfig is removed. Good.
* Stale sec:relaxation is gone. Good.
* “coordination” appears only in a citation key and in “coordination-free evaluation” for Ameloot. That is fine.

Page budget

Since the body is exactly 15 pages, I would not add new prose unless you cut something.

If you need space, cut in this order:

1. Delete the relational-difference paragraph and appendix proposition. It is currently wrong and saves space.
2. Shorten the probability-space paragraph by 2–3 lines.
3. Trim the responsibility body paragraph by 2–3 lines.
4. In Related Work, compress the provenance-systems paragraph.
5. In Figure 1, consider moving the table to appendix if body pressure becomes severe. I would avoid this unless necessary; the table is useful.

Final priority list

Must fix before submission

1. Change line 303 “maximal” to “maximum.”
2. Fix Corollary 3.5’s selection/projection proof.
3. Remove or rewrite the relational-difference proposition and body reference.
4. Weaken or remove the risky monus lemma; use a support-test assumption instead.
5. Delete Proposition 4.2’s remaining converse/classification sentence unless fully proved.
6. Qualify Datalog generality in abstract/conclusion.
7. Change “robustness becomes a hypothesis test” to “probability-one property.”
8. Add the RC outcome-abstraction sentence or similar.

Should fix

1. Mark transaction table rows as representative determinations.
2. Change depth-1 PDB proposition to “support-isomorphic to PDB lineage.”
3. Soften heredity canonicalization from “same set” to “isomorphic structure.”
4. Fix PDB related-work depth-0/depth-1 wording.
5. Add CCS/keywords and final ACM metadata.
6. Fix the three overfull boxes.

Final verdict

This is now a strong draft. The main paper has a real, coherent contribution and the appendices mostly support rather than distract. I would not do another conceptual revision. I would do a final technical trust pass focused on the points above, especially the selection/projection proof, the relational-difference claim, and the monus lemma.

If those are fixed, I would be comfortable calling it submission-ready.