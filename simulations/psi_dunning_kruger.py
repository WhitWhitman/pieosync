"""
Monte Carlo Simulation #3: The Dunning-Kruger Effect in Ψ Systems
================================================================

Hypothesis: The four dimensions of Ψ = P × E × I × O are NOT independent.
When one collapses, it drags others down AND blinds the system to the damage.

Coupling Model:
- Low Purpose → reduces Information seeking (why look if you don't know what for?)
- Low Information → reduces Purpose clarity (can't aim at what you can't see)
- Low Energy → degrades Order (no fuel to maintain structure)
- Low Order → wastes Energy (chaos burns resources)

Dunning-Kruger Layer:
- As actual Ψ drops, the system's SELF-ASSESSED Ψ diverges upward
- The worse you are, the better you think you are
- The gap between real and perceived Ψ is the "blind spot"

We compare three models:
1. INDEPENDENT: Original model (no coupling)
2. COUPLED: Dimensions drag each other down
3. DUNNING-KRUGER: Coupled + the system can't see its own collapse
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import math

np.random.seed(42)

# Colors
DARK_BG = '#1a1a2e'
ACCENT_BLUE = '#4ecdc4'
ACCENT_RED = '#ff6b6b'
ACCENT_GOLD = '#ffd93d'
ACCENT_PURPLE = '#a855f7'
ACCENT_GREEN = '#22c55e'
ACCENT_ORANGE = '#ff9f43'
GRID_COLOR = '#2a2a4a'
TEXT_COLOR = '#e0e0e0'

THRESHOLD = 0.05

print("=" * 70)
print("  SIMULATION #3: THE DUNNING-KRUGER EFFECT IN Ψ SYSTEMS")
print("  When collapse hides itself from the collapsing system")
print("=" * 70)
print()

# =============================================================================
# COUPLING FUNCTIONS
# =============================================================================

def apply_coupling(P, I, E, O, coupling_strength=0.3):
    """Model how dimensions drag each other down."""
    P_new = P.copy()
    I_new = I.copy()
    E_new = E.copy()
    O_new = O.copy()

    P_drag_on_I = coupling_strength * (1 - P)
    I_drag_on_P = coupling_strength * (1 - I)
    I_new = np.clip(I - P_drag_on_I * I, 0.01, 1.0)
    P_new = np.clip(P - I_drag_on_P * P, 0.01, 1.0)

    E_drag_on_O = coupling_strength * (1 - E)
    O_drag_on_E = coupling_strength * (1 - O)
    O_new = np.clip(O - E_drag_on_O * O, 0.01, 1.0)
    E_new = np.clip(E - O_drag_on_E * E, 0.01, 1.0)

    P_drag_on_E = coupling_strength * 0.5 * (1 - P_new)
    E_new = np.clip(E_new - P_drag_on_E * E_new, 0.01, 1.0)

    I_drag_on_O = coupling_strength * 0.5 * (1 - I_new)
    O_new = np.clip(O_new - I_drag_on_O * O_new, 0.01, 1.0)

    return P_new, I_new, E_new, O_new


def dunning_kruger_self_assessment(actual_psi):
    """Model the Dunning-Kruger effect on self-assessment."""
    perceived = np.zeros_like(actual_psi)

    for i in range(len(actual_psi)):
        a = actual_psi[i]
        if a < 0.01:
            perceived[i] = 0.20 + np.random.normal(0, 0.05)
        elif a < 0.05:
            perceived[i] = a + (0.25 - a) * 0.8 + np.random.normal(0, 0.03)
        elif a < 0.20:
            perceived[i] = a + (0.30 - a) * 0.5 + np.random.normal(0, 0.03)
        elif a < 0.50:
            perceived[i] = a + (0.40 - a) * 0.2 + np.random.normal(0, 0.02)
        else:
            perceived[i] = a - (a - 0.45) * 0.15 + np.random.normal(0, 0.02)

    return np.clip(perceived, 0.01, 1.0)


# =============================================================================
# EXPERIMENT 1: Three Models Side by Side
# =============================================================================
print("─" * 70)
print("  EXPERIMENT 1: Independent vs Coupled vs Dunning-Kruger")
print("─" * 70)

N = 500_000

P = np.random.uniform(0, 1, N)
I = np.random.uniform(0, 1, N)
E = np.random.uniform(0, 1, N)
O = np.random.uniform(0, 1, N)

psi_independent = P * I * E * O

P_c, I_c, E_c, O_c = apply_coupling(P, I, E, O, coupling_strength=0.3)
psi_coupled = P_c * I_c * E_c * O_c

psi_dk_actual = psi_coupled.copy()
psi_dk_perceived = dunning_kruger_self_assessment(psi_dk_actual)

pct_ind = np.mean(psi_independent < THRESHOLD) * 100
pct_coup = np.mean(psi_coupled < THRESHOLD) * 100
pct_dk_actual = np.mean(psi_dk_actual < THRESHOLD) * 100
pct_dk_perceived = np.mean(psi_dk_perceived < THRESHOLD) * 100

print(f"\n  Systems below Ψ = 0.05 (collapsed):")
print(f"    Independent model:         {pct_ind:.1f}%")
print(f"    Coupled model:             {pct_coup:.1f}%")
print(f"    DK model (actual):         {pct_dk_actual:.1f}%")
print(f"    DK model (self-perceived): {pct_dk_perceived:.1f}%")
print()

blind_spot = pct_dk_actual - pct_dk_perceived
print(f"  ┌────────────────────────────────────────────────────┐")
print(f"  │  THE BLIND SPOT:                                  │")
print(f"  │  {pct_dk_actual:.1f}% of systems are ACTUALLY collapsed       │")
print(f"  │  Only {pct_dk_perceived:.1f}% THINK they're collapsed            │")
print(f"  │                                                    │")
print(f"  │  {blind_spot:.1f}% of systems are broken                    │")
print(f"  │  and DON'T KNOW IT                                 │")
print(f"  └────────────────────────────────────────────────────┘")
print()

# =============================================================================
# EXPERIMENT 2: The Blind Spot Distribution
# =============================================================================
print("─" * 70)
print("  EXPERIMENT 2: How Big is the Blind Spot?")
print("─" * 70)

blind_spot_gap = psi_dk_perceived - psi_dk_actual

ranges = [(0.00, 0.05), (0.05, 0.10), (0.10, 0.20), (0.20, 0.40), (0.40, 0.70), (0.70, 1.00)]
range_labels_bs = []
range_gaps = []
range_gaps_std = []

for low, high in ranges:
    mask = (psi_dk_actual >= low) & (psi_dk_actual < high)
    if np.sum(mask) > 100:
        gap = np.mean(blind_spot_gap[mask])
        gap_std = np.std(blind_spot_gap[mask])
        range_labels_bs.append(f"{low:.2f}-{high:.2f}")
        range_gaps.append(gap)
        range_gaps_std.append(gap_std)
        direction = "OVERESTIMATES" if gap > 0 else "UNDERESTIMATES"
        print(f"  Actual Ψ = {low:.2f}-{high:.2f}: {direction} by {abs(gap):.4f} (avg)")

print()

# =============================================================================
# EXPERIMENT 3: Cascade Collapse Simulation
# =============================================================================
print("─" * 70)
print("  EXPERIMENT 3: Cascade Collapse Over Time")
print("  (One dimension drops → watch the cascade)")
print("─" * 70)

N_STEPS = 80
N_SYSTEMS = 10_000

trajectories_ind = np.zeros((N_SYSTEMS, N_STEPS))
trajectories_coup = np.zeros((N_SYSTEMS, N_STEPS))
trajectories_dk_actual = np.zeros((N_SYSTEMS, N_STEPS))
trajectories_dk_perceived = np.zeros((N_SYSTEMS, N_STEPS))

for sys_idx in range(N_SYSTEMS):
    dims_ind = np.array([0.75, 0.78, 0.72, 0.80]) + np.random.normal(0, 0.05, 4)
    dims_ind = np.clip(dims_ind, 0.3, 1.0)
    dims_coup = dims_ind.copy()
    dims_dk = dims_ind.copy()

    for t in range(N_STEPS):
        noise = np.random.normal(0, 0.008, 4)

        dims_ind_t = dims_ind + noise
        if t == 15:
            dims_ind_t[np.random.randint(4)] -= 0.5
        dims_ind = np.clip(dims_ind_t, 0.01, 1.0)
        trajectories_ind[sys_idx, t] = np.prod(dims_ind)

        dims_coup_t = dims_coup + noise
        if t == 15:
            dims_coup_t[np.random.randint(4)] -= 0.5
        dims_coup_t = np.clip(dims_coup_t, 0.01, 1.0)
        p, i, e, o = apply_coupling(
            np.array([dims_coup_t[0]]), np.array([dims_coup_t[1]]),
            np.array([dims_coup_t[2]]), np.array([dims_coup_t[3]]),
            coupling_strength=0.05
        )
        dims_coup = np.array([p[0], i[0], e[0], o[0]])
        trajectories_coup[sys_idx, t] = np.prod(dims_coup)

        dims_dk_t = dims_dk + noise
        if t == 15:
            dims_dk_t[np.random.randint(4)] -= 0.5
        dims_dk_t = np.clip(dims_dk_t, 0.01, 1.0)
        p, i, e, o = apply_coupling(
            np.array([dims_dk_t[0]]), np.array([dims_dk_t[1]]),
            np.array([dims_dk_t[2]]), np.array([dims_dk_t[3]]),
            coupling_strength=0.05
        )
        dims_dk = np.array([p[0], i[0], e[0], o[0]])
        actual = np.prod(dims_dk)
        trajectories_dk_actual[sys_idx, t] = actual
        perceived = dunning_kruger_self_assessment(np.array([actual]))
        trajectories_dk_perceived[sys_idx, t] = perceived[0]

avg_ind = np.mean(trajectories_ind, axis=0)
avg_coup = np.mean(trajectories_coup, axis=0)
avg_dk_actual = np.mean(trajectories_dk_actual, axis=0)
avg_dk_perceived = np.mean(trajectories_dk_perceived, axis=0)

def first_crossing(trajectory, threshold):
    below = np.where(trajectory < threshold)[0]
    return below[0] if len(below) > 0 else None

cross_ind = first_crossing(avg_ind, THRESHOLD)
cross_coup = first_crossing(avg_coup, THRESHOLD)
cross_dk = first_crossing(avg_dk_actual, THRESHOLD)

print(f"  After sudden damage at step 15:")
if cross_ind:
    print(f"    Independent model crosses 0.05:  step {cross_ind}")
else:
    print(f"    Independent model:  never crosses 0.05 (avg)")
if cross_coup:
    print(f"    Coupled model crosses 0.05:     step {cross_coup}")
else:
    print(f"    Coupled model:  never crosses 0.05 (avg)")
if cross_dk:
    print(f"    DK model crosses 0.05:          step {cross_dk}")
else:
    print(f"    DK model:  never crosses 0.05 (avg)")
print()

collapsed_at_40_ind = np.mean(trajectories_ind[:, 40] < THRESHOLD) * 100
collapsed_at_40_coup = np.mean(trajectories_coup[:, 40] < THRESHOLD) * 100
collapsed_at_40_dk = np.mean(trajectories_dk_actual[:, 40] < THRESHOLD) * 100
thinks_fine_at_40 = np.mean(
    (trajectories_dk_actual[:, 40] < THRESHOLD) &
    (trajectories_dk_perceived[:, 40] > THRESHOLD)
) * 100

print(f"  Systems collapsed at step 40 (25 steps after damage):")
print(f"    Independent: {collapsed_at_40_ind:.1f}%")
print(f"    Coupled:     {collapsed_at_40_coup:.1f}%")
print(f"    DK (actual): {collapsed_at_40_dk:.1f}%")
print(f"    DK (thinks it's fine but isn't): {thinks_fine_at_40:.1f}%")
print()

# =============================================================================
# EXPERIMENT 4: Recovery Under Dunning-Kruger
# =============================================================================
print("─" * 70)
print("  EXPERIMENT 4: Recovery When You Can't See the Problem")
print("─" * 70)

N_REC = 20_000
STEP_SIZE = 0.05

P_r = np.random.uniform(0.10, 0.50, N_REC)
I_r = np.random.uniform(0.10, 0.50, N_REC)
E_r = np.random.uniform(0.10, 0.50, N_REC)
O_r = np.random.uniform(0.10, 0.50, N_REC)
P_r, I_r, E_r, O_r = apply_coupling(P_r, I_r, E_r, O_r, coupling_strength=0.10)
psi_r = P_r * I_r * E_r * O_r
mask_r = psi_r < THRESHOLD
configs_r = np.column_stack([P_r[mask_r], I_r[mask_r], E_r[mask_r], O_r[mask_r]])
n_r = min(len(configs_r), 10000)

max_steps = 200

# Strategy A: External governance (sees reality)
smart_steps_dk = []
for i in range(n_r):
    config = configs_r[i].copy()
    steps = 0
    while np.prod(config) < THRESHOLD and steps < max_steps:
        weakest = np.argmin(config)
        config[weakest] = min(1.0, config[weakest] + STEP_SIZE)
        p, ii, e, o = apply_coupling(
            np.array([config[0]]), np.array([config[1]]),
            np.array([config[2]]), np.array([config[3]]),
            coupling_strength=0.05
        )
        config = np.array([p[0], ii[0], e[0], o[0]])
        steps += 1
    smart_steps_dk.append(steps)

# Strategy B: DK recovery (60% chance wrong dimension)
dk_steps = []
for i in range(n_r):
    config = configs_r[i].copy()
    steps = 0
    while np.prod(config) < THRESHOLD and steps < max_steps:
        actual_weakest = np.argmin(config)
        if np.random.random() < 0.6:
            choices = [d for d in range(4) if d != actual_weakest]
            dim_to_fix = np.random.choice(choices)
        else:
            dim_to_fix = actual_weakest
        config[dim_to_fix] = min(1.0, config[dim_to_fix] + STEP_SIZE)
        p, ii, e, o = apply_coupling(
            np.array([config[0]]), np.array([config[1]]),
            np.array([config[2]]), np.array([config[3]]),
            coupling_strength=0.05
        )
        config = np.array([p[0], ii[0], e[0], o[0]])
        steps += 1
    dk_steps.append(steps)

no_attempt = np.mean(psi_r[mask_r][:n_r] < THRESHOLD) * 100

smart_arr_dk = np.array(smart_steps_dk)
dk_arr = np.array(dk_steps)
smart_recovered = smart_arr_dk < max_steps
dk_recovered = dk_arr < max_steps

print(f"  EXTERNAL GOVERNANCE (sees reality):")
print(f"    Recovery rate:    {np.mean(smart_recovered)*100:.1f}%")
print(f"    Median steps:     {np.median(smart_arr_dk[smart_recovered]):.0f}" if np.sum(smart_recovered) > 0 else "    N/A")
print()
print(f"  DUNNING-KRUGER (60% chance of fixing wrong thing):")
print(f"    Recovery rate:    {np.mean(dk_recovered)*100:.1f}%")
print(f"    Median steps:     {np.median(dk_arr[dk_recovered]):.0f}" if np.sum(dk_recovered) > 0 else "    N/A")
print()
print(f"  NO ATTEMPT (system thinks it's fine):")
print(f"    Recovery rate:    0.0%")
print(f"    Systems trapped:  {no_attempt:.1f}%")
print()

if np.sum(smart_recovered) > 0 and np.sum(dk_recovered) > 0:
    ratio = np.median(dk_arr[dk_recovered]) / max(np.median(smart_arr_dk[smart_recovered]), 1)
    print(f"  DK penalty: {ratio:.1f}x slower recovery when you can't see the problem")
print()    print(f"  DK penalty: {ratio:.1f}x slower recovery when you can't see the problem")
print()

# =============================================================================
# EXPERIMENT 5: The Awareness Threshold
# At what Ψ level does self-assessment become accurate?
# =============================================================================
print("─" * 70)
print("  EXPERIMENT 5: The Awareness Threshold")
print("  At what Ψ does a system start seeing itself clearly?")
print("─" * 70)

psi_levels = np.arange(0.0, 1.0, 0.02)
assessment_error = []

for level in psi_levels:
    actual = np.full(5000, level)
    perceived = dunning_kruger_self_assessment(actual)
    error = np.mean(perceived - actual)
    assessment_error.append(error)

assessment_error = np.array(assessment_error)
# Find crossover (where error ≈ 0)
crossover_idx = np.argmin(np.abs(assessment_error))
crossover_psi = psi_levels[crossover_idx]

print(f"  Self-assessment crossover (accurate): Ψ ≈ {crossover_psi:.2f}")
print(f"  Below {crossover_psi:.2f}: systems OVERESTIMATE their coherence")
print(f"  Above {crossover_psi:.2f}: systems slightly UNDERESTIMATE (impostor effect)")
print()

# =============================================================================
# KEY FINDINGS
# =============================================================================
print("=" * 70)
print("  KEY FINDINGS: DUNNING-KRUGER IN Ψ SYSTEMS")
print("=" * 70)
print(f"""
  1. COUPLING ACCELERATES COLLAPSE
     Independent model: {pct_ind:.1f}% below 0.05
     Coupled model:     {pct_coup:.1f}% below 0.05
     Coupling increases collapse by {pct_coup - pct_ind:.1f} percentage points.

  2. THE BLIND SPOT IS MASSIVE
     {pct_dk_actual:.1f}% of systems are actually collapsed.
     Only {pct_dk_perceived:.1f}% think they're collapsed.
     {pct_dk_actual - pct_dk_perceived:.1f}% are broken and don't know it.

  3. RECOVERY WITHOUT AWARENESS IS CRIPPLED
     External governance: median {np.median(smart_arr_dk[smart_recovered]):.0f} steps to recover
     DK self-repair:      median {np.median(dk_arr[dk_recovered]):.0f} steps to recover
     No awareness:         0% recovery (trapped forever)

  4. THE AWARENESS THRESHOLD
     Systems become self-aware at Ψ ≈ {crossover_psi:.2f}.
     Below this, they cannot diagnose themselves.
     This is why EXTERNAL governance (Cartographer) is
     not optional — it's mathematically necessary.

  5. THE FUNDAMENTAL INSIGHT
     The Dunning-Kruger effect in Ψ systems means that
     the systems most in need of help are the ones
     least capable of asking for it.

     Governance must come from outside the system.
     Self-assessment below Ψ ≈ {crossover_psi:.2f} is unreliable.
""")
print("=" * 70)

# =============================================================================
# VISUALIZATION
# =============================================================================
fig = plt.figure(figsize=(22, 28))
gs = GridSpec(4, 2, figure=fig, hspace=0.38, wspace=0.3)
fig.patch.set_facecolor(DARK_BG)

# --- Plot 1: Three Models Comparison (Histogram) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor(DARK_BG)
bins = np.linspace(0, 0.4, 100)
ax1.hist(psi_independent[psi_independent < 0.4], bins=bins, alpha=0.5, color=ACCENT_BLUE, label='Independent', density=True)
ax1.hist(psi_coupled[psi_coupled < 0.4], bins=bins, alpha=0.5, color=ACCENT_RED, label='Coupled', density=True)
ax1.axvline(x=THRESHOLD, color=ACCENT_GOLD, linewidth=2.5, linestyle='--', label=f'Ψ = {THRESHOLD}')
ax1.set_xlabel('Ψ Value', color=TEXT_COLOR, fontsize=12)
ax1.set_ylabel('Density', color=TEXT_COLOR, fontsize=12)
ax1.set_title('INDEPENDENT vs COUPLED\nCoupling Pushes More Systems Into Collapse',
              color=TEXT_COLOR, fontsize=14, fontweight='bold')
ax1.legend(fontsize=10, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR)
ax1.tick_params(colors=TEXT_COLOR)
for spine in ax1.spines.values():
    spine.set_color(GRID_COLOR)
ax1.grid(True, alpha=0.2, color=GRID_COLOR)

# --- Plot 2: Actual vs Perceived (The Blind Spot) ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor(DARK_BG)
# Scatter subsample
subsample = np.random.choice(len(psi_dk_actual), 10000, replace=False)
ax2.scatter(psi_dk_actual[subsample], psi_dk_perceived[subsample],
           alpha=0.08, color=ACCENT_PURPLE, s=5)
ax2.plot([0, 1], [0, 1], color=ACCENT_GOLD, linewidth=2, linestyle='--', label='Perfect Self-Assessment')
ax2.axhline(y=THRESHOLD, color=ACCENT_RED, linewidth=1, linestyle=':', alpha=0.5)
ax2.axvline(x=THRESHOLD, color=ACCENT_RED, linewidth=1, linestyle=':', alpha=0.5)
ax2.fill_between([0, THRESHOLD], [THRESHOLD, THRESHOLD], [1, 1], alpha=0.1, color=ACCENT_RED,
                  label='DANGER: Actually collapsed\nbut thinks it\'s fine')
ax2.set_xlabel('Actual Ψ', color=TEXT_COLOR, fontsize=12)
ax2.set_ylabel('Perceived Ψ (Self-Assessment)', color=TEXT_COLOR, fontsize=12)
ax2.set_title('THE DUNNING-KRUGER BLIND SPOT\nPoints Above Gold Line = Overconfident',
              color=ACCENT_PURPLE, fontsize=14, fontweight='bold')
ax2.set_xlim(0, 0.6)
ax2.set_ylim(0, 0.6)
ax2.legend(fontsize=9, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR, loc='lower right')
ax2.tick_params(colors=TEXT_COLOR)
for spine in ax2.spines.values():
    spine.set_color(GRID_COLOR)
ax2.grid(True, alpha=0.2, color=GRID_COLOR)

# --- Plot 3: Cascade Timeline ---
ax3 = fig.add_subplot(gs[1, :])
ax3.set_facecolor(DARK_BG)
time = np.arange(N_STEPS)
ax3.plot(time, avg_ind, color=ACCENT_BLUE, linewidth=2.5, label='Independent (no cascade)')
ax3.plot(time, avg_coup, color=ACCENT_RED, linewidth=2.5, label='Coupled (cascade)')
ax3.plot(time, avg_dk_actual, color=ACCENT_PURPLE, linewidth=2.5, label='DK Actual (cascade + blind)')
ax3.plot(time, avg_dk_perceived, color=ACCENT_ORANGE, linewidth=2.5, linestyle=':',
         label='DK Perceived (what system thinks)')
ax3.axhline(y=THRESHOLD, color=ACCENT_GOLD, linewidth=2, linestyle='--', alpha=0.7, label='Collapse Threshold')
ax3.axvline(x=15, color='white', linewidth=1.5, linestyle=':', alpha=0.4)
ax3.annotate('DAMAGE\nHERE', xy=(15, max(avg_ind)*0.9), fontsize=11, color='white',
            fontweight='bold', ha='center', alpha=0.6)

# Shade the blind spot (gap between DK actual and perceived)
ax3.fill_between(time, avg_dk_actual, avg_dk_perceived,
                  where=avg_dk_perceived > avg_dk_actual,
                  alpha=0.15, color=ACCENT_ORANGE, label='THE BLIND SPOT')

ax3.set_xlabel('Time Steps', color=TEXT_COLOR, fontsize=13)
ax3.set_ylabel('Ψ (Coherence)', color=TEXT_COLOR, fontsize=13)
ax3.set_title('CASCADE COLLAPSE: Three Models After Sudden Damage\n'
              'Orange shading = the gap between reality and self-perception',
              color=TEXT_COLOR, fontsize=15, fontweight='bold')
ax3.legend(fontsize=10, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR, ncol=2)
ax3.tick_params(colors=TEXT_COLOR)
for spine in ax3.spines.values():
    spine.set_color(GRID_COLOR)
ax3.grid(True, alpha=0.2, color=GRID_COLOR)

# --- Plot 4: Blind Spot by Ψ Level ---
ax4 = fig.add_subplot(gs[2, 0])
ax4.set_facecolor(DARK_BG)
ax4.bar(range_labels_bs, range_gaps, color=[ACCENT_RED if g > 0.05 else ACCENT_ORANGE if g > 0 else ACCENT_GREEN for g in range_gaps],
        alpha=0.85, edgecolor='none')
ax4.axhline(y=0, color=ACCENT_GOLD, linewidth=1.5, linestyle='--', alpha=0.7)
ax4.set_xlabel('Actual Ψ Range', color=TEXT_COLOR, fontsize=12)
ax4.set_ylabel('Self-Assessment Error\n(positive = overconfident)', color=TEXT_COLOR, fontsize=12)
ax4.set_title('HOW WRONG IS SELF-ASSESSMENT?\nBy Actual Coherence Level',
              color=TEXT_COLOR, fontsize=14, fontweight='bold')
ax4.tick_params(colors=TEXT_COLOR)
for spine in ax4.spines.values():
    spine.set_color(GRID_COLOR)
ax4.grid(True, alpha=0.2, color=GRID_COLOR, axis='y')

# --- Plot 5: Recovery Comparison ---
ax5 = fig.add_subplot(gs[2, 1])
ax5.set_facecolor(DARK_BG)
strategies = ['External\nGovernance\n(sees reality)', 'DK Self-Repair\n(60% wrong\ndiagnosis)', 'No Awareness\n(thinks it\'s fine)']
recovery_rates_dk = [
    np.mean(smart_recovered)*100,
    np.mean(dk_recovered)*100,
    0
]
colors_rec = [ACCENT_GREEN, ACCENT_ORANGE, ACCENT_RED]
bars = ax5.bar(strategies, recovery_rates_dk, color=colors_rec, alpha=0.85, edgecolor='none', width=0.6)
ax5.set_ylabel('Recovery Rate (%)', color=TEXT_COLOR, fontsize=12)
ax5.set_title('RECOVERY UNDER DUNNING-KRUGER\nCan You Heal What You Can\'t See?',
              color=TEXT_COLOR, fontsize=14, fontweight='bold')
for bar, val in zip(bars, recovery_rates_dk):
    ax5.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
            f'{val:.1f}%', ha='center', va='bottom', color=TEXT_COLOR, fontsize=13, fontweight='bold')
ax5.tick_params(colors=TEXT_COLOR)
for spine in ax5.spines.values():
    spine.set_color(GRID_COLOR)
ax5.grid(True, alpha=0.2, color=GRID_COLOR, axis='y')

# --- Plot 6: The Awareness Curve ---
ax6 = fig.add_subplot(gs[3, 0])
ax6.set_facecolor(DARK_BG)
ax6.plot(psi_levels, assessment_error, color=ACCENT_PURPLE, linewidth=2.5)
ax6.axhline(y=0, color=ACCENT_GOLD, linewidth=2, linestyle='--', label='Perfect Accuracy')
ax6.axvline(x=crossover_psi, color=ACCENT_GREEN, linewidth=2, linestyle=':',
            label=f'Awareness Threshold (Ψ ≈ {crossover_psi:.2f})')
ax6.fill_between(psi_levels, assessment_error, 0,
                  where=np.array(assessment_error) > 0,
                  alpha=0.15, color=ACCENT_RED, label='Overconfident Zone')
ax6.fill_between(psi_levels, assessment_error, 0,
                  where=np.array(assessment_error) < 0,
                  alpha=0.15, color=ACCENT_BLUE, label='Impostor Zone')
ax6.set_xlabel('Actual Ψ Level', color=TEXT_COLOR, fontsize=12)
ax6.set_ylabel('Assessment Error\n(+ = overconfident, - = underconfident)', color=TEXT_COLOR, fontsize=12)
ax6.set_title('THE AWARENESS CURVE\nDunning-Kruger Mapped onto Ψ',
              color=ACCENT_PURPLE, fontsize=14, fontweight='bold')
ax6.legend(fontsize=9, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR)
ax6.tick_params(colors=TEXT_COLOR)
for spine in ax6.spines.values():
    spine.set_color(GRID_COLOR)
ax6.grid(True, alpha=0.2, color=GRID_COLOR)

# --- Plot 7: Summary Panel ---
ax7 = fig.add_subplot(gs[3, 1])
ax7.set_facecolor(DARK_BG)
ax7.axis('off')

med_smart = np.median(smart_arr_dk[smart_recovered]) if np.sum(smart_recovered) > 0 else 0
med_dk = np.median(dk_arr[dk_recovered]) if np.sum(dk_recovered) > 0 else 0

summary = f"""
  DUNNING-KRUGER IN Ψ SYSTEMS
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Coupling increases collapse:
    Independent: {pct_ind:.1f}% collapsed
    Coupled:     {pct_coup:.1f}% collapsed

  The Blind Spot:
    {pct_dk_actual:.1f}% actually collapsed
    {pct_dk_perceived:.1f}% think they're collapsed
    {pct_dk_actual - pct_dk_perceived:.1f}% broken & don't know it

  Recovery with governance:  {med_smart:.0f} steps
  Recovery without (DK):     {med_dk:.0f} steps
  Recovery with no awareness: impossible

  Awareness threshold: Ψ ≈ {crossover_psi:.2f}

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  CONCLUSION:
  Systems below Ψ ≈ {crossover_psi:.2f} cannot
  accurately self-assess.

  External governance isn't a luxury.
  It's a mathematical necessity.

  The Cartographer exists because
  broken systems can't see
  that they're broken.
"""

ax7.text(0.05, 0.95, summary, transform=ax7.transAxes, fontsize=12,
         verticalalignment='top', fontfamily='monospace', color=ACCENT_GOLD,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#0d0d1a', edgecolor=ACCENT_PURPLE, alpha=0.9))

fig.suptitle('THE DUNNING-KRUGER EFFECT IN Ψ SYSTEMS\n'
             'When Collapse Hides Itself From The Collapsing System',
             fontsize=20, fontweight='bold', color=ACCENT_PURPLE, y=0.98)

import os
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', 'psi_dunning_kruger_analysis.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=DARK_BG, edgecolor='none')
print(f"\n  Visualization saved to: {output_path}")
print("  Simulation complete.")
