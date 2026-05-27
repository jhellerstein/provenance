"""
Compute Shapley values for the multi-layer responsibility example.

MODEL (ordering basis under SER):
- For a 3-cycle T1—T2—T3: orient one edge. The node not on that edge
  is the victim. T1→T2 and T2→T1 both abort T3. So a 3-cycle gives a
  3-way victim choice.
- For a directed 2-cycle T1⇄T2 (rw+wr): exactly one must abort.
  Binary commitment: who wins.

DEPTH-2 EXAMPLE:
- 2-cycle A: T1⇄T2. Commitment φ₁: abort T1 or abort T2.
- 2-cycle B: T2⇄T3. Commitment φ₂: abort T2 or abort T3.
- T2 is shared across both cycles.

Depth structure:
- If φ₁ aborts T2: 2-cycle B auto-resolved (T2 gone). Done. Depth 1.
- If φ₁ aborts T1: T2 survives, 2-cycle B needs resolution. Depth 2.

The determination space is a TREE, not a product:
  D1: abort T2              (φ₁ only; φ₂ never discharged)
  D2: abort T1, abort T2    (both layers)
  D3: abort T1, abort T3    (both layers)

Three determinations total.

Tuple t written by T3. t holds iff T3 not aborted.
  D1: T3 survives. t holds.
  D2: T3 survives. t holds.
  D3: T3 aborted. t ABSENT.

Support of t: {D1, D2} — 2 out of 3.

RESPONSIBILITY (per-layer, as defined in the paper):

The paper says: "responsibility at layer k is the Shapley value in the
presence game conditioned on layers 1,...,k-1 being discharged."

LAYER 1 GAME:
- 1 binary commitment φ₁. n=1.
- Determination space at layer 1: {abort T1, abort T2}.
- Realized D*: we consider D* = (abort T1, abort T2) — both layers needed.
- At layer 1, D*[φ₁] = "abort T1".
- Does t hold given only layer-1 information?
  * If φ₁ = abort T2 (= D1): t holds (T3 survives, done).
  * If φ₁ = abort T1: t's status depends on layer 2 (not yet resolved).
- For the presence game at layer 1, we need to define v(C):
  v(C) = Pr[t holds | commitments in C agree with D*]
  where the probability is uniform over completions of uncommitted layers.

  v(∅) = Pr[t holds] over all 3 determinations uniformly = 2/3.
  v({φ₁}) where φ₁ agrees with D* (φ₁ = abort T1):
    = Pr[t holds | φ₁ = abort T1] = conditioned on layer 2 being needed,
      uniform over φ₂ choices = 1/2 (abort T2 → t holds; abort T3 → t absent).

  Shapley for 1 player: ρ(φ₁) = v({φ₁}) - v(∅) = 1/2 - 2/3 = -1/6.

  Interpretation: φ₁'s choice (abort T1 rather than T2) DECREASED the
  probability of t holding from 2/3 to 1/2. Negative responsibility.

LAYER 2 GAME (conditioned on φ₁ = abort T1):
- 1 binary commitment φ₂. n=1.
- Determination space at layer 2: {abort T2, abort T3}.
- Realized D*[φ₂] = "abort T2".
- Does t hold?
  * If φ₂ = abort T2: t holds.
  * If φ₂ = abort T3: t absent.

  v(∅) = Pr[t holds | layer 2 uniform] = 1/2.
  v({φ₂}) where φ₂ = abort T2: = 1 (t certainly holds).

  Shapley: ρ(φ₂) = v({φ₂}) - v(∅) = 1 - 1/2 = 1/2.

  Interpretation: φ₂'s choice (abort T2, saving T3) raised t's
  probability from 1/2 to 1. Strong positive responsibility.

TOTAL: ρ(φ₁) + ρ(φ₂) = -1/6 + 1/2 = 1/3.
This equals v_final - v_prior = 1 - 2/3 = 1/3. ✓

ALTERNATIVE D*: D* = D1 (abort T2, layer 1 resolves everything).
Layer 1 only (no layer 2):
  v(∅) = 2/3.
  v({φ₁}) where φ₁ = abort T2: Pr[t holds | φ₁ = abort T2] = 1.
  ρ(φ₁) = 1 - 2/3 = 1/3.

  No layer-2 responsibility (layer 2 never discharged).
  Total: 1/3. Same budget, all concentrated on φ₁.
"""

from fractions import Fraction


print("=" * 60)
print("DEPTH-2 EXAMPLE: T1⇄T2⇄T3 (two overlapping 2-cycles)")
print("Tuple t written by T3. t holds iff T3 not aborted.")
print("=" * 60)
print()
print("Determination space (tree, not product):")
print("  D1: abort T2              → t holds")
print("  D2: abort T1, abort T2    → t holds")
print("  D3: abort T1, abort T3    → t ABSENT")
print()
print("Support of t: {D1, D2} — 2 out of 3")
print()

# Prior probability of t holding (uniform over determinations)
prior = Fraction(2, 3)
print(f"Prior Pr[t holds] = {prior}")
print()

# ============================================================
print("=" * 60)
print("CASE 1: D* = (abort T1, abort T2) — both layers needed")
print("=" * 60)
print()

# Layer 1
print("Layer 1: φ₁ = abort T1 (D*'s choice)")
v_empty_L1 = Fraction(2, 3)  # 2 of 3 determinations have t
# Conditioned on φ₁ = abort T1: two sub-determinations (D2, D3)
# t holds in D2, absent in D3
v_phi1_L1 = Fraction(1, 2)
rho_phi1 = v_phi1_L1 - v_empty_L1
print(f"  v(∅) = {v_empty_L1}")
print(f"  v({{φ₁}}) = {v_phi1_L1}")
print(f"  ρ(φ₁) = {rho_phi1}")
print()

# Layer 2 (conditioned on φ₁ = abort T1)
print("Layer 2 (conditioned on φ₁ = abort T1): φ₂ = abort T2")
v_empty_L2 = Fraction(1, 2)  # uniform over {abort T2, abort T3}
v_phi2_L2 = Fraction(1, 1)   # φ₂ = abort T2 → t certainly holds
rho_phi2 = v_phi2_L2 - v_empty_L2
print(f"  v(∅) = {v_empty_L2}")
print(f"  v({{φ₂}}) = {v_phi2_L2}")
print(f"  ρ(φ₂) = {rho_phi2}")
print()

total = rho_phi1 + rho_phi2
expected = Fraction(1, 1) - prior  # final certainty minus prior
print(f"Total responsibility: {rho_phi1} + {rho_phi2} = {total}")
print(f"Check: v_final - prior = 1 - {prior} = {expected}")
assert total == expected
print()

# ============================================================
print("=" * 60)
print("CASE 2: D* = abort T2 — layer 1 resolves everything")
print("=" * 60)
print()

print("Layer 1: φ₁ = abort T2 (D*'s choice)")
v_empty_L1b = Fraction(2, 3)
# Conditioned on φ₁ = abort T2: only D1, which has t. Certainty.
v_phi1_L1b = Fraction(1, 1)
rho_phi1_b = v_phi1_L1b - v_empty_L1b
print(f"  v(∅) = {v_empty_L1b}")
print(f"  v({{φ₁}}) = {v_phi1_L1b}")
print(f"  ρ(φ₁) = {rho_phi1_b}")
print()
print("No layer 2 (φ₂ never discharged).")
print(f"Total responsibility: {rho_phi1_b}")
expected_b = Fraction(1, 1) - prior
print(f"Check: v_final - prior = {expected_b}")
assert rho_phi1_b == expected_b
print()

# ============================================================
print("=" * 60)
print("CASE 3: D* = (abort T1, abort T3) — t ABSENT")
print("=" * 60)
print()

print("Layer 1: φ₁ = abort T1")
# Same as Case 1 layer 1
v_phi1_L1c = Fraction(1, 2)
rho_phi1_c = v_phi1_L1c - v_empty_L1
print(f"  v(∅) = {v_empty_L1}")
print(f"  v({{φ₁}}) = {v_phi1_L1c}")
print(f"  ρ(φ₁) = {rho_phi1_c}")
print()

print("Layer 2 (conditioned on φ₁ = abort T1): φ₂ = abort T3")
v_phi2_L2c = Fraction(0, 1)  # φ₂ = abort T3 → t absent (certainty of absence)
rho_phi2_c = v_phi2_L2c - v_empty_L2
print(f"  v(∅) = {v_empty_L2}")
print(f"  v({{φ₂}}) = {v_phi2_L2c}")
print(f"  ρ(φ₂) = {rho_phi2_c}")
print()

total_c = rho_phi1_c + rho_phi2_c
# Final: t is absent = 0. Prior = 2/3. So 0 - 2/3 = -2/3.
expected_c = Fraction(0, 1) - prior
print(f"Total responsibility: {rho_phi1_c} + {rho_phi2_c} = {total_c}")
print(f"Check: v_final - prior = 0 - {prior} = {expected_c}")
assert total_c == expected_c
