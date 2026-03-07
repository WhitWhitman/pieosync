# Ψ Monte Carlo Simulations

Reproducible simulations validating the Ψ = 0.05 collapse boundary in the Realima Taxonomy's multiplicative coherence framework.

## Requirements

```
Python 3.8+
numpy
matplotlib
scipy
```

Install:
```bash
pip install numpy matplotlib scipy
```

## The Three Simulations

### 1. `psi_montecarlo.py` — Baseline Collapse Boundary

Generates **1,000,000 random system configurations** (P, E, I, O each sampled uniformly from [0,1]) and analyzes the distribution of Ψ = P × E × I × O.

**Key findings:**
- 64.8% of random configurations fall below Ψ = 0.05
- Only 3.4% achieve healthy coherence (Ψ > 0.30)
- 23.9% of collapsed systems cannot recover by boosting a single dimension
- The 0.05 threshold marks a structural transition, not an arbitrary cutoff

```bash
python psi_montecarlo.py
```

### 2. `psi_asymmetry.py` — Collapse vs Recovery Asymmetry

Tests how fast systems break versus how slowly they heal.

**Key findings:**
- A single-dimension hit can collapse a healthy system in 1 step
- Recovery takes a median of 18 incremental steps (18:1 asymmetry)
- Deeper collapse = harder recovery (gravity well effect)
- Best recovery strategy: fix the weakest dimension first

```bash
python psi_asymmetry.py
```

### 3. `psi_dunning_kruger.py` — Coupled Dimensions + Blind Spot

Extends the model with two real-world effects:
- **Dimensional coupling:** Low Purpose drags down Information; Low Energy degrades Order
- **Dunning-Kruger effect:** Collapsed systems overestimate their own coherence

**Key findings:**
- Coupling increases collapse from 64.7% to 79.1%
- 79% of coupled systems are collapsed; only 0.1% self-report as collapsed
- Self-assessment becomes unreliable below Ψ ≈ 0.40
- External governance is mathematically necessary — broken systems can't see they're broken

```bash
python psi_dunning_kruger.py
```

## Results

Pre-generated visualizations are in `results/`:

- `psi_montecarlo_analysis.png` — Distribution, recovery, dimensional analysis
- `psi_asymmetry_analysis.png` — Collapse speed vs recovery time
- `psi_dunning_kruger_analysis.png` — Blind spot, cascade, awareness threshold

## Reproducing

Every simulation uses `np.random.seed(42)` for reproducibility. Run any script and compare your output to the pre-generated results.

## Citation

If you use these simulations in research, please cite:

```
Whitman, W. (2026). The Realima Taxonomy: A Cross-Substrate Classification
Framework for Coherent Entities (v3.1). https://github.com/WhitWhitman/pieosync
```

## License

CC BY 4.0 — same as the parent repository.
