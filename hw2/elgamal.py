from random import randint

fin = open('elgamal.in')
fout = open('output.txt', 'w')
p = int(next(fin))
g = int(next(fin))
m = int(next(fin))
ga = int(next(fin))

def fast_power(g, x, n):
    result = 1
    g = g % n
    while(x > 0):
        if(x % 2 == 1):
            result = (result * g) % n
        x = x >> 1
        g = (g * g) % n
    return result

k = randint(2, p - 1)
c1 = fast_power(g,k,p)
c2 = (m * fast_power(ga, k, p)) % p
print >> fout, c1, c2

