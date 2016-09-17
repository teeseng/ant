#!/usr/bin/python

import math

p = int(input())
b = int(input())
for x in range(0, p - 1):
    if(x * x % p == b):
        print x


