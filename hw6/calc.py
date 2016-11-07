#!usr/bin/env

k = 5803
p = 348149

e = ((209176 + 217800)) % (p-1)
e = e - (153405 + 127561)
e = e + p - 1
print e
e = e/((-2 * 208913) + (p-1))
e = e + (p-1)
print e

# checking e


