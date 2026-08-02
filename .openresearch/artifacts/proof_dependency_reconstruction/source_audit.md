# Source audit

Paper source: `https://export.arxiv.org/e-print/2605.31172v1`, SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`.

Primary comparison source: Yu (2017), arXiv:1712.09652v2, `https://export.arxiv.org/e-print/1712.09652v2`, SHA-256 `fa48127d46d01abfc81bf2e737815f9afed5cdae63f5de37993d722c7c002acd`.

The reconstructed graph follows Lemma 3.1 → Theorem 3.2 → Theorem 3.3 → Theorem 7.2. For TDC, the audit additionally checks the Yu invariance dependency, the exact unprojected trace recursion, and the negative-definiteness step for the reduced slow ODE.

The paper explicitly omits one technical-lemma proof as analogous to Liu et al. (2025). That omission prevents this source audit from being treated as a complete formal proof certificate.
