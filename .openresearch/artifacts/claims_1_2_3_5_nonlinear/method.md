# Nonlinear scaling method

The fast equilibrium map is `lambda(y)=My+q+0.06 abs(y)`. The fast drift is `-(x-lambda(y))`; the slow drift is `-(y-y*)+0.18 abs(x-lambda(y))`. Absolute value is globally Lipschitz and positively homogeneous for the positive rescalings in B.4. Thus the B.4 remainder is exactly `1/c` times the fixed offset and Markov noise, the reduced slow ODE is `dy/dt=-(y-y*)`, the limiting fast equilibrium is `My+0.06 abs(y)`, and the limiting reduced ODE is `dy/dt=-y`.

The run crosses dimensions 8/32/64, Markov self-transition weights 0.20/0.78/0.96, initial scales 1/12, and 100,000 iterations. It records errors at five predeclared horizons, deterministic seeds, maximum unprojected norm, empirical and analytic K, stationary residual, spectral gap, and final timescale ratio.

Controls separately violate B.1, B.2, B.6, and the no-projection contract. The independent verifier rejects any assumption failure, growth outside the registered envelope, inadequate tracking/joint reduction, K-certificate violation, malformed control, or tampered evidence.

Compute estimate: one core because all paths execute serially. Selected compute is Hugging Face `cpu-upgrade` (advertised 8 vCPU/32 GB), with actual allocation and runtime recorded inside the run.
