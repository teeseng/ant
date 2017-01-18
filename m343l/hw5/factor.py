#!usr/bin/env

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

n = 1291233941
e1 = 1103927639
d1 = 76923209
e2 = 387632407
d2 = 7764043

g = gcd(((e1*d1) - 1), ((e2*d2) - 1))
bound = n + 1 - g

for i in range(3,(bound/2)):
    if(n % i == 0):
        print i
