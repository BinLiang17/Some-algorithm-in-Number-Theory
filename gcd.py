# coding=utf-8
# Euclid’s algorithm
# Author : Bin.Liang

def euclid_gcd(b, a):
    a = abs(a)
    b = abs(b)
    if a < b:
        c = b
        b = a
        a = c

    r = a % b

    if r == 0:
        return b

    while r != 0:
        if b % r == 0:
            break
        else:
            d = r
            r = b % r
            b = d

    return abs(r)


def euclid_form(b, a):

    a = abs(a)
    b = abs(b)
    x = abs(a)
    y = abs(b)
    if x < y:
        c = y
        y = x
        x = c
        a = x
        b = y
    u_1 = 1
    u_2 = 0
    v_1 = 0
    v_2 = 1
    t = 1

    if x % y == 0:
        v_1 = (x / y) - 1
        v_2 = 1
    while x % y != 0 and y % x != 0:
        if t % 2 == 1:
            m = (x - x % y) / y
            u_2 = -1 * m * v_2 + u_2
            u_1 = -1 * m * v_1 + u_1
            x = x % y
            t = t + 1
        else:
            n = (y - y % x) / x
            v_1 = -1 * n * u_1 + v_1
            v_2 = -1 * n * u_2 + v_2
            y = y % x
            t = t + 1
    if x > y:
        factors = [int(v_1), int(v_2)]
        r = y
    else:
        factors = [int(u_1), int(u_2)]
        r = x
    if abs(factors[0]*a) < abs(factors[1]*b):
        factors[0] = - abs(factors[0])
        factors[1] = abs(factors[1])
    else:
        factors[0] = abs(factors[0])
        factors[1] = -abs(factors[1])

    print(str(r) + "=" + str(a)+  "*" +
          str(factors[0]) + "+" +str(b) +
          "*" + str(factors[1]))

    return factors
