
import random

def gen_r(n):
    mgroup = []
    for i in range(1, n):
        if(gcd(i,n) == 1):
            mgroup.append(i)
    r = random.choice(mgroup)
    return r

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


fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

# m g n
m = int(fin.next())
g = int(fin.next())
n = int(fin.next())

r = gen_r(n)
gm = fast_exp(m,g,n**2)
rn = fast_exp(n,r,n**2)
c = (gm * rn) % (n**2) # ciphertext c

print >> fout, c

