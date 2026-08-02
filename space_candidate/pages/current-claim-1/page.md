# Claim 1 — Theorem 3.2 stability

## Exact claim

Under the Appendix B assumptions, the unprojected two-timescale iterates satisfy `sup_n ||z_n|| < ∞` almost surely. The domain is the general Markovian stochastic-approximation recursion, and the quantifiers cover every iterate on almost every eligible sample path—not one finite design.

Source: arXiv:2605.31172v1, Theorem 3.2, HTML anchor `#S3.Thmtheorem2`; registered source SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`.

## Assumptions and methods

The numerical families check a unique stationary finite Markov chain, Robbins–Monro rates with β/α→0, exact infinity scaling, global Lipschitzness, globally stable fast and reduced-slow ODEs, and bounded-chain weighted LLN. No path uses projection or clipping.

Four routes were completed: historical d=3 paths; nonlinear dimensions 8/32/64 across three mixing regimes; a hash-pinned proof-dependency reconstruction; and an adversarial nonnormal falsification search with twelve 150k cells plus two new-seed 400k holdouts.

## Raw observed evidence

- Nonlinear grid: 18/18 assumption audits passed; maximum norm 129.514 and maximum growth 1.0.
- Falsification grid: the worst transient reached norm 2,502,590, or 31,813.83× its initial norm, while retaining the encoded sufficient assumptions.
- Promoted holdouts: shear 5, stickiness .96, seeds 8101/8102. Growth was 86.39×/60.56×; joint-norm tail slopes were −.337/−.343 by 400k steps.
- The unstable-fast-ODE detector grew by 4,684,032×, triggered, and was rejected because B.6 was violated.

Download [nonlinear raw JSON](../../raw/claims-1-2-3-nonlinear.json), [complete falsification raw JSON](../../raw/falsification-route.json), and [run metadata](../../raw/run-metadata.json).

## Code, checker, and reproducibility

Current code: [runner.py](../../current/runner.py); independent fail-closed checker: [verify.py](../../current/verify.py). Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: Python 3.12 [uv.lock](../../current/uv.lock). Evidence SHA: `7f24f1dce0b64a254d51e483a4b3f581f4610a6a`. Seeds: 4101–4102, 7001–7002, 8101–8102. HF `cpu-upgrade`; final cumulative runtime 652.200 s; zero GPU devices. [Checker output](../../checker/independent-checker.json).

## Limitations and verdict

Negative tail slopes after a severe transient are substantial corroboration, not a proof of an infinite supremum on almost every path. The source dependency graph is not kernel-checked, and no valid assumption-satisfying counterexample was established.

**Verdict: BLOCKED. Confidence: LOW.** Unblocks with a machine-checkable general proof, complete independent symbolic derivation, exhaustive verification over a matching finite domain, or a valid counterexample.
