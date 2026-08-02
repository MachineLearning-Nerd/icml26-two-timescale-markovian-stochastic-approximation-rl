# Historical baseline method

The fixed command runs eight deterministic-seed paths of a 3+3-dimensional linear two-timescale SA and five paths of a 5-state, 3-feature TDC instance at `lambda=0`. It records boundedness, equilibrium tracking, joint error, an empirical running-max ratio, exact finite-chain stationarity, ODE eigenvalues, and TDC fixed-point residuals. No projection, clipping, GPU, or local research compute is used.

This intentionally matches the criticized scale and cannot verify the paper's universal almost-sure statements or its eligibility-trace claim.
