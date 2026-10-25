"""Independent exact checks for the theorem statements in main.tex.

These finite checks are diagnostic only.  They deliberately reconstruct G_n
from its defining convolution instead of importing the research certificates.
"""

from fractions import Fraction
from math import comb, isqrt


def primes_upto(limit):
    out = []
    for n in range(2, limit + 1):
        if all(n % q for q in range(2, isqrt(n) + 1)):
            out.append(n)
    return out


def representation(p, d):
    for y in range(isqrt(p // d) + 1):
        x2 = p - d * y * y
        x = isqrt(x2)
        if x * x == x2:
            return x, y
    raise AssertionError((p, d))


def apery_G(n):
    return sum(comb(2 * k, k) ** 2 * comb(2 * n - 2 * k, n - k)
               * 4 ** (n - k) for k in range(n + 1))


LIMIT = 101
PRIMES = [p for p in primes_upto(LIMIT) if p > 3]
G = [apery_G(n) for n in range(LIMIT)]


def g_sum(p, denominator, weighted, modulus):
    return sum((n if weighted else 1) * comb(2 * n, n) * G[n]
               * pow(denominator, -n, modulus)
               for n in range(p)) % modulus


def triple_sum(p, denominator, weighted, modulus):
    return sum((k if weighted else 1) * comb(2 * k, k) ** 2
               * comb(4 * k, 2 * k) * pow(denominator, -k, modulus)
               for k in range(p)) % modulus


def q_value(a):
    from math import factorial

    f = [(-1) ** i * comb(a, i) * comb(a + i, i) for i in range(a + 1)]
    total = Fraction(0)
    for j in range(a):
        for k in range(a - j):
            w = Fraction((-1) ** k * factorial(a - k - 1)
                         * factorial(k) ** 2,
                         factorial(a + k + 1))
            total += f[k + j + 1] * w * Fraction(1, 2) ** j
    return total


def check_formal_identity(degree=28):
    # Expand K(4z(1-z)) directly.
    rhs = [Fraction(0) for _ in range(degree + 1)]
    for k in range(degree + 1):
        c = Fraction(comb(2 * k, k) ** 2 * comb(4 * k, 2 * k), 256 ** k)
        for j in range(k + 1):
            n = k + j
            if n <= degree:
                rhs[n] += c * 4 ** k * (-1) ** j * comb(k, j)
    lhs = [Fraction(comb(2 * n, n) * G[n], 64 ** n)
           for n in range(degree + 1)]
    assert lhs == rhs


def check_main_congruences():
    for p in PRIMES:
        p2, p3 = p * p, p ** 3

        # Center bridge, reconstructed on both sides.
        assert g_sum(p, 128, False, p3) == triple_sum(p, 256, False, p3)

        # Weighted pair A and its common value.
        a72 = g_sum(p, 72, True, p2)
        a576 = g_sum(p, 576, True, p2)
        assert (a72 + 8 * a576) % p2 == 0
        if p % 4 == 1:
            x, _ = representation(p, 4)
            assert a72 == (4 * x * x - 3 * p) % p2
        else:
            assert a72 == p

        # Weighted pair B and its common value.
        b48 = g_sum(p, 48, True, p2)
        bm192 = g_sum(p, -192, True, p2)
        assert (b48 - 4 * bm192) % p2 == 0
        if p % 3 == 1:
            x, _ = representation(p, 3)
            assert b48 == (3 * p - 4 * x * x) % p2
        else:
            assert b48 == (-p) % p2

        # Weighted pair C is meaningful only away from p=7.
        if p != 7:
            c63 = g_sum(p, 63, True, p2)
            cm4032 = g_sum(p, -4032, True, p2)
            assert (c63 - 64 * cm4032) % p2 == 0
            if p % 7 in (1, 2, 4):
                x, _ = representation(p, 7)
                assert c63 == (-8 * (4 * x * x - 3 * p)) % p2
            else:
                assert c63 == (-8 * p) % p2

        # Denominator 128, all residue classes.
        center = g_sum(p, 128, False, p3)
        if p % 8 in (1, 3):
            x, _ = representation(p, 2)
            rhs = (4 * x * x - 2 * p
                   - p * p * pow(4 * x * x, -1, p3)) % p3
        else:
            C = comb(p // 4, p // 8)
            if p % 8 == 5:
                rhs = p * p * pow(3 * C * C, -1, p3) % p3
            else:
                rhs = -3 * p * p * pow(2 * C * C, -1, p3) % p3
        assert center == rhs % p3


def check_odd_center_identity():
    for a in range(1, 32, 2):
        got = q_value(a)
        want = -Fraction(2 ** (a - 1),
                         a * comb(a - 1, (a - 1) // 2)) ** 2
        assert got == want, (a, got, want)


if __name__ == "__main__":
    check_formal_identity()
    check_main_congruences()
    check_odd_center_identity()
    print(f"PASS: formal identity through degree 28; all stated branches for primes 5..{LIMIT}; odd-center identity for a<=31")
