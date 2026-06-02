## Review: "Determination Provenance: From Ambiguity to Algebra" (Revised)

This revision has made substantial improvements. The most critical structural problem from the previous version — the Datalog/filtration result buried in an appendix — is now addressed with Theorem 5.1, and the paper reads considerably better as a self-contained body. The persistence canonicalization (Appendix H) is a welcome addition that addresses the "is persistence necessary?" concern. Below is a detailed assessment of what works, what remains problematic, and what is new.

---

### What Has Improved

**Theorem 5.1 is the right move.** Promoting the filtration-recovers-negation-semantics result to a named theorem with a proof sketch is the single most important improvement. The claim is now formally asserted in the body and a PODS reviewer can evaluate it at pages 1–15. The table summarizing the four semantics as determination prefixes is clean and informative.

**The persistence issue is largely resolved.** Proposition H.1 and the canonicalization construction in Appendix H directly address the previous concern that persistence was assumed without justification of necessity. The phrase "every basis can be canonicalized to an equivalent persistent one" in Section 2.3, with a forward pointer, is the right lightweight in-body treatment. The majority-vote example is now correctly framed as a non-persistent commitment that *becomes* persistent after sealing its dependency set.

**Section 3.1 now separates the two algebraic structures explicitly.** The parenthetical clarifying that the determination semiring operates on supports while determination provenance pairs supports with K-valued annotations was missing before and resolves the conflation concern from the previous review.

**Proposition 4.2 consolidates the depth characterizations.** Collapsing the three separate propositions into one saves space and signals clearly that the depth result is a unified theorem about isolation levels, not three independent observations.

**Section 4.5's "Expressive Power" paragraph is new and valuable.** The four named query types (robustness, counterfactuals, tail bounds, diagnosis) give PODS reviewers a concrete grip on why this framework matters beyond classical provenance. This was implicitly in Appendix G before but belongs in the body.

---

### Remaining Major Issues

**1. Theorem 5.1's proof sketch is not yet sufficient for PODS.**

The sketch says "the sealing prefix is shared by all resolving determinations... hence all determinations agree at level k: F_k = {∅, D}." This is stated rather than argued. The key non-trivial step is showing that the stratification uniquely determines the sealing prefix — that is, there is no alternative set of sealing commitments that would also resolve the stratified fragment. Without this, the claim that all determinations *share* the prefix (rather than merely *having* a prefix of that depth) is unproven. 

Additionally, the sketch says "WFS computes the same sealing prefix and classifies atoms by their support at level k: robust (t), robustly absent (f), or contingent (u) — without discharging layer k+1." This glosses over the substantive content of the WFS correspondence: why does the alternating fixpoint compute *exactly* the same classification as reading supports at filtration level k? The Van Gelder-Ross-Schlipf characterization of WFS in terms of the alternating fixpoint is non-trivial, and the identification of WFS with "support classification at level k" is the theorem's most interesting claim. It should say more than "full proof in Appendix F" — even one sentence explaining the identification mechanism would help a reviewer decide whether to trust the statement.

**2. The "why-not" claim remains underdeveloped for a PODS audience.**

Remark 3.1 says the determination semiring "treats presence and absence symmetrically" and that determination provenance "adds the semantic dimension, recording which commitments made the absence (or presence) possible." Section 5 gives the example that s(c) is absent under D^(r) because of the commitment φ_{r(c)=t} — a semantic choice rather than a blocked derivation.

This is correct but it is a description, not a theory. The paper claims to "address longstanding gaps in provenance for queries with negation and why-not explanations" (abstract). A PODS reviewer familiar with Buneman et al. [6] and Köhler et al. [16] will want to know: given a tuple that is absent under some determination D, what does determination provenance provide that classical why-not provenance under the fixed model (Spec|D) does not? The answer — that you additionally know *which commitments were required to make D the resolution, and which of those commitments were responsible for the absence* — is compelling but is never stated as a theorem or even a precise definition. Consider adding a definition of "determination why-not provenance" parallel to Definition 3.1 for the absent case, even if it is brief.

**3. Finiteness of D is asserted but not adequately justified.**

Section 3.1 now says D is finite because there are "finitely many commitments, each applied at most once." This is slightly circular: it assumes that determinations never reuse a commitment predicate, but the framework allows φ_i ∈ Φ to appear multiple times in a determination (Definition 2.7 allows repeated application). More precisely, what justifies finiteness is that *minimal* resolving determinations have bounded length (bounded by the number of admissible outcomes, since each commitment strictly shrinks the admissible set). This argument should be stated, as it is not obvious from Definition 2.7 alone.

**4. The notation clash between ⊲ (layer sequencing) and ⊲⊳ (join) persists.**

This was flagged in the previous review and has not been fixed. In Corollary 3.1, the statement "qdepth(t₁ ⊲⊳ t₂) ≤ max(...)" uses ⊲⊳ for join. Earlier in the same section and throughout Section 2, ⊲ is used for layer sequencing. The visual similarity (⊲ vs ⊲⊳) is a genuine source of confusion when both appear in adjacent lines, as they do in Example 3.1 ("𝑃(𝑏 ⊲⊳ 𝑇(𝑏))") and Section 3.3. Please use a different symbol for one of them — the standard ⋈ for join would eliminate the ambiguity entirely.

---

### Moderate Issues

**5. Definition 2.5 is cleaner but loses something from the previous version.**

The previous version of Definition 2.5 explicitly said "the result may depend on the full set Spec(H), not only on individual outcomes — this is what allows commitments to be non-commutative." The revised version drops this sentence. It should be restored or an equivalent statement made, because without it the reader has no early warning that the non-commutativity of commitments is a consequence of set-valued application rather than an ad hoc assumption. It is the conceptually important point that distinguishes this from a simpler filtering model.

**6. The relationship between D (minimal resolving determinations) and non-minimal ones is never clarified.**

Definition 2.9 defines a resolving determination as any determination D such that Spec|D is a function. Section 3.1 restricts attention to *minimal* resolving determinations. But the paper never explains what it means for a non-minimal determination to have a "determination provenance" — is it well-defined, is it the same as the provenance under the minimal sub-determination, or is it simply outside the framework? This matters because in practice (e.g., under MVTO) a system might apply redundant commitments. A sentence clarifying that determination provenance is defined over minimal determinations and that any resolving determination can be reduced to a minimal one (by dropping redundant commitments) would close this gap.

**7. Proposition 3.5 (Reachability) has a gap in the proof.**

The proof says: "Level k for 1 ≤ k ≤ d: a tuple whose presence depends on the choice at layer k but not on layers k+1,...,d has support that is a union of level-k classes but not of level-(k-1) classes." This is a description of what such a tuple would look like, not a proof that such a tuple *exists*. The existence argument requires constructing a concrete base tuple or query that has this property, which requires assumptions about the determination structure beyond "non-trivial choices at each layer." The proof as written is circular: it assumes the existence of the thing it is trying to prove exists.

**8. Corollary 3.1 uses the wrong symbol for join (see point 4), and its statement is slightly imprecise.**

The corollary says "and likewise for union" without stating it formally. Given the parallel structure between join and union in the proof, this is a small omission but worth fixing for precision: the corollary should state both cases explicitly, mirroring the structure of Proposition C.1.

---

### Minor Issues

**9.** The abstract says determination provenance "enables new expressive power for systems settings — answering robustness, counterfactual, and tail-bound queries over transaction schedules and distributed traces." This is accurate but "tail-bound queries" may puzzle a PODS reviewer who does not immediately see the connection to provenance. A brief parenthetical — "(queries about what fraction of admissible schedules satisfy a predicate)" — would help.

**10.** Proposition 4.1 proves commutativity for independent transactions but Remark 4.1 describes non-commutativity only informally. Since non-commutativity is the source of depth > 1, and depth is the paper's main structural parameter, this asymmetry feels unbalanced. Consider adding a brief formal statement (even a one-line corollary) that "when T_i and T_j share a conflict cycle, φ_commit(Ti) and φ_commit(Tj) do not commute," citing the cycle structure as the proof.

**11.** Section 2.3's "three forces" taxonomy is used more effectively now (Example 2.1 explicitly connects it to both instantiations, and the alternating fixpoint is later classified as an entailment in Sections 5 and F.2). However, the taxonomy still plays no role in any formal result. Consider either adding a formal lemma — something like "depth is determined by commitments, not entailments" — or trimming the taxonomy to a remark and folding the content into Definition 2.5.

**12.** The "Expressive Power" paragraph in Section 4.5 mentions "tail bounds: under what fraction of admissible serializations does a latency-sensitive query meet its SLA?" This is a quantitative claim. The determination semiring as defined computes supports (sets of determinations), and |supp|/|D| gives a ratio, but this presupposes a uniform distribution over D. The paper should acknowledge this assumption — the structural tail bound is valid only when D is equipped with a uniform measure, which may not reflect actual scheduler distributions. Adding "under a uniform distribution over admissible serializations" would be accurate; alternatively a sentence noting that other distributions over D yield weighted versions of the same machinery.

**13.** The new Appendix H is well-constructed. One small issue: Proposition H.1(c) says "for any history H at which S has stabilized (no further events of types in S will arrive)." But "stabilized" is an informal notion — in the framework of Section 2, histories can always be extended. The condition should be stated more precisely, perhaps as: "for any history H that is a final extension (no further environment events of types in S are added in any extension)," or by appealing to the quiescent-history assumption mentioned in the appendix's closing paragraph.

**14.** The reference to "Proposition H.1" in Section 2.3 is a forward reference to an appendix that reviewers need not read. Since the canonicalization is now load-bearing (it justifies that persistence is WLOG), the in-body statement should say something slightly stronger than a bare pointer: at minimum, "persistence is without loss of generality: Appendix H shows that any non-persistent basis can be replaced by a persistent one that produces the same resolved outcomes, by sealing the commitment's dependency set before applying it."

---

### Assessment

The revision is meaningfully stronger. The two most urgent remaining issues are the proof sketch for Theorem 5.1 (the WFS correspondence needs more than a pointer to Appendix F) and the formal treatment of why-not determination provenance (the abstract's claim needs formal grounding in the body). Addressing these, plus the notation clash and the finiteness argument, would make the paper ready for a confident PODS submission.