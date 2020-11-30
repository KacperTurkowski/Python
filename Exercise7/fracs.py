import math


class Frac:
    """Klasa reprezentująca ułamki."""

    def _short(self):
        gcd = math.gcd(self.x, self.y)
        if gcd > 1:
            return int(self.x/gcd), int(self.y/gcd)
        return self.x, self.y
    @staticmethod
    def _float_to_frac(other):
        x = other.as_integer_ratio()
        return Frac(x[0], x[1])

    @staticmethod
    def _int_to_frac(other):
        return Frac(other, 1)

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError
        self.x = int(x)
        self.y = int(y)
        self.x, self.y = self._short()

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return self.__float__() == other.__float__()

    def __ne__(self, other):
        return self.__float__() != other.__float__()

    def __lt__(self, other):
        return self.__float__() < other.__float__()

    def __le__(self, other):
        return self.__float__() <= other.__float__()

    def __add__(self, other):  # frac1+frac2, frac+int
        if type(other) is int:
            other = Frac._int_to_frac(other)
        elif type(other) is float:
            other = Frac._float_to_frac(other)
        nominator = self.x * other.y + other.x * self.y
        denominator = self.y * other.y
        return Frac(nominator, denominator)

    __radd__ = __add__

    def __sub__(self, other):  # frac1-frac2, frac-int
        if type(other) is int:
            other = Frac._int_to_frac(other)
        elif type(other) is float:
            other = Frac._float_to_frac(other)
        nominator = self.x*other.y-other.x*self.y
        denominator = self.y*other.y
        return Frac(nominator, denominator)

    def __rsub__(self, other):
        return self.__sub__(other).__neg__()

    def __mul__(self, other):  # frac1*frac2, frac*int
        if type(other) is int:
            other = Frac._int_to_frac(other)
        elif type(other) is float:
            other = Frac._float_to_frac(other)
        nominator = self.x * other.x
        denominator = self.y * other.y
        return Frac(nominator, denominator)

    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other):  # frac1/frac2, frac/int, Python 3
        if type(other) is int:
            other = Frac._int_to_frac(other)
        elif type(other) is float:
            other = Frac._float_to_frac(other)
        nominator = self.x*other.y
        denominator = self.y*other.x
        return Frac(nominator, denominator)

    def __rtruediv__(self, other):  # int/frac, Python 3
        return Frac.__invert__(self.__truediv__(other))

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self): return Frac(-self.x, self.y)        # -frac = (-1)*frac

    def __invert__(self):
        if self.x == 0:
            raise ValueError
        return Frac(self.y, self.x)      # odwrotnosc: ~frac

    def __float__(self):  # float(frac)
        if self.y != 0:
            return float(self.x / self.y)
        raise ValueError

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])