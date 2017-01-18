#!usr/bin/env

# ==========
#    RSA
# ==========
# andy tseng
# ==========

import random
from math import sqrt

# --------
# is_prime
# --------
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
        return True
# ---
# gcd
# ---
def gcd(x,y):
    if(x < 0 | y < 0):
        return -1
    elif(x == 0 | y == 0):
        return 0
    r = x % y
    while(r > 0):
        x = y
        y = r
        r = x % y
    return y


# ------
# make_e
# ------
def make_e(p,q):
    N = p * q
    a = []
    for e in range(1, int(sqrt(N))):
        if(gcd(e, (p-1) * (q-1)) == 1):
            a.append(e)
    return a

# ------
# pair_d
# ------
def pair_d(p,q,e):
    for d in range(1,p*q) :
        if((d * e) % ((p-1) * (q-1)) == 1):
            return d

# --------
# generate
# --------
primes = [i for i in range(3000,10000) if is_prime(i)]

# choosing random primes numbers
p = random.choice(primes)
q = random.choice(primes)
while(p == q):
    q = random.choice(primes)
N = p * q
elist = make_e(p,q)
e = random.choice(elist)
d = pair_d(p,q,e)

# I/O handling
fin = open("input.txt", 'r');
fout = open("output.txt", 'w');
doc = int(fin.next())
S = (doc**d) % N
print >> fout, S
print >> fout, N,e

