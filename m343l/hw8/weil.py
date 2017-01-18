#!usr/bin/env
# weil pairing algorithm

import math
import sys

#def weil_py(p,a,b,m,px,py,qx,qy):

def mod_comp(left, right, p):
    for i in range(0,p):
        if (left * i) % p == right:
            return i
    return right/left

def find_point_on_curve(p,a,b):
    for i in range(1, p):
       y = ((i**3) + (a * i) + b)
       if((math.floor(math.sqrt(y))** 2) == y):
           return [i, math.sqrt(y)]

def slope(p, px, py, qx, qy):
    if(px == qx):
        return None
    top = qy-py
    bot = qx-px
    if(bot < 0):
        bot = bot + p
    if(top < 0):
        top = top + p

    return mod_comp(bot, top, p)

def on_curve(x,y,a,b):
    lhs = (y ** 2)
    rhs = (x**3 + (a * x) + b)
    return lhs == rhs

def e_add(p,a,b,x1,y1,x2,y2):
    if(x1 == x2 and y1 != y2):
        return None
    if on_curve(x1,y1,a,b):
        return [x2,y2]
    elif on_curve(x2,y2,a,b):
        return [x1,y1]
    elif (x1 == x2 and y1 == (-1 * y2)):
        return -1
    else:
        slope = 0
        if x1 == x2 and y1 == y2 :
            slope = mod_comp( ((2 * y1) % p), ((3 * (x1 ** 2) + a) % p), p)
        else:
            top = y2 - y1
            bot = x2 - x1
            if(y2 - y1 < 0):
                top = top + p
            if(x2 - x1 < 0):
                bot = bot + p
            slope = mod_comp(bot, top, p)
        x3 = ((slope ** 2) - x1 - x2) % p
        y3 = ((slope * (x1 - x3)) - y1) % p
        return [x3,y3]

def find_bit_length(m):
    length = 0;
    while m > 0:
        m = m >> 1;
        length = length + 1;
    return length


def g(P,Q,S,fp):
    s = slope(fp, P[0], P[1], Q[0], Q[1])
    if P[0] == Q[0]:
        if S[0] - P[0] < 0:
            return (S[0] - P[0]) * -1
        return S[0] - P[0]
    else:
        bot = (S[0] + P[0] + Q[0] - (s**2))
        if bot < 0:
            bot = bot
        top = S[1] - P[1] - (s * (S[0] - P[0]))
        return  mod_comp(bot,top,fp)


def f(P, S, m, p, a, b):
    f = 1
    T = P
    n = find_bit_length(m)
    bits = bin(m)[2:]

    #loop here
    for i in range(1, n):
        if bits[i] == 1:
            g_TP = g(T,P,S,p)
            f = (f * g_TP)
            T = e_add(p, a, b, T[0], T[1], P[0], P[1])
        else:
            g_TT = g(T,T,S,p)
            f = ((f**2) * g_TT)
            T = e_add(p, a, b , T[0], T[1], T[0], T[1])
    return f

fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

p = int(fin.next())
a = int(fin.next())
b = int(fin.next())
m = int(fin.next())
px = int(fin.next())
py = int(fin.next())
qx = int(fin.next())
qy = int(fin.next())

P = [36, 60]
Q = [121, 387]
S = [0,36]

print f(P,S,m,p,a,b) % p-1
print f(P,S,m,p,a,b)


