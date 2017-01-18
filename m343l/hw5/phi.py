#!usr/bin/env

# Euler's phi function

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

n = 1
while(n != "q"):
    n = input("choose a number: ")
    count = 0
    for i in range(0,n):
        if(gcd(i,n) == 1):
            count = count + 1
    print count

