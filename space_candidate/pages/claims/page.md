# claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_89a97c2739ab", "created_at": "2026-07-29T14:56:25+00:00", "title": "Claims to reproduce"}
-->
## Claims to reproduce

1. **Theorem 3.2 (stability):** the two-timescale SA iterates z_n=(x_n,y_n) are stable (sup_n‖z_n‖<∞ a.s.) without projection, even under Markovian noise.
2. **Theorem 3.3 (convergence):** z_n → (λ(y*), y*) a.s.; the fast iterate x_n → λ(y_n), where λ(y) is the GAS equilibrium of dx/dt=h(x,y) and y* the GAS equilibrium of dy/dt=g(λ(y),y).
3. **Lemma 3.1 (max-slow-controls-fast):** ‖x_n‖ ≤ K(1+‖y_n^max‖) a.s. — the methodological innovation tying the timescales.
4. **Theorem 7.2 (TDC(λ)):** the first almost-sure convergence proof for off-policy TDC(λ) (gradient correction + eligibility traces) under Markovian noise + function approximation.
5. **Assumptions B.1-B.7:** unique stationary distribution; learning rates α,β→0 with β/α→0; Hurwitz limiting ODEs.
