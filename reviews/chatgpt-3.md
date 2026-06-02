Independent PODS-style review

I read this as a fresh submission, not as a diff. My simulated review is:

Borderline / weak accept if tightened; weak reject if the reviewer is formalism-first.
The paper has a genuinely interesting organizing idea: provenance should range over semantic resolutions, not just derivations inside one resolved semantics. The best part is the filtered semiring structure and the attempt to connect it to Datalog negation and quantitative responsibility. But the paper still asks the reader to accept several large abstractions whose formal foundations are only partly stabilized. The biggest acceptance risk is that a reviewer may see the work as a provocative framework paper with attractive examples, but not yet enough theorem-level precision for PODS.

I would not call it “not ready.” I would call it close, but still carrying avoidable review risk.

⸻

1. High-level contribution: strong idea, but too many claims compete for center stage

The paper’s central move is compelling: ambiguous specifications are relations, determinations narrow them to functions, and once a determination is fixed, ordinary semiring provenance applies. The introduction states this clearly and cleanly.  ￼

The support semiring plus filtration is also a good algebraic hook. The abstract says determination provenance is a K-relation indexed by resolutions, with supports forming a semiring whose layers induce a filtration respected by query evaluation.  ￼ That is a plausible PODS contribution.

But the paper now has three centers of gravity:

1. Determination provenance / filtered semiring.
2. Datalog negation semantics as filtration levels.
3. Determination responsibility via Shapley values and treewidth.

All three are interesting, but together they make the paper feel a little overfull. Section 6 is especially weighty: it introduces a new quantitative diagnosis measure, hardness, bounded-treewidth tractability, an FPRAS, and multilayer responsibility.  ￼ This is a lot for a paper whose core formal apparatus is already new.

Reviewer risk: A reviewer may conclude that the paper is “idea-rich but underproved.” You can mitigate this by making the hierarchy explicit:

Main contribution: filtered determination provenance.
Main database-theory application: negation.
Secondary quantitative application: responsibility.

Right now the abstract elevates responsibility almost to parity with the core framework. That may be strategically risky.

⸻

2. The formal core is attractive, but definitions still need sharpening

The framework defines histories, outcomes, specifications, commitments, and determinations in a natural progression. Histories are finite posets with an extension relation that may add events without revising the past.  ￼ Specifications relate histories to admissible outcomes ordered by refinement.  ￼ Commitments then filter the admissible set and are sequenced into determinations.  ￼

This is a good setup. The part that still worries me is the claim that every commitment basis can be canonicalized to an equivalent persistent one without changing the determination structure. The main text says exactly that: different bases yield different structures, but every basis can be canonicalized to an equivalent persistent one without changing the determination structure.  ￼

That is a very strong claim. Sealing a dependency set and then applying an entailment may preserve final outcomes in a retrospective setting, but it almost certainly changes at least one of:

* what counts as a commitment,
* whether a step is filtering or entailing,
* the explanatory vocabulary,
* the visible depth,
* the independence relation used by the filtration.

The majority-vote example is intuitively useful, but it also makes the problem vivid: “seal voter pool, then compute majority” feels structurally different from “majority vote.”  ￼

Recommendation: weaken this claim. Say persistence is an assumption of the main theory, and non-persistent commitments can often be represented by a persistent seal plus entailment in a retrospective analysis. Do not claim “without changing the determination structure” unless you prove a precise isomorphism of determinations, layers, supports, and responsibility values.

⸻

3. Theorem 2.1 remains a likely target

Theorem 2.1 says classical semiring provenance over Spec—a single K-relation consistent with all admissible outcomes—is well-defined iff Spec is determined.  ￼

I understand the intended point: ordinary Green-style provenance expects one resolved instance/model, not a set of possible models. But as stated, this theorem still feels more philosophical than mathematical. “Well-defined” is doing a lot of work. A reviewer could object that provenance can be lifted to products, powersets, functions from worlds to K, possible-world annotations, or other semiring constructions. Indeed, this paper’s own determination provenance is a lifted D → K object.

You can keep the point without making it an iff theorem:

Classical semiring provenance is directly defined over a resolved instance/model. For an ambiguous specification, one must either choose a determination first or lift provenance pointwise over determinations. This paper develops the latter construction.

That is cleaner, harder to attack, and still motivates everything.

⸻

4. History-invariance is improved but still delicate

The revised Lemma 2.1 is much better scoped: it now quantifies over a completed history H* and prefixes containing the dependency set of D.  ￼ That is the right direction.

But the proof still has a directionality issue. It says: since D resolves at H*, every other outcome is excluded by some commitment at the corresponding prefix of H*; since H ⊑ H* and the basis is persistent, the same exclusion holds at the corresponding prefix of H.  ￼ Persistence as defined says exclusions at an earlier history persist to later histories. It does not generally say that an exclusion observed at H* also held at an earlier prefix H. That is the reverse direction.

You try to handle this by requiring H to contain the dependency set of D, but then the lemma needs to state and use a stronger property:

If H contains the dependency set needed by φ, then applying φ at H and at any extension H′ produces the same exclusions.

That is not persistence; it is dependency-set sufficiency or locality. You may have this in the appendix, but it needs to be explicit in the lemma statement.

Concrete fix: replace the proof’s appeal to persistence with a dependency-closure lemma:

For each commitment φ_i, if two histories agree on dep(φ_i), then φ_i excludes the same outcomes in both histories.

Then Lemma 2.1 follows for prefixes containing all dependency sets. Without that, a careful reviewer can reject the proof.

⸻

5. The filtration is the best part, and the recursive agreement definition helps

Section 3.3 is now one of the strongest parts of the paper. The recursive definition of D ≡_k D′ is exactly the right move: level 0 agreement is vacuous; level k+1 agreement requires level k agreement plus equality of the next maximal commuting layer.  ￼ This makes the filtration much more credible than a handwave to Foata normal form.

Still, two issues remain.

First, “next maximal commuting layer” needs uniqueness. If there can be two different maximal commuting batches from the same prefix, the equivalence relation may depend on a choice of layering. The text says different valid orderings within a layer do not affect the construction, but that is weaker than uniqueness of the maximal layer itself.  ￼

Second, the claim that ≡_k is an equivalence relation is asserted with a short parenthetical.  ￼ For PODS, I would put the inductive proof in the main text or in a short lemma. It is not hard, but because the filtration is central, the paper should not ask readers to trust it.

Recommendation: Add a short lemma:

If the next-layer operator Next(P) is uniquely defined for every valid prefix P, then ≡_k is an equivalence relation for every k.

Then either define Next(P) canonically or explicitly say the filtration is relative to a chosen deterministic layering policy.

⸻

6. Minimal resolving determinations: finiteness claim is not quite right

The paper defines D as minimal resolving determinations with no proper subsequence that also resolves, and claims finiteness because each commitment strictly shrinks the admissible set, giving length at most |Spec(H)| - 1.  ￼

Two concerns:

1. Definition 2.5 says applying a commitment produces a nonempty subset Spec(H·φ) ⊆ Spec(H), but it does not require a proper subset. Later prose says commitments replace the admissible set with a proper subset, but the formal definition allows equality.  ￼ If equality is allowed, the strict-shrinkage length bound does not follow.
2. Even with strict shrinkage, |Spec(H)| may be infinite unless finite outcome sets are assumed. Histories are finite, but outcome domains need not be.

This is easy to fix. Either require commitments to be proper filters when they appear in minimal determinations, or explicitly restrict the main development to finite D and finite relevant outcome sets.

Suggested text:

We assume throughout that the set of minimal resolving determinations under the chosen basis is finite. This holds in the finite settings considered here because each nonredundant commitment strictly decreases a finite admissible set.

That is safer than proving finiteness from definitions that do not quite imply it.

⸻

7. Transactions: better, but still the most fragile instantiation

The transaction section is conceptually useful and gives the reader an intuitive example. I like that the running example now explicitly uses ordering commitments rather than pretending commit order is always the formal basis.  ￼

However, the transaction model is still likely to be challenged by concurrency-control experts.

The paper defines a conflict graph over active transactions and says committed or aborted transactions are removed, with commit “finalizing” serial position.  ￼ Then serializability is described via acyclicity constraints over conflict graphs.  ￼ This is still not a standard enough formulation to be left with only a short statement and no proof.

Proposition 4.2 is also too broad for the support given in the main body. It claims depth 0 for read committed, depth 1 for serializability when the graph is acyclic or has disjoint cycles, depth ≥ 2 for overlapping cycles, and O(n) for SI from FCW-to-snapshot dependencies.  ￼ That is a lot of transaction theory in one proposition without proof in the first 15 pages.

The most robust move would be to narrow Section 4:

* Use transactions primarily as an illustrative instantiation.
* State Proposition 4.2 as “informal characterization” or “examples of depth behavior.”
* Move detailed claims about SER/SI depth to appendix.
* Avoid saying “governed by conflict-graph topology” as a formal contribution unless fully proved.

The Datalog section is the more natural PODS anchor. Do not let a debatable transaction model become the reason for rejection.

⸻

8. Datalog section: stronger, but theorem is intentionally restricted

Theorem 5.1 is now appropriately restricted: finite normal Datalog programs whose dependency graph has k stratification layers and whose negative SCCs, after condensation, are mutually independent and form a single final choice layer.  ￼ That restriction is a good defensive choice.

But the prose around it still sometimes sounds broader than the theorem. The abstract says “For Datalog, the classical negation semantics—stratified, well-founded, and stable-model—differ only in which filtration level they read.”  ￼ The theorem covers a constrained class. That mismatch could irritate reviewers.

Also, the proof sketch says WFS classifies atoms by whether they hold in all stable models, no stable models, or some but not all.  ￼ For the restricted class, this may be okay, but in general WFS is not merely skeptical/cautious stable-model intersection in all the ways one might casually infer. Since the theorem is restricted, keep the wording anchored to the restricted class.

Recommendation: revise abstract/contribution language:

For a natural class of finite normal Datalog programs with independent final negative SCCs, stratified, well-founded, and stable-model readings correspond to different filtration levels.

That is less sweeping but much safer.

⸻

9. Responsibility section: interesting, but risky as a headline

Determination responsibility is a nice addition. The presence game is well motivated: condition on a realized determination, fix a coalition of commitments, and measure the probability that the tuple still holds under random completion.  ￼ The SLA example is also intuitive.  ￼

However, Section 6 may be the most review-sensitive part of the paper after transactions.

9.1 #P-hardness proof is too compressed

Theorem 6.1 says computing responsibility is #P-hard even for single-layer DNF support. The proof says a marginal requires #DNF under random restriction, which is #P-hard by reduction from #SAT.  ￼

That is plausible, but for a main theorem it is too compressed. A reviewer may ask whether computing the Shapley value of a DNF support function is known and whether your game’s normalized probability definition changes the reduction. You should either cite known results on Shapley-value computation for Boolean games / weighted voting / DNF reliability, or give the reduction in a few more lines.

9.2 The bounded-treewidth theorem needs a sharper bridge

Theorem 6.2 says the support is a positive Boolean formula with primal-graph treewidth at most the conflict treewidth, so weighted model counting is FPT.  ￼ This is plausible only if the support formula is actually constructed from local conflict constraints whose primal graph is the conflict graph. But earlier, support is an arbitrary subset of determinations induced by query evaluation. A query can create dependencies not present in the transaction conflict graph.

You need an assumption like:

The support formula for the queried predicate has primal graph bounded by the commitment conflict graph.

or

For the transactional SLA predicates considered here, support formulas are local over the conflict graph.

Without that, “conflict treewidth” may not bound formula treewidth.

9.3 The FPRAS claim may be too strong as stated

Proposition 6.3 says there is an FPRAS for determination responsibility by sampling random permutations and evaluating two determinations.  ￼ This is a standard unbiased-estimator argument for additive approximation of Shapley values when marginal contributions are bounded. But “ε-approximated” is ambiguous: additive or relative? An FPRAS usually means relative approximation for nonnegative quantities. Shapley values here can be small, zero, or maybe negative depending on the game/predicate, unless monotonicity is guaranteed. A relative FPRAS for arbitrary small/zero values is not implied by Hoeffding over bounded samples.

Fix this by saying:

additive ε-approximation

or prove nonnegativity and relative approximation under additional assumptions. I would not use “FPRAS” unless you really mean the standard relative notion.

This is probably the most important technical correction in Section 6.

⸻

10. Related work: good but should mention possible-worlds/probabilistic DBs more directly

The related work visible in the first 15 pages does a good job positioning against semiring provenance, negation provenance, systems lineage, and causal responsibility.  ￼ But the obvious reviewer question is still:

“Isn’t this just possible-worlds provenance?”

You should answer that explicitly in the main related work, not only implicitly. The answer is good:

* possible worlds give support sets;
* your determinations are structured by commitments;
* the filtration/independence structure is the novelty;
* responsibility is over semantic commitments, not tuple uncertainty.

A short paragraph would help a lot.

⸻

11. Acceptance risks ranked

If I were reviewing, my top concerns would be:

1. FPRAS terminology / approximation guarantee: likely technically incorrect as stated unless changed to additive approximation.
2. History-invariance proof direction: persistence alone does not imply exclusions transfer from completed history back to prefix.
3. Persistence canonicalization “without changing determination structure”: too strong.
4. Transaction model: active conflict graph and depth claims need more support or weaker framing.
5. Treewidth theorem bridge: conflict treewidth does not automatically bound support-formula treewidth.
6. Theorem 2.1 as iff: rhetorically useful but formally vulnerable.
7. Datalog abstract overgeneralization: theorem is restricted; abstract sounds general.

⸻

What I would change before submission

Must-fix

Change Proposition 6.3 from “FPRAS” to “additive randomized approximation scheme,” unless you can prove a standard relative FPRAS. State the approximation type explicitly.

Fix Lemma 2.1 by adding a dependency-sufficiency/locality assumption. Persistence alone is not enough.

Weaken the canonicalization claim to avoid “without changing determination structure.”

Add assumptions to Theorem 6.2 connecting conflict treewidth to support-formula treewidth.

Should-fix

Demote Theorem 2.1 to an observation or define “classical semiring provenance over an ambiguous spec” more formally.

Soften transaction claims in Section 4 or prove Proposition 4.2 in the main body.

Make the Datalog claims in the abstract match the restricted theorem.

Add a possible-worlds/probabilistic provenance paragraph to related work.

Nice-to-have

Add a small figure for the filtration: determinations as leaves of a layered decision tree; supports as unions of equivalence classes at each depth. This would make the core concept immediately legible.

⸻

Bottom line

This draft has a real PODS idea. The strongest version of the paper is:

A filtered semiring model of provenance over semantic resolutions, with Datalog negation as the main formal application and responsibility as a promising quantitative extension.

The paper will be safer if it stops trying to prove that every part of the world fits cleanly into the framework. The core is strong enough. Tighten the formal claims, make responsibility’s approximation theorem precise, and keep transactions as an illustrative systems instantiation rather than the main burden-bearing proof object. Then I think the paper becomes a credible PODS submission rather than a provocative but fragile one.