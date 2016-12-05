def BinaryExpansion(x, bits=False):
    nums = []
    x_bits = bin(x)[2:]
    n = len(x_bits)
    for i in range(n):
        bit = int(x_bits[i])
        if bits:
            nums.append(bit)
        elif bit:
            nums.append(2 ** (n - i - 1))
    return nums

def RingMultiply(a, b, m):
    return (a * b) % m

def RingDivide(a, b, m):
    inv = MultInverse(b % m, m)
    return RingMultiply(a % m, inv, m)