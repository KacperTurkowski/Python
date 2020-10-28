# 3.1 Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
# a)
x = 2;
y = 3;
if (x > y):
    result = x;
else:
    result = y;
# Odp.: Kod poprawny niepotrzebne średniki oraz bezsensowny if
# b)
# for i in "qwerty": if ord(i) < 100: print (i)
# Odp.: Niepoprawny, wszystko po dwukropku należy przenieść do następnej linijki
# c)
# for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Odp.: Niepoprawny, wszystko po dwukropku należy przenieść do następnej linijki

# 3.2 Co jest złego w kodzie:
# a)
# L = [3, 5, 4] ; L = L.sort()
# Odp.: Funkcja sort nie zwraca niczego
# b)
# x, y = 1, 2, 3
# Odp.: Błędny, trzy liczby są przypisywane do dwóch zmiennych
# c)
# X = 1, 2, 3 ; X[1] = 4
# Odp.: Błędny, krotki są niezmiennymi sekwencjami
# d)
# X = [1, 2, 3] ; X[3] = 4
# Odp.: Błędny, przypisanie poza zakresem tablicy
# e)
# X = "abc" ; X.append("d")
# Odp.: Błędny, funkcji append nie można wywołać na obiekcie typu string
# f)
# L = list(map(pow, range(8)))
# Odp.:Błędny, funkcja pow wymaga conajmniej dwóch argumentów

# 3.3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
print("#3.3: ")
[print(x, end=" ") for x in range(0, 30) if (x % 3 != 0)]

# 3.4 Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
# i wypisujący parę x i trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i
# kontynuować pracę.
print("\n#3.4: ")
while True:
    x = input("Proszę podać liczbę: ")
    if x == "stop":
        break
    else:
        try:
            x = float(x)
        except ValueError:
            print("Nie jest to typ float")
        print(str(x) + " " + str(pow(x, 3)))

#  3.5 Napisać program rysujący "miarkę" o zadanej długości.
#  Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
#  (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
#  Należy zbudować pełny string, a potem go wypisać.
print("#3.5: ")
check = True
scale = "....|"
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

ruler = ['|', '0']
for i in range(1, x+1):
    ruler[0] += scale
    ruler[1] += "%5s" % i
print(ruler[0]+"\n"+ruler[1])
# 3.6 Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.
# Przykładowy prostokąt składający się 2x4 pól ma postać:
print("#3.6: ")
while True:
    check = True
    x = input("Proszę podać współrzędną x: ")
    y = input("Proszę podać współrzędną y: ")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Nie jest to typ int")
        check = False
    if check:
        break

arrayV = '|'
arrayH = '+'
vertical = '   |'
horizontal = '---+'
result = ''
for i in range(1, x+1):
    arrayV += vertical
    arrayH += horizontal
for i in range(1, y+1):
    result += arrayH + '\n'
    result += arrayV + '\n'
result += arrayH
print(result)

# 3.8 Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach
# (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
print("#3.8: ")
first = [(0, 4, 5, 9), (3, 4, 13), (1, 2, 678, 79)]
second = [[1, 3, 9, 17], (13, 22, 2), [3, 4], (55, 6, 7)]
Set1 = set()
Set2 = set()
for element in second:
    Set1.update(set(element))
for element in first:
    Set2.update(set(element))
print(Set1.intersection(Set2))
print(Set1.union(Set2))
# 3.9 Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
print("#3.9: ")
sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(list(map(lambda temp: sum(temp), sequence)))
# 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
# (z literami I, V, X, L, C, D, M) na liczby arabskie
# (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
print("#3.10: ")
line = 'MCDIV'
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0
i = 0

while True:
    if i >= len(line):
        break
    current = int(roman[line[i]])
    if i != len(line)-1 and int(roman[line[i+1]]) > current:
        result += int(roman[line[i+1]]) - current
        i += 1
    else:
        result += current
    i += 1
print(result)
