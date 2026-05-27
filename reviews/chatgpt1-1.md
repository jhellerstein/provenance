I read the newly uploaded file /mnt/data/provenance.tex directly from the sandbox. This is the paper titled “Determination Provenance: From Ambiguity to Algebra.” I did not use /mnt/data/main.tex. I also ran a quick LaTeX compile on provenance.tex; it completed and produced a 37-page PDF in the sandbox, with expected unresolved-citation/reference warnings because I did not run a full BibTeX/cross-reference build in your project environment.

This is a strong and interesting paper. The central pitch is now clear:

Classical provenance explains derivations after semantics are fixed; determination provenance explains the semantic commitments that fixed the semantics.

That is a good PODS-shaped idea. The paper has a real algebraic core — supports over determinations, Boolean semiring structure, filtration, and query-relative depth — and the transactional and Datalog-with-negation instantiations are compelling. But the draft is still doing too much, and several theorem statements are broader than the proof sketches support.

Below is feedback on the body, then appendices, then a prioritized punchlist.

⸻

Body feedback

1. The paper’s conceptual hook is strong

The introduction works. The example with S(k,y), concurrent insert/delete/query, and robust vs contingent answers is a good opening. It makes clear why classical provenance is under-specified in ambiguous settings: before resolution, a tuple’s provenance question may be “why” under one determination and “why-not” under another.

The sentence:

“Classical provenance applies within each determination; determination provenance tracks which commitments were needed and how query results depend on them.”

is exactly the thesis. I would keep it near the front no matter how the introduction changes.

The paper also succeeds in giving readers a simple algebraic object to hold onto:

supp(P(t)) = {D ∈ 𝒟 | P(t)(D) ≠ 0}

and then:

join = intersection of supports
union = union of supports

That is elegant.

⸻

2. The definition of “resolved/determined” needs a little more care

You define a specification as a relation Spec ⊆ Hist × O, and Spec(H) is the admissible set at H. Then:

A specification is determined at H if all outcomes in Spec(H) are
pairwise Ord-comparable.

This is sensible if comparable outcomes are refinements of the same semantic alternative rather than incompatible alternatives. But later, when defining conditioned provenance, you write:

For a determination D extracted from a resolved history H, the
conditioned provenance P_D(t) is the classical semiring provenance
of tuple t computed over the resolved outcome Spec(H).

Here Spec(H) is still a set, possibly a chain with multiple comparable outcomes, not a single outcome. The phrase “the resolved outcome Spec(H)” is therefore slightly ambiguous.

You need one of these clarifications:

* resolved histories have a canonical maximal outcome in the chain, and provenance is computed over that maximal outcome;
* provenance is computed at the concrete outcome exposed by the history;
* or comparable outcomes are quotient-equivalent for tuple membership and derivation, so the choice within the chain does not matter.

Right now, the definition of determined does not by itself guarantee unique tuple membership/provenance. If o1 ⪯ o2 and o2 refines o1 by adding detail, tuple membership might differ unless the outcome order preserves the relevant query answer. That matters for P_D(t).

Suggested patch:

When Spec(H) is a chain, we evaluate classical provenance at its maximal exposed outcome; in the instantiations below this outcome is unique up to query/provenance equivalence.

or:

All comparable outcomes in a resolved chain are treated as the same semantic alternative for provenance queries; P_D(t) is invariant within the chain.

This is a high-priority clarity fix.

⸻

3. The theorem “Classical provenance is pointwise in determinations” is conceptually right but over-labeled and a bit too broad

The theorem has three labels:

\label{thm:resolution-implies-monotone}
\label{thm:necessity}
\label{ass:prefix-closed}

That is confusing. ass:prefix-closed in particular looks stale. Use one label.

The theorem statement says:

“Any provenance representation that correctly accounts for every admissible outcome must distinguish determinations that disagree on tuple membership or derivation.”

That is plausible but broad. The proof only argues that if P_D1(t) ≠ P_D2(t), no single classical semiring annotation can explain both presence/absence. It does not prove a general lower bound for “any provenance representation.”

I would narrow the theorem:

A single classical K-relation suffices exactly when all resolving determinations agree on tuple membership and conditioned provenance; otherwise provenance must be indexed by determination or carry equivalent information.

That is still strong and exactly what you need.

⸻

4. The determination semiring is clear, but the name “semiring” may need one sentence

You define supports as a Boolean algebra:

(2^𝒟, ∪, ∩, ∅, 𝒟)

and call it the determination semiring. This is fine: it is the Boolean/idempotent semiring of sets with union and intersection. But because you also have an arbitrary provenance semiring K, a reader may briefly wonder whether the full object is 𝒟 → K, 2^𝒟, or a product semiring.

The text does explain it, but a crisp sentence would help:

The determination semiring is the Boolean support semiring obtained by forgetting the nonzero K-annotations and retaining only the set of determinations under which the tuple exists.

Or, if you intend the richer object 𝒟 → K, say that support is the Boolean shadow of a function semiring. Right now the paper moves between “determination provenance is 𝒟 → K” and “supports form the semiring.” That is fine but should be made explicit.

⸻

5. The filtration section is one of the strongest parts

The definitions of layered commitment basis, level-k agreement, level-k support, filtration, and query-relative depth are good. The algebra is clean:

* 𝔽_k is the set of unions of level-k equivalence classes.
* Unions and intersections stay inside 𝔽_k.
* Positive relational algebra cannot increase depth.

That is the most theorem-like core of the paper, and it reads well.

One small prose issue:

Two determinations D(H), D'(H') ∈ 𝒟 agree at level k, written D ≡_k D',
defined inductively:

This is missing “are” or “is”:

“… are defined inductively:”

or

“… is defined inductively as follows:”

Low priority, but visible.

⸻

6. The single-layer/PDB proposition should be worded carefully

You state:

“When all commitments commute (a single layer), … the determination semiring coincides with PosBool(Φ).”

Then you clarify:

“The formulas are interpreted over the set of valid minimal determinations, not over all truth assignments to Φ.”

That caveat is important. Without it, independent tuple-existence PDBs suggest all Boolean assignments are possible, while valid minimal determinations may impose constraints among commitments.

The later proposition:

Depth-1 = tuple-independent PDB

is therefore a little too strong as stated:

“A depth-1 determination semiring over n binary commitments is isomorphic to a tuple-independent PDB over n tuple-existence events…”

This is true only if all 2^n assignments are valid or if you are allowing a PDB conditioned on the valid-determination set. If valid minimal determinations are a strict subset, then it is more like a constrained/correlated PDB, not tuple-independent.

I would revise the proposition:

If a depth-1 determination space contains all assignments to n independent binary commitments, it is isomorphic to a tuple-independent PDB. In general, depth-1 supports are positive Boolean formulas over the valid determination set.

This is high/medium priority because PDB reviewers will notice.

⸻

7. Transactional section is compelling but overclaims in places

The transactional framing is good: isolation levels as specifications over decision traces, commitments as ordering choices, depth as scheduling/validation ambiguity. The example and the table are useful.

But Theorem 3.1 is broad:

“Under any isolation level L that forbids some cycle type … with scheduling discretion: worst-case depth Θ(n).”

This is plausible as a high-level theorem, but the proof sketch is not enough for the breadth of the statement. It relies on a “surviving transaction T_∞” construction and says the appendix covers SER and SI. But the statement names “serializability, snapshot isolation, repeatable read, etc.” and “any such L.” That is quite broad.

I would narrow it:

For the isolation levels considered here, including SER and SI, and for any protocol with victim-selection or scheduling discretion capable of preserving a live conflicting transaction, worst-case depth is Θ(n).

or keep the theorem broad but add an explicit condition:

any isolation level whose forbidden pattern can be regenerated around a surviving transaction.

You already say this after the proof; I would move that condition into the theorem statement.

The “per-batch depth is 2” claim is interesting and likely right under your modeling convention: seal the batch, then choose a total order. But it is a bit surprising next to worst-case Θ(n). You explain it; I’d leave it.

⸻

8. The isolation-sensitive tuples proposition is too strong as an iff

This proposition says:

A tuple has different qdepth under SER and SI iff its transaction participates in either write skew or FCW-forced abort.

The examples are right, but the “iff” is ambitious. SI/SER comparisons can involve interactions of rw, ww, snapshots, and cycles in more complex graphs. A transaction could participate in both patterns, or a ww conflict inside a larger cycle, or a tuple’s support could be affected by downstream derivation even if its writing transaction does not match the local pattern exactly.

The proposition is likely correct for the simplified conflict model you have in mind, but the statement should say so:

In the conflict-graph model above, for tuples directly derived from a transaction’s writes, the primitive SER/SI separation patterns are…

or change “iff” to “only if” plus “these patterns witness incomparability.” The main contribution does not require a full characterization of all SI/SER qdepth differences.

Suggested safer statement:

These two patterns witness incomparability of SER and SI in query-relative depth.

Then keep the current proof as examples. This is high priority if you leave it as an iff.

⸻

9. The Datalog-with-negation section is exciting but too sweeping in theorem form

The body theorem says:

For a finite Datalog^neg program having k stratification layers and d negative SCCs in the longest dependency chain, the determination semiring has depth k+d. Stable, well-founded, and stratified semantics correspond to filtration levels…

This is a very strong claim. The appendix later has a more nuanced general theorem:

WFS reads 𝔽_{k+d*} where d* ≤ d is the number of consecutive choice layers whose resolution is forced.

That nuance is absent from the body theorem, where WFS simply reads 𝔽_k. That is not generally true beyond the representative class where all negative-cycle choices remain ambiguous at WFS. The body intro to the section says “for the representative class below,” which helps, but the theorem statement itself says “For a finite Datalog^neg program…” without that restriction.

Fix:

For the representative class described above…

or:

For programs in which negative SCCs remain genuinely ambiguous under WFS…

Then refer to the appendix for the general nested case.

Similarly, “each choice layer resolves SCC C_i” may be too simple for arbitrary stable model structure: stable models of an SCC are not always binary atom choices; there may be multiple local stable extensions with constraints. The appendix canonical basis handles this better. The body theorem should either cite “canonical layered choice basis” or restrict to the simple binary-cycle example class.

⸻

10. The monus-elimination theorem is too strong without a proof sketch

The theorem says:

For any finite stratified Datalog^neg program and any naturally ordered, zero-divisor-free commutative semiring K, supports computed via sealing commitments over (K,+,·) equal supports computed via least fixpoint with monus.

This is a strong technical claim, and the proof is deferred to the appendix. I looked for a detailed proof in the appendix; the Datalog appendix discusses stable/WFS/stratified semantics and canonical bases, but I did not see a fully explicit proof of monus elimination at the level this theorem deserves.

If this theorem stays in the body, the appendix should include a named proof. If space is tight, soften the theorem to a proposition for the class considered or move it entirely to appendix.

Also, the prose after the theorem says:

“annotates sealed absence as 0_K”

The comment in the source just above says “sealed absence → 1_K,” while the prose says 0_K. Only the prose is visible, but you should check the intended algebra carefully. In semiring provenance, an absent atom typically has annotation 0; but a successful negated literal often contributes multiplicative identity 1. The distinction is important:

* annotation of the atom p being absent: 0;
* annotation/contribution of the literal not p after sealing absence: 1.

Clarify this in the text. This is high priority for the Datalog section.

⸻

11. Consequences section is good but the bypass complexity claim appears before proof support

The bypass criterion is clean. The coNP-completeness statement is plausible and has appendix support.

However:

“both instantiations admit polynomial sufficient checks: in transactions, absence from L-forbidden cycles; in Datalog, absence of transitive dependency on any negative SCC.”

This is useful, but “absence from forbidden cycles” may require computing which tuples derive from transactions in those cycles. That is fine, just phrase as a sufficient syntactic/dataflow check rather than exact if not exact.

The “work regret / semantic shift” distinction is excellent. That may be one of the most practically useful ideas in the paper.

⸻

Appendix feedback

Appendix A: Robustness proofs

The coNP-completeness theorem is clean and plausible:

robustness asks whether supp(t)=𝒟; non-robustness has a witness determination.

The reduction from TAUTOLOGY/UNSAT style is fine at a sketch level. But make sure the theorem says “in the residual width” and that the input representation of supports/formulas is explicit. It currently does.

The transactional hardness proof is more of a sketch, but acceptable for appendix.

⸻

Appendix B/C: Responsibility material

The Shapley/responsibility appendix is interesting, but it feels somewhat orthogonal to the main paper. It is okay in the appendix, but I would not bring more of it into the body.

The hardness theorem is plausible: single-layer determinations with DNF support reduce to Shapley-value computation / model counting. Good.

The “responsibility budget under join and union” proposition is attractive. I did not fully verify the inequalities, but they seem plausible under the definitions. If polishing, check the union part carefully: depending on supports, union can reduce absence budget substantially. The statement says join increases budget and union decreases it, which aligns with support intersection/union.

⸻

Appendix D/E: Algebraic details

These appendices are valuable but contain some redundancy with the body. That is fine.

One concern: Appendix “Within a Determination: Algebraic Details” uses broad language like “determined specifications admit semiring provenance.” This depends on the resolved-outcome ambiguity discussed above. Make sure the appendix uses the same “canonical maximal outcome / query-equivalence” convention as the body.

⸻

Appendix F/G: Transactional worked examples and protocol-specific structures

The transactional appendix is useful and gives the details body readers need if they question Θ(n).

However, some protocol-specific claims are still broad:

* “Under serializability with any protocol that permits either victim selection or batched scheduling…” — okay, but then the proof should explicitly construct for both.
* MVTO section: timestamp assignment may be modeled as a commitment, but if timestamps are deterministic by arrival order, depth can collapse. You discuss this, but make sure the statement distinguishes protocol class from implementation instance.

The “fine-grained separation of SER and SI” section supports the body, but it also reveals why the body’s iff proposition should probably be softened.

⸻

Appendix H: Datalog negation

The Datalog appendix is substantial and ambitious.

The canonical layered choice basis is a good idea, but the soundness/completeness proposition says:

each resolving determination produces a stable model, and every stable model is produced by exactly one resolving determination.

This “exactly one” is strong. It depends on the choice basis being canonical enough to avoid duplicate encodings of the same stable model. You likely intend the choice predicate to encode the entire local stable extension of each SCC, not independent atom choices. Make that explicit:

choice predicates range over local stable extensions of the SCC, not arbitrary atom truth assignments.

The current definition says “binary choice predicates for the atoms in C_i,” which can produce inconsistent assignments not corresponding to any local stable model unless additional constraints are imposed. The subsequent proof text mentions “locally stable extension,” so the definition should be updated to match the proof.

This is high priority if the Datalog appendix is meant to support the body theorem.

⸻

Appendix I/J/K: Systems agenda, open questions, depth reduction

These appendices are interesting but read more like research agenda notes than proof support. That is okay for an extended version, but for a PODS submission appendix, they may be too much.

The “Future Work: Systems Agenda” is good but long. If page limits or reviewer focus are a concern, this is the first appendix material I would trim.

“Heredity Canonicalization” and “Depth Reduction” are promising but feel under-integrated. They introduce new definitions and propositions very late. Unless they are important for submission, consider moving them to a technical report or shortening to a brief future-work paragraph.

⸻

Cross-cutting issues

A. Scope creep

The paper has at least four papers inside it:

1. determination semiring + filtration;
2. transactions/isolation analysis;
3. Datalog negation semantics;
4. responsibility/depth-reduction/systems agenda.

The body does a decent job keeping one through-line, but the appendices amplify the sprawl. For submission, I would ensure the abstract and intro do not promise every appendix result as a central contribution.

B. Finite 𝒟 assumption

You often say “in both instantiations, 𝒟 is finite.” Good. But some algebraic definitions look general while some propositions depend on finiteness. Consider adding a standing assumption before the semiring section:

In the main development, we assume the set of resolving determinations under the chosen basis is finite.

You already say this informally. Making it a standing assumption would simplify.

C. History-indexed commitments are important but easy to miss

This is a key novelty:

same commitment operator may have different effects at different histories.

You state it, but the algebra later sometimes treats commitments as symbolic variables. The paper handles this by saying elements of 𝒟 are resolved histories, not abstract possible worlds. I would emphasize this once more before the filtration: layers classify operators, but determinations are history-indexed records.

⸻

Punchlist

High priority

1. Clarify what “resolved outcome Spec(H)” means when Spec(H) is a chain, not a singleton.
    Define canonical maximal/exposed outcome or query-equivalence within a chain.
2. Narrow or rephrase Theorem “Classical provenance is pointwise in determinations.”
    Remove stale multiple labels and state it specifically for single classical K-relation provenance versus determination-indexed provenance.
3. Soften or condition the transaction depth theorem.
    Move the “repeatably generable around a surviving transaction” condition into the theorem statement or restrict to SER/SI constructions.
4. Soften the isolation-sensitive tuples proposition from a global iff to a witnessed separation, or explicitly state the simplified conflict-graph assumptions under which the iff holds.
5. Restrict the body Datalog theorem to the representative class / canonical basis.
    The current “finite Datalog^neg program” statement is too broad relative to the proof sketch and appendix nuance.
6. Clarify monus elimination.
    Distinguish annotation of absent atom (0) from contribution of successful negated literal (1), and ensure the appendix contains a named proof.
7. Fix the canonical Datalog choice-basis definition.
    Choice predicates should range over local stable extensions of SCCs, or you need constraints excluding inconsistent atom-wise choices.

Medium priority

8. Revise Depth-1 = tuple-independent PDB to account for valid-determination constraints.
    State full tuple-independent equivalence only when all binary commitment assignments are valid.
9. Add a standing finiteness assumption for 𝒟 in the main algebra section.
10. Clarify minimal resolving determination deletion.
    Say what it means to remove a commitment event while retaining later dependent events; invalid histories count as unresolved, or dependency closure is removed.
11. Check union/join responsibility-budget inequalities in appendix.
    They seem plausible but should be verified carefully.
12. In MVTO/protocol appendix, consistently distinguish protocol class from deterministic implementation instance.
13. Make conv/resolution terminology consistent: resolved, determined, resolving determination, outcome equivalence.
14. Fix small grammar issue: “written D ≡_k D', defined inductively” → “is defined inductively.”

Low priority

15. Consider trimming or moving systems agenda / heredity canonicalization / depth reduction appendices.
    They are interesting but peripheral and make the submission feel sprawling.
16. Reduce duplicate algebra exposition between body and appendices if page count matters.
17. Run full BibTeX/cross-reference build and inspect PDF.
    The sandbox compile succeeded but citations were unresolved.
18. Consider adding a small table of core objects.
    Spec, Hist, O, D, P_D, P(t), supp, 𝔽_k, qdepth — the paper introduces many symbols quickly.
19. Search for overbroad “any finite Datalog^neg” / “any isolation level” phrases and qualify them.
20. Final proof-label cleanup.
    Remove unused/stale labels and make theorem/proposition names match their actual role.

Bottom line

This is a promising and substantially different paper from the Complete CALM draft. The core algebra — supports over resolving determinations and the filtration — is compelling. The main risks are overclaiming in the two instantiations: transaction isolation and Datalog negation. If you narrow those theorem statements to exactly what the proofs support, and clarify the resolved-outcome semantics, the paper will be much more defensible.