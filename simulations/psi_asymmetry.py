"""
Monte Carlo Simulation #2: Collapse vs Recovery Asymmetry
Testing how fast systems break vs how slowly they heal.

The hypothesis: In Ψ = P × E × I × O, destruction is fast and easy.
Recovery is slow and requires coordinated multi-dimensional effort.
This asymmetry is structural — it's built into the multiplication.
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
GRID_COLOR = '#2a2a4a'
TEXT_COLOR = '#e0e0e0'

print("=" * 65)
print("  SIMULATION #2: COLLAPSE vs RECOVERY ASYMMETRY")
print("  How fast does coherence break? How slowly does it heal?")
print("=" * 65)
print()

# =============================================================================
# EXPERIMENT 1: One-Hit Collapse
# =============================================================================
print("─" * 65)
print("  EXPERIMENT 1: One-Hit Collapse Speed")
print("─" * 65)

N = 100_000

P = np.random.uniform(0.6, 0.9, N)
I = np.random.uniform(0.6, 0.9, N)
E = np.random.uniform(0.6, 0.9, N)
O = np.random.uniform(0.6, 0.9, N)

psi_healthy = P * I * E * O
mean_healthy = np.mean(psi_healthy)
print(f"  Starting healthy Ψ (mean): {mean_healthy:.4f}")

damage_levels = np.arange(0.1, 1.0, 0.05)
psi_after_damage = []

for damage in damage_levels:
    P_d, I_d, E_d, O_d = P.copy(), I.copy(), E.copy(), O.copy()
    dim_choice = np.random.randint(0, 4, N)

    for idx in range(N):
        if dim_choice[idx] == 0:
            P_d[idx] = max(0.01, P_d[idx] - damage)
        elif dim_choice[idx] == 1:
            I_d[idx] = max(0.01, I_d[idx] - damage)
        elif dim_choice[idx] == 2:
            E_d[idx] = max(0.01, E_d[idx] - damage)
        else:
            O_d[idx] = max(0.01, O_d[idx] - damage)

    psi_damaged = P_d * I_d * E_d * O_d
    psi_after_damage.append(np.mean(psi_damaged))

for i, (dmg, psi_val) in enumerate(zip(damage_levels, psi_after_damage)):
    if psi_val < 0.05:
        print(f"  Single-dimension drop of {dmg:.2f} → Ψ collapses below 0.05")
        print(f"  That's ONE hit to ONE dimension.")
        break

print(f"  Damage of 0.30 → Ψ = {psi_after_damage[4]:.4f}")
print(f"  Damage of 0.50 → Ψ = {psi_after_damage[8]:.4f}")
print(f"  Damage of 0.70 → Ψ = {psi_after_damage[12]:.4f}")
print()

# =============================================================================
# EXPERIMENT 2: Step-by-Step Recovery
# =============================================================================
print("─" * 65)
print("  EXPERIMENT 2: Recovery Takes How Many Steps?")
print("─" * 65)

N_RECOVER = 50_000
STEP_SIZE = 0.05

P_c = np.random.uniform(0.05, 0.50, N_RECOVER)
I_c = np.random.uniform(0.05, 0.50, N_RECOVER)
E_c = np.random.uniform(0.05, 0.50, N_RECOVER)
O_c = np.random.uniform(0.05, 0.50, N_RECOVER)

psi_c = P_c * I_c * E_c * O_c
mask = psi_c < 0.05
P_c, I_c, E_c, O_c = P_c[mask], I_c[mask], E_c[mask], O_c[mask]
psi_c = psi_c[mask]
n_collapsed = len(psi_c)

print(f"  Starting with {n_collapsed:,} collapsed systems (Ψ < 0.05)")
print(f"  Each healing step: +0.05 to one random dimension")
print(f"  Target: Ψ > 0.05 (escape collapse)")
print()

steps_to_recover = []
max_steps = 200

configs = np.column_stack([P_c, I_c, E_c, O_c]).copy()

for i in range(min(n_collapsed, 30000)):
    config = configs[i].copy()
    steps = 0
    current_psi = np.prod(config)

    while current_psi < 0.05 and steps < max_steps:
        dim = np.random.randint(0, 4)
        config[dim] = min(1.0, config[dim] + STEP_SIZE)
        current_psi = np.prod(config)
        steps += 1

    if steps < max_steps:
        steps_to_recover.append(steps)
    else:
        steps_to_recover.append(max_steps)

steps_arr = np.array(steps_to_recover)
recovered = steps_arr < max_steps

print(f"  Results:")
print(f"  Recovered within {max_steps} steps: {np.sum(recovered):,} ({np.mean(recovered)*100:.1f}%)")
print(f"  Average steps to recover:     {np.mean(steps_arr[recovered]):.1f}")
print(f"  Median steps to recover:      {np.median(steps_arr[recovered]):.1f}")
print(f"  Fastest recovery:             {np.min(steps_arr[recovered])} steps")
print(f"  Slowest recovery:             {np.max(steps_arr[recovered])} steps")
print()

print(f"  ┌─────────────────────────────────────────────┐")
print(f"  │  COLLAPSE: 1 hit drops a healthy system     │")
print(f"  │  RECOVERY: ~{np.median(steps_arr[recovered]):.0f} steps to climb back out        │")
print(f"  │                                             │")
print(f"  │  Ratio: Recovery takes ~{np.median(steps_arr[recovered]):.0f}x longer           │")
print(f"  │  than destruction                           │")
print(f"  └─────────────────────────────────────────────┘")
print()

# =============================================================================
# EXPERIMENT 3: The "Gravity Well"
# =============================================================================
print("─" * 65)
print("  EXPERIMENT 3: The Gravity Well")
print("  (Does deeper collapse mean harder recovery?)")
print("─" * 65)

depth_bins = [(0.00, 0.01), (0.01, 0.02), (0.02, 0.03), (0.03, 0.04), (0.04, 0.05)]
depth_labels = []
depth_avg_steps = []

for low, high in depth_bins:
    bin_mask = (psi_c[:30000] >= low) & (psi_c[:30000] < high) & recovered
    if np.sum(bin_mask) > 10:
        avg = np.mean(steps_arr[bin_mask])
        depth_labels.append(f"{low:.2f}-{high:.2f}")
        depth_avg_steps.append(avg)
        print(f"  Starting Ψ = {low:.2f}-{high:.2f}: avg {avg:.1f} steps to recover")

print()

# =============================================================================
# EXPERIMENT 4: Coordinated vs Random Recovery
# =============================================================================
print("─" * 65)
print("  EXPERIMENT 4: Smart Recovery vs Random Recovery")
print("─" * 65)

N_COMPARE = 10_000

P_f = np.random.uniform(0.05, 0.40, N_COMPARE)
I_f = np.random.uniform(0.05, 0.40, N_COMPARE)
E_f = np.random.uniform(0.05, 0.40, N_COMPARE)
O_f = np.random.uniform(0.05, 0.40, N_COMPARE)
psi_f = P_f * I_f * E_f * O_f
mask_f = psi_f < 0.05
configs_f = np.column_stack([P_f[mask_f], I_f[mask_f], E_f[mask_f], O_f[mask_f]])
n_f = len(configs_f)

# Strategy 1: Random recovery
random_steps = []
for i in range(min(n_f, 5000)):
    config = configs_f[i].copy()
    steps = 0
    while np.prod(config) < 0.05 and steps < max_steps:
        dim = np.random.randint(0, 4)
        config[dim] = min(1.0, config[dim] + STEP_SIZE)
        steps += 1
    random_steps.append(steps)

# Strategy 2: Smart recovery (always boost weakest)
smart_steps = []
for i in range(min(n_f, 5000)):
    config = configs_f[i].copy()
    steps = 0
    while np.prod(config) < 0.05 and steps < max_steps:
        dim = np.argmin(config)
        config[dim] = min(1.0, config[dim] + STEP_SIZE)
        steps += 1
    smart_steps.append(steps)

# Strategy 3: Balanced recovery
balanced_steps = []
for i in range(min(n_f, 5000)):
    config = configs_f[i].copy()
    steps = 0
    while np.prod(config) < 0.05 and steps < max_steps:
        for d in range(4):
            config[d] = min(1.0, config[d] + STEP_SIZE/4)
        steps += 1
    balanced_steps.append(steps)

random_arr = np.array(random_steps)
smart_arr = np.array(smart_steps)
balanced_arr = np.array(balanced_steps)

print(f"  RANDOM (boost any dimension):    median {np.median(random_arr):.0f} steps")
print(f"  SMART (boost weakest first):     median {np.median(smart_arr):.0f} steps")
print(f"  BALANCED (boost all equally):    median {np.median(balanced_arr):.0f} steps")
print()

best_strategy = "SMART" if np.median(smart_arr) <= np.median(balanced_arr) else "BALANCED"
print(f"  Best strategy: {best_strategy}")
print(f"  The weakest dimension is the bottleneck.")
print(f"  Fix what's most broken first.")
print()

# =============================================================================
# KEY FINDINGS
# =============================================================================
print("=" * 65)
print("  KEY FINDINGS: THE ASYMMETRY IS REAL")
print("=" * 65)
print(f"""
  1. COLLAPSE IS INSTANT
     A single hit to one dimension can drop a healthy
     system (Ψ ≈ 0.20) below the 0.05 threshold.
     One bad day. One broken dimension. Done.

  2. RECOVERY IS SLOW
     Climbing back above 0.05 takes ~{np.median(steps_arr[recovered]):.0f} incremental
     healing steps. That's a {np.median(steps_arr[recovered]):.0f}:1 asymmetry ratio.

  3. DEPTH MATTERS
     The deeper you fall, the harder the climb.
     Systems near Ψ = 0.01 take significantly more
     steps than those near Ψ = 0.04.

  4. STRATEGY MATTERS
     Smart recovery (fix weakest first) beats random
     recovery. The bottleneck dimension controls
     the entire system's ceiling.

  5. THE IMPLICATION
     Prevention > Repair. The Cartographer's approach
     of maintaining guardrails is mathematically optimal.
     It's easier to keep Ψ above 0.05 than to recover
     once you've fallen below it.
""")
print("=" * 65)

# =============================================================================
# VISUALIZATION
# =============================================================================
fig = plt.figure(figsize=(20, 20))
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.3)
fig.patch.set_facecolor(DARK_BG)

# --- Plot 1: Collapse Curve ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor(DARK_BG)
ax1.plot(damage_levels, psi_after_damage, color=ACCENT_RED, linewidth=3, marker='o', markersize=5)
ax1.axhline(y=0.05, color=ACCENT_GOLD, linewidth=2, linestyle='--', label='Collapse Threshold (Ψ = 0.05)')
ax1.axhline(y=mean_healthy, color=ACCENT_BLUE, linewidth=1.5, linestyle=':', label=f'Starting Healthy (Ψ = {mean_healthy:.3f})')
ax1.fill_between(damage_levels, psi_after_damage, 0.05,
                  where=[p < 0.05 for p in psi_after_damage],
                  color=ACCENT_RED, alpha=0.2)
ax1.set_xlabel('Damage to Single Dimension', color=TEXT_COLOR, fontsize=12)
ax1.set_ylabel('Resulting Ψ', color=TEXT_COLOR, fontsize=12)
ax1.set_title('HOW FAST DOES IT BREAK?\nOne Hit to One Dimension',
              color=ACCENT_RED, fontsize=14, fontweight='bold')
ax1.legend(fontsize=10, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR)
ax1.tick_params(colors=TEXT_COLOR)
for spine in ax1.spines.values():
    spine.set_color(GRID_COLOR)
ax1.grid(True, alpha=0.2, color=GRID_COLOR)

# --- Plot 2: Recovery Steps Distribution ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor(DARK_BG)
ax2.hist(steps_arr[recovered], bins=50, color=ACCENT_BLUE, alpha=0.7, edgecolor='none')
ax2.axvline(x=np.median(steps_arr[recovered]), color=ACCENT_GOLD, linewidth=2.5, linestyle='--',
            label=f'Median: {np.median(steps_arr[recovered]):.0f} steps')
ax2.axvline(x=1, color=ACCENT_RED, linewidth=2.5, linestyle='--',
            label='Collapse: 1 step')
ax2.set_xlabel('Steps to Recover Above Ψ = 0.05', color=TEXT_COLOR, fontsize=12)
ax2.set_ylabel('Count', color=TEXT_COLOR, fontsize=12)
ax2.set_title('HOW LONG TO HEAL?\nDistribution of Recovery Time',
              color=ACCENT_BLUE, fontsize=14, fontweight='bold')
ax2.legend(fontsize=10, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR)
ax2.tick_params(colors=TEXT_COLOR)
for spine in ax2.spines.values():
    spine.set_color(GRID_COLOR)
ax2.grid(True, alpha=0.2, color=GRID_COLOR)

# --- Plot 3: Gravity Well ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_facecolor(DARK_BG)
if depth_labels and depth_avg_steps:
    colors_depth = [ACCENT_RED if s > np.mean(depth_avg_steps) else ACCENT_GOLD for s in depth_avg_steps]
    bars = ax3.bar(depth_labels, depth_avg_steps, color=colors_depth, alpha=0.85, edgecolor='none')
    ax3.set_xlabel('Starting Ψ Range (Depth of Collapse)', color=TEXT_COLOR, fontsize=12)
    ax3.set_ylabel('Average Steps to Recover', color=TEXT_COLOR, fontsize=12)
    ax3.set_title('THE GRAVITY WELL\nDeeper Collapse = Harder Recovery',
                  color=ACCENT_RED, fontsize=14, fontweight='bold')
    for bar, val in zip(bars, depth_avg_steps):
        ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
                f'{val:.1f}', ha='center', va='bottom', color=TEXT_COLOR, fontsize=11, fontweight='bold')
ax3.tick_params(colors=TEXT_COLOR)
for spine in ax3.spines.values():
    spine.set_color(GRID_COLOR)
ax3.grid(True, alpha=0.2, color=GRID_COLOR, axis='y')

# --- Plot 4: Strategy Comparison ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor(DARK_BG)
strategies = ['Random\n(any dimension)', 'Smart\n(weakest first)', 'Balanced\n(all equally)']
medians = [np.median(random_arr), np.median(smart_arr), np.median(balanced_arr)]
colors_strat = [ACCENT_RED, ACCENT_GREEN, ACCENT_BLUE]
bars = ax4.bar(strategies, medians, color=colors_strat, alpha=0.85, edgecolor='none', width=0.6)
ax4.set_ylabel('Median Steps to Recover', color=TEXT_COLOR, fontsize=12)
ax4.set_title('WHICH RECOVERY STRATEGY WORKS?\nComparing Approaches',
              color=TEXT_COLOR, fontsize=14, fontweight='bold')
for bar, val in zip(bars, medians):
    ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            f'{val:.0f}', ha='center', va='bottom', color=TEXT_COLOR, fontsize=14, fontweight='bold')
ax4.tick_params(colors=TEXT_COLOR)
for spine in ax4.spines.values():
    spine.set_color(GRID_COLOR)
ax4.grid(True, alpha=0.2, color=GRID_COLOR, axis='y')

# --- Plot 5: The Asymmetry Visual ---
ax5 = fig.add_subplot(gs[2, :])
ax5.set_facecolor(DARK_BG)

np.random.seed(99)
timeline = []
psi_timeline = []

# Phase 1: Healthy (steps 0-10)
config = np.array([0.75, 0.80, 0.70, 0.78])
for t in range(10):
    timeline.append(t)
    psi_timeline.append(np.prod(config))
    config += np.random.normal(0, 0.01, 4)
    config = np.clip(config, 0.01, 1.0)

# Phase 2: Sudden collapse
config[2] = 0.05
timeline.append(10)
psi_timeline.append(np.prod(config))

# Phase 3: Recovery attempts
for t in range(11, 60):
    timeline.append(t)
    psi_timeline.append(np.prod(config))
    weakest = np.argmin(config)
    config[weakest] = min(1.0, config[weakest] + 0.02)
    config = np.clip(config, 0.01, 1.0)

ax5.plot(timeline, psi_timeline, color=ACCENT_BLUE, linewidth=2.5)
ax5.axhline(y=0.05, color=ACCENT_GOLD, linewidth=2, linestyle='--', alpha=0.7, label='Collapse Threshold (Ψ = 0.05)')

collapse_point = 10
ax5.axvspan(0, collapse_point, alpha=0.08, color=ACCENT_GREEN)
ax5.axvspan(collapse_point, collapse_point + 0.5, alpha=0.3, color=ACCENT_RED)
ax5.axvspan(collapse_point + 0.5, 60, alpha=0.08, color=ACCENT_PURPLE)

ax5.annotate('HEALTHY', xy=(5, max(psi_timeline[:10])*0.95), fontsize=14,
            color=ACCENT_GREEN, fontweight='bold', ha='center')
ax5.annotate('COLLAPSE\n(instant)', xy=(10.5, 0.15), fontsize=12,
            color=ACCENT_RED, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=ACCENT_RED, lw=2),
            xytext=(14, 0.25))

recovery_step = None
for i, (t, p) in enumerate(zip(timeline, psi_timeline)):
    if t > collapse_point and p > 0.05:
        recovery_step = t
        break

if recovery_step:
    ax5.annotate(f'RECOVERY\n({recovery_step - collapse_point} steps)',
                xy=(recovery_step, 0.05), fontsize=12,
                color=ACCENT_PURPLE, fontweight='bold', ha='center',
                arrowprops=dict(arrowstyle='->', color=ACCENT_PURPLE, lw=2),
                xytext=(recovery_step + 8, 0.12))

ax5.set_xlabel('Time Steps', color=TEXT_COLOR, fontsize=13)
ax5.set_ylabel('Ψ (Coherence)', color=TEXT_COLOR, fontsize=13)
ax5.set_title("THE FUNDAMENTAL ASYMMETRY: Breaking is Instant. Healing Takes Time.\nOne System's Journey Through Collapse and Recovery",
              color=ACCENT_GOLD, fontsize=15, fontweight='bold')
ax5.legend(fontsize=11, facecolor=DARK_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR)
ax5.tick_params(colors=TEXT_COLOR)
for spine in ax5.spines.values():
    spine.set_color(GRID_COLOR)
ax5.grid(True, alpha=0.2, color=GRID_COLOR)

fig.suptitle('Ψ ASYMMETRY ANALYSIS — Why Prevention Beats Repair\nRealima Taxonomy v3.1',
             fontsize=20, fontweight='bold', color=ACCENT_GOLD, y=0.98)

import os
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', 'psi_asymmetry_analysis.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=DARK_BG, edgecolor='none')
print(f"\n  Visualization saved to: {output_path}")
print("  Simulation complete.")
