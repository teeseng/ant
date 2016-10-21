#!/usr/bin/env

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

def fast_power(g,x,n):
    result = 1
    g = g % n
    while(x > 0):
        if(x % 2 == 1):
            result = (result * g) % n
        x = x >> 1
        g = (g * g) % n
    return result

# Pollard's Algorithm!
def pollard(n):
    a = 2
    for j in range(2,n):
        a = fast_power(a,j,n)
        d = gcd(a - 1, n)
        if(d > 1 & d < n):
            return d

# Pollard's Algorithm!
fin = open("input.txt", 'r');
fout = open("output.txt", 'w');

n = int(fin.next())
d = pollard(n)
print >> fout, d

fin.close();
fout.close();
