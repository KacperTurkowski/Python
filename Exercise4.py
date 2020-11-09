def readint():
    while True:
        check = True
        x = input("Proszę podać liczbę: ")
        try:
            x = int(x)
        except ValueError:
            print("Nie jest to typ int")
            check = False
        if check:
            break
    return x


# zadanie 4.1
# Jaki będzie wynik poniższego kodu i dlaczego?
X = "qwerty"


def func():
    print(X)


func()
print("#4.1 Program wypiszę zmienną X czyli qwerty")


def func():
    X = "abc"


func()
print(X)
print(
    "#4.1 Program wypiszę zmienną X czyli qwerty, ponieważ wewnątrz funkcji tworzy się nowa zmienna o tej samej nazwie, ale nie jest to ta sama zmienna.")

X = "qwerty"


def func():
    global X
    X = "abc"


func()
print(X)
print("#4.1 Program wypiszę abc, ponieważ słowo kluczowe global umożliwia nam nadpisywanie zmiennej globalnej wewnątrz funkcji")


# zadanie 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return

def ruller(x):
    check = True
    scale = "....|"
    ruler = ['|', '0']
    for i in range(1, x + 1):
        ruler[0] += scale
        ruler[1] += "%5s" % i
    return ruler[0] + "\n" + ruler[1]


print("#4.2 a): ")

print(ruller(readint()))


def rectangle(x, y):
    arrayV = '|'
    arrayH = '+'
    vertical = '   |'
    horizontal = '---+'
    result = ''
    for i in range(1, x + 1):
        arrayV += vertical
        arrayH += horizontal
    for i in range(1, y + 1):
        result += arrayH + '\n'
        result += arrayV + '\n'
    result += arrayH
    return result


print("#4.2 b): ")
print(rectangle(readint(), readint()))


# ZADANIE 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.


def factorial(n):
    if n < 0:
        return "value is smaller than 0"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print("4.3:")
print(factorial(readint()))


# ZADANIE 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
#[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
def fibonacci(n):
    bigger, smaller = 0, 1
    for i in range(1, n+1):
        temp = bigger
        bigger += smaller
        smaller = temp
    return bigger


print("#4.4")
print(fibonacci(readint()))
# ZADANIE 4.5
# Napisać funkcję odwracanie(L, left, right)
# odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
l, r = 3, 9
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("#4.5")


def odwracanieIter(L, left, right):
    temp = L[0:]
    while left <= right:
        temp[left], temp[right] = temp[right], temp[left]
        left += 1
        right -= 1
    return temp


def odwracanieRekur(L, left, right):
    temp = L[0:]
    if left > right:
        return temp
    temp = odwracanieRekur(temp, left + 1, right - 1)
    temp[left], temp[right] = temp[right], temp[left]
    return temp


print("Odwracanie Rekurencyjne: "+str(odwracanieRekur(li, l, r)))
print("Odwracanie Iteracyjne: "+str(odwracanieIter(li, l, r)))

# ZADANIE 4.6
# Napisać funkcję sum_seq(sequence)
# obliczającą sumę liczb zawartych w sekwencji,
# która może zawierać zagnieżdżone podsekwencje.
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("#4.6")


def sum_seq(sequence):
    sum = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            sum += sum_seq(x)
        else:
            sum += x
    return sum


print("Suma cyfr w sekwencji "+str(seq)+" wynosi: "+str(sum_seq(seq)))
# ZADANIE 4.7
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.


def flatten(sequence):
    result = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result


print("#4.7: ")
print(flatten(seq))
