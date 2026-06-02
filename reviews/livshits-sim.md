# Simulated Review: Ester Livshits (Technion)

**Paper:** Determination Provenance: From Ambiguity to Algebra

## Summary

The paper introduces "determination provenance," a framework that extends classical semiring provenance to settings where multiple admissible outcomes exist for the same input. The key construction is a "determination semiring" (a Boolean algebra on supports) equipped with a filtration induced by layered commitments. The paper instantiates this for transactions and Datalog with negation, and proves that deciding robustness (whether a tuple holds under every resolving determination) is coNP-complete.

## Strengths

- **Clean conceptual separation.** The distinction between derivational provenance (within a fixed determination) and determination provenance (across determinations) is well-motivated and clearly articulated. The observation that classical provenance presupposes a resolved semantics is simple but has not been formalized before.

- **The filtration is the right contribution.** The paper correctly identifies that the powerset semiring on supports is trivial, and that the interesting structure is the filtration induced by non-commuting commitment layers. The non-expansiveness of positive RA (Corollary 3.1) and the depth-increasing behavior of difference (Proposition 3.4) are clean results that justify the filtration as a meaningful algebraic object.

- **Datalog instantiation is compelling.** Theorem 5.1—recovering stratified, well-founded, and stable-model semantics as different filtration levels—is an elegant observation that connects the framework to well-studied objects in database theory.

- **The framework is well-scoped for a theory paper.** The paper does not overclaim algorithmic contributions; it is honest that the complexity section is a validation rather than a headline result.

## Weaknesses

**1. The coNP-completeness result (Theorem 6.1) is not a genuine complexity contribution.**

The theorem states: if you have n independent binary commitments, polynomial validity checking, and polynomial query evaluation, then robustness is coNP-complete. The proof is a direct encoding of DNF-Validity: commitments biject with truth assignments, a UCQ encodes the DNF, and robustness = validity.

This is a completely standard reduction that follows immediately from the definitions. It does not require any insight specific to the determination framework. Any setting where you have exponentially many "worlds" and polynomial-time evaluation of a query in each world will yield coNP-completeness of universality by the same argument. The result is already known for:
- Certain answers in CQA (Arenas et al. 1999)
- Skeptical reasoning in stable models (Marek & Truszczyński 1991)
- Possible-worlds query evaluation (Abiteboul et al. 1991)

The paper acknowledges this ("the same reduction independently proves coNP-hardness of skeptical reasoning"), but then still lists it as contribution (iv) and devotes a full section to it. For PODS, a complexity section should either prove something new or provide a non-trivial dichotomy. This does neither.

**Suggestion:** Demote to a remark or fold into the Datalog section as a corollary. The space would be better used for tractability results or connections to structural parameters of the query/program.

**2. No tractability results beyond brute-force bounded width.**

Corollary 6.1 gives an O(2^{wd} · p(n)) brute-force bound. This is not a tractability result—it is the trivial enumeration algorithm. For PODS, I would expect at least one of:
- A dichotomy (robustness is in PTIME for some syntactically defined class of queries/programs, coNP-complete otherwise)
- A connection to structural parameters of the query (treewidth, hypertreewidth) that yield polynomial-time robustness
- An approximation algorithm for the support ratio (the "tail-bound" application)
- A connection to #P counting that would enable Shapley-value-style responsibility measures

The paper mentions "tail bounds" and "diagnosis" as applications (Section 4.5) but provides no algorithms for computing them. The support ratio |supp|/|D| requires enumerating D, which is exponential. Without approximation algorithms or sampling guarantees, these applications are purely conceptual.

**3. No connection to causality, responsibility, or Shapley values.**

The paper cites Halpern & Pearl [14] and Meliou et al. [19] in the related work but does not develop the connection. Determination provenance is naturally suited to responsibility-style questions: "how many determinations must be changed to make a contingent tuple robust?" or "what is the Shapley value of a commitment with respect to a tuple's support?" These are the quantitative measures that would make the framework actionable for explanation, and they are entirely absent.

The "diagnosis" application in Section 4.5 ("which ordering commitment is shared by all violating determinations?") is essentially asking for a prime implicant of the complement of the support—a well-studied problem in Boolean function analysis. The paper does not connect to this literature or provide complexity bounds for this specific question.

**4. The framework is purely definitional—no algorithms are provided.**

The paper defines determination provenance, proves structural properties (filtration, non-expansiveness), and establishes a complexity lower bound. But it provides no algorithm for:
- Computing the set D of minimal resolving determinations
- Computing the support of a tuple
- Deciding robustness in practice (beyond brute-force enumeration)
- Approximating the support ratio
- Computing certificates (defined in the appendix but with no algorithmic content)

For a framework paper at PODS, this is acceptable if the structural results are sufficiently deep. But the structural results here are relatively straightforward (the filtration is a chain of sub-Boolean-algebras defined by an equivalence relation), and the complexity result is standard. The paper would be significantly stronger with even one non-trivial algorithmic result.

**5. The "tail-bound" application assumes a uniform distribution without justification.**

Section 4.5 claims that |supp|/|D| gives a "structural tail bound" for SLA compliance. This assumes a uniform distribution over D. But in practice, schedulers are not uniform—they have biases toward certain orderings (e.g., FIFO, priority-based). The paper acknowledges this parenthetically ("other distributions yield weighted variants") but does not develop the weighted case. Without a justification for uniformity or an algorithm for the weighted case, this application is speculative.

## Questions for the Authors

1. **Tractability:** Are there natural restrictions on the commitment basis or query language under which robustness drops to PTIME? For example: if the query is a single conjunctive query (not a UCQ), is robustness still coNP-complete? The lower bound uses a UCQ; does it hold for CQs?

2. **Responsibility:** Can you define a natural notion of "responsibility of a commitment for a tuple" analogous to Meliou et al.'s causal responsibility? What is the complexity of computing it?

3. **Approximation:** Is there a polynomial-time approximation scheme for the support ratio? Or is it #P-hard to compute exactly (as one would expect from the connection to model counting)?

4. **Certificates:** The appendix defines certificates as over-approximations of commitments. Is there an efficient algorithm for computing minimal sufficient certificates for a given query family?

5. **Comparison to possible-worlds:** How does determination provenance differ from simply defining a possible-worlds database where each world corresponds to a determination? The support is then the set of certain answers' complement. What does the filtration add that possible-worlds semantics does not provide?

## Minor Comments

- Line 608: "has length at most |Spec(H)| - 1" — this bound is loose. In practice, minimal determinations are much shorter. Is there a tighter characterization?

- The paper uses "determination semiring" for (2^D, ∪, ∩) but this is just the free Boolean algebra on |D| atoms. The name may mislead readers into thinking there is more algebraic structure than a powerset lattice.

- Proposition 3.5 (Reachability): The proof assumes existence of tuples at each depth without constructing them. This is a minor gap but worth noting.

- The "three forces" taxonomy (Section 2.3) is never used in any formal result. It could be removed without affecting the paper's content.

## Overall Recommendation

**Weak Accept.**

The paper introduces a clean conceptual framework with a genuinely interesting structural observation (the filtration). The Datalog instantiation (Theorem 5.1) is the strongest result and connects to important questions in database theory. However, the complexity section adds nothing to the state of the art, the paper provides no algorithms, and the quantitative applications (tail bounds, diagnosis) are undeveloped. The paper would be significantly stronger with either (a) a non-trivial tractability result, (b) a connection to responsibility/Shapley values, or (c) an approximation algorithm for the support ratio. As submitted, it is a well-written framework paper whose technical depth is concentrated in the filtration construction and the Datalog correspondence, with the remaining contributions being either standard (coNP) or purely conceptual (systems applications).
