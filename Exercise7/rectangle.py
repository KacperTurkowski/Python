class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return '('+str(self.x) + ", " + str(self.y)+')'

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return '['+str(self.pt1)+', '+str(self.pt2)+']'

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle('+str(self.pt1.x)+', '+str(self.pt1.y)+', '+str(self.pt2.x)+', '+str(self.pt2.y)+')'

    def __eq__(self, other):  # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and other.pt2 == self.pt2:
            return True
        return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x)/2
        y = (self.pt1.y + self.pt2.y)/2
        return Point(x, y)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x+x, self.pt1.y+y, self.pt2.x+x, self.pt2.y+y)

    def intersection(self, other):  # część wspólna prostokątów
        a, b = self, other
        x1 = max(a.pt1.x, b.pt1.x)
        y1 = max(a.pt1.y, b.pt1.y)
        x2 = min(a.pt2.x, b.pt2.x)
        y2 = min(a.pt2.y, b.pt2.y)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        return

    def cover(self, other):  # prostąkąt nakrywający oba
        a, b = self, other
        x1 = min(a.pt1.x, b.pt1.x)
        y1 = min(a.pt1.y, b.pt1.y)
        x2 = max(a.pt2.x, b.pt2.x)
        y2 = max(a.pt2.y, b.pt2.y)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        return

    def make4(self):  # zwraca krotkę czterech mniejszych
        t = tuple()
        central = self.center()
        R1 = Rectangle(self.pt1.x, self.pt1.y, central.x, central.y)
        R2 = Rectangle(self.pt1.x, central.y, central.x, self.pt2.y)
        R3 = Rectangle(central.x, self.pt1.y, self.pt2.x, central.y)
        R4 = Rectangle(central.x, central.y, self.pt2.x, self.pt2.y)
        t = (R1, R2, R3, R4)
        return t
