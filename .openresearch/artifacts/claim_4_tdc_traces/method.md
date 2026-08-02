# Method

The cumulative command reruns the frozen historical toy suite, then constructs a 20-state, two-action, ten-feature finite MDP with action-dependent transitions, distinct behavior and target policies, nontrivial importance ratios, and no projection or clipping.

For each lambda in 0, 0.25, 0.55, and 0.85, an independent checker forms the behavior stationary distribution and evaluates the paper's closed forms

`A = Phi^T D_mu (P_(pi,lambda)-I) Phi` and `b = Phi^T D_mu r_(pi,lambda)`.

Four deterministic 240,000-step paths execute Definition 7.1. The sampled trace moments are compared with the analytic A, b, C, and D matrices. Lambda zero is a control and never counts as eligibility-trace evidence. Other controls violate F.2, F.1, and B.2 separately. `reproduction/verify.py` raises on any failed gate; the runner also injects a false invertibility certificate and requires rejection.

Compute estimate: one core because the implementation is single-process; selected hardware: Hugging Face `cpu-upgrade` (8-vCPU advertised flavor, 32 GB). Actual CPU affinity and runtime are read inside the job and printed in the evidence payload.
