class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node     # stary head
            self.head = node          # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node     # stary tail
            self.tail = node          # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            node.next = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            node.prev = None
            self.length -= 1
            return node

    def find_max(self):
        max = self.head
        x = self.head
        while x.next != None:
            if x.next.data > max.data:
                max = x.next
            x = x.next
        return max
    # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.

    def find_min(self):
        min = self.head
        x = self.head
        while x.next != None:
            if x.next.data < min.data:
                min = x.next
            x = x.next
        return min
    # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def remove(self, node):
        prevN = node.prev
        nextN = node.next
        if prevN == None and nextN == None:
            self.head = None
            self.tail = None
            self.length = 0
        elif prevN == None:
            nextN.prev = None
            self.head = nextN
        elif nextN == None:
            prevN.next = None
            self.tail = prevN
        else:
            prevN.next = nextN
            nextN.prev = prevN
    # Usuwa wskazany węzeł z listy.

    def clear(self):
        while self.length != 0:
            x = self.remove_head()
            # czyszczenie listy
