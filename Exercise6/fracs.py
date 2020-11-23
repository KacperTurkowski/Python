import math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x)+"/"+str(self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac("+str(self.x)+", "+str(self.y)+")"

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return self.__float__() == other.__float__()

    def __ne__(self, other):
        return self.__float__() != other.__float__()

    def __lt__(self, other):
        return self.__float__() < other.__float__()

    def __le__(self, other):
        return self.__float__() <= other.__float__()

    def __gt__(self, other):
        return self.__float__() > other.__float__()

    def __ge__(self, other):
        return self.__float__() >= other.__float__()

    def __add__(self, other):  # frac1 + frac2
        if self.__eq__(Frac(0, 1)) and other.__eq__(Frac(0, 1)):
            return Frac(0, 1)
        elif self.__eq__(Frac(0, 1)):
            return other
        elif other.__eq__(Frac(0, 1)):
            return self
        nominator = self.x*other.y+other.x*self.y
        denominator = self.y*other.y
        gcd = math.gcd(nominator, denominator)
        nominator /= gcd
        denominator /= gcd
        return Frac(nominator, denominator)

    def __sub__(self, other):  # frac1 - frac2
        if self.__eq__(Frac(0, 1)) and other.__eq__(Frac(0, 1)):
            return Frac(0, 1)
        elif self.__eq__(Frac(0, 1)):
            return Frac(-other.x, other.y)
        elif other.__eq__(Frac(0, 1)):
            return self
        nominator = self.x*other.y-other.x*self.y
        denominator = self.y*other.y
        gcd = math.gcd(nominator, denominator)
        nominator /= gcd
        denominator /= gcd
        return Frac(nominator, denominator)

    def __mul__(self, other):  # frac1 * frac2
        if self.__eq__(Frac(0, 1)) or other.__eq__(Frac(0, 1)):
            return Frac(0, 1)
        nominator = self.x*other.x
        denominator = self.y*other.y
        gcd = math.gcd(nominator, denominator)
        nominator /= gcd
        denominator /= gcd
        return Frac(nominator, denominator)

    def __div__(self, other):  # frac1 / frac2
        if self.__eq__(Frac(0, 1)) and other.__eq__(Frac(0, 1)):
            return
        elif self.__eq__(Frac(0, 1)):
            return Frac(0, 1)
        elif other.__eq__(Frac(0, 1)):
            return
        nominator = self.x*other.y
        denominator = self.y*other.x
        gcd = math.gcd(nominator, denominator)
        nominator /= gcd
        denominator /= gcd
        return Frac(nominator, denominator)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        if self.x == 0:
            return "denominator is 0"
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        if self.y != 0:
            return float(self.x/self.y)
        return "denominator is 0"
