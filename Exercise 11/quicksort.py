import module


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def division(array, l, r):
    i = l-1
    x = array[r]

    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1


def quicksort(array, l, r):
    size = r-l+1

    stack = Stack()
    stack.push(-1)
    stack.push(l)
    stack.push(r)

    while len(stack.items) >= 2:

        r = stack.pop()
        l = stack.pop()

        p = division(array, l, r)

        if p-1>l:
            stack.push(l)
            stack.push(p-1)
        if p+1<r:
            stack.push(p+1)
            stack.push(r)


array = module.getrandom(10)
print("Lista przed posortowaniem: ", array)
quicksort(array, 0, len(array)-1)
print("Lista po posortowaniu: ", array)
