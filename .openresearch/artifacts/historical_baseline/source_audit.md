# Source audit

- Source: https://ar5iv.labs.arxiv.org/html/2605.31172
- Retrieved with explicit `OpenResearch-Reproduction/1.0` User-Agent: 2026-08-02T08:11:41Z
- SHA-256: `ae486220f918b74b90b5750a5d50cc7d0974299dd09867534fc555d9e3c59087`
- Version shown by the source: arXiv:2605.31172v1, 29 May 2026

## Exact result anchors and quantifiers

- Lemma 3.1: `#S3.Thmtheorem1`, under the Appendix B assumptions, there exists a sample-path-dependent `K` such that for every `n`, `||x_n|| <= K(1 + ||y_n^max||)` almost surely; `y_n^max` is an iterate attaining `max_{i<=n} ||y_i||`.
- Theorem 3.2: `#S3.Thmtheorem2`, `sup_n ||z_n|| < infinity` almost surely. Its assumptions are inherited from the surrounding Section 3 setup and Lemma 3.1.
- Theorem 3.3: `#S3.Thmtheorem3`, if Assumptions B.1 through B.7 hold, then almost surely `lim_n ||x_n-lambda(y_n)||=0` and `lim_n ||z_n-(lambda(y*),y*)||=0`.
- Definition 7.1: `#S7.Thmtheorem1`, equations (36)-(39) define the exact TDC(lambda) eligibility, TD error, fast `nu`, and slow `theta` updates.
- Theorem 7.2: `#S7.Thmtheorem2`, under Appendix F assumptions, TDC with eligibility traces converges almost surely.

## Assumptions

- B.1 `#A2.Thmtheorem1`: the Markov chain has a unique invariant probability measure.
- B.2 `#A2.Thmtheorem2`: positive decreasing step sizes; both sums diverge; both sequences tend to zero; the relative one-step changes are `O(alpha(i))` and `O(beta(i))`; and `beta(i)/alpha(i) -> 0`.
- B.3 is a remark, not an assumption.
- B.4 `#A2.Thmtheorem4`: measurable limiting drifts and factored vanishing rescaling errors with integrable Lipschitz envelope.
- B.5 `#A2.Thmtheorem5`: `H`, `G`, `H_infinity`, and `G_infinity` share an integrable random Lipschitz envelope; their stationary expectations exist and are finite.
- B.6 `#A2.Thmtheorem6`: fast and slow mean ODEs have unique globally asymptotically stable equilibria; rescaled mean drifts converge uniformly on compacts; the limiting fast equilibrium map is Lipschitz, homogeneous, and zero at zero; the limiting slow ODE has zero as its unique GAS equilibrium.
- B.7 `#A2.Thmtheorem7`: for `H(x,y,.)`, `G(x,y,.)`, `L_b`, and `L`, the alpha- and beta-scaled centered partial sums converge almost surely to zero for every initial noise state, on one common probability-one set.
- F.1 `#A6.Thmxassumption1`: finite state/action spaces, irreducible behavior-policy state chain, and positive behavior probability for every state-action pair.
- F.2 `#A6.Thmxassumption2`: full-rank feature matrix.
