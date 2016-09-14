import math
fin = open('shanks.in')
fout = open('output.txt', 'w')
p = int(next(fin))
g = int(next(fin))
h = int(next(fin))

def fast_power(g, x, n):
    result = 1
    g = g % n
    while(x > 0):
        if(x % 2 == 1):
            result = (result * g) % n
        x = x >> 1
        g = (g * g) % n
    return result

order = 0
for x in range(2, p) :
    if((p-1) % x == 0):
        if(fast_power(g, x, p) == 1):
            order = x 
            break

n = int(math.ceil(math.sqrt(p-1)))
print >> fout, n

baby = []
giant = []
x = 0;

for j in range(0, n-1):
    baby.append(fast_power(g, j, p))

for k in range(0, n-1):
    val = h * (g**(-1 * k * n))
    giant.append(val)
    for j in range(0, n-1):
        if baby[j] == giant[k]:
            x = j + (n * k);       

print >> fout, x

