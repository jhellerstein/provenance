## Review: "Determination Provenance: From Ambiguity to Algebra" — Correctness and Reviewer Assessment

This revision makes several important technical repairs and introduces Theorem G.2 (the general Datalog case), which was the most important missing piece. The paper is substantially closer to submission-ready. Below is a focused correctness analysis followed by an overall assessment.

---

### Correctness Issues

**1. Factual error in the example for Theorem G.2.**

The example states: "Two stable models exist for each resolution of (a,b), giving four total stable models." This is wrong. The program is $a \leftarrow \neg b.\; b \leftarrow \neg a.\; c \leftarrow a, \neg d.\; d \leftarrow \neg c.$ with EDB $\emptyset$.

When layer $k{+}1$ chooses $a = \mathbf{f}$ (so $b = \mathbf{t}$): the rule $c \leftarrow a, \neg d$ becomes $c \leftarrow \mathbf{f}, \neg d = \mathbf{f}$, so $c$ is forced false. Then $d \leftarrow \neg c$ gives $d = \mathbf{t}$. The choice layer for $(c,d)$ is *not* binary — only $\{b, d\}$ is a valid stable model under this branch.

When layer $k{+}1$ chooses $a = \mathbf{t}$ (so $b = \mathbf{f}$): the $(c,d)$ cycle becomes $c \leftarrow \neg d,\; d \leftarrow \neg c$, which does have two stable extensions — giving models $\{a,c\}$ and $\{a,d\}$.

The total is three stable models, not four. You can verify directly that $\{a, c\}$, $\{a, d\}$, and $\{b, d\}$ are the stable models (all pass the Gelfond–Lifschitz reduct test), and $\{b, c\}$ is not (since $c \leftarrow a,\neg d$ requires $a = \mathbf{t}$).

This error matters because the example is the primary illustration of the theorem's bijection claim. The theorem itself is not broken — the bijection holds with three determinations and three stable models, because when $a = \mathbf{f}$ is chosen at layer $k{+}1$, the layer $k{+}2$ choice is forced to a single option. This is actually a good illustration of a *forced* choice layer (the $d^*$ concept), and the example should say so. But as written, the claim of four models is incorrect and will be caught by any reviewer who checks.

**2. Theorem G.2, Part (a): the bijection proof needs one additional sentence.**

The proof says "each resolving determination D discharges all $k{+}d$ layers, producing a unique two-valued assignment — a stable model." It does not address the case where a later choice layer becomes forced (only one valid option) due to earlier choices. As the corrected example shows, this happens: when $a = \mathbf{f}$ at layer $k{+}1$, the "binary choice" at layer $k{+}2$ degenerates to a forced choice. The bijection still holds, but the proof needs to explicitly note that forced choices at later layers reduce the number of resolving determinations below $2^d$, and that this matches the actual stable model count.

**3. Reachability (Appendix D) still has no proof.**

This has been flagged in every review. The proposition appears for the fourth time without proof. The construction is straightforward: for each level $k$, take a base fact $f$ that is inserted by a transaction $T_{\varphi_k}$ whose ordering commitment $\varphi_{T_{\varphi_k} \prec T_Q}$ appears exactly in layer $k$. Then $f$ is present under exactly those determinations that include $\varphi_{T_{\varphi_k} \prec T_Q}$ at layer $k$, giving $\mathrm{qdepth}(f) = k$. Please add this proof — it is two sentences.

**4. Theorem 5.2 (Monus elimination) is now correctly scoped but the claim in the contributions list is not.**

The theorem as stated is correct: it claims support equality (which determinations yield $v > 0_K$), not $K$-valued annotation equality. The proof is sound because monus in naturally ordered semirings produces only $\{0_K, 1_K\}$ as annotations for negated sealed atoms, and zero-divisor-free semirings preserve the zero/nonzero structure through positive polynomial evaluation.

However, Contribution (iii) in the introduction still says "monus elimination shows that layered monotone semirings *subsume* semirings-with-monus for provenance under negation." The word "subsume" implies full expressiveness equivalence, but the theorem only establishes support equality — the $K$-valued annotations within each determination differ (the monus version may assign non-Boolean annotations to negated atoms in intermediate strata, while the sealing version assigns $0_K$ or $1_K$). Change "subsume" to something like "agree on supports with" or "reproduce the support structure of."

**5. Theorem 6.2 is now correctly stated, but the sufficient condition needs precision.**

The theorem is now stated in terms of support formula treewidth directly, which is correct. The paragraph "Conflict treewidth is a sufficient condition: for predicates that depend only on pairwise ordering relationships..." is a correct informal claim, but it lacks formal precision. For a PODS audience, "depends only on pairwise ordering relationships" should be replaced with a precise condition, e.g.: "for support predicates that are expressible as monotone Boolean formulas where each clause involves only commitments sharing a conflict edge." As written, a reviewer cannot verify when this condition holds for arbitrary SLA predicates.

**6. Theorem G.2, Part (c): "forced layers" needs formal definition.**

The proof describes a forced layer as one where "both the optimistic and skeptical iterations converge to the same assignment for $C_i$'s atoms." This is operationally correct for the alternating fixpoint but is not a formal definition in terms of the framework. A forced layer in framework terms is one where, after discharging layers $k{+}1, \ldots, k{+}i{-}1$, the specification $\Spec \mid D_{k+i-1}$ has a unique extension for the atoms of $C_i$ — i.e., all admissible completions agree on those atoms. This should be stated formally in the definition of $d^*$.

---

### Technical Improvements That Are Correct

**Monus elimination (revised).** The support-level claim is sound. The key step — that $1_K \dot{-} v = 0_K$ whenever $v > 0_K$ in any naturally ordered semiring, so sealed negation produces the same Boolean annotation as monus — is correct for all standard provenance semirings including $\mathbb{N}[X]$.

**Budget compositionality.** The retreat from individual responsibility monotonicity to budget monotonicity is the right move. The proof ($B(t_1 \bowtie t_2) \geq \max(B(t_1), B(t_2))$ follows from $|S_1 \cap S_2| \leq |S_j|$) is completely correct. The accompanying note that "individual commitments' responsibilities redistribute within the budget but are not individually monotone under join" is honest and technically accurate.

**Theorem 6.2 renaming.** Stating the tractability result directly in terms of support formula treewidth closes the gap from prior versions. Correct.

**Theorem G.2 structure.** The proof of parts (a) and (b) is sound, modulo the example error and the bijection footnote noted above. The overall structure — $k$ sealing layers, $d$ choice layers ordered by SCC dependency, depth $k{+}d$ — is correct for programs whose negative SCC DAG is a path. For programs with parallel branches, the layers at the same depth in the DAG can be merged into a single layer (their choices commute), so the actual depth is $k + \ell$ where $\ell$ is the longest path in the SCC DAG — which is what the theorem states.

---

### Reviewer Assessment

**How will this land?**

The paper is now in genuinely good shape. The core algebraic contributions — the determination semiring, filtration, Theorem 5.1, and the determination responsibility framework — are sound and well-developed. The general Datalog case (Theorem G.2) directly addresses the criticism that was most likely to sink the paper, and the proof structure is correct.

The realistic outcome at PODS is **accept with shepherding or minor revision**, contingent on fixing the items above. The three things most likely to generate a conditional reject are:

First, the example error in Theorem G.2. A reviewer who checks the stable model count will find 3, not 4, and will have reduced confidence in the proof. This is fixable in an afternoon and must be fixed before submission.

Second, the Reachability proposition with no proof. After four reviews this reads as a known gap that the authors are declining to fill. Given the proof takes two sentences, there is no good reason not to include it.

Third, the "subsume" language in Contribution (iii). A reviewer familiar with Dannert et al. will correctly observe that the theorem proves support equality but not full $K$-valued annotation subsumption, and will view the contribution claim as overclaimed. Softening the language costs nothing.

If these three items are fixed, the paper makes a clean, self-contained contribution that covers genuinely new ground — a framework for provenance under semantic ambiguity, with two fully developed instantiations, a complexity frontier, and tight connections to the existing literature. That is a legitimate PODS paper.