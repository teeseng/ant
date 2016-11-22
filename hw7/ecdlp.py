#!usr/bin/env
def on_curve(x,y,a,b):
    lhs = y ** 2
    rhs = x**3 + (a * x) + b
    return lhs == rhs

def mod_comp(left, right, p):
    for i in range(0,p):
        if (left * i) % p == right:
            return i;

def ellipse_add(p,a,b,x1,y1,x2,y2):
    if on_curve(x1,y1,a,b):
        return [x2,y2]
    elif on_curve(x2,y2,a,b):
        return [x1,y1]
    elif (x1 == x2 and y1 == (-1 * y2)):
        return [-1,-1]
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

fin = open("ecdlp.in", 'r');
fout = open("ecdlp.out", 'w');

p = int(fin.next())
a = int(fin.next())
b = int(fin.next())

x1 = int(fin.next())
y1 = int(fin.next())
x2 = int(fin.next())
y2 = int(fin.next())

ellipse_add(p,a,b,x1,y1,x2,y2)
for i in range(1, 5):
    rescoord = ellipse_add(p,a,b,x1,y1,x2,y2)
    x1 = rescoord[0]
    y1 = rescoord[1]
    print x1,y1

# eyeball the output to find Q(0,1)
