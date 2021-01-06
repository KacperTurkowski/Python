import random


class RandomQueue:

    def __init__(self):
        self.elements = []

    def insert(self, item):
        self.elements.append(item)

    def remove(self):  # zwraca losowy element
        index = random.randint(0, len(self.elements)-1)
        element = self.elements[index]
        self.elements[index] = self.elements[-1]
        self.elements[-1] = element
        return self.elements.pop()

    def is_empty(self):
        if len(self.elements) != 0:
            return False
        else:
            return True

    def is_full(self):
        return False

    def clear(self):  # czyszczenie listy
        self.elements = []
