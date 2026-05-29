# Final Review Request

Please review the attached `main.tex` (the full paper) with particular attention to the changes made since your last review (chatgpt-15.md). Below is a summary of what changed; please focus your review on whether these changes are correct, well-integrated, and don't introduce new problems.

## Changes since last review

### Body changes

1. **Abstract rewritten** — now leads with the problem (multiple admissible outcomes exist) rather than a definition of provenance. More engaging opening.

2. **Intro flow** — added bridging sentence before Example 1; rewrote the "semantic mismatch" paragraph to avoid jarring transition from general claim to banking scenario; broke up the dense filtration-preview paragraph.

3. **Terminology cleanup** — removed all uses of "coordination" (undefined jargon) and replaced with "resolution" or "commitment layers" throughout (abstract, contributions, body, appendices).

4. **Definition 2.3 (Determined specification)** — now requires "a maximum element" (not just a chain) and uses "as shorthand for $\max_\Ord \Spec(H)$" instead of "by abuse of notation."

5. **Theorem 2.1** — softened "provenance must be indexed by determination" to "any sound representation must distinguish $D_1$ from $D_2$."

6. **Filtration section** — added parenthetical noting dynamic commutativity is subtle in general but unambiguous in our instantiations (with forward ref to open questions).

7. **Cross-specification comparison** — added zero-extension sentence ("we extend each support by zero outside $\mathcal{D}_I$").

8. **Transaction example (4.1)** — "Two equivalence classes arise" → "Two query-outcome equivalence classes arise (we write representative members)."

9. **Transaction theorem (4.1c)** — moved "repeatably generable" caveat into the theorem statement; removed post-proof paragraph.

10. **Proposition 4.2** — renamed from "Isolation-sensitive transactions" (with "iff") to "SER/SI qdepth incomparability" (witnesses only).

11. **Corollary 3.5 proof** — added selection/projection reasoning.

12. **Section 5 opening** — added "We now turn to our second instantiation."

13. **Negation section payoff** — broke the long "twofold" sentence into three short ones.

14. **Monus theorem** — added parenthetical noting PosBool result is immediate; the lemma is a stronger sufficient condition.

15. **Conclusion** — added probability-space paragraph (D is sample space, supports are measurable sets, filtration is measure-theoretic; robustness → hypothesis test, work regret → expected regret; "developing this is a natural next step").

16. **Related work** — added Ameloot et al. 2013 (CALM/Van den Bussche), Dalvi & Suciu 2012 (PDB dichotomy), Wijsen 2019 (CQA). Connected Ameloot ("when coordination is needed") → Anonymous ("complexity of resolution cost") → our paper ("algebraic consequences of determinations").

### Appendix changes

17. **Appendix reordered** to: Algebraic Details → Robustness → Responsibility → Transactional SI → Protocols → Datalog → Heredity → Systems Directions → Depth Reduction → Open Questions.

18. **Appendix Theorem 6.1 (general Datalog)** — added "satisfying the layered-choice decomposition of Proposition 6.1" to the theorem statement.

19. **Seal commutativity** — qualified "do not commute across strata" → "do not commute across dependent strata."

20. **Budget Compositionality** — cut entirely (sign issue, not central).

21. **Additive Approximation proof** — shortened to 3 lines.

22. **Removed** unused `wrapfig` package, stale `sec:relaxation` label, dead labels on theorems.

23. **Conclusion appendix list** — updated to match new ordering (no more ranges).

## What to check

1. **Do the body changes read smoothly?** Especially the abstract, intro, and conclusion.
2. **Are the related work citations well-integrated?** Does the Ameloot/Anonymous/our-paper positioning make sense?
3. **Is the conclusion's probability-space paragraph appropriate for PODS?** Too speculative? Too vague? Or a nice forward-looking note?
4. **Any remaining inconsistencies** between body claims and appendix content after the reordering?
5. **Any remaining overclaims** given the scoping changes (Prop 4.2 weakened, Datalog theorem conditionalized, etc.)?
6. **Page budget**: the body is exactly 15 pages. Any suggestions for what to cut if we need to add anything?

Please be direct about any remaining risks for PODS reviewers.
