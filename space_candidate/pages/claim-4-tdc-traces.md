# Claim 4 — TDC with eligibility traces

**Current theorem verdict: BLOCKED after four routes.** This route completed successfully as faithful finite evidence. The prior lambda-zero result is preserved below as a **Historical rejected baseline**; it is not the current verifier and earns no eligibility-trace credit.

The exact source claim is almost-sure convergence of the unprojected off-policy, Markov-sampled TDC(lambda) recurrences in Definition 7.1 under Appendix F and the invoked Appendix B assumptions. The historical priority phrase “first proof” is audited separately from convergence.

## Current verifier

- Algorithm: `reproduction/runner.py`
- Independent checker: `reproduction/verify.py`
- Claim contract: `.openresearch/artifacts/claim_4_tdc_traces/claim_contract.json`
- Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`
- Environment: Python 3.12 with repository `uv.lock`
- Compute: Hugging Face `cpu-upgrade`; estimated one required core; no GPU permitted

This verifier executed lambda 0.25, 0.55, and 0.85, four seeds each, on a 20-state/two-action/ten-feature action-dependent MDP without projection. It compared sampled trace moments and residuals against an independently derived analytic finite-MDP system. Mean residual ratios were .4702, .4599, and .3149; maximum trace norms were 1.146, 2.156, and 6.596. See [the canonical Claim 4 page](#/current-claim-4).

## Historical rejected baseline

Run `5b87e9c4-68a4-4691-97ed-fb7046375494` at Git `381bc33d2e04aec9314fae159c6680ee44ef407b` used only lambda zero on five states and three features. Across seeds 0-4, the median residual-reduction ratio was 0.212453 and median parameter error was 0.425524 after 45,000 steps. Lambda zero makes `e_t = phi_t`, eliminating eligibility accumulation. Raw JSON: `.openresearch/artifacts/claim_4_tdc_traces/historical_rejected_raw.json`.

## Limitation

Even successful finite paths are scoped corroboration, not a proof of an almost-sure theorem. The theorem-level result remains BLOCKED unless the separate symbolic-proof route succeeds; an assumption-satisfying counterexample would instead be FALSIFIED.
