#!usr/bin/env

import sys

def on_curve(x,y,a,b):
    lhs = y ** 2
    rhs = x**3 + (a * x) + b
    return lhs == rhs

def mod_comp(left, right, p):
    for i in range(0,p):
        if (left * i) % p == right:
            return i;

fin = open("input.txt", 'r');
fout = open("output.txt", 'w');

p = int(fin.next())
a = int(fin.next())
b = int(fin.next())

x1 = int(fin.next())
y1 = int(fin.next())
x2 = int(fin.next())
y2 = int(fin.next())

if(x1 == x2):
    print >> fout, "none"
    sys.exit("")

if on_curve(x1,y1,a,b):
    print >> fout, x2,y2
elif on_curve(x2,y2,a,b):
    print >> fout, x1,y1
elif (x1 == x2 and y1 == (-1 * y2)):
    print >> fout, -1
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
    print >> fout, x3,y3
