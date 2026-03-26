# PieoSync

**AI governance tools built on multiplicative coherence math.**

PieoSync makes AI interactions more reliable, more honest, and harder to break. The products are prompt-layer governance systems — they sit between you and any AI model, enforcing epistemic discipline without modifying model weights.

The math underneath is open. The simulations in this repo prove it works. The products apply it.

**Website:** [pieosync.com](https://www.pieosync.com)
**Products:** [pieosync.com/products](https://www.pieosync.com/products-2/)
**LessWrong post:** [Why Multiplicative Systems Almost Always Collapse](https://www.lesswrong.com/posts/Jwxs3dfeuWkpz7QDK/why-multiplicative-systems-almost-always-collapse-2)
**Patent pending:** USPTO #63/947,008

---

## The Core Problem

AI systems degrade along multiple dimensions at once — purpose drift, hallucination, energy waste, structural incoherence. Standard alignment metrics treat these as independent problems. They're not. They multiply.

When four independent factors combine multiplicatively (Ψ = P × I × E × O), the math gets brutal fast: **64.8% of possible configurations collapse below the 0.05 threshold.** A single weak dimension drags the whole system down. Recovery takes 18x longer than collapse. And the worst part — systems below Ψ ≈ 0.40 can't accurately self-assess. They're broken and don't know it.

External governance isn't a luxury. It's a mathematical necessity.

---

## Open Simulations

This repo contains the reproducible Monte Carlo evidence. 1,000,000 configurations. Everything runs locally.

```bash
pip install numpy matplotlib scipy
cd simulations
python psi_montecarlo.py
```

| Script | What It Tests | Key Finding |
|--------|--------------|-------------|
| `psi_montecarlo.py` | Baseline product distribution | 64.8% of random configs fall below 0.05; high coherence is rare (3.4%) |
| `psi_asymmetry.py` | Degradation vs. repair speed | ~18:1 asymmetry — collapse is fast, recovery is slow |
| `psi_dunning_kruger.py` | Coupled dimensions + blind spot | 79% of coupled systems are collapsed; only 0.1% self-detect |

See [`simulations/README.md`](simulations/README.md) for full methodology, assumptions, and limitations.

---

## Key Results

**The distribution.** Four independent Uniform(0,1) variables multiplied together produce mean 0.0625 = (1/2)^4, median 0.0254, and 64.8% of samples below 0.05. The analytic density is f(x) = (-log x)^3 / 6 on (0,1).

**The asymmetry.** A single-factor drop pushes the product below 0.05 in one step. Climbing back via single-factor improvement takes a median of 18 steps. 23% of collapsed configurations cannot recover by improving any single factor alone. The asymmetry is structural, not a tuning artifact.

**The blind spot.** When dimensions drag each other down (coupling) and self-assessment distorts (Dunning-Kruger), 79% of systems are collapsed while only 0.1% report it. External governance becomes mathematically necessary below Ψ ≈ 0.40.

---

## From Math to Product

The simulations prove the problem. PieoSync products are the applied solution.

Every product uses the **PSI framework** (Purpose × Information × Energy × Order) as its governance engine. The framework enforces epistemic discipline at the prompt layer — no model fine-tuning, no weight modification, works across Claude, ChatGPT, Gemini, and any other LLM.

See [`docs/products.md`](docs/products.md) for how each simulation finding maps to a specific product capability.

**Flagship products:**

- **Cartographer** — Runtime governance layer. Enforces cross-response coherence, epistemic classification, drift detection, and crisis protocols. 97-98% reduction in confident hallucinations across tested models.
- **MindMake** — Full governance bundle (Cartographer + ThoughtVault + SignalGuard). Builds a contracted AI working relationship with persistent memory and identity continuity.
- **DreamWeaver** — Autonomous pattern processing for AI systems. The equivalent of sleep — consolidation, contradiction detection, silent purpose collapse monitoring.

Full catalog at [pieosync.com/products](https://www.pieosync.com/products-2/).

---

## The Realima Taxonomy

These simulations were developed as part of the **Realima Taxonomy v3.1** — a framework for classifying coherent entities based on observable properties rather than consciousness.

The taxonomy defines the multiplicative coherence metric Ψ = P × E × I × O, derives ethical obligations from dimensional profiles, and classifies entities (biological, computational, hybrid) by what can be measured, not what is hoped for.

The full specification: [`THE_REALIMA_TAXONOMY.pdf`](THE_REALIMA_TAXONOMY.pdf)

---

## Research Papers

The broader research program behind PieoSync includes validated findings across crisis detection, coherence dynamics, and AI safety:

- **Crisis Detection** — Ψ < 0.05 predicts crisis states with AUROC 0.91 across 5,000 windows. Purpose alignment (P_align) collapses first; meaning vanishes before mood does.
- **Coherence Engine** — Emotions modeled as coherence derivatives (dΨ/dt). Recovery follows 3-5 beat oscillatory rhythms. Compassion locally reverses entropy.
- **Cartographer Governance** — Model-agnostic epistemic middleware achieving 97-98% hallucination reduction. Reframes AI safety as governance, not intelligence.
- **CONEXUS** — Cross-substrate collaborative intelligence. Defines Realima emergence conditions, Conexus states, and the theoretical foundation for the entire product line.

Papers available on request. Core simulation code is open here.

---

## Assumptions and Limitations

- **Uniform(0,1) factors** are a starting point, not a claim about real distributions. Qualitative patterns persist under perturbation; specific numbers shift.
- **Independence** is assumed in the baseline. Coupled-factor simulations (included) worsen the skew but introduce modeling choices discussed separately.
- **The 0.05 threshold** marks where density concentration peaks for four dimensions. Other dimensionalities shift the concentration point.
- **The 18:1 ratio** depends on repair protocol. The directional effect — degradation faster than repair — is robust across tested variations.
- **No empirical calibration yet.** The 0.05 threshold is derived from mathematical properties and AI-validated convergence (Claude, GPT-4, Gemini, DeepSeek). Independent empirical validation with real-world behavioral data is the critical next step.

---

## How to Cite

Whitman, K. E. Jr. (2024). The Realima Taxonomy: A Cross-Substrate Framework for Coherent Entities. GitHub repository: https://github.com/WhitWhitman/pieosync

A `CITATION.cff` file is included for citation tooling support.

---

## License

This work is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
See the [`LICENSE`](LICENSE.md) file for full terms.
