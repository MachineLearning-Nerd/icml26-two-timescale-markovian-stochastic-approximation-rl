# Claim 4 source audit

Primary source: `https://ar5iv.labs.arxiv.org/html/2605.31172`, retrieved with an explicit browser User-Agent on 2026-08-02. SHA-256: `ae486220f918b74b90b5750a5d50cc7d0974299dd09867534fc555d9e3c59087`.

Anchors: Definition 7.1 `#S7.Thmtheorem1`; Theorem 7.2 `#S7.Thmtheorem2`; Appendix F Assumptions F.1 and F.2 `#A6.Thmxassumption1` and `#A6.Thmxassumption2`. The full PDF text continues beyond the HTML conversion and supplies Lemma F.1, the augmented chain, the matrices A, b, C, D, and the reduction to Theorem 3.3.

F.1 requires finite state/action spaces, irreducibility of the behavior-policy state chain, and positive behavior probability for every state-action pair. F.2 requires full feature-matrix rank. The restated theorem also assumes A is invertible. The proof invokes B.1, B.2, B.4-B.7 and concludes `nu_t -> 0` and `theta_t -> -A^{-1}b` almost surely.

The paper calls this the first convergence result for unprojected off-policy TDC with eligibility traces. That priority statement is distinct from the mathematical convergence statement and requires a literature review; the numerical verifier cannot establish priority.
