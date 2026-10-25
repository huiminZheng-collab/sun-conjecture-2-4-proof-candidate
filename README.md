# Sun Conjecture 2.4: proof candidate

This repository contains the paper

> Huimin Zheng, *A finite Euler--Clausen transfer for Apéry-like sums, with an application to a conjecture of Zhi-Hong Sun*.

The manuscript proves the nine congruences stated in Conjecture 2.4 of Z.-H. Sun, *New congruences involving Apéry-like numbers* (arXiv:2004.07172v2). Its main device is a finite, truncated form of the quadratic Euler--Clausen transformation. The method transfers weighted and unweighted sums involving the Almkvist--Zudilin sequence

\[
G_n=\sum_{k=0}^n {2k\choose k}^2 {2n-2k\choose n-k}4^{n-k}
\]

to truncated hypergeometric sums for which CM special values are available in the literature.

## Contents

- `paper/main.pdf`: compiled 23-page manuscript.
- `source/main.tex`, `source/references.bib`: LaTeX source.
- `checks/adversarial_checks.py`: independent exact-arithmetic regression checks. These checks are diagnostic evidence, not a substitute for the proofs.
- `ADVERSARIAL_REVIEW.md`: release audit, repairs, and residual limitations.
- `RELEASE-MANIFEST.sha256`: SHA-256 hashes of the released payload.

## Build

From the `source` directory, run:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The only nonstandard input is the included bibliography file. The release PDF was built with TeX Live 2024.

## Checks

With Python 3.10 or later:

```text
python checks/adversarial_checks.py
```

The script reconstructs `G_n` from its defining sum, verifies the formal generating-series identity through degree 28, tests every stated congruence branch for all relevant primes from 5 through 101, and checks the odd-center identity for odd parameters through 31.

## Status

This is a public proof candidate, not a journal acceptance notice. Before release the manuscript underwent an adversarial audit; essential proof sketches were expanded, the nearest 2026 related preprint was discussed, the source was rebuilt without LaTeX warnings, and the final PDF was visually inspected page by page. See `ADVERSARIAL_REVIEW.md` for the precise scope.

## Author and AI disclosure

Author: Huimin Zheng, Anhui Science and Technology University. ORCID: 0009-0004-8605-2713.

As stated in the manuscript, the proofs and initial manuscript draft were developed with substantial assistance from OpenAI's Codex. The author checked the arguments, references, computations, and final presentation and assumes responsibility for the content.

## Rights

See `RIGHTS.md`.
