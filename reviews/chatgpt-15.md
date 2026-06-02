I read the newly attached /mnt/data/provenance2.tex directly, cover to cover, including appendices, and compiled it locally. This version is much closer to submission-ready than the file I previously reviewed. The line-311 point about taking the maximum/maximal resolved outcome is present, and it addresses the earlier “resolved spec as function” concern in spirit.

My overall take:

Body: strong and coherent.
Appendices: substantially improved, but still contain a few theorem-level risks.
Pre-submission status: close, but I would make several targeted fixes before sending.

I would put this version around 70–80% submission strength after the final fixes below. The core paper is now clear: determination provenance, support semiring, filtration/qdepth, transactions, Datalog, quantitative measures.

Top must-fix items

1. “Maximal element” should be “maximum,” and the definition needs existence

You note at lines 311–320 that retrospective analysis takes the maximal element of \(\Spec(H)\), and Definition 2.3 says a determined history has a chain and then writes \(\Spec(H)\) for the chain’s maximum.

This basically fixes the earlier issue, but I would tighten the language:

* A chain can have multiple maximal elements only if comparable, but it may have no maximum unless finite or complete.
* You say “maximal” at line 313, then “maximum” at line 320. Use maximum consistently.
* Definition 2.3 should require the maximum to exist.

Suggested revision:

A specification is determined at $H$ if $\Spec(H)$ is a nonempty chain
under $\Ord$ with a maximum element. For a determined history, we write
$\Spec(H)$ by abuse of notation for this maximum resolved outcome.

This keeps your intended “resolved spec is a function” point, while avoiding a technical nit.

2. The notation \(\Spec(H)\) is overloaded in a way reviewers may trip on

Before Definition 2.3, \(\Spec(H)\) is a set of admissible outcomes. After Definition 2.3, for determined histories, you write \(\Spec(H)\) for the maximum element.

That is convenient but dangerous. You already flag it, but a few later lines become ambiguous, especially where you write things like:

\mathsf{obs}(\Spec(H))

at line 577. That only typechecks if \(\Spec(H)\) is the resolved outcome, not the set.

I would introduce a separate notation:

\res_\Spec(H) \triangleq \max_\Ord \Spec(H)

Then use \(\mathsf{obs}(\res_\Spec(H))\) in the provenance definition. You can still say “by abuse of notation we write \(\Spec(H)\)” informally, but formal definitions should use \(\res_\Spec(H)\).

This is a small notation fix with high trust value.

3. Theorem 2.1 still says “provenance must be indexed by determination”

The theorem is now much safer than older versions, but line 501 says:

provenance must be indexed by determination.

That is a bit too absolute. A possible-worlds provenance reviewer may say a representation could encode alternatives in some other richer object.

Change to:

any sound and complete representation must distinguish the two determinations.

The theorem title “Classical provenance is pointwise in determinations” is good. Preserve that. Just avoid “must be indexed” as a universal representation claim.

4. Cross-specification comparison needs zero-extension over the ambient carrier

Lines 726–732 define an ambient determination space \mathcal D^\star_\Phi and say each specification I selects a resolving subset \mathcal D_I. Good. But to compare supports/qdepth over the common carrier, you should explicitly extend supports by zero outside \mathcal D_I.

Add after line 732:

We extend each support by zero outside $\mathcal D_I$, so every
specification denotes a support over the common carrier
$\mathcal D^\star_\Phi$.

This makes work regret and semantic shift formally grounded.

5. The transaction running example still compresses equivalence classes too much

The intro handles the delete-before-insert no-op case correctly. But in Example 4.1, lines 963–970 say two equivalence classes arise and then define:

D_{\mathsf{in}} =
\varphi_{T_2 \prec T_Q}\cdot \varphi_{T_Q \prec T_3}

and

D_{\mathsf{out}} =
\varphi_{T_2 \prec T_3}\cdot \varphi_{T_3 \prec T_Q}.

This is okay only if these are explicitly representatives of query-equivalence classes. Otherwise the visible case T_3 \prec T_2 \prec T_Q is missing.

Change:

Two equivalence classes of determinations arise:

to:

For the query $Q$, the resolving determinations quotient into two
query-outcome/provenance equivalence classes. We write representative
members as:

Then the example is safe.

6. RC depth 0 needs the outcome-abstraction sentence

The theorem says RC depth 0 because no cycle type is forbidden and all outcomes are \(\Ord\)-comparable. But the transactional outcome domain is decision traces ordered by subtrace inclusion. If traces include conflict orderings, different RC schedules may still be incomparable unless \(\Ord_{\mathrm{RC}}\) quotients distinctions RC does not observe.

Add in the transactional specification paragraph, around lines 945–951:

For each isolation level $L$, $\Ord_L$ quotients distinctions not
observable to $L$: under RC, conflict orderings that do not affect
committed-read validity are compatible; under SER and SI, the orderings
needed to rule out forbidden cycles remain observable.

Or say “depth 0 relative to the isolation-validity abstraction.” Without this, a transaction reviewer may push on why RC is determined.

7. Proposition 4.2’s “iff” is still too strong

Lines 1074–1094 state an iff classification of isolation-sensitive transactions:

iff T_i participates in write-skew or FCW-forced abort pattern.

This is risky as a theorem unless you prove it for the exact Adya model, tuple class, query class, and output-tuples notion. The proof is really a pair of witnesses plus a sketchy converse.

I would weaken the title and statement:

\begin{proposition}[SER/SI qdepth incomparability]
...
The following two patterns witness the two directions of incomparability.

Then state:

* write skew gives \mathrm{qdepth}_{SER} > \mathrm{qdepth}_{SI};
* FCW-forced abort gives \mathrm{qdepth}_{SI} > \mathrm{qdepth}_{SER}.

If you want a classification, make it explicitly for “transaction-local output tuples in the simplified Adya graph model.” But the incomparability result is enough and much safer.

8. Datalog general theorem should repeat the layered-choice assumption

The body theorem is nicely restricted:

whose negative SCCs admit a layered choice basis sound and complete for stable models

But Appendix Theorem 6.1 at lines 2455–2475 says:

For a finite Datalog{}^\neg program having k stratification layers and nesting depth d…

It does not restate the layered-choice assumption, even though Proposition 6.1 just above does. To avoid overclaiming, make the theorem itself conditional:

For a finite $\mbox{Datalog}^\neg$ program satisfying the layered-choice
decomposition assumptions of Proposition~\ref{prop:canonical-basis-sc},
with $k$ stratification layers and nesting depth $d$, ...

This one-line edit would eliminate a major reviewer objection.

9. The monus lemma remains the riskiest proof in the paper

The monus section is much clearer, but the algebraic lemma is still the most mathematically vulnerable part.

The proof at lines 2705–2722 uses repeated squaring, a descending chain, and says:

By \omega-continuity this chain has an infimum…

Standard \omega-continuity for semirings is usually about directed suprema / increasing chains, not arbitrary descending infima. The proof also asserts that the infimum is still nonzero; that is not generally guaranteed.

I would not want to defend this lemma as written unless you are very sure about the exact order-theoretic assumptions.

The safe fix is to state the exact support-test property as an assumption:

For any finite stratified $\mbox{Datalog}^\neg$ program and any
commutative semiring with monus satisfying
\[
1_K \dot{-} v \neq 0_K \iff v=0_K,
\]
sealing and monus compute the same supports.

Then say:

This includes the Boolean support abstraction used in this paper; a
full algebraic characterization of quantitative monus support-tests is
left open.

This weakens the theorem but makes it bulletproof. If you keep the stronger lemma, at least move it to a “sufficient algebraic condition” proposition and add the needed order-completeness assumptions very carefully.

10. Related Work still has a small depth-0/depth-1 tension

Lines 1499–1505 say probabilistic provenance operates after a fixed semantic model and is depth 0. Lines 1520–1526 say tuple-independent PDB is depth 1. This is explainable, but as written it can look inconsistent.

Change the first paragraph to:

Semiring provenance and its extensions operate after the semantic model
is fixed. PDB lineage adds flat uncertainty over tuple-existence events,
but no non-commuting commitment layers.

Then the depth-1 PDB claim fits naturally.

Medium-priority issues

11. Corollary “positive RA respects filtration” only proves join/union

The corollary says “Under positive relational algebra” but only states join and union. Selection and projection are standard and should be mentioned.

Add to the proof:

Selection preserves supports; projection unions supports over preimages.
Since each $\mathcal F_k$ is closed under union, both preserve filtration
membership.

Then “positive RA” is fully justified.

12. The depth-1 = PDB proposition is slightly overbroad

Line 1477:

A depth-1 determination semiring over n binary commitments is isomorphic to a tuple-independent PDB.

Strictly, tuple-independent PDB also has probabilities; your structure is lineage/support. Better:

A depth-$1$ determination semiring over $n$ binary commitments is
support-isomorphic to tuple-independent PDB lineage over $n$
tuple-existence events.

Then you can say a probability measure can be placed on commitments if desired.

13. The Datalog theorem’s WFS clause is still a modeling claim

The theorem says WFS reads \mathcal F_k in the representative body theorem and \mathcal F_{k+d^*} in the appendix theorem. That is okay if the representative class has d^*=0. But the body theorem should say “for this representative class” more explicitly in the theorem statement or proof.

Currently it says “The classical negation semantics correspond…” which may sound general despite the restricted premise. I would change:

The classical negation semantics correspond to filtration levels:

to:

For this class, the usual negation semantics correspond to filtration levels:

14. The figure/table for transaction depths still has stale shorthand

Figure 1 lines 1159–1163 shows:

* SER, d visible: T_2 \prec T_Q \prec T_3
* SER, d absent: T_2 \prec T_3 \prec T_Q

Same issue as above. Add “representative” in the table entries or caption:

SER, $d$ visible representative
SER, $d$ absent representative

or use the support prose instead of exact sequences.

15. Responsibility appendix is improved, but still long and slightly confusing

The presence game definition is now coherent, and the worked example acknowledges negative responsibility for absence. That is good.

But the multi-layer worked example is long and may distract. It is appendix-only, so not a correctness blocker. If page pressure exists, this is one of the first cuts.

Also, at lines 1825–1826:

Total responsibility sums across layers to 1-\Pr[t \text{ holds}] when t holds in D^*

This is true for the examples, but only if the value function is exactly the conditional probability game and layers are traversed along the realized path. I would say:

In this telescoping layer-by-layer calculation...

to make clear it is not the general Shapley-sum theorem.

16. The appendix statement “WFS stops discharging further layers” is too operational

Lines 2500–2502 say WFS stops discharging further layers that depend on an unforced SCC. That is a helpful intuition, but WFS is not literally executing your commitment basis. Maybe:

In filtration terms, layers depending on that unresolved SCC remain unread.

This avoids making a procedural claim about WFS.

17. “Sealing predicates do not commute across strata” is too absolute

Line 2383:

Sealing predicates do not commute across strata

If stratum i+1 genuinely depends on stratum i, yes. But independent strata could commute. Safer:

Sealing predicates are ordered by stratum dependencies; they need not
commute across dependent strata.

This aligns with your note that independent SCCs can share layers.

Copyediting and style fixes

Abstract

The abstract is clean. One caveat: line 84 says:

in both, classical semantic variants … correspond to different views of a single shared filtration.

For Datalog this is only for the representative/layered-choice class. Suggested:

We instantiate the framework for transactional isolation and for a
representative class of $\mbox{Datalog}^\neg$ programs...

Introduction

Line 119:

A determination is a layered sequence…

Given your history-indexed definition later, I would change to:

A determination is a history-indexed, layered record...

Small but more accurate.

Line 164:

quantitative diagnosis from the support’s measure

Maybe:

quantitative diagnosis can be obtained by placing a measure on supports

This avoids implying a canonical uniform measure.

Contributions

Contribution (i) says “The determination semiring.” That is fine, but maybe use:

The support semiring over determinations

to avoid the old nit that determinations themselves do not form the semiring.

Contribution (ii) says worst-case \Theta(n) “with scheduling discretion.” Good, but maybe add “for repeatably generable forbidden patterns” or leave that in the theorem. Since the contribution list is high-level, it is okay.

Conclusion

Line 1577–1578 repeats:

in both, classical semantic variants … correspond to different views of a shared filtration.

Again, for Datalog qualify:

in transactions, isolation levels correspond...; in the Datalog class we study, negation semantics correspond...

LaTeX / mechanical issues

I compiled /mnt/data/provenance2.tex twice. It compiles to 34 pages in this sandbox. The bibliography file was not attached, so all citation warnings are expected here if the repo has the .bib.

Mechanical items:

* ACM metadata is still placeholder unless this is a draft-only file:
    * Full Conference Name
    * Month Year
    * Location
    * fake ISBN.
* ACM warnings:
    * CCS concepts mandatory.
    * keywords mandatory.
* Undefined citations in this sandbox due to missing bibliography.
* No persistent undefined cross-references after rerun except citation-related noise? There are reference warnings on first run; after second run the grep mostly shows citation warnings, but check in your full repo with .bib.
* Overfull boxes:
    * lines 325–331: determined-spec paragraph.
    * lines 760–762: short proof of filtration closure.
    * lines 2010–2015: SI appendix / table-ish paragraph.
    * lines 2565–2570: stable-model provenance line.
* wrapfig is imported but appears unused now. Remove it.
* \jmh macro is still defined. Remove if unused.
* \label{sec:relaxation} remains attached to Depth Reduction. Not harmful, but stale. Rename to sec:depth-reduction or remove the extra label.
* There are multiple labels on several sections. Not fatal, but for final submission I would reduce duplicates unless needed for old references.

Suggested final punchlist

Must fix

1. Change “maximal element” to “maximum element” and require maximum existence in Definition 2.3.
2. Introduce or use \(\res_\Spec(H)\) for the resolved outcome to avoid \(\Spec(H)\) set/element overload in formal definitions.
3. Soften Theorem 2.1’s “must be indexed” to “must distinguish.”
4. Add zero-extension outside \mathcal D_I for cross-spec comparisons.
5. Clarify running transaction equivalence classes as representatives in Example 4.1 and Figure 1.
6. Add the RC outcome-abstraction/quotient sentence.
7. Weaken Proposition 4.2 from “iff classification” to “SER/SI qdepth incomparability witnesses,” or state a narrower model.
8. Add the layered-choice assumption directly to Appendix Theorem 6.1.
9. Weaken/reframe the monus lemma or add the exact support-test assumption.
10. Fix Related Work’s depth-0/depth-1 PDB wording.

Should fix

1. Add projection/selection to the positive RA filtration proof.
2. Change depth-1 PDB proposition to “support-isomorphic to PDB lineage.”
3. Qualify Datalog “classical semantics” phrasing in abstract/conclusion.
4. Replace “sealing predicates do not commute” with dependency-qualified wording.
5. Shorten or clarify the responsibility worked example if appendix space matters.

Mechanical

1. Fill ACM metadata, CCS, keywords.
2. Remove unused wrapfig and \jmh.
3. Fix overfull boxes.
4. Check .bib in the repo.
5. Remove stale extra label sec:relaxation unless needed.

Final verdict

This is now a strong and coherent draft. The big conceptual problems from earlier are mostly gone. The paper’s remaining vulnerabilities are localized:

* one notation issue around resolved outcomes;
* one over-strong transaction classification;
* one too-general Datalog appendix theorem;
* one risky monus algebra lemma.

Fix those, and I would be comfortable calling this submission-ready.