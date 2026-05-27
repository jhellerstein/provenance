I read the current /mnt/data/main.tex body and appendices. This is a noticeably tighter body than the prior version, and the new Quantitative Measures framing is a better fit than “bypass” as an operational story. The paper now reads more like:

determination provenance gives a filtered support algebra; the filtration supports robustness, qdepth, cross-spec comparison, quantitative responsibility, and complexity connections.

That is a good shape. But there are several stale seams and appendix inconsistencies that I would fix before submission.

Overall take

Body: much improved and close.
Appendices: still too sprawling and now contain some stale references/claims from earlier versions. Today’s tightening should focus on removing or compressing appendices that no longer carry their weight, and aligning the remaining appendix statements with the body.

My acceptance estimate for the current version, assuming the body page limit is now under control:

~60–70% as-is, ~70–80% after a final trust/tightening pass.

The main body has a strong arc. The biggest risk now is that a careful reviewer finds a stale appendix claim or mismatch and loses confidence.

Biggest issues to fix

1. The “bypass” rename is only half-complete

The body section is now called Consequences of the Filtration, and the subsection is Quantitative Measures. Good. But the paper still sells “bypass” in several places:

* Introduction: “bypass” is listed as one of the three forms of reasoning.
* Contribution item (iv): “Layer bypass and semantic-change analysis.”
* Contribution item (v): “robustness and bypass verification are coNP-complete.”
* Related Work: “layer bypass” has no PDB analog.
* The section label is still sec:bypass.
* Proposition label is still prop:bypass.

If bypass no longer has an operational payoff, stop leading with it. I would rephrase this as compositional depth bounds or irrelevance of higher layers.

Suggested contribution rewrite:

\item \emph{Quantitative comparison and complexity}: the filtration
      supports per-tuple depth measures, work regret, semantic shift,
      commitment responsibility, and a connection to PDB lineage:
      depth-$1$ provenance coincides with tuple-independent PDB lineage,
      while higher depths correspond to layered correlations
      (Section~\ref{sec:filtration-consequences}).

Then change “bypass verification is coNP-complete” to something like:

robustness and depth-certification are coNP-complete

or remove the bypass hardness claim entirely unless you define it explicitly.

2. The responsibility section is inconsistent between body and appendix

The body says:

each commitment is a player; the game’s value is 1 if t’s support changes when that commitment is removed

But the appendix defines a different game:

v(C)=|\{D\in S \mid D \text{ agrees with }D^*\text{ on }C\}|/2^{n-|C|}.

That is a conditional probability / expected presence game, not a “support changes when removed” game. These need to match.

I would change the body to match the appendix:

Fix a realized determination $D^*$ and a tuple $t$.  For a set of
commitments $C$, the game value is the fraction of completions agreeing
with $D^*$ on $C$ in which $t$ holds.  The Shapley value of a commitment
is its average marginal contribution to that conditional presence
probability.

Also, the body example says:

\varphi_{T_2 \prec T_Q} has Shapley value 1 for d’s contingency: removing it makes d robust.

That does not look right. Removing the commitment does not make d robust; it makes the situation less resolved. In the running example, d’s visibility depends on a class of orderings, not one single commitment in a simple way. I would delete that numerical claim and replace it with a softer sentence:

In Example~\ref{ex:running-revisited}, responsibility is concentrated on
the ordering commitments that determine whether $T_Q$ observes
$T_2$'s insert before an effective delete.

Let the appendix handle exact responsibility.

3. The multi-layer responsibility appendix is stale

Appendix “Multi-Layer Responsibility: Worked Example” says it uses Example~\ref{ex:overlapping-cycles}: five transactions with two cycles sharing T_3.

But in the body, ex:overlapping-cycles is now the OCC per-batch depth example with three transactions T_1,T_2,T_3. So the appendix is referring to an old version of the example.

This is a serious stale-reference issue. Either:

* rename the appendix example and define the five-transaction example locally, or
* cut the entire appendix.

Given page pressure, I would cut it. The responsibility appendix already has enough material, and the stale example is risky.

4. The Datalog general appendix still overclaims

The body theorem is carefully conditional:

programs whose negative SCCs admit a layered choice basis sound and complete for stable models

Good.

But the appendix states:

For any finite Datalog^\neg program, the canonical layered choice basis ...
is sound and complete.

That is too broad. Stable models may not exist; SCC-local stable extensions do not always compose without splitting assumptions; WFS is not generally “consecutive forced layers” unless the layered-choice structure behaves well.

Change the appendix proposition to:

For programs satisfying the layered-choice assumptions of
Theorem~\ref{thm:negation-filtration}, the canonical layered choice
basis is sound and complete...

Or:

For the class considered in Theorem~\ref{thm:negation-filtration}...

Also change the theorem “General negation semantics as filtration levels” to “Layered-choice negation semantics as filtration levels.”

This is probably the highest-priority appendix correctness fix.

5. The monus-elimination proof is too strong

The theorem statement says support equivalence, but the proof concludes:

the final annotation of every atom is identical under both approaches.

That is stronger than support equivalence and may be false depending on the monus semiring. The line

1_K \dot{-} v = 0_K \quad \text{for all } v\neq 0_K

is not something I would want to defend for arbitrary naturally ordered, zero-divisor-free commutative semirings without very careful assumptions.

Safer version:

* State the theorem as Boolean support equivalence only.
* In the proof, only show zero/nonzero equivalence.
* Avoid claiming identical annotations.

Suggested replacement:

Thus the negated literal is nonzero under monus exactly when the sealed
atom has zero support. Since subsequent positive evaluation over a
zero-divisor-free semiring preserves zero/nonzero status, the two
constructions produce the same supports. We do not claim equality of
full $K$-annotations.

That should neutralize a likely reviewer objection.

6. RC depth 0 still needs a modeling sentence

The transaction section says outcomes are decision traces ordered by sub-trace inclusion. Then RC says all outcomes are comparable / no outcome contradicted. That is not obvious if two traces differ by conflict order.

Add one sentence in the transactional specification paragraph:

For each isolation level $L$, $\Ord_L$ quotients distinctions not
observable to $L$: under RC, conflict orderings that do not affect
committed-read validity are compatible; under SER and SI, orderings
needed to rule out forbidden cycles remain observable.

Or phrase Theorem 4.1(a) as:

depth 0 relative to the isolation-validity abstraction.

Without this, a transaction reviewer may ask why RC has depth 0 if the trace still records incomparable schedules.

7. Theorem 4.1 remains slightly too broad

The theorem says:

Under any isolation level L that forbids some cycle type … with scheduling discretion: worst-case depth \Theta(n).

Then you add a caveat after the proof. Better to move the caveat into the theorem:

Under any such $L$ whose forbidden pattern can be generated repeatedly
around a surviving discretionary transaction...

This avoids a universal claim that the proof does not quite establish.

8. The qdepth transaction example still has stale shorthand

In Example 3.4, line paraphrase:

d has qdepth 1: determinations where T_Q is serialized before T_3

This misses the insert condition and the delete-before-insert no-op case. Replace with:

determinations where $T_Q$ observes $T_2$'s insert before any effective delete

This is minor but important because the intro now gets this right.

Appendix tightening plan

Since you said today is appendix tightening, here is the concrete cut/compress proposal.

Cut entirely: Multi-Layer Responsibility Worked Example

Savings: roughly 0.6–0.8 pages.
Reason: stale reference, not essential, and responsibility is already developed later.

If you want to keep the idea, add one paragraph at the end of “Multi-Layer Responsibility”:

In multi-layer settings, responsibility is computed layer-by-layer,
conditioned on earlier commitments.  A tuple with qdepth $k$ has zero
responsibility in layers deeper than $k$.

That already appears in substance.

Compress: Responsibility Additional Results

Savings: 0.4–0.6 pages.

Keep:

* definition of presence game;
* #P-hardness theorem;
* bounded-treewidth theorem;
* one paragraph on multi-layer conditioning.

Cut:

* additive approximation proof, or reduce to one sentence;
* budget compositionality theorem, unless you need it for body claims.

The budget theorem is nice but not central. It also assumes the full independent cube 2^n and a realized presence game. If kept, add:

assuming D^*\in\mathrm{supp}(t)

because B(t)=1-|\mathrm{supp}(t)|/2^n uses v(N)=1.

Compress: Protocol-Specific Determination Structures

Savings: 0.7–1.0 pages.

This appendix repeats the body. Keep only the precise witnesses and protocol distinctions.

I would cut or shrink:

* “Protocol-Agnostic Depth Bounds” prose repeating Theorem 4.1.
* Some 2PL detail.
* Some MVTO detail.

Keep:

* explicit T_\infty lower-bound witness;
* per-batch 2PL/OCC/MVTO depth 2 summary;
* one paragraph comparing protocols.

Right now this appendix reads like a second transaction section. The body already does most of the work.

Compress or conditionalize: Datalog General Case

Savings: 0.5–0.8 pages.

This is the riskiest appendix. You can improve both correctness and length by replacing the broad general proof with a conditional statement:

For programs satisfying the layered-choice assumptions of
Theorem~\ref{thm:negation-filtration}, the proof is by induction over
the SCC condensation order...

Then keep the nested-cycles example, but shorten the WFS discussion.

Cut or sharply shorten: Within a Determination

Savings: 0.5 pages.

This appendix is philosophically useful but not essential. The main body already explains the support semiring and filtration. I would keep only:

* sequential discharge vs algebraic combination;
* one proposition: determined specs admit semiring provenance.

Move “Open Questions” inside it to the final Open Questions appendix or cut duplicated universality text.

Keep: Across Determinations

This appendix supports the core algebra. But remove duplication with body if needed. The join/union/projection/selection proposition is useful.

Keep but shorten: Systems Agenda

This is now well-framed, but it is still long. If page count matters beyond body, trim examples and keep the three-level map plus vertical/horizontal parsimony. The certificates section is useful but could be half as long.

Keep: Heredity Canonicalization

This is now technically aligned with H^*-conditioning and should stay if you need it for theoretical cleanliness. But it can be shorter. The proof is verbose; compress (b)–(e).

Keep: Depth Reduction

This is a nice final appendix and connects to practice. But the proof can be one paragraph. The examples are useful; keep them.

Body tightening suggestions

The body is mostly fine, but I would make these edits.

Rename Section label and contribution

Change:

\label{sec:bypass}

to:

\label{sec:filtration-consequences}

Update references. This prevents old “bypass” terminology from leaking.

Contribution item (iv)

Current:

Layer bypass and semantic-change analysis

Change to:

Quantitative measures and semantic-change analysis

or:

Filtration-based quantitative diagnosis

Contribution item (v)

Current:

robustness and bypass verification are coNP-complete

Change to:

robustness and depth-certification are coNP-complete

or just:

robustness is coNP-complete

Since “bypass verification” is no longer a front-facing concept, I would drop it.

Related Work PDB paragraph

The first related-work paragraph says algebraic provenance and probabilistic provenance operate at depth 0, but the PDB paragraph says tuple-independent PDB is depth 1. That is a small contradiction.

Change the first paragraph to:

Classical semiring provenance operates after a semantics is fixed; PDB lineage adds flat uncertainty but no non-commuting commitment layers.

Then the later depth-1 PDB statement fits.

Remove “aggregate” from provenance queries

Line paraphrase:

provenance queries can select individual tuples, join across transactions, or aggregate

But the paper’s query language is positive RA; aggregation is not developed. Either remove “or aggregate” or say “monotone aggregate extensions, not treated here.”

I would remove it.

Technical issues worth fixing

Support semiring with projection/selection

The appendix says projection support is a superset and selection support is a subset. The body says positive RA cannot increase qdepth. Projection can union supports over preimages, but since \mathcal F_k is closed under union, depth still does not increase. Selection is fine. Add one sentence to the body corollary proof or statement:

Projection unions supports over preimages and selection takes subsets induced by predicates; both preserve filtration membership.

This fully justifies “positive RA,” not only join/union.

Ambient determination space comparison

The body now defines \mathcal D^\star_\Phi, good. But it says each specification selects a resolving subset and supports/qdepth are compared over the common carrier. Add:

We extend each support by zero outside $\mathcal D_I$.

This makes cross-spec comparison precise.

Datalog WFS theorem

The body theorem says WFS reads \mathcal F_k. The appendix general theorem says WFS may read \mathcal F_{k+d^*}. These are not consistent unless the body theorem is restricted to the representative case where d^*=0.

Fix body theorem:

For the representative class below, where the negative choice layers are
not forced by the sealing prefix, WFS reads $\mathcal F_k$...

Or generalize body theorem to mention d^*. I prefer the first; it keeps the body simple.

Punchlist

Must fix

1. Align “bypass” terminology with the new Quantitative Measures section.
2. Fix responsibility game mismatch between body and appendix.
3. Delete or repair the stale Multi-Layer Responsibility appendix.
4. Restrict the Datalog general appendix to the layered-choice class.
5. Weaken the monus-elimination proof to support equivalence only.
6. Add a sentence making RC depth 0 relative to the RC outcome/order abstraction.
7. Move the “repeatably generable forbidden pattern” caveat into Theorem 4.1.
8. Fix the stale qdepth wording for d in Example 3.4.

Should fix

1. Extend supports by zero outside \mathcal D_I for cross-spec comparison.
2. Remove “aggregate” from provenance queries.
3. Resolve PDB depth-0/depth-1 wording in Related Work.
4. Add projection/selection sentence to positive RA filtration preservation.
5. Rename sec:bypass and prop:bypass.

Appendix cuts

1. Cut Multi-Layer Responsibility worked example.
2. Compress Responsibility appendix by dropping approximation proof and maybe budget theorem.
3. Compress Protocol-Specific appendix by removing repeated explanation.
4. Conditionalize and shorten Datalog General Case.
5. Trim Systems Agenda examples.
6. Merge/cut “Within a Determination” open questions with final Open Questions.

Final take

The body is now close to where it should be. The new quantitative section is a better endpoint than the old bypass story, but the terminology needs to catch up. The appendices are where the danger is: they contain several stale or overbroad claims, and they are longer than needed.

I would not rethink the main paper. I would do a targeted appendix cleanup: remove stale examples, conditionalize Datalog generality, align responsibility definitions, and cut repeated protocol prose. After that, this should read as a tight, credible theory submission with useful systems implications.