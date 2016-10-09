a = 476
b = 537
p = 1291

for i in range(0,10000):
    d = b**2 + (2 * b * i * p) + (i**2 * p**2)
    if(d % (p**2) == a):
        print i 
        print " " 

"""
k = 1291
print (a) % p
print (2 * b * k * p) % p**2
print (k**2 * p**2) % p**2
print b**2 % p**2
print b**2 % p
"""
