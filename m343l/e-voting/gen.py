#!usr/bin/env

import random
import time
start_time = time.time()

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

# generates the the large primes of p and q
def gen_pq():
    primes = [i for i in range(500,10000) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)

    p_bits = bin(p)[2:]
    q_bits = bin(q)[2:]
    while(len(p_bits) != len(q_bits) or p == q):
        p = random.choice(primes)
        p_bits = bin(p)[2:]
        q = random.choice(primes)
        q_bits = bin(q)[2:]
    return [p,q]

# generates g for the public key
def gen_g(lambdas, n):
    mgroup = []
    for i in range(1, n^2):
        if(gcd(i,n) == 1):
            mgroup.append(i)
    g = random.choice(mgroup)
    L = (fast_exp(lambdas, g, n**2) - 1)/n
    while(gcd(L,n) != 1):
        g = random.choice(mgroup)
        L = (fast_exp(lambdas, g, n**2) - 1)/n
    return g

# generates alpha and beta to generate g for the public key
def gen_ab(g,n):
    mgroup = []
    for i in range(1, n):
        if(gcd(i,n) == 1):
            mgroup.append(i)
    a = random.choice(mgroup)
    b = random.choice(mgroup)
    beta = b**n
    g = (((a * n) + 1) * beta) % (n**2)
    return g

# calculates the u for the private decryption key
def calc_u(g, n, lamb):
    g = fast_exp(lamb,g,n**2)
    L = (g - 1)/n
    L = modinv(L,n)
    u = L % n
    return u

def fast_exp(exp, base, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return int(result)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

random_primes =  gen_pq()
p = random_primes[0]
q = random_primes[1]

n = p * q

lcm = ((p-1) * (q-1))/gcd((p-1),(q-1))

g = gen_g(lcm,n)
u = calc_u(g,n,lcm)


public = [n,g]
private = [lcm,u]

print public,private
print("--- %s seconds ---" % (time.time() - start_time))

