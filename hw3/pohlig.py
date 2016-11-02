#!/usr/bin/env python3.5

# Pohlig-Hellman Implementation

from math import ceil, sqrt, floor
from collections import Counter

def prime_factors(n):
    F = []
    while n % 2 == 0:
        F.append(2);
        n /= 2
    for i in range(3, int(sqrt(n)), 2):
        while n % i == 0:
            F.append(int(i))
            n /= i
    if n > 2:
        F.append(int(n))

    return F;

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return (x0, y0)

def fast_exp(exp, base, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return int(result)

def combine(F, result):
    A, x, n = [], 0, 1
    for i in F:
        A.append(i**F[i])
    for i in A:
        n *= i
    for i in range(len(A)):
        (u, _) = xgcd(int(n / A[i]), int(A[i]))
        v = u * (int(n / A[i]))
        x += result[i] * v

    return x

def dl_solver(g, h, p, n=1): # Solve g^x = h (mod p^n) under a cyclic group G of order p^n
    s = floor(sqrt(p ** n))
    A, B = [], []
    for r in range(s):
        value = h * (g ** r) % p
        A.append(value)
    for t in range(1, s + 1):
        value = g ** (t*s) % p
        B.append(value)

    x1, x2 =0, 0

    for r in A:
        for t in B:
            if r == t:
                x1 = A.index(r)
                x2 = B.index(t)
                break

    return int(((x2 + 1) * s - x1) % p)

def pohlig_hellman(g, h, p):
    F = prime_factors(p - 1)
    F = Counter(F)
    (ginv, _) = xgcd(g, p)
    ginv %= p

    result, u, prev = [], 0, h
    for i in F:
        x = fast_exp((p-1)/i, g, p)
        for j in range(F[i]):
            y = fast_exp((p-1)/(i**(j+1)), h, p)
            for k in range(i): # or k = dl_solver(x, y, p)
                if pow(x, k, p) == y:
                    u += k * (i ** j)
                    break
            h = (h * fast_exp((i ** j) * k, ginv, p)) % p
        result.append(u)
        h = prev
        u = 0

    return combine(F, result)

if __name__ == "__main__":
    with open("input.txt", "r") as fi:
        g = int(fi.readline())
        h = int(fi.readline())
        p = int(fi.readline())

    with open("output.txt", "w") as fi:
        fi.write(str(pohlig_hellman(g, h, p)))
