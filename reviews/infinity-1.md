- **Section 8 (Conclusion):** Appropriately brief. The connection to CALM/declarative systems is a nice framing for the broader agenda.

---

## Comments on the Appendices

- **Appendix A (Robustness Proofs):** The DNF-Validity reduction is clean and correct. The Datalog hardness instantiation is a nice parallel. Both proofs are well-structured.

- **Appendix B-C (Responsibility):** The multi-layer worked example (Appendix B) is helpful for understanding the layered Shapley game. The additive approximation (Proposition C.2) is standard but useful to include. **Note:** The round-5 tracker flags Proposition 6.4 (join concentrates responsibility) as likely false—I don't see this proposition in the current body. If it was removed, good. If it's still present under a different numbering, it needs to be fixed or removed.

- **Appendix D (Within-determination algebra):** The "sequential discharge vs. algebraic combination" distinction is important and well-explained. The open questions (universality, composition laws) are genuine and interesting.

- **Appendix E (Across-determinations):** The full proofs of filtration closure and the difference-increases-depth proposition are straightforward but necessary for completeness.

- **Appendix F (Transactional worked examples):** The SER and SI worked examples are helpful. The write-skew discussion is clear. The fine-grained SER/SI separation (Appendix F.3) provides the full characterization that the body only sketches.

- **Appendix G (Protocols):** Thorough treatment of 2PL, OCC, MVTO. The key insight—all three have the same worst-case depth but differ in which discretionary choices they expose—is well-argued. Per-batch depth 2 for all three is a clean unifying result.

- **Appendix H (Datalog):** The stable → well-founded → stratified progression is well-developed. The general case (nested cycles, Theorem H.2) fills the gap left by the body. The "nontrivial example" ($d(c) \leftarrow r(c); d(c) \leftarrow s(c)$) showing WFS can discover robust atoms without resolving cycles is a nice illustration.

- **Appendix I (Systems Agenda):** Ambitious and well-motivated. The Dapper example (Example I.1) makes the systems relevance concrete. The parsimony dimensions (truncation via filtration, compression via certificates) are a clean design-space decomposition. This appendix reads as a compelling research agenda.

- **Appendix J (Heredity Canonicalization):** The proof that non-hereditary bases can be canonicalized to hereditary ones (in the retrospective setting) is careful and complete. The key insight—that the seal is non-filtering when the dependency set has already stabilized—is well-explained.

- **Appendix K (Open Questions):** Genuine open questions. Dynamic Foata normal form and universality are the most interesting. The "program-bounded vs. input-recurrent depth" question is well-posed.

- **Appendix L (Depth Reduction):** The three mechanisms (coarsening, commutation, entailment) are a useful taxonomy. The transactional and Datalog examples make them concrete.

---

## Suggestions for Improvement (within 15-page body constraint)

1. **Demote Theorem 2.1 to an observation or remark.** It's motivational, not technical. Use the freed space to strengthen the Datalog proof sketch.

2. **In Section 4, lead with per-batch depth 2 as the representative result.** The $\Theta(n)$ worst-case is a theoretical completeness result; the per-batch structure is what matters for systems and for the bypass application.

3. **In Section 5, add one sentence about the general case's key difficulty.** Something like: "When negative SCCs interact (later choices depend on earlier outcomes), the choice layers do not commute, giving depth $k+d$ rather than $k+1$; the full construction appears in Appendix H."

4. **In Section 6.3 (PDB connection), state the formal correspondence precisely.** Even one proposition ("A depth-1 determination semiring over $n$ binary commitments is isomorphic to a tuple-independent PDB over $n$ tuple-existence events") would anchor the discussion.

5. **Clarify the scope of Theorem 5.2 (Monus Elimination).** The round-5 tracker identified that the theorem is overclaimed for general $K$. If the fix is to state it at the support level (Boolean), say so explicitly in the body. The current statement says "naturally ordered, zero-divisor-free commutative semiring $K$" which may still be too broad.

6. **Add a forward reference from Definition 2.5 (commitment basis) to the instantiations.** The definition is abstract; a sentence like "In Section 4, the basis consists of ordering commitments; in Section 5, of sealing and choice predicates" would help the reader.

---

## Verdict Rationale

The paper introduces a genuinely novel conceptual framework (determination provenance) with a clean algebraic formulation (the filtered determination semiring) and two non-trivial instantiations. The filtration is the right abstraction, and the compositionality result is useful. The negation-semantics-as-filtration-levels theorem is elegant.

The weaknesses are: (1) the computational story is thin for PODS (no algorithms for computing supports/qdepth, bypass certification claimed polynomial but not proved in body); (2) some results are weaker than their framing suggests (Theorem 2.1 is trivial, the $\Theta(n)$ depth bound is pathological); (3) the $K$-valued structure beyond supports is never exploited. These are addressable within the page budget (mostly by recalibrating claims rather than adding material).

The paper is above the acceptance threshold for PODS: it introduces a new algebraic framework, proves non-trivial structural results, and opens a clear research direction. The conceptual contribution (making semantic commitments explicit and composable) is significant. With the suggested tightening, this would be a solid accept.