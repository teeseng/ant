#!usr/bin/env
from math import log
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

def fast_exp(exp, base, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return int(result)

# -----------
# f_{x_{i}}()
# -----------
def f_x(x,p,g,h):
    x = x % p
    if(x > 0 and x < (p/3)):
        return (g * x) % p
    elif(x >= (p/3) and x < ((2*p)/3)):
        return (x**2) % p
    else:
        return (h * x) % p

# ----------------
# f_{\alpha_{i}}()
# ----------------
def f_a(a,x,p,g,h):
    x = x % p
    if(x >= 0 and x < (p/3)):
        return (a + 1) % (p - 1)
    elif(x >= (p/3) and x < ((2*p)/3)):
        return (2 * a) % (p -1)
    else:
        return a % (p-1)

# ----------------
# f_{\beta_{i}}()
# ----------------
def f_b(b,x,p,g,h):
    x = x % p
    if(x >= 0 and x < (p/3)):
        return b % (p-1)
    elif(x >= (p/3) and x < ((2*p)/3)):
        return 2*b % (p-1)
    else:
        return (b + 1) % (p-1)

# -------
# pollard
# -------
def pollard(ai,bi,gamma,epsilon,g, x, h, p):
    xi = f_x(1,p,g,h)
    yi = f_x(xi,p,g,h)
    ai = f_a(0,xi,p,g,h)
    bi = f_b(0,xi,p,g,h)
    gamma = f_a(f_a(0,xi,p,g,h),xi,p,g,h)
    epsilon = f_b(f_b(0,xi,p,g,h),xi,p,g,h)
    step = 1
    while(xi != yi):
        ai = f_a(ai,xi,p,g,h)
        bi = f_b(bi,xi,p,g,h)
        gamma = f_a( f_a(gamma,yi,p,g,h), f_x(yi,p,g,h), p,g,h)
        epsilon = f_b( f_b(epsilon,yi,p,g,h), f_x(yi,p,g,h), p,g,h)
        xi = f_x(xi,p,g,h)
        yi = f_x(f_x(yi, p, g, h), p, g, h)
        step = step + 1
    a = [ai,bi,gamma,epsilon,step]
    return a

# ----
# main
# ----

fin = open("input.txt", 'r');
fout = open("output.txt", 'w');
g = int(fin.next())
h = int(fin.next())
p = int(fin.next())

ai = 0
bi = 0
gamma_i = 0
epsilon_i = 0
res = pollard(ai, bi, gamma_i, epsilon_i, g, 1, h, p);

ai = res[0]
bi = res[1]
gamma_i = res[2]
epsilon_i = res[3]
step = res[4]

u = ai - gamma_i
if(u < 0):
    u = u + p - 1
v = (epsilon_i - bi)
if(v < 0):
    v = v + p - 1

gcd = gcd(v,p-1)
m = 0
for i in range(0,v):
    if((v * i) % (p-1) == gcd):
        m = i
        break
m = ((m * u) % (p-1))/gcd
n = (p-1)/gcd

while(m < p):
    rho = fast_exp(m,g,p) # fast_exp is faster for calculating these large numbers ofp
    if(rho == h):
        break
    m = m + n;
print >> fout, g,m,h
