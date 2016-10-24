#!/usr/bin/env

"""
n = 12191
e = 37
c = 587

p = 0
q = 0

for i in range(1, 100): # 100 because we know that it has a factor below 100
    if(n % i == 0):
        p = i

print p

a = (p - 1) * ((n/p) - 1) # (p-1)(q-1)
print a

d = 0

for i in range (1,a):
    if( ((e * i) % a) == 1):
        d = i
"""
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


n = 18889570071
e1 = 1021763679
e2 = 519424709

c1 = 1244183534
c2 = 732959706
g = gcd(e1,e2)

sol = (c1 * c2) % n
print sol

