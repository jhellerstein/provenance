# Review Tracker — Round 3

## Consensus issues (raised by 2+ reviewers)

| # | Issue | Source | Priority | Notes |
|---|-------|--------|----------|-------|
| 1 | Theorem 5.1 scope overclaimed in abstract/intro — restricted class not disclosed | Claude, ChatGPT | **High** | Abstract says "differ only in which filtration level they read" without qualification. Theorem covers only programs with independent final negative SCCs. |
| 2 | Theorem 6.1 (#P-hardness) proof too compressed / wrong citation | Claude, ChatGPT | **High** | Valiant [29] is about the permanent, not #DNF Shapley. Need either a proper reduction or cite Shapley-value-for-Boolean-games literature (Deng & Papadimitriou, Bachrach et al.). |
| 3 | Theorem 6.2 (treewidth tractability): gap between conflict treewidth and support-formula treewidth | Claude, ChatGPT | **High** | Conflict graph connects commitments sharing a transaction; support formula's primal graph connects variables co-appearing in a clause. These are related but not proven equal. Need a lemma or explicit assumption. |
| 4 | FPRAS terminology incorrect — should be "additive approximation," not FPRAS (which implies relative) | ChatGPT | **High** | Shapley values can be small/zero; relative approximation is not implied by permutation sampling. Fix terminology or prove nonnegativity + relative guarantee. |
| 5 | Persistence canonicalization "without changing determination structure" — still too strong? | ChatGPT | **Medium** | ChatGPT argues seal+entailment changes what counts as a commitment vs. entailment, even if outcomes are preserved. Claude doesn't flag this round. Divergent. |
| 6 | History-invariance proof direction: persistence goes forward (H₁→H₂), but proof needs backward (H*→H) | ChatGPT | **Medium** | ChatGPT says persistence alone doesn't imply exclusions at H* also held at prefix H. Needs dependency-sufficiency/locality lemma. Claude doesn't flag. |
| 7 | Why-not claim lacks formal definition | Claude, Gemini | **Medium** | No definition of "determination why-not provenance." The observation (absence from commitment vs. blocked derivation) is correct but not formalized. |
| 8 | Related work: missing possible-worlds/probabilistic DB comparison | ChatGPT, Gemini | **Medium** | Obvious reviewer question: "isn't this just possible-worlds provenance?" Need explicit paragraph distinguishing. |

## Single-reviewer issues (worth considering)

| # | Issue | Source | Priority | Notes |
|---|-------|--------|----------|-------|
| 9 | Proposition D.4 (Reachability) has no proof in appendix | Claude | Low | Easy to add — construct a base fact present in exactly the determinations agreeing on a layer-k choice. |
| 10 | Lemma 2.1 uses "dependency set" which is defined only in appendix | Claude | Medium | Reader of body can't evaluate the hypothesis. Rephrase or define inline. |
| 11 | Theorem 2.1 (resolution iff provenance) still vulnerable as an iff | ChatGPT | Medium | ChatGPT suggests demoting to observation. Claude doesn't flag this round. |
| 12 | Finiteness: Definition 2.5 allows non-strict filtering (⊆ not ⊊) | ChatGPT | Low | Formal definition allows equality; strict shrinkage is only in prose. Fix definition or add assumption. |
| 13 | "Normal" Datalog undefined in main text | Claude | Low | Should state: at most one negative literal per rule body. |
| 14 | Filtration: uniqueness of "next maximal commuting layer" not proved | ChatGPT | Medium | If multiple maximal commuting batches exist from same prefix, ≡_k may depend on layering choice. |
| 15 | Section 6 competes with core framework for center stage | ChatGPT | Strategic | ChatGPT suggests framing responsibility as "secondary quantitative application" not co-equal with filtration. |
| 16 | Transaction section: Prop 4.2 too broad for support given | ChatGPT | Low | Depth claims for SER/SI stated without proof in body. Consider "informal characterization." |
| 17 | Related work: Shapley-in-provenance literature (Livshits et al. PODS 2021) not cited | Claude, Gemini | Medium | Section 6 is a full Shapley section; related work only mentions Meliou. |
| 18 | |Spec(H)| in finiteness bound is ambiguous (which H?) | Claude | Low | Should say |Spec(H₀)| for initial history. |

## Divergent viewpoints

| Issue | Claude | ChatGPT | Gemini | Assessment |
|-------|--------|---------|--------|------------|
| Persistence WLOG | Not flagged | Still too strong | Not flagged | We proved the stronger result; ChatGPT may not have fully parsed the appendix proof. But the body claim "without changing determination structure" does need the retrospective assumption stated inline. |
| History-invariance proof | Not flagged | Proof direction wrong | Not flagged | ChatGPT's concern is subtle: persistence says exclusions propagate forward (H₁→H₂). Our proof applies it "backward" (from H* to prefix H). But our proof actually goes: D resolves at H*, so o* is the unique outcome there; for any o≠o*, some φᵢ excluded it at some prefix of H*; since H⊑H* and persistence goes forward, the exclusion at H (earlier) implies exclusion at H* (later) — which is the direction we need. ChatGPT may be confused. Need to verify. |
| Theorem 2.1 as iff | Not flagged | Demote to observation | Not flagged | Recurring concern from ChatGPT across all rounds. The theorem is defensible if "classical semiring provenance over Spec" is read as "a single K-relation consistent with all outcomes." But it's a philosophical claim dressed as a theorem. |
| Section 6 prominence | Not flagged | Too prominent | Positive | Gemini loves it ("algorithmic depth"). ChatGPT worries it makes the paper "overfull." Strategic choice. |

## Recommended priorities

**Must-fix before submission:**
1. Fix #P-hardness citation/proof (#2)
2. Add lemma bridging conflict treewidth → formula treewidth (#3)
3. Fix FPRAS → additive approximation (#4)
4. Scope Theorem 5.1 claim in abstract (#1)
5. Add possible-worlds paragraph to related work (#8)
6. Cite Livshits et al. Shapley-in-provenance (#17)

**Should-fix:**
7. Verify history-invariance proof direction is correct (#6) — may be a non-issue
8. Define "dependency set" inline or rephrase Lemma 2.1 (#10)
9. Add proof of Reachability in appendix (#9)
10. Define "normal" for Datalog (#13)
11. Formalize why-not briefly (#7)

**Strategic decisions needed:**
- How prominent should Section 6 be? (ChatGPT says secondary; Gemini says highlight)
- Should we weaken persistence WLOG claim in body? (ChatGPT says yes; proof says no)
- Should Theorem 2.1 be demoted? (ChatGPT says yes; others don't flag)
