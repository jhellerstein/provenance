No — after checking the re-attached /mnt/data/main.tex directly, my previous response was not reliable for this version. It looks like I either saw a stale/mismatched file state or over-reported older issues that are in fact fixed in the current source. Thanks for catching it.

I verified the disputed items in the reattached file. Several things I previously flagged are actually fixed:

* \mathcal D is explicitly history-indexed: the paper defines elements as resolved histories with minimal determinations, modulo outcome/provenance equivalence.
* Minimality is now relative to the same history context: removing a commitment while keeping the rest of the history fixed.
* The layered commitment basis is explicitly an input, with a layering function \lambda:\Phi\to\{1,\ldots,d\}.
* The stale “non-HAT” phrase appears to be gone.
* Per-batch depth is stated as seal + processing-order commitment.
* MVTO batching is now stated as depth 2, while fully reactive MVTO is depth 0. That distinction is coherent.
* Heredity canonicalization is now explicitly H^*-conditioned, using \(\Spec_{H^*}\).
* “Supports over resolving determinations form a semiring” is present in the contributions.
* Datalog is qualified in the contribution as “for a representative class.”

So I need to retract the earlier claim that the uploaded source had regressed to the old theorem stack. That was wrong for this reattached file.

What I still see as real issues in this version

1. Theorem title: “Classical provenance requires resolution”

The statement itself is much safer than the old “iff determined” claim. It says any representation must distinguish determinations that disagree on tuple membership or annotation, and that classical provenance as a single K-relation suffices only when all determinations agree.

That is basically fine.

But the title still sounds like the older overclaim. I would rename it:

\begin{theorem}[Classical provenance is pointwise in determinations]

or:

\begin{theorem}[Single-instance provenance requires agreement across determinations]

This is a rhetoric/trust fix, not a formal blocker.

2. Transaction theorem still says “protocol-agnostic”

The theorem begins:

The result is protocol-agnostic:

But the content is really about protocol classes: reactive protocols, discretionary protocols, and batched protocols. I would change this to:

The result abstracts over protocols by class:

or:

The following bounds depend only on the protocol's resolution class:

“Protocol-agnostic” slightly overpromises because the proof depends on whether the protocol has scheduling/victim discretion.

3. The \Theta(n) lower-bound witness has explicit edges, but both are labeled rw

In the appendix lower bound, you now use two objects:

T_\infty reads x and writes y.
T_i writes x and reads y.

and then say:

T_\infty \xrightarrow{\mathsf{rw}} T_i
...
T_i \xrightarrow{\mathsf{rw}} T_\infty

This gives a cycle, but the second edge deserves checking. If T_i reads y before T_\infty writes y, then yes, T_i \xrightarrow{\mathsf{rw}} T_\infty. That is coherent. Earlier I had suggested a wr edge, but two rw anti-dependencies are also a valid Adya-style cycle if the history makes those read-before-write relationships explicit.

Actionable suggestion: make the event order explicit in one sentence:

The history orders each $T_i$'s read of $y$ before $T_\infty$'s later write of $y$,
so the second edge is an anti-dependency
$T_i \xrightarrow{\mathsf{rw}} T_\infty$.

That prevents a reviewer from wondering how T_i can read y from T_\infty.

4. The theorem’s “any isolation level that forbids some cycle type” is still broad

Current statement:

Under any isolation level $L$ that forbids some cycle type ...
with scheduling discretion: worst-case depth $\Theta(n)$.

This is likely true for the class you mean, but as written it is a bit too universal. I would add one qualifier:

Under any Adya-style isolation level $L$ whose forbidden cycle pattern
can be generated repeatedly around a surviving transaction ...

or add after the theorem:

The lower bound assumes the forbidden pattern is repeatably generable
around a transaction whose survival remains discretionary; this includes
the SER and SI constructions in Appendix~...

That makes the theorem much safer.

5. “Canonical” layering language may still be a little strong

The filtration section says:

In the instantiations below, the layering is canonical: it is the
coarsest assignment consistent with the commutativity and dependency
structure of $\Phi$.

This is probably okay if you are confident, but “canonical” invites proof obligations. Safer:

In the instantiations below, we use the natural coarsest assignment
consistent with the commutativity and dependency structure of $\Phi$.

or:

In the instantiations below, the domain supplies a natural coarsest
layering...

6. The abstract/contributions still undersell the newer transaction result

This is not a correctness issue. But the current paper has enough transaction substance that I would make sure the abstract says:

* reactive protocols have depth 0;
* discretionary protocols can have \Theta(n) depth;
* batching gives constant per-batch depth;
* SER and SI are incomparable in query-relative depth.

That is a real result and should be visible up front.

Updated meta-assessment

For this reattached version, my prior “40–50%” estimate was too pessimistic. Based on the actual source now in /mnt/data/main.tex, I would put it back around:

~60–70% PODS odds after a final precision pass.

The main remaining work is not conceptual. It is a small trust pass:

1. rename the classical-provenance theorem;
2. qualify the transaction theorem’s universality;
3. make the lower-bound event order explicit;
4. soften “protocol-agnostic” and “canonical” wording;
5. strengthen the abstract/contribution pitch around the transaction results.

----
I think you ignored new material in the section before Related Work (which was also now foreshadowed earlier and has associated new appendices)

----
Yes — you’re right. I underweighted the new Layer Bypass / Filtration Structure / Depth Reduction material, and that changes the paper’s current shape. The paper is no longer just:

determination provenance + transactions + Datalog

It is more like:

determination provenance gives a filtered support algebra; the filtration enables bypass, relaxation assessment, query-complexity analysis, and depth-reduction transformations.

That is a stronger and more unified story. It also means the abstract/intro/contributions should be adjusted to make the filtration consequences visible earlier.

What the new material adds

The new section before Related Work does three important things.

First, Layer Bypass makes qdepth operational. It says: if the tuples needed by a provenance query are already settled before layer k, then the query can skip layers k,\ldots,d. That turns qdepth from a descriptive measure into an optimization/reduction criterion.

Second, Filtration Structure reframes the filtration as a shared coordinate system across specifications. This gives you two new payoffs:

* Quantitative relaxation assessment: compare two specs tuple-by-tuple by separating “work regret” from “semantic shift.”
* Provenance query complexity: depth-1 support behaves like PDB lineage; higher depth behaves like layered PDB evaluation with conditioning between layers.

Third, the new Depth Reduction appendix makes the theory constructive: depth can be reduced by coarsening \(\Ord\), forcing commutation, or replacing commitments by entailments. That gives a nice “design knobs” story for transactions and Datalog.

This is not peripheral. It should be part of the paper’s front-facing contribution.

Suggested revised contribution list

I would now use six contributions, not five. Something like:

\paragraph{Contributions.}
\begin{enumerate}[label=(\roman*),nosep,leftmargin=*]
  \item \textbf{Determination provenance.}
        We formalize ambiguous specifications whose admissible outcomes
        may be incompatible, and model their resolution by
        history-indexed commitment events.  Classical semiring
        provenance is pointwise in each resolved history; determination
        provenance records, for each tuple, the set of resolved-history
        classes in which it holds.
  \item \textbf{A filtered support semiring.}
        Supports over resolving determinations form a commutative
        semiring.  A layered commitment basis induces a filtration of
        sub-semirings, yielding \emph{query-relative depth}: the number
        of semantic-resolution layers a tuple depends on.  Positive
        relational algebra respects this filtration.
  \item \textbf{Layer bypass and semantic-change analysis.}
        The filtration gives operational consequences.  Queries whose
        inputs have depth below layer $k$ can bypass layers
        $k,\ldots,d$.  Because specifications over the same commitment
        basis share a filtration, we can compare specification changes
        tuple-by-tuple, separating coordination \emph{work regret} from
        genuine \emph{semantic shift}.
  \item \textbf{Transactional determination depth.}
        We instantiate the framework using Adya-style conflict cycles.
        Read committed and reactive protocols have depth zero relative
        to isolation validity; discretionary conflict resolution can
        have worst-case depth $\Theta(n)$; and batched protocols have
        constant per-batch depth via a seal plus a batch-order
        commitment.  The filtration also gives a per-tuple separation of
        serializability and snapshot isolation: neither dominates the
        other in query-relative depth.
  \item \textbf{Negation as layered determination.}
        For a representative class of Datalog programs with negation,
        stratified, well-founded, and stable-model semantics correspond
        to different readings of a single filtration.  For stratified
        negation, monus elimination shows that layered monotone
        supports are support-equivalent to semirings with monus.
  \item \textbf{Complexity, attribution, and depth reduction.}
        Robustness is coNP-complete, and commitment responsibility gives
        a Shapley-style attribution of contingency to semantic
        commitments.  We relate depth-1 determination provenance to PDB
        lineage, view higher depths as layered PDB evaluation, and
        identify three mechanisms for reducing determination depth:
        coarsening outcomes, forcing commutation, and replacing
        commitments by entailments.
\end{enumerate}

This better reflects the current paper. The new material deserves its own contribution item because it is the part that makes the framework useful beyond the two instantiations.

Suggested abstract adjustment

The abstract should also mention bypass/depth reduction. I would modify the middle/end to something like:

These supports form a commutative semiring, and layered commitments
induce a filtration of sub-semirings.  The filtration measures a tuple's
query-relative depth: how many layers of semantic resolution the tuple
depends on.  Positive relational algebra respects the filtration, giving
a bypass principle: queries whose inputs are settled before layer $k$
can skip later layers.  The same filtration provides a common coordinate
system for comparing specifications, separating coordination work
regret from genuine semantic shift, and suggests three mechanisms for
reducing depth: coarsening outcomes, forcing commutation, and replacing
commitments by entailments.

Then the instantiation paragraph can stay, but I would add one sentence about PDBs:

At depth one, the support algebra coincides with Boolean PDB lineage;
at higher depths, determination provenance behaves like layered PDB
evaluation with conditioning between layers.

That makes the “Filtration Structure” section visible in the abstract.

Where to foreshadow in the intro

I would add a short paragraph after the first description of qdepth:

The filtration is not merely descriptive.  It supports three forms of
reasoning.  First, \emph{bypass}: if the inputs to a provenance query
are settled before layer $k$, then positive query evaluation cannot
introduce dependence on layer $k$ or above.  Second, \emph{semantic-change
analysis}: two specifications over the same commitment basis can be
compared tuple-by-tuple, distinguishing coordination work that did not
affect the answer from changes in the answer's meaning.  Third,
\emph{depth reduction}: a specification can lower its determination
complexity by coarsening the outcome order, making commitments commute,
or replacing discretionary commitments by deterministic entailments.

This paragraph would prepare the reader for the section before Related Work and make it feel like a planned culmination rather than a late add-on.

Feedback on the new material itself

Layer Bypass is strong, but the theorem should be framed as static-analysis cost

The bypass theorem says checking all input tuples have \mathrm{qdepth}<k is coNP-complete in residual width. That is plausible, but the phrase “checking whether all input tuples of Q” may sound like runtime query evaluation. I would call it bypass verification or static bypass certification.

Suggested tweak:

Certifying bypass for an arbitrary provenance query is coNP-complete…

Then the transactional and Datalog examples show tractable sufficient checks. That is a good structure.

The transactional bypass example needs one phrase of caution

It says:

A transaction bypasses the conflict-resolution layer if it participates in no L-forbidden cycle.

This is fine for transaction-local outputs. But for query tuples derived from multiple transactions, bypass depends on all input tuples/transactions. Maybe say:

A transaction-local tuple bypasses…

or:

For a tuple whose provenance depends on a transaction T, a sufficient condition is that T participates in no L-forbidden cycle.

That aligns it with the positive-query propagation theorem.

“Work regret” and “semantic shift” are excellent terms

These are worth surfacing earlier. They give the paper a memorable payoff.

I would define them in the intro very briefly:

* work regret: coordination/depth paid under one spec but not needed under another for the same tuple outcome;
* semantic shift: support changes, so the tuple means/holds differently.

This is a nice contribution because it moves beyond binary portability.

The PDB complexity proposition is interesting but needs a caveat

The proposition says depth-d provenance reduces to layered PDB evaluation, where within each level variables are independent and each level conditions on previous levels.

This is a good insight, but “joint distribution” might be too strong if the paper has not introduced probabilities. Since the semiring is Boolean support, I would phrase first in lineage/support terms, then say a probability measure can be added.

Instead of:

their joint distribution is conditioned…

use:

the valid assignments/supports at level \ell are restricted by the commitments chosen at levels 1,\ldots,\ell-1.

Then add:

When a probability measure is placed on commitments, this becomes ordinary conditional PDB evaluation.

That avoids importing probabilistic semantics before they are defined.

Depth Reduction appendix is a real asset

The three mechanisms are conceptually strong:

1. Coarsening \(\Ord\): weaken the spec so distinctions disappear.
2. Commutation: restructure decisions to make them simultaneous.
3. Entailment: make the choice deterministic.

This is a beautiful way to connect theory to systems design. It should be mentioned in the body, not only in the appendix. The new Section 7 gestures toward relaxation but not all three mechanisms. I would add a sentence in “Filtration Structure”:

Appendix~\ref{app:depth-reduction} develops the corresponding design transformations: coarsening, commutation, and entailment.

Actually, the conclusion already may gesture at systems, but this should be right in the new material.

The depth-reduction proposition is a little too terse

The proof says each part follows directly from definitions. For an appendix, that may be okay, but I would add one sentence per item:

* Coarsening: eliminated layer has no incompatible alternatives to resolve.
* Commutation: the two layers satisfy the within-layer commutativity condition, so they can be assigned the same layer.
* Entailment: deterministic commitments do not branch the support, so they do not contribute to depth.

This would make it read less hand-wavy.

One possible reordering

The current ordering is:

1. Transactions
2. Datalog
3. Layer Bypass
4. Filtration Structure
5. Related Work

That is good. But “Layer Bypass” and “Filtration Structure” are both consequences of the filtration, and Layer Bypass is operational while Filtration Structure is broader. I might retitle:

* \section{Consequences of the Filtration}
    * \subsection{Layer Bypass}
    * \subsection{Quantitative Relaxation Assessment}
    * \subsection{Provenance Query Complexity}

This would make the section before Related Work feel less like two short independent sections and more like the paper’s synthesis. It would also help the introduction/contribution list point to one place.

Current Layer Bypass is about 1.5 pages and Filtration Structure is about 1 page. Combining them under a single synthesis section could strengthen flow.

Suggested title:

\section{Consequences of the Filtration}
\label{sec:filtration-consequences}

Subsections:

\subsection{Layer Bypass}
\subsection{Quantitative Relaxation Assessment}
\subsection{Provenance Query Complexity}

This is probably the biggest structural suggestion I’d make.

Revised acceptance implication

Accounting for this new material, I would revise my characterization upward: the paper has a stronger “why this matters” arc than I acknowledged. The filtration now supports:

* optimization: bypass;
* migration analysis: work regret vs semantic shift;
* complexity framing: layered PDBs;
* design transformations: depth reduction.

That makes the paper more than a semantic model; it becomes a toolkit.

My main advice is to surface this toolkit earlier and group it more clearly. If the paper presents the new material as the culmination of the framework rather than as late discussion, it will read as significantly stronger.