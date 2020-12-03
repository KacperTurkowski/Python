import random


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0:
        raise ValueError
    elif c == 0:
        if a == 0:
            return "y = 0"
        elif b == 0:
            return "x = 0"
        else:
            return "y = "+str(-a/b) + "x"
    if a == 0:
        return "y = "+str(-c/b)
    elif b == 0:
        return "x = "+str(-c/a)
    else:
        return "y = " + str(a / -b) + f'x {(c / -b):+}'


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""

    hit = 0
    for i in range(1, n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            hit += 1
    return float(hit)*4/n


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5


def P_R(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif j == 0:
        return 0.0
    elif i == 0:
        return 1.0
    else:
        return 0.5 * (P_R(i-1, j) + P_R(i, j-1))



def P(i, j):
    p = [[None for x in range(j+1)] for y in range(i+1)]

    for temp in range(j+1):
        p[0][temp] = 1.0
    for temp in range(i+1):
        p[temp][0] = 0.0
    p[0][0] = 0.5

    for y in range(1, j+1):
        for x in range(1, i+1):
            p[x][y] = 0.5*(p[x-1][y] + p[x][y-1])

    return p[i][j]
