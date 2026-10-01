Dear Joseph Hellerstein,

I am writing to inform you that the programme committee has decided not to accept your paper for PODS 2027. I am sorry for this outcome. I hope that the reviews can help improve your paper and you will resubmit a stronger version of your paper to an upcoming conference.

Best wishes,
Dan Olteanu
The PC Chair of PODS 2027

SUBMISSION: 6084
TITLE: Determination Provenance: From Ambiguity to Algebra

----------------------- REVIEW 1 ---------------------

SUBMISSION: 6084
TITLE: Determination Provenance: From Ambiguity to Algebra

----------- Overall evaluation -----------
SCORE: -1 (weak reject)
----- TEXT:
The goal of the paper is to formalize provenance for non-deterministic programs, motivated by concurrent transactions, datalog^\neg under stable model semantics, and distributed consensus protocols. The goal is to develop a formalism where one can ask if the provenance of a tuple holds in all executions, in some executions, or in no executions. Formalizing query outputs and their provenance for non-deterministic programs is an important problem, and it would be really nice to have a clean formalism.

The paper is very difficult to read; I made two attempts, but could not reach the end.  The authors appear to be very knowledgeable about concurrent programming, but do a poor job formalizing it. I really wanted to understand the paper, but, despite efforts, I got lost.

I cannot recommend the paper for PODS in its current form. I do believe in its motivation, however, and hope the authors will improve the formalism and publish the paper eventually.

DETAILED COMMENTS.

line 105: "The class {\cal H} of all histories represents all possible states across all possible runs." What are "states"? Is the set {\cal H} defined over a fixed set of events E? In other words, do any two histories H1, H2 in {\cal H} have same E? And does {\cal H} consists of all partial orders on E? Or only some partial orders?  For example, Definition 4.1 specializes histories to transactions.  In that case I assume that E is fixed (namely the set of operations (begin/commit/abort/read/write) of a fixed set of transactions), and that case {\cal H} is well defined, as all possible partial orders on this fixed set of events, that respects the order within each transaction.

Example 2.1 This example is very confusing. What is E? What is H? One expects O to be the set of outcomes of the query Q, for example O = {{b},{d},{b,d}} but instead O is described more like it is the set of histories {\cal H}.

Definition 2.5: "A commitment 𝜑 is an operator that can be applied at a history 𝐻 to produce an extended history 𝐻·𝜑"  Is 𝐻·𝜑 still considered a "history"?  It appears so, for example in line 198 the paper writes 𝐻·𝜑·𝐸·𝜓, which seems to assume that 𝐻·𝜑 is a history (i.e. a partial order) which ends with a the maximal element 𝜑, which we are allowed to extend by adding a new maximal element E, then extend it further by adding 𝜓.

I assume that authors meant to define histories as being partial orders on events AND commitments, with the restriction that every commitment 𝜑 partitions the history H into H1·𝜑·H2.  I read the paper under this assumption.

Line 187: "Note that Spec itself is a fixed relation—it does not change as history grows" I don't understand this. Spec is defined to be function. Functions don't change. Spec(H1) and Spec(H2) may be two different sets of outcomes, but the function Spec(-) is the same, how can it be otherwise?

Theorem 2.1 is a statement about concepts that were not defined.  The semiring provenance in [15] has a formal definition, which requires the presence of a database instance D and a query Q. It does not talk about specification Spec, nor correctness. The statement "Classical semiring provenance (a single 𝐾-relation) correctly represents a specification Spec iff..." is meaningless here: there is no database, no query, no specification, and no definition of "correctness".

Line 240. "when D(H1) and D(H2) produce the same resolved outcome" This is confusing. D(H1) and D(H2) are sequences of commitment events removed from their history (Def. 2.7) and they don't "produce outcomes". As Def. 2.5 stated "a commitment has no history-independent semantics", so we cannot do anything with D(H1) and D(H2) because they don't have any semantics, once we removed them from their history. I believe the intent here is to say that Spec(H1)=Spec(H2). This also applies later in the paper: whenever the paper refers to a "determination D" it seems to mean a "history H with determination D(H)".

Line 242. "Unlike abstract possible worlds, elements of D are grounded in event structure: the same commitment may have different effects at different histories, so determinations are history-indexed records, not symbolic labels." I do not understand this. What are "abstract possible worlds"? And "determinations are history-indexed records, not symbolic labels": I thought determinations are defined formally in Def. 2.7: is there anything to add?

Line 257. A suggestion: the function obs : O -> Inst(S) seems redundant. It may be simpler to say that O is the set of database instances for Datalog^\neg, and the set of decision traces for transactions. (I still don't understand the "decision traces" outcomes of transactions.)

The definition of Determination Provenance Semiring K^D is elegant (provided the formal definition of D is clarified), and so is Def. 3.2.

Example 3.1. Are {\cal D} and D_in, D_out determinations in the sense of Def. 2.7? In the examples we have seen earlier the determinations looked like \phi_{T1<T2}, but here D_in, D_out are unspecified.

Line 310. "Write L1(D), L2(D), ... for the successive layers of D;" This is the third notation for the same concept: first in line 183 and the second in line 204.

Lines 330-335 I did not understand this paragraph.

Minor typo in Line 360: "level 1" should be "level 0"

Proposition 3.3: this is nice.

Example 3.2.  The statement that all transaction-commit orderings commitments commute requires defining the commitment basis \Phi.  Otherwise, if one choose \Phi to be standard commit statements, then CO2; CO3 is not the same as CO3; CO2.  My guess is that the paper assumes the basis \Phi to consists of statements of the form \phi_{T1<T2}, \phi_{T2<T3}, etc: these indeed commute.

Example 4.1. seems a repeat of Example 3.2.  Same question here: the basis \Phi needs to be defined.

Theorem 4.1, again, this looks nice.


----------------------- REVIEW 2 ---------------------

SUBMISSION: 6084
TITLE: Determination Provenance: From Ambiguity to Algebra

----------- Overall evaluation -----------
SCORE: -2 (reject)
----- TEXT:
This work falls in the broader area of data provenance. The starting point is the observation that for settings where the outcome in not unique, it is unclear what is the data provenance of a certain result. The classical data provenance framework can be applied only when a certain outcome has been chosen. A concrete scenario from a database perspective is, for example, why-provenance of Datalog with negation under the stable model semantics. Indeed, given a database D and a Datalog program with stable negation P, there are several stable models of D and P. Thus, to explain why a certain fact f is entailed, we first need to fix a stable model M of D and P and ask why f occurs in M. In fact, the latter problem has been recently studied in the following KR 2026 paper:

Bogaerts et al., Why(-Not)-Provenance for Datalog with Negation

The submission addresses the above issue by introducing the so-called determination provenance framework, which is then instantiated for transactional systems and Datalog with stable negation.

On the positive side, I find the problem under investigation very natural. For example, focussing on Datalog, the current provenance framework only deals with positive Datalog programs. So, understanding how to define a provenance framework for Datalog programs with negation under different well-established semantics (well-founded, stable semantics, etc.) is indeed a crucial task.

On the negative side, I fear that the whole technical development underlying the proposed determination provenance framework is not presented and explained at a satisfactory level, and thus, I have difficulties to follow the details of the generic framework and how it is applied to transactional systems or Datalog with negation. There are several technical notions that are introduced without any intuition. Moreover, several parts of the paper (including definitions and statements) look more like a preliminary draft than a finalized PODS submission.

Summing up, I believe that the submission deals with an important question that deserves our attention. However, the way the proposed framework is defined and presented is far from what we expect from a typical PODS paper, and thus, the paper cannot be accepted in its current form.


----------------------- REVIEW 3 ---------------------

SUBMISSION: 6084
TITLE: Determination Provenance: From Ambiguity to Algebra

----------- Overall evaluation -----------
SCORE: -1 (weak reject)
----- TEXT:
This paper extends the classical provenance framework to the case of relational settings allowing different possible outcomes.
In the classical provenance setting the outcome is fixed and provenance tracks information about each result tuple within this fixed outcome. The framework proposed in the current submission consider systems where different possible outcomes are possible; the new notion of provenance extends  classical provenance by additionally tracking commitments that produced the outcome.

This provenance information is based on tracking determinations — i.e. sequences of subsequent commitments responsible for an outcome — in a structured way.   In fact the framework also tracks at which level in the sequence of commitments the outcome is already determined, using the notion of filtrations.

The purely algebraic framework is then instantiated on two applications : transaction scheduling (where commitments are transaction ordering decisions), and logic program (Datalog\neg) model computation (where commitments are choices on atomic truth values or atom sealings). It is shown that in these two settings determination provenance captures different isolation levels semantics and different negation semantics, respectively.

This is a framework paper whose underlying vision is very elegant: a purely abstract framework is able to unify and explain existing scenarios, opening the way to a uniform treatment of many provenance-like problems.
However I don’t believe it can be accepted as is. The present formalisation has too many issues, which I detail next. In summary almost all key notions are underspecified — i.e they formalisation is not precise enough to remove ambiguity; even worse, statements are at times sloppy and informal. In addition, presentation is extremely poor, with definitions used before being stated, and prose referring to notions not yet introduced.  Statements are at times unreadable (see my detail comments below), even to a the attentive and eager reader.
While I really appreciate the paper’s goal and approach, its current version does not meet PODS standards, and needs major rewriting.   

Next I detail the major difficulties I encountered in understanding the paper, in order of occurrence, hoping this can be helpful to make the paper more rigorous and accessible:

- Example 1.2 is very hard to understand at the point where it is introduced, without knowing what a transaction history is (which will only be said in Section 4.1). The example should at least spell out H (which used without saying what it is). Moreover the example talks about decision traces as history outcomes, while Example 1.1 was focusing on a query result. This makes the example unclear until reaching Section 3.1 where it is clarified that there exists a mapping from outcomes to relational instances. This mapping should be introduce earlier in the paper to help interpreting examples.

- Definition 2.4 defines “determined specification at H”, but then  uses the phrasing “H is determined” and the same notion is defined later as “H is resolved” (right after Definition 2.7). This creates confusion.

- Definition 2.5 leaves out the meaning of H \cdot \phi, which is only given in the following text. This text should part of the definition (otherwise H\cdot \phi in the definition is interested as an arbitrary extension). To the contrary, the sentence  “The effect of \phi…” should not be part of the definition, as it just informally rephrases what is formally captured bu the notion of operator.

- The text often talks about “the effect of \phi”; only after several occurrences the reader understand that it meant the reduction in possible outcomes. It would deserve a definition.   

- In Definition 2.5 defining commitment events as operators raises some questions which are not discussed. Are we assuming commitment events in a history are always compatible with the anterior events? I.e whenever a history H contains a a commitment event e, then e = \phi(H’), where H’ are all events in H preceding e ?
If this is the case then it should be formally stated as a constraint in defining  commitment events. If, to the contrary, this is not required then it is not clear how \phi is used as an operator. Moreover it does not seem a very good idea to call \phi both the operator and the event it adds to the history.

- In Definition 2.6 the final sentence “Different bases /…” is just a comment, it should not be part of a definition.

- Line 168 mentions “The set of pairwise ordering decision”. It is impossible to understand what this means here. It will only become clear in Section 4.2.

- Section 2.5 talks about tuples and classical provenance propagation while in the framework no notion of tuple exists yet. It will only be introduced in Section 3. The paragraph  “Observables and provenance query” where this is introduced must come earlier in the paper, definitely before Section 2.5.

- Paragraph “Three forces on a history”: either these notions are formally defined or better not to talk at all about them , as they are ambiguous definitions and do not add anything to the intuition.

- Definition 2.7: A determination is defined as a subsequence. A subsequence of which sequence? A history is not a sequence. And by the way, there are other places where the discussion treats a history as a sequence.

- Theorem 2.1: I cannot understand this theorem, as the notion of “K-relation” that “correctly represents a specification” is not defined, and I cannot even guess what it means. Also the provided characterization is unreadable at this point, as the notion of tuple associated to an outcome has not been defined yet, neither the notation P_D(t). The (short) proof does not help clarifying: what does it mean than a representation distinguishes D_1 and D_2 ?
Also I guess the statement of the theorem should talk about “all resolving determinations *of the same history*”.

- The set D of resolved histories introduced at line 239 is by definition a set of histories, each with its minimal resolving determination. However in almost all the sequel, D is treated as a set of determinations, as if there were a one-to-one correspondence between the two. However, unless I missed something, this is not case as a resolving determination does not determine the non-commitment events.
There are places like Definition 3.1 where it is important that D is interpreted as a set of histories (since Spec applies to histories, not determination).
Shall “determination” be read everywhere as “history paired with a resolving determination” ? If yes this notion should have a clean formal counterpart; informal descriptions such as “history-indexed record” are too ambiguous.

- Def 3.4 : What is d here? Are we assuming here that there is a maximum number of layers for all determinations. As I understand, this may not always be the case. Is this an implicit assumption for the notion of Filtration to be well defined ?
Also, the text right after this definition uses qdepth, which has not been defined yet.

- Proposition 3.2: What does it mean that supports “coincide” with a set of boolean formula? These are two different formal objects, say what it means that they correspond. Reading the proof one can get the meaning of “coincide”, however it is still not clear how a formula that only talks about commitment events can represent a full history (possibly including non-commitment events).

- Proposition 3.3 is not a proposition just a comment on the definition of qdepth.

- It is unclear what is the role of qdepth in the propose provenance framework. It is treated as a notion separate from determination provenance. However this seems an important parameter, as it tells up to which layer history influences the outcome. Is is to be considered a refinement of determination provenance?

- Proposition 4.2 is simply unreadable with the only background provided by the paper so far. This may be the effect of a coarse reduction to meet page limits.

- Section 5: the instantiation to Datalog\neg should be better introduced: It does not say what the histories are and how they are ordered. Moreover the specification Spec is only informally defined and it is not clear how it is a function of the history.

- Theorem 5.1 has a very ambiguous statement. What does it mean that a semantics “reads” a filtration level ?

- Typo : line 152 : the wrong “less than” symbol is used