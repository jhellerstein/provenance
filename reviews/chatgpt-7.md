I read the new main.tex cover to cover, including the appendices. This version is substantially stronger than the one I saw before. The main previous structural objections are mostly fixed: the pointwise-provenance theorem is safer, sealing/non-filtering commitments are now acknowledged, the layered basis is explicit input, the related-work/PDB positioning is much better, and responsibility has been moved out of the main line.

My updated acceptance estimate:

Current PODS odds: ~40–50%.
With one more focused cleanup pass: ~55–65%.

That is a real improvement. The paper now has a coherent thesis and a recognizable PODS contribution. The remaining risk is that some formal statements still overreach, especially around history-invariance, transactions, WFS/stable semantics, and safe relaxation.

Big-picture assessment

The strongest version of the paper is now visible:

Determination provenance separates derivational provenance from the semantic commitments that make derivation meaningful. Supports over determinations form a Boolean semiring, but the new contribution is the filtration induced by layered commitments, which measures query-relative dependence on semantic resolution.

That is a good paper. The filtration is the actual conceptual win. It is simple, compositional, and useful. The paper is at its best when it says: “possible worlds are not enough; the possible worlds have a commitment structure.”

The biggest remaining issue is that the paper sometimes presents domain-specific interpretations—especially transactions and negation—as if they were already theorem-level settled facts. I would make those claims more carefully staged: core algebra is formal; applications are instantiations, examples, and restricted propositions.

High-priority issues

1. The history-invariance lemma is still formally wrong as written

This is the most important technical issue I found.

The lemma says: if a persistent basis resolves at a completed history H^*, then for any prefix H \sqsubseteq H^* containing all dependency events, applying the same determination gives the same outcome.

But the proof uses persistence in the wrong direction. Your definition says:

\[
H_1 \sqsubseteq H_2,\quad o \notin \Spec(H_1\cdot\varphi)
\Rightarrow
o \notin \Spec(H_2\cdot\varphi).
\]

That is prefix-to-extension preservation of exclusion.

The proof needs the reverse direction:

\[
o \notin \Spec(H^*\cdot\varphi)
\Rightarrow
o \notin \Spec(H\cdot\varphi).
\]

That does not follow.

You try to handle this with “H contains all events on which D’s commitments depend,” but then the proof must rely on dependency sufficiency, not persistence alone. I would fix this by adding a formal assumption/definition:

A commitment \varphi has dependency set \Delta(\varphi,H^*) such that for any H\sqsubseteq H^* containing \Delta,
\[
> \Spec(H\cdot\varphi)=\Spec(H^*\cdot\varphi)
> \]
relative to the outcomes under consideration.

Then the lemma becomes true. Or weaken the lemma to:

Under a completed history H^*, determination provenance is evaluated at H^*. Persistence guarantees stability under extensions of H^*, not arbitrary prefixes.

For submission, I would either fix the lemma or remove it from the main line. Right now a formal reviewer could seize on it.

2. The finiteness/minimality claim for \mathcal D is too casual

The text says \mathcal D is finite because filtering commitments strictly shrink \(\Spec(H)\), and minimal determinations have length at most \(2(|\Spec(H)|-1)\).

This needs assumptions. It only holds when:

* \(\Spec(H)\) is finite, or you are working over a finite quotient;
* the commitment basis is finite;
* each filtering commitment removes at least one distinguishable outcome;
* there is at most one needed seal per filtering commitment, which is asserted but not proven.

I would add a compact standing assumption before the determination semiring section:

In this paper we work over a finite observational quotient of outcomes and a finite commitment basis. Thus \mathcal D denotes the finite set of minimal resolving determinations modulo query-relevant outcome/provenance equivalence.

This also helps the running transaction example, where \mathcal D=\{D_{\mathsf{in}},D_{\mathsf{out}}\} is really quotienting many serializations.

3. Theorem 2.1 is improved, but clause (b) still sounds too strong

The new theorem is much better. But the proof still says:

no single annotation can simultaneously explain presence under D_1 and absence under D_2 or two distinct nonzero annotations.

For absence, fine. For two distinct nonzero annotations, a provenance object could in principle be a richer annotation carrying alternatives. The statement should specify “single ordinary K-annotation in the classical semiring model.”

Suggested wording:

no single ordinary K-annotation, interpreted as classical positive provenance for one fixed instance, is sound and complete for both conditioned instances.

That avoids an avoidable attack from possible-world/probabilistic provenance people.

4. The transaction section is improved but remains the riskiest application

The transaction material is clearer now, but several claims are still likely to be challenged.

The read-committed claim is still slippery. You now say RC is depth 0 when the outcome is the committed database state with version order determined by commit order. But if commit order is in the history, yes; if not, commit order is itself a semantic resolution. The phrase “once all commit/abort decisions are fixed by the history” is not enough: commit/abort does not determine last-writer-wins unless the commit order is also fixed.

I would revise the proposition to:

Under RC, if the outcome is defined as the final committed state and the history includes commit order, then no additional semantic ordering commitments are needed beyond the history; depth 0 relative to that history representation.

That is a much safer and more precise claim.

The serializability depth statement also needs softening. “Depth 1 when the conflict graph is acyclic or has only disjoint cycles; depth \ge 2 when cycles overlap” is intuitive but not fully proven. In particular, disjoint cycles can be resolved independently in one layer if the victim choices commute, but overlapping cycles may still sometimes have a one-layer resolution if the shared transaction is aborted. Your example says aborting T_3 breaks both cycles at depth 1, while aborting T_1 requires a second abort. So “overlapping cycles imply depth \ge 2” is not true for all determinations; it is true for some branches or for worst-case/minimal-basis structure.

Rewrite as:

With overlapping cycles, some valid resolution branches may require sequential decisions, so worst-case determination depth can exceed 1; aborting a shared transaction can collapse the depth.

That would align with your own example.

5. The running example is better, but \mathcal D=\{D_{\mathsf{in}},D_{\mathsf{out}}\} still needs one more caveat

You now say “two equivalence classes of determinations arise, quotienting by query-outcome equivalence.” Good. But later you write:

\mathcal D=\{D_{\mathsf{in}},D_{\mathsf{out}}\}

“throughout.” That is fine only if \mathcal D is explicitly defined as query-relative quotient determinations in this example, not the global minimal resolving determinations of the whole transactional specification.

I would change the sentence to:

For this query we write \mathcal D_Q=\{D_{\mathsf{in}},D_{\mathsf{out}}\} for the quotient of resolving determinations by Q-outcome/provenance equivalence.

Then use \mathcal D_Q in the example. This prevents a reviewer from objecting that there are more serializations.

6. The WFS/stable-model correspondence is still a little too broad

The main theorem is now nicely restricted. But the appendix re-expands to a general theorem for “any finite normal Datalog program with k stratification layers and nesting depth d.” That is too strong.

Problems:

* Not every finite normal program has stable models.
* Stable models do not always correspond cleanly to independent binary choices over SCCs.
* WFS is not generally “read \mathcal F_{k+d^*}” for a number of consecutive forced layers. The alternating fixpoint can propagate unfounded-set reasoning in ways not captured by a simple prefix of SCC choices.
* Negative SCCs are not necessarily binary choice components.

I would either delete the “General negation semantics as filtration levels” theorem or explicitly mark it as a design pattern for a restricted class. The current restricted theorem in the body is defensible; the appendix theorem reintroduces the overclaim.

Suggested replacement:

For nested negative cycles satisfying the layered-choice assumptions below, the same correspondence extends with depth k+d.

Then make the theorem conditional on the layered choice basis being sound and complete for stable models.

7. The monus-elimination theorem still overstates its domain

It says “for any finite normal Datalog program P” and then discusses monus over LFP. But monus provenance is a stratified-negation story; for arbitrary normal Datalog, “LFP with monus” is not generally the right semantics.

I would restrict the theorem to:

finite stratified Datalog with negation

or say:

For any stratum in a stratified evaluation of a finite normal Datalog program…

Then leave the unstratified sentence as contrast:

For unstratified negation, there is no single stratified complement against which monus can be applied; determination provenance instead indexes stable-model completions when they exist.

That will be much harder to attack.

8. Safe relaxation theorem is interesting but underproved

The safe-relaxation theorem is a good idea, but the proof sketch currently assumes too much. The key line is:

\[
\Spec'(H\cdot\psi)\supseteq \Spec(H\cdot\psi)\neq\emptyset.
\]

This does not automatically follow from relaxing \(\Ord\) or removing layer-k exclusions. A commitment \psi’s applicability/effect may depend intensionally on the prior structure, not just set inclusion. You need a monotonicity/stability assumption for upper-layer commitments under relaxation.

Add an explicit assumption:

Upper-layer commitment stability: if \psi is valid after a layer-k prefix in \(\Spec\), then under a layer-k relaxation its effect is defined on the merged admissible set and preserves all outcomes it preserved before.

Without something like that, part (a) is not proven. Part (b) is also existential and vague: “some relaxation invalidates…” needs construction or should be softened.

For PODS, I would mark safe relaxation as “under stable upper-layer commitments” and present it as a sufficient condition, not a biconditional-like characterization.

Medium-priority issues

9. The abstract still overpromises slightly

The sentence:

For Datalog with negation, the classical semantics—stratified, well-founded, stable-model—differ only in which filtration level they read.

This is catchy, but too broad. I would change it to:

For a restricted but representative class of Datalog programs with negation, stratified, well-founded, and stable-model semantics can be viewed as different readings of the same filtration.

Similarly, the transaction sentence should not imply a fully general isolation-level theorem unless you want reviewers to demand one.

10. “Aggregation” appears in the motivation but is not developed

The intro mentions aggregation as a non-monotone operation requiring sealing. That is plausible and useful, but the paper does not instantiate aggregation. Either add a two-sentence mini-example or remove aggregation from the headline list. As written, it looks like an unfulfilled promise.

11. The “determination semiring” name may invite the wrong expectation

You now explicitly say the Boolean support algebra is elementary, which helps. But “the space of all resolving determinations forms a commutative semiring” is still slightly misleading: subsets/supports of determinations form the semiring, not determinations themselves.

I would consistently say:

supports over resolving determinations form a semiring.

This is precise and avoids the “individual determinations don’t add/multiply” objection.

12. Layer numbering is inconsistent in intuition

In the main text, layers are numbered 1,\ldots,d in discharge order. In the appendix, “Layers are numbered bottom-up: M_1 is the first layer discharged, M_k the last.” “Bottom-up” may confuse readers because earlier sections use “prefix” and “above/below” in semantic-dependency terms. I would avoid “bottom-up” and just say “in discharge order.”

13. The transaction appendix uses a different running example

The main example has initial \{S(0,b)\} and T_1,T_2,T_3,T_Q. The appendix switches to an initially empty database with five transactions. That is less damaging than before, but still jarring.

Either rename it “A second transactional example” or align it with the main example. Given the paper’s complexity, I would strongly prefer one running example throughout.

14. The systems-lineage appendix is interesting but still too much

The systems-lineage appendix is good thought leadership, but for PODS it reads speculative compared with the formal core. If page budget or reviewer patience is an issue, cut it aggressively. The strongest appendix material is:

* robustness proof,
* responsibility details,
* semiring/filtration details,
* Datalog proof restrictions,
* transaction worked example.

The lineage/certificates material feels like a follow-on paper or vision appendix.

Low-level / cleanup issues

* The ACM metadata is still placeholder: Full Conference Name, fake ISBN, etc.
* The file compiles to 34 pages without a .bib; all citations are undefined in this sandbox because no bibliography was attached. Presumably fine if your build has the .bib, but check.
* ACM warnings: missing CCS concepts and keywords.
* The wraptable in the Datalog section still creates awkward prose: “only when they resolve” / table / “everything.” I would avoid the wraptable and use a normal table.
* There are several \vspace warnings from acmart.
* Two overfull boxes appear around the filtration paragraph and the reachability proposition.
* The theorem “Robustness is coNP-complete in width” should probably say “as a function of width” or “when width is part of the input.” The current phrasing is a bit nonstandard.
* The responsibility budget B(t)=1-|\mathrm{supp}(t)|/2^n assumes v(N)=1, i.e. the realized determination supports t. Say this is the presence game for a tuple present under D^*. Otherwise the budget formula can be wrong.

Recommended punchlist

High criticality

1. Fix or remove the history-invariance lemma; persistence is used in the wrong direction.
2. Add finite quotient / finite basis assumptions for \mathcal D.
3. Weaken the transaction depth proposition, especially RC and overlapping-cycle claims.
4. Restrict the monus-elimination theorem to stratified negation or stratum-local use.
5. Downgrade or restrict the appendix general theorem on nested negative cycles.
6. Add an explicit upper-layer stability assumption to the safe-relaxation theorem.

Medium criticality

1. Use \mathcal D_Q or similar for query-relative quotient determinations in the running example.
2. Tone down the abstract’s “classical semantics differ only…” sentence.
3. Decide whether aggregation is in scope; either instantiate or remove.
4. Make the appendix transaction example match the main example or explicitly call it a second example.
5. Replace the Datalog wraptable with a normal table.
6. Tighten “supports over determinations form a semiring” terminology.

Low criticality

1. Clean ACM metadata, CCS, keywords.
2. Check .bib completeness.
3. Remove unused \jmh macro if not needed.
4. Fix overfull boxes and \vspace warnings.
5. Consider trimming systems-lineage appendix.

Revised acceptance outlook

This is now clearly a serious PODS submission. I would no longer describe it as a manifesto with a fragile formal core. It has a real formal object: a filtered Boolean support semiring over resolving determinations, plus a credible story about why that object matters.

The paper’s acceptance case will be strongest if the main theorem stack is modest and bulletproof:

1. ambiguous specs require determination-indexed provenance;
2. supports over determinations form a Boolean semiring;
3. layered commitment bases induce a filtration;
4. positive relational algebra respects the filtration;
5. Datalog/transactions instantiate this structure under stated assumptions.

That is enough. The more general claims about all normal Datalog, all isolation levels, or safe relaxation as a complete characterization are the places where the current draft still risks reviewer pushback.