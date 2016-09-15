#!/usr/bin/python
import math
m = int(input())
stuff = [1,3,7,9];
list = []
for i in range(1,m):
    d = 1
    r = 2;
    while(r != 1):
        r = (d * i) % m
        list.append(r)
        d = d + 1
    print list
    del list[:]
print "-------------------------------------"
d = 1
r = 2;
while(r != 1):
    r = 9**d % m
    list.append(r)
    d = d + 1
print list
del list[:]
