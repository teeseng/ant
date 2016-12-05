def IsIdentity(p):
    return p["x"] == 0 and p["x"] == p["y"]

def Slope(p1, p2, A=0, fp=None):
    diffx = p2["x"] - p1["x"]
    diffy = p2["y"] - p1["y"]
    if diffx == 0:
        if p1["y"] == -1 * p2["y"]:
            return float("inf")
        diffy = 3 * p1["x"] * p1["x"] + A
        diffx = 2 * p1["y"]
    if fp:
        numer = diffy % fp
        denom = diffx % fp
        if not(denom == 1):
            return RingDivide(numer, denom, fp)
        return numer
    m = float(diffy) / diffx
    return m

def GetAbsY(A, B, x, fp=None):
    x_cube = x ** 3
    y_sqr = x_cube + A * x + B
    if fp:
        y_sqr %= fp
    abs_y = math.sqrt(fp)
    return dict(x=x, y=abs_y)

def CheckPoint(A, B, p, fp=None):
    if p["x"] == 0 and p["x"] == p["y"]:
        return True
    x_cube = p["x"] ** 3
    y_sqr = p["y"] ** 2
    if fp:
        y_sqr %= fp
        return y_sqr == (x_cube + A * p["x"] + B) % fp
    return y_sqr == x_cube + A * p["x"] + B

def CheckCurve(A, B):
    A_cube = A ** 3
    B_sqr = B ** 2
    return not (4 * A_cube + 27 * B_sqr == 0)

def AdditiveInverse(P, fp=None):
    P["y"] = -1 * P["y"]
    if fp:
        P["y"] = P["y"] % fp
    return P

def AddPoints(A, B, p1, p2, fp=None):
    if IsIdentity(p1):
        return p2
    if IsIdentity(p2):
        return p1
    m = Slope(p1, p2, A, fp)
    if not m or m == float("inf"):
        return dict(x=0, y=0)
    x3 = m ** 2 - p1["x"] - p2["x"]
    y3 = m * (p1["x"] - x3) - p1["y"]
    if fp:
        x3 %= fp
        y3 %= fp
    return dict(x=x3, y=y3)

def MultiplyPoints(A, B, P, n, fp=None):
    if not(CheckCurve(A, B)):
        print("4 * {}^3 + 27 * {}^2 == 0. Invalid curve.".format(A, B))
        return
    if not(CheckPoint(A, B, P, fp)):
        print("The point ({}, {}) is not on the ".format(P["x"], P["y"]) +\
            "curve Y^2 = X^3 + {}*x + {}".format(A, B))
        return
    p = P
    if n == 0:
        return dict(x=0, y=0)
    if n < 0:
        n *= -1
        P = AdditiveInverse(P, fp)
    n -= 1
    while n > 0:
        p = AddPoints(A, B, p, P, fp)
        n -= 1
    return p

def SubtractPoints(A, B, p1, p2, fp=None):
    return AddPoints(A, B, p1, AdditiveInverse(p2), fp)

def g(A, P, Q, R, fp=None):
    m = Slope(P, Q, A, fp)
    if m == float("inf"):
        return R["x"] - P["x"]
    numer = R["y"] - P["y"] - m * (R["x"] - P["x"])
    denom = R["x"] + P["x"] + Q["x"] - m * m
    if fp:
        return RingDivide(numer, denom, fp)
    return numer / float(denom)

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

def Miller(A, B, n, P, R, fp=None):
    T = P
    f = 1
    print("Runing millers.")
    for bit in n:
        if fp:
            f = RingMultiply(RingMultiply(f, f, fp), g(A, T, T, R, fp), fp)
        else:
            f = f * f * g(A, T, T, R)
        T = AddPoints(A, B, T, T, fp)
        if bit:
            if fp:
                f = RingMultiply(f, g(A, T, P, R, fp), fp)
            else:
                f = f * g(A, T, P, R)
            T = AddPoints(A, B, T, P, fp)
    print("Done with millers. Returning {}".format(f))
    return f

def Weil(A, B, m, P, Q, S, fp=None):
    n = BinaryExpansion(m, True)[1:]
    if fp:
        f_p_numer = Miller(A, B, n, P, AddPoints(A, B, Q, S, fp), fp)
        f_p_denom = Miller(A, B, n, P, S, fp)
        f_q_numer = Miller(A, B, n, Q, SubtractPoints(A, B, P, S, fp), fp)
        f_q_denom = Miller(A, B, n, Q, AdditiveInverse(S, fp), fp)
        f_p = RingDivide(f_p_numer, f_p_denom, fp)
        f_q = RingDivide(f_q_numer, f_q_denom, fp)
        print("({} / {}) / ({} / {})".format(\
                f_p_numer, f_p_denom, f_q_numer,f_q_denom))
        print("{} / {}".format(f_p, f_q))
        return RingDivide(f_p, f_q, fp)
        f_p = Miller(A, B, n, P, AddPoints(A, B, Q, S)) /\
                float(Miller(A, B, n, P, S))
        f_q = Miller(A, B, n, Q, SubtractPoints(A, B, P, S)) /\
                float(Miller(A, B, n, Q, AdditiveInverse(S)))
        return f_p / f_q

print "Starting Weil"
print Weil(30,34,5,[36,60], [121, 387], [0,36], 631)

