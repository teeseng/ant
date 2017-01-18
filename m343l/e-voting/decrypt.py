

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

def L(u,n):
    return (u - 1)/n


# c \lambda u
c = int(fin.next())
lamb = int(fin.next())
u = int(fin.next())
n = int(fin.next())

cl = fast_exp(lamb, c, n**2)
m = (L(cl,n) * u) % n

print >> fout, m








