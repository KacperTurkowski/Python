import random
from math import sqrt


def getrandom(n):
    return random.sample(range(n), n)


def getpartlyrandom(n):
    result = []
    for i in range(n):
        result.append(i)
    for i in range(n-1):
        check = random.randint(0, 1)
        if check == 1:
            result[i], result[i+1] = result[i+1], result[i]
    return result


def getpartlyrandominvert(n):
    result = []
    for i in range(n-1, -1, -1):
        result.append(i)
    for i in range(n-1):
        check = random.randint(0, 1)
        if check == 1:
            result[i], result[i+1] = result[i+1], result[i]
    return result


def getrandomgauss(n):
    result = []
    for i in range(n):
        result.append(random.gauss(0, 1))
    return result


def getrandomwithrepeats(n):
    result = []
    k = int(sqrt(n))
    for i in range(n):
        result.append(random.randint(0, k))
    return result

