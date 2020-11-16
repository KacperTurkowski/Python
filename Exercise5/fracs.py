import math


def add_frac(frac1, frac2):
    if is_zero(frac1) and is_zero(frac2):
        return [0, 0]
    elif is_zero(frac1):
        return frac2
    elif is_zero(frac2):
        return frac1
    counter = frac1[0]*frac2[1]+frac1[1]*frac2[0]
    denominator = frac1[1]*frac2[1]
    gcd = math.gcd(counter, denominator)
    counter /= gcd
    denominator /= gcd
    return [counter, denominator]


def sub_frac(frac1, frac2):
    if is_zero(frac1) and is_zero(frac2):
        return [0, 0]
    elif is_zero(frac1):
        return [-frac2[0], frac2[1]]
    elif is_zero(frac2):
        return frac1
    counter = frac1[0]*frac2[1]-frac1[1]*frac2[0]
    denominator = frac1[1]*frac2[1]
    gcd = math.gcd(counter, denominator)
    counter /= gcd
    denominator /= gcd
    return [counter, denominator]


def mul_frac(frac1, frac2):
    if is_zero(frac1) or is_zero(frac2):
        return [0, 0]
    counter = frac1[0]*frac2[0]
    denominator = frac1[1]*frac2[1]
    gcd = math.gcd(counter, denominator)
    counter /= gcd
    denominator /= gcd
    return [counter, denominator]


def div_frac(frac1, frac2):
    if is_zero(frac1) and is_zero(frac2):
        return
    elif is_zero(frac1):
        return [0, 0]
    elif is_zero(frac2):
        return
    counter = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    gcd = math.gcd(counter, denominator)
    counter /= gcd
    denominator /= gcd
    return [counter, denominator]


def is_positive(frac):            # bool, czy dodatni
    if frac2float(frac) > 0:
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    if frac2float(frac1) > frac2float(frac2):
        return -1
    elif frac2float(frac1) == frac2float(frac2):
        return 0
    else:
        return 1


def frac2float(frac):              # konwersja do float
    return float(frac[0]/frac[1])
