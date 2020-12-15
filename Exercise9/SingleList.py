class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):
        if self.length == 0:  # length = 0
            raise ValueError
        node = self.tail
        if self.tail == self.head:  # length = 1
            self.head = self.tail = None
        else:  # length >= 2
            x = self.head
            while x.next != self.tail:
                x = x.next
            self.tail = x
            x.next = None
        node.next = None
        self.length -= -1
        return node

    # klasy O(N)
    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length = self.length + other.length
        other.clear()
    # klasy O(1)
    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):
        while self.length != 0:
            x = self.remove_head()
        # czyszczenie listy

    def search(self, data):
        x = self.head
        if x == None:
            return None
        while x.next != None:
            if x.next.data == data:
                return x.next
            x = x.next
        return None
    # klasy O(N)
    # Zwraca łącze do węzła o podanym kluczu lub None.

    def find_min(self):
        min = self.head
        x = self.head
        while x.next != None:
            if x.next.data < min.data:
                min = x.next
            x = x.next
        return min
        # klasy O(N)
    # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def find_max(self):
        max = self.head
        x = self.head
        while x.next != None:
            if x.next.data > max.data:
                max = x.next
            x = x.next
        return max
    # klasy O(N)
    # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.

    def reverse(self):
        temp = SingleList()
        while self.length != 0:
            x = self.remove_head()
            temp.insert_head(x)
        return temp
    # klasy O(N)
    # Odwracanie kolejności węzłów na liście.
