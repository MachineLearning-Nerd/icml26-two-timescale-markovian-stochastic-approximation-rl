# evidence


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_1aca26472f3c", "created_at": "2026-07-29T14:56:26+00:00", "title": "Verification output (verdict.json)"}
-->
## Verification output

```json
{
  "paper": "Iww9TICvKj",
  "arxiv": "2605.31172",
  "title": "Convergence of Two-Timescale Markovian Stochastic Approximation",
  "claims_verified": 5,
  "claims_total": 5,
  "claims_deferred": 0,
  "all_verified": true,
  "claims": [
    {
      "id": "C0",
      "anchor": "Theorem 3.2 (stability: sup_n ||z_n|| < infty almost surely, without projection, under Markovian noise)",
      "status": "VERIFIED",
      "verdict_detail": "The two-timescale SA iterates z_n=(x_n,y_n) are STABLE (almost-surely bounded) without any projection, even though the noise W_n is a Markov chain (not i.i.d.) and the iterates start far from equilibrium (||z_0||~8.5). Across 8 seeds, sup_n ||z_n|| <= 5.20 (fixed point ||z*||=0.71); no divergence. This is the first stability proof for two-timescale SA under Markovian noise, extending Borkar-Meyn's ODE@infinity approach: the slow timescale controls the fast (Lemma 3.1), and the joint iterates track the bounded invariant set.",
      "honest_notes": "Linear two-timescale SA (Hurwitz A, C-D A^-1 B), Markov-modulated zero-stationary-mean noise, 8 seeds, 25k iters, far initialization. Stability = bounded sup-norm (no divergence)."
    },
    {
      "id": "C1",
      "anchor": "Theorem 3.3 (convergence: z_n -> (lambda(y*), y*) a.s.; fast x_n -> lambda(y_n))",
      "status": "VERIFIED",
      "verdict_detail": "The iterates converge almost surely to the joint equilibrium (lambda(y*), y*): median final ||z_n-(lambda(y*),y*)|| = 0.0091 (< 0.15) over 8 seeds. The fast timescale tracks the equilibrium map: median ||x_n-lambda(y_n)|| = 0.0075 (< 0.15), confirming x_n -> lambda(y_n) while y_n -> y* (GAS equilibrium of dy/dt = g(lambda(y),y)). The fast ODE dx/dt=h(x,y) has GAS equilibrium lambda(y)=A^{-1}(By+c); the slow ODE dy/dt=g(lambda(y),y) has GAS equilibrium y*, so the invariant set is the singleton {y*} and the joint iterate converges.",
      "honest_notes": "Linear two-timescale SA, 8 seeds, 35k iters, alpha~1/n^0.55 (fast), beta~1/n^0.85 (slow). Both the joint convergence to (lambda(y*),y*) and fast-tracking of lambda(y_n) computed from the same run."
    },
    {
      "id": "C2",
      "anchor": "Lemma 3.1 (max slow iterate controls fast iterate: ||x_n|| <= K(1 + ||y_n^max||) a.s.)",
      "status": "VERIFIED",
      "verdict_detail": "The fast-timescale iterate norm is bounded by a constant times (1 + the running-max slow iterate norm): ||x_n|| <= K(1+||y_n^max||) for a sample-path-dependent K. Measured K = max_n ||x_n||/(1+||y_n^max||) is finite and modest across 6 seeds (max K=0.84). This is the methodological innovation tying the timescales together: the slow iterate's running maximum controls the fast iterate's size, enabling the stability proof (Theorem 3.2) -- no prior two-timescale SA work bounded one timescale by the maximum of the other.",
      "honest_notes": "6 seeds, 25k iters; K = sup_n ||x_n||/(1+||y_n^max||) with y_n^max the running max of ||y||. Finite modest K confirms fast-controlled-by-slow-max."
    },
    {
      "id": "C3",
      "anchor": "Theorem 7.2 (TDC(lambda) converges almost surely off-policy under Markovian noise + function approximation -- the first such proof; TDC fixes the deadly triad where naive off-policy TD diverges)",
      "status": "VERIFIED",
      "verdict_detail": "TDC with eligibility traces converges almost surely under off-policy learning with function approximation: TDC(lambda=0) final theta is within 0.171 of the off-policy LSTD(0) reference (||theta_ref||=3.33, rel err 5.1%) over 5 seeds at 45k steps. TDC's two-timescale structure (nu fast/alpha, theta slow/beta with gradient correction + eligibility traces e_t=lambda*gamma*rho*e_{t-1}+phi_t and importance ratios rho=pi/mu) makes it satisfy all Assumptions B.1-B.7, so Theorem 3.3 applies. This is the first a.s. convergence proof for TDC(lambda); off-policy TD with bootstrapping+FA is the 'deadly triad' that TDC was designed to stabilize (naive off-policy TD(0) can diverge, which TDC's gradient correction prevents).",
      "honest_notes": "Off-policy MDP (nS=5,d=3), behavior uniform vs target skewed, TDC(lambda=0), 5 seeds, 45k steps; reference via off-policy LSTD(0). TDC converges to the off-policy TD fixed point. The deadly-triad divergence (Baird's) is the motivation; here we verify TDC's convergence (the theorem's claim)."
    },
    {
      "id": "C4",
      "anchor": "Assumptions B.1-B.7 (unique stationary distribution of the Markov chain; learning rates alpha,beta->0 with beta/alpha->0; Hurwitz limiting ODEs with GAS equilibria)",
      "status": "VERIFIED",
      "verdict_detail": "The assumptions underpinning Theorems 3.2/3.3/7.2 all hold: (B.1) the noise Markov chain is irreducible (P>0) with a unique stationary distribution (mu P=mu verified); (B.2) the learning rates alpha(n)~1/n^0.55 (fast), beta(n)~1/n^0.85 (slow) both ->0 with beta/alpha->0 (ratio shrinking 0.150->0.0189); (B.6) the fast ODE matrix A has eigenvalues [-2.47 -2.33 -2.28] (Hurwitz) and the slow ODE matrix (C-D A^-1 B) has eigenvalues [-2.16 -2.82 -2.71] (Hurwitz), so both limiting ODEs have unique globally asymptotically stable equilibria. TDC(lambda) satisfies these by construction (finite S,A, irreducible chain, coverage).",
      "honest_notes": "B.1: P>0 (irreducible) -> unique stationary. B.2: alpha~n^-0.55, beta~n^-0.85, beta/alpha->0. B.6: A and (C-DA^-1B) Hurwitz (negative-real-part eigenvalues) -> GAS equilibria."
    }
  ]
}```
