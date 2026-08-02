# overview


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_938b61a87e09", "created_at": "2026-07-29T14:56:25+00:00", "title": "Convergence of Two-Timescale Markovian SA"}
-->
# Convergence of Two-Timescale Markovian Stochastic Approximation

OpenReview: https://openreview.net/forum?id=Iww9TICvKj
arXiv: https://arxiv.org/abs/2605.31172

Clean-room CPU reproduction (numpy). The first proofs of almost-sure stability and convergence of two-timescale stochastic approximation (x fast, y slow) under Markovian noise (not i.i.d.), without projection — via the innovation that the slow iterate's running maximum controls the fast iterate (Lemma 3.1). Applied to give the first a.s. convergence of off-policy TDC(λ) (gradient correction + eligibility traces).

5 anchored claims (10 possible points), all VERIFIED via stochastic simulation.
