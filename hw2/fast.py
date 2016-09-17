#!/usr/bin/python

def fast_power(g, x, n):
    result = 1
    g = g % n
    while(x > 0):
        if(x % 2 == 1):
            result = (result * g) % n
        x = x >> 1
        g = (g * g) % n
    return result

g = int(input())
x = int(input())
n = int(input())

print fast_power(g,x,n)
