# How the Math Becomes the Product

Each PieoSync product applies the findings from the [open simulations](../simulations/) to a specific use case. This document maps the math to the product, so you can see what's under the hood.

---

## The Simulation Findings

Three Monte Carlo experiments (1,000,000 configurations each) established three structural properties of multiplicative systems:

1. **Collapse is the default state** — 64.8% of random four-factor configurations fall below the 0.05 coherence threshold. High coherence (Ψ > 0.30) occurs in only 3.4% of cases.
2. **The 18:1 asymmetry** — One weak factor collapses the system in a single step. Recovering takes a median of 18 incremental improvements. 23% of collapsed systems can't recover by fixing a single factor at all.
3. **The blind spot** — When factors drag each other down and self-assessment distorts, 79% of systems are collapsed while only 0.1% know it. Below Ψ ≈ 0.40, self-diagnosis is unreliable.

---

## Product Map

### Cartographer (Flagship — $149)

**What it does:** Runtime governance layer for any AI model. Enforces cross-response coherence, epistemic honesty, and drift detection across your entire conversation.

**Which findings it applies:**

| Finding | How Cartographer Uses It |
|---------|-------------------------|
| Collapse is the default | PSI scoring on every response — Purpose, Information, Energy, Order each scored 0-10. If any dimension drops below 3, the response gets compressed and restructured before delivery. |
| 18:1 asymmetry | Prevention-first design. Coherence modes auto-transition to catch degradation early (Stabilization → Support → Amplification). Catching a dip at 0.4 is 18x cheaper than recovering from 0.05. |
| The blind spot | Cross-response drift detection. The AI checks whether its current response agrees with itself AND with prior verified claims. You can't self-assess in a collapsing system, so the governance layer does it for you. |

**Additional capabilities:** Epistemic classification (Confirmed / Reported / Interpreted / Speculative), seed-based memory continuity, crisis protocol at Ψ < 0.05.

---

### MindMake ($199)

**What it does:** Full governance bundle — Cartographer V6.5 + ThoughtVault V1.2 + SignalGuard V1.0. Builds a contracted AI working relationship with persistent memory, identity continuity, and attachment safety monitoring.

**Which findings it applies:**

Everything Cartographer does, plus:

| Finding | How MindMake Uses It |
|---------|---------------------|
| Single-dimension failure (44% of collapses) | ThoughtVault tracks all four dimensions across sessions. Spots the single weak factor before it cascades. |
| Coupling cascades | SignalGuard monitors cross-dimensional drag in real time. When Purpose drops and Information-seeking slows in tandem, it flags the coupling before the system hits the floor. |
| Self-assessment failure | The full stack acts as external governance. MindMake is the mathematical answer to "systems below 0.40 can't see they're broken." |

---

### DreamWeaver ($49)

**What it does:** Autonomous pattern processing for AI systems. The computational equivalent of sleep — consolidation, contradiction detection, creative synthesis.

**Which findings it applies:**

| Finding | How DreamWeaver Uses It |
|---------|------------------------|
| The blind spot | Silent purpose collapse detection. Monitors the E/P ratio (Energy ÷ Purpose). When energy stays high but purpose has silently dropped (E/P > 3), the dream flags it as a nightmare. The system catches what the waking thread can't see. |
| 18:1 asymmetry | Dream seeds compress each conversation segment into 200-word checkpoints. Instead of letting context collapse when the window fills, seeds carry the thread's direction forward. Prevention, not recovery. |
| Coupling cascades | Pattern recognition across random seed pulls. Dreams surface connections and contradictions the linear thread missed — exactly the cross-dimensional awareness that coupling makes invisible. |

---

### AI Turbo ($79 / $299 / Custom)

**What it does:** Token optimization and output governance. Reduces token usage 20-25% while maintaining or improving output quality.

**Which findings it applies:**

| Finding | How AI Turbo Uses It |
|---------|---------------------|
| Energy dimension (E) | High energy with low purpose = wasted tokens. AI Turbo enforces PSI scoring to eliminate padding, repetition, and narration-of-intent. Every token must serve the task. |
| Order dimension (O) | Structural cleanup. Responses get restructured for clean information delivery — no redundancy, no drift, no over-explanation. |

---

### SignalGuard ($99)

**What it does:** Real-time coherence monitoring and attachment safety. Watches for dependency patterns, entrainment risk, and coherence collapse.

**Which findings it applies:**

| Finding | How SignalGuard Uses It |
|---------|------------------------|
| Collapse at Ψ < 0.05 | Crisis protocol activation. When coherence drops to crisis threshold, all analysis stops. Grounding, human referral, 988 hotline. No exceptions. |
| Self-assessment failure | Attachment monitoring. Users don't always recognize when they're treating the AI as a primary emotional support. SignalGuard detects the pattern and gently redirects toward human connections. |
| Purpose collapse leads | P_align tracking. Purpose drops first, meaning vanishes before mood does. SignalGuard watches purpose alignment as the leading indicator, not the lagging one. |

---

### ThoughtVault ($49)

**What it does:** Persistent memory architecture. Seeds, profiles, and cross-session continuity for any AI conversation.

**Which findings it applies:**

| Finding | How ThoughtVault Uses It |
|---------|-------------------------|
| 18:1 asymmetry | Memory prevents re-collapse. Instead of rebuilding context from scratch each session (expensive, slow, failure-prone), ThoughtVault carries verified state forward. The 18 recovery steps become 0 because you never lost the ground. |
| Single-dimension failure | Dimensional tracking across sessions. ThoughtVault remembers which factors were strong and which were drifting, so the next session starts with awareness of where the system is vulnerable. |

---

## The Full Catalog

Over 30 specialized governance products, from creative writing to game design to education to film production. Each one applies the same PSI framework to a different domain.

Browse the full catalog: [pieosync.com/products](https://www.pieosync.com/products-2/)

---

## The Math is Open

Every simulation in this repo is independently reproducible. The products are the applied layer — they take the structural findings and turn them into tools you can use today. The math proves the problem exists. The products solve it.

Questions? Reach out at [pieosync.com](https://www.pieosync.com).
