class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def count_leafs(top):
        if top.left is None and top.right is None:  # jestem w liściu
            return 1
        left = 0
        right = 0
        if top.left is not None:
            left = top.left.count_leafs()  # lewa gałąź
        if top.right is not None:
            right = top.right.count_leafs()  # Prawa gałąź
        return left + right

    def count_total(top):
        if top.left is None and top.right is None:  # jestem w liściu
            return top.data
        left = 0
        right = 0
        if top.left is not None:
            left = top.left.count_total()  # lewa gałąź
        if top.right is not None:
            right = top.right.count_total()  # Prawa gałąź
        return left + right + top.data
