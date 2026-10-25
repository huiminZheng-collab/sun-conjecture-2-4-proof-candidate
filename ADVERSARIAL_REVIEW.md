# Adversarial review of the release candidate

Date: 2026-10-25

Verdict: **PASS AFTER REPAIRS**. No contradiction or fatal gap was found in the nine claimed congruences. The version in this repository is suitable for public circulation as a proof candidate, subject to normal independent mathematical review.

## Scope

The audit treated the following as separate obligations:

1. the exact generating-series identity and its coefficient normalization;
2. the finite center transfer modulo `p^3`;
3. the differentiated transfer modulo `p^2`;
4. the defect polynomial, reflection symmetry, forcing equation, and kernel formula;
5. the three weighted CM specializations;
6. the denominator-128 split and inert branches;
7. the exact odd-center symmetric-square identity;
8. exceptional-prime certificates, citations, novelty language, and reproducibility;
9. compilation and visual integrity of the released PDF.

## Blocking issues found and repaired

The first candidate was **not** released. Two sections carrying essential mathematical load were too compressed:

- the derivation of the defect kernel and its constant-coefficient forcing equation;
- the parameter deformation and corrected reflection argument needed for the inert denominator-128 branches.

The final manuscript expands these arguments. It now states the tail decomposition, Wilson-reversal step, local double-zero calculation, kernel recurrence, integrality needed for reduction, and the exact parameter match used in the final specialization. A central-term divisibility step in the `G_{p-1}` congruence was also made explicit.

## Literature and novelty audit

The introduction now distinguishes the genuinely new finite-truncation transfer from already published CM evaluations. It credits the CM input to the cited literature and discusses Z.-H. Sun's later preprint, *Generalizations of the Christoffel--Darboux formula and congruences involving Apéry-like numbers* (arXiv:2608.13192v1), whose endpoint/bilinear method is related context but does not supply the finite Euler--Clausen transfer used here.

The paper deliberately avoids an absolute priority claim. The supported claim is narrower: the manuscript supplies a proof of all nine formulas of the cited Conjecture 2.4 by the displayed transfer mechanism.

## Independent checks

- Clean `latexmk` build under TeX Live 2024: 23 pages, with no LaTeX warnings, undefined references, or overfull boxes.
- Visual inspection of all 23 rendered pages: no clipping, overlap, missing glyphs, or broken displays found.
- Exact-arithmetic regression script: formal identity through degree 28; all stated congruence branches for the relevant primes `5 <= p <= 101`; odd-center identity for odd parameters through 31.
- Source scan: no local absolute paths, credentials, placeholders, or internal project labels in the public payload.

The computation is intentionally described as a regression check. It is not used as proof and it does not establish novelty.

## Residual limitations

- The full manuscript has not been formalized in Lean. Only selected algebraic components are stated in the paper as having been checked in Lean.
- The literature search cannot logically prove absence of an unpublished or differently indexed proof; priority language therefore remains qualified.
- The argument still depends on cited CM special-value theorems. The manuscript specializes and transfers those inputs rather than reproving their complete theory.

These limitations do not invalidate the stated proof, but they delimit what this release certifies.
