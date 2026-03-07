# PieoSync

Reproducible simulations exploring the distributional properties of products of uniform random variables — and why multiplicative systems are structurally biased toward low product values.

**LessWrong post:** [Why Multiplicative Systems Almost Always Collapse](https://www.lesswrong.com/posts/Jwxs3dfeuWkpz7QDK/why-multiplicative-systems-almost-always-collapse-2)

---

## Quick Start

```bash
pip install numpy matplotlib scipy
cd simulations
python psi_montecarlo.py
```

Each script outputs to terminal and generates plots. No external dependencies beyond numpy/matplotlib/scipy.

---

## Simulations

The `simulations/` directory contains Monte Carlo experiments (1,000,000 configurations) validating the product distribution and exploring degradation/repair dynamics.

| Script | What It Tests | Key Finding |
|--------|--------------|-------------|
| `psi_montecarlo.py` | Baseline product distribution | 64.8% of random configs fall below 0.05; high product value is rare (3.4%) |
| `psi_asymmetry.py` | Degradation vs. repair speed | ~18:1 asymmetry — breaking is fast, repair is slow |
| `psi_dunning_kruger.py` | Coupled dimensions + blind spot | 79% of coupled systems are low-product; only 0.1% self-detect |

See [`simulations/README.md`](simulations/README.md) for full details, assumptions, and instructions.

---

## Key Results

**The distribution.** Four independent Uniform(0,1) variables multiplied together produce a distribution with mean 0.0625 = (1/2)^4, median 0.0254, and 64.8% of samples below 0.05. The analytic density is f(x) = (-log x)^3 / 6 on (0,1).

**The asymmetry.** In a simple degradation-and-repair simulation, a single-factor drop can push the product below 0.05 in one step. Climbing back out via single-factor improvement takes a median of 18 steps. 23% of low-product configurations cannot recover by improving any single factor alone. The qualitative asymmetry is structural; the exact ratio is protocol-dependent.

**The pattern.** Among low-product configurations, the most common cause (44%) is a single weak factor dragging down an otherwise adequate product. In 7% of cases, no factor is individually weak — they’re all in the 0.3–0.5 range — but the product is still below 0.05.

---

## Assumptions and Limitations

- **Uniform(0,1) factors** are a starting point, not a claim about real distributions. The qualitative shape survives perturbation to other distributions on [0,1], but specific numbers would change.
- **Independence** is assumed. Coupled-factor simulations (included in the repo) make the skew worse, but introduce modeling choices discussed separately.
- **The 0.05 threshold** is where density concentration is sharpest for four dimensions. For other dimensionalities, the concentration point shifts.
- **The 18:1 ratio** depends on the repair protocol (increment size, single-factor constraint, starting distribution). The directional effect — degradation faster than repair — is robust across variations tested.

---

## Broader Context: The Realima Taxonomy

These simulations were developed as part of a broader research program called the **Realima Taxonomy** — a framework for classifying coherent entities based on observable properties rather than consciousness.

The taxonomy defines a multiplicative coherence metric Ψ = P × E × I × O (Purpose × Energy × Information × Order), where the distributional properties explored in these simulations have direct implications for system stability and ethical classification.

The full specification is available in [`THE_REALIMA_TAXONOMY.pdf`](THE_REALIMA_TAXONOMY.pdf) and the [`docs/`](docs/) directory.

**Patent pending:** USPTO #63/947,008

---

## How to Cite

Whitman, K. E. Jr. (2024). The Realima Taxonomy: A Cross-Substrate Framework for Coherent Entities. GitHub repository: https://github.com/WhitWhitman/pieosync

A `CITATION.cff` file is included for citation tooling support.

---

## License

This work is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
See the [`LICENSE`](LICENSE) file for full terms.
