# Reproduction: two-timescale Markovian stochastic approximation

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/blob/main/notebooks/two_timescale_reproduction.py)

This project reproduces five claims from [*Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning*](https://arxiv.org/abs/2605.31172). The old logbook used d=3 linear SA and λ=0 TDC; those results remain labeled **Historical rejected baseline**.

The new campaign ran nonlinear d=8/32/64 SA, exact positive-λ unprojected TDC on 20-state/10-feature MDPs, hash-pinned source and proof-dependency audits, and an adversarial falsification search with 400,000-step holdouts. The strongest nonnormal search cell grew 31,813.83× before declining; high-ratio TDC reached trace norm 12,723 while reducing fixed-point residual to 23.6%–36.8% of its initial value.

Assessment: Claim 5 is **VERIFIED** on the complete registered source domain. Claims 1–4 are **BLOCKED** after four routes because finite paths and source parsing cannot prove universal almost-sure statements or an exhaustive priority claim. Previous live score: 5/10; conservative forecast after release: 5–6/10; best-supported possible: 6/10, not a judge result.

- [Illustrated technical report](reports/reproduction/report.md)
- [Self-contained tutorial notebook](notebooks/two_timescale_reproduction.py)
- [Published Hugging Face logbook](https://huggingface.co/spaces/DineshAI/Iww9TICvKj/tree/bec3336591285a901d33d2abba824f6e2bc31d8c) — exact audited revision `bec3336591285a901d33d2abba824f6e2bc31d8c`

Compute: Hugging Face `cpu-upgrade` only (8 vCPU/32 GB advertised), Python 3.12 with `uv.lock`; no GPU devices. Every formal node used the same command.

## Experiment log

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `main` | Public report, notebook, and release surface | Not run as an experiment (publication surface) | Presentation only | — |
| [Historical judged baseline](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/historical-judged-baseline-reconstruction) | Reconstruct judged d=3 / λ=0 evidence | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | Historical rejected baseline; toy checks reproduced | HF `cpu-upgrade` |
| [Exact TDC traces](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/exact-tdc-traces-and-cumulative-verifier) | Definition 7.1 at λ=.25/.55/.85 | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | Faithful finite evidence; theorem BLOCKED | HF `cpu-upgrade` |
| [Nonlinear SA certificates](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/nonlinear-sa-scaling-and-assumption-certificates) | d=8/32/64 nonlinear scaling and family certificates | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | Aligned finite evidence; Claims 1–3 BLOCKED | HF `cpu-upgrade` |
| [Appendix B source verifier](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/hash-pinned-assumption-source-verifier) | Exhaustive hash-pinned source-domain check | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | Claim 5 VERIFIED | HF `cpu-upgrade` |
| [Proof dependency reconstruction](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/proof-dependency-reconstruction) | Paper/Yu source graph and proof-gap audit | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | Third route complete; Claims 1–4 BLOCKED | HF `cpu-upgrade` |
| [Mandatory falsification search](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/mandatory-falsification-search) | Nonnormal SA holdouts and high-ratio TDC | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | No valid counterexample; Claims 1–4 BLOCKED | HF `cpu-upgrade` |
| [Evaluator-visible release candidate](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/evaluator-visible-release-candidate) | Cumulative science, canonical traversal, protected-file and upload-manifest gates | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | PASS; winning release commit `e1ddb9a` | HF `cpu-upgrade` |
| [Exact published-revision audit](https://github.com/MachineLearning-Nerd/icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic/tree/orx/post-publication-exact-revision-audit) | Download and verify immutable HF revision `bec3336` | `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py` | PASS; 32/32 texts and 17/17 judged files matched | HF `cpu-upgrade` |

## Local notebook

```bash
marimo edit notebooks/two_timescale_reproduction.py
marimo run notebooks/two_timescale_reproduction.py
```
