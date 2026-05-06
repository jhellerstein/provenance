# Review Tracker — Round 5

## Verdicts: Gemini Strong Accept, Claude ~Weak Accept (flags broken proofs), ChatGPT ~Weak Accept

The "non-monotone as commitment" reframing is landing strongly across all three. Two new results introduced this round have proof issues that must be fixed before submission.

## Must-fix (broken results)

| # | Issue | Source | Notes |
|---|-------|--------|-------|
| 1 | **Theorem 5.2 (Monus Elimination) overclaimed for N[X].** Proof assumes negation produces 0/1 annotations; this is only true for Boolean/why-provenance semirings, not N[X] where monus isn't even well-defined. Dannert et al. work with ω-continuous naturally-ordered semirings where the natural order gives 0/1 truth values at the Boolean level. | Claude | Scope to: "For any naturally ordered semiring K in which negated atoms receive annotations in {0_K, 1_K} (as holds for the Boolean, why-provenance, and PosBool semirings used in practice)." Or: state it for the Boolean abstraction (support level) and note that derivational annotations within each determination use unrestricted K. |
| 2 | **Proposition 6.4 (join concentrates responsibility) proof is invalid.** Shapley values don't behave monotonically under support containment in general. The intuition (smaller support → larger marginals) is plausible but the one-line proof doesn't establish it. | Claude | Options: (a) prove it properly via the game-theoretic definition, (b) demote to conjecture, (c) prove a weaker bound. The inequality may actually be false in general — need a counterexample check. |
| 3 | **Aggregation mentioned in abstract/intro but never developed.** "Non-monotone operations—negation, conflict resolution, aggregation" — but no aggregation instantiation exists. | Claude | Either remove "aggregation" from the list or add one sentence explaining how it fits (seal the input relation, then aggregate as entailment) without claiming a full instantiation. |

## Should-fix (recurring issues)

| # | Issue | Source | Notes |
|---|-------|--------|-------|
| 4 | Treewidth gap: support formula's primal graph may exceed conflict graph (transitive ordering constraints). | Claude | Need locality lemma or weaken to "support-formula treewidth" as the parameter. |
| 5 | General Datalog case (Appendix G.4) is bullet points, no theorems. | Claude | Either prove or label as conjecture/sketch. |
| 6 | Lemma 2.1 "events on which D's commitments depend" undefined in body. | Claude, ChatGPT | Add brief inline definition or forward ref. |
| 7 | Persistence canonicalization "without changing determination structure" — still flagged by ChatGPT. | ChatGPT | Consider adding "in the retrospective setting" more prominently. |

## Low priority

| # | Issue | Source | Notes |
|---|-------|--------|-------|
| 8 | Defensive parenthetical about filtration degeneracy draws attention to weakness. | Claude | Remove or rephrase neutrally. |
| 9 | Monotonicity condition in Theorem 6.2: "when earlier serialization implies lower latency" is non-trivial workload assumption. | Claude | State as explicit workload condition. |
| 10 | Additive approximation is weak for small responsibility values. | Claude | Note limitation. |
| 11 | Reachability proposition still unproved in appendix. | Claude | Add 2-line construction. |
| 12 | Gemini wants explicit semiring operations (⊕, ⊗) defined in body. | Gemini | Already defined as (∪, ∩) on supports; could be more explicit. |

## What's working

- **"Non-monotone as commitment" framing:** All three praise it as the paper's most important conceptual advance
- **Hardness proof (Theorem 6.1):** Now correct, no complaints
- **Compositionality claim (qualitative):** All find it useful even if proof needs work
- **Monus elimination (concept):** All find it interesting; issue is scope, not idea
- **Overall structure:** Gemini gives Strong Accept; paper's shape is right

## Priorities for next pass

1. **Fix Theorem 5.2:** Scope to appropriate semiring class (Boolean/why-provenance level, or state at support level)
2. **Fix or demote Prop 6.4:** Check if inequality is actually true; if so prove properly, if not demote
3. **Remove "aggregation" or add one-sentence justification**
4. **Treewidth: weaken to "support-formula treewidth ≤ w" as the condition**

## Discussion points

- Theorem 5.2: The right scope is probably "at the support level" — our framework tracks which determinations support a tuple (Boolean), and within each determination uses unrestricted K. The monus elimination applies to the support computation (Boolean), not to the K-valued derivational annotations. This is actually what the paper already does — the determination semiring is (2^D, ∪, ∩), which is Boolean. The monus elimination says: you don't need Boolean monus to compute supports if you have sealing.

- Prop 6.4: The inequality ρ(φᵢ, t₁⋈t₂) ≥ max(ρ(φᵢ,t₁), ρ(φᵢ,t₂)) is likely FALSE in general. Counterexample: if φᵢ is irrelevant to t₁ (ρ=0) but critical to t₂ (ρ=0.5), and t₁'s support is a strict subset of t₂'s support, then the join's support equals t₁'s support (since S₁∩S₂ = S₁), and φᵢ's responsibility for the join equals its responsibility for t₁ = 0. So ρ(join) = 0 < 0.5 = max. The inequality is wrong. We should retract it or replace with a correct bound.
