# Claim 4 — Theorem 7.2 exact TDC(λ)

## Exact claim

With Appendix F and inherited Appendix B premises, the exact unprojected Definition 7.1 TDC algorithm with eligibility traces converges almost surely under off-policy Markovian sampling. The paper also describes this as the first such result. The claim therefore combines a mathematical almost-sure quantifier and a literature-priority quantifier.

Source: Definition 7.1 `#S7.Thmtheorem1`, Theorem 7.2 `#S7.Thmtheorem2`, Appendix F; arXiv source SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`.

## Exact algorithm and assumptions

The runner implements `e_t = λγρ_{t−1}e_{t−1}+φ_t`, the TD error, the fast ν update, and the slow gradient-correction θ update exactly as Definition 7.1, with no projection or clipping. The independent analytic system derives A, b, C, D and `θ* = −A⁻¹b` from the finite MDP. Checks cover finite irreducible behavior chain, full policy support, full-rank features, A invertibility, separated rates, and A+C−D.

## Raw observed evidence

- Moderate design: 20 states, 10 features, four seeds, 240k steps at λ=.25/.55/.85. Mean residual ratios were .4702, .4599, and .3149; maximum trace norms 1.146, 2.156, and 6.596.
- Stress design: λ=.90/.97, four seeds, 160k steps, max importance ratio 5.022. Residual ratios were .3429, .3676, .2363, and .2637; trace maxima 2,821, 5,898, 6,239, and 12,723.
- Sample A/b error grows under heavy traces (up to .637/.392), an explicitly reported finite-sampling limitation rather than hidden disagreement.
- λ=0-only, rank-deficient, reducible-chain, equal-timescale, and projected variants were rejected. The unstable control was also rejected for violating B.6.

Download [moderate TDC raw JSON](../../raw/claim-4-tdc.json), [high-ratio TDC raw JSON](../../raw/falsification-route.json), and [proof/priority source audit](../../raw/proof-route.json).

## Primary-source comparison

Yu (2017), arXiv:1712.09652v2, was independently hash-pinned to `fa48127d46d01abfc81bf2e737815f9afed5cdae63f5de37993d722c7c002acd`. Its source identifies TDC as GTDb, treats two-timescale GTDb with constraints, and reserves its unconstrained result for single-timescale GTDa. This supports the paper's comparison but is not an exhaustive search over all literature.

## Code, checker, and reproducibility

[runner.py](../../current/runner.py), [verify.py](../../current/verify.py), fixed command `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`, Python 3.12 [uv.lock](../../current/uv.lock), Git SHA `7f24f1dce0b64a254d51e483a4b3f581f4610a6a`. Seeds 3101–3104 and 7301–7302. HF `cpu-upgrade`, cumulative runtime 652.200 s, no GPU. [Checker output](../../checker/independent-checker.json).

## Limitations and verdict

These runs finally test genuine eligibility traces and the named unprojected algorithm, but finite residual reduction cannot prove almost-sure convergence, and two sources cannot establish a global priority claim.

**Verdict: BLOCKED. Confidence: LOW.**
