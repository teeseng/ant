#!/usr/bin/env

fin = open("input.txt", 'r');
fout = open("output.txt", 'w');
p = int(fin.next())
m = int(fin.next())
q1 = int(fin.next())
q2 = int(fin.next())

a = (q1 + q2) % m
b = (q1 * q2) % m
a = a % m
b = b % m

print >> fout, a,b

fin.close()
fout.close()

