import re

line = """Guido van Rossum (GvR) (ur. 31 stycznia 1956 r. w Haarlem)
    holenderski programista
twórca języka   programowania Python."""

L = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 99, 101, 199, 999]

# 2.10 Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami
# (spacja, tabulacja, newline).

lineTab = line.split(None)
print("#2.10 Liczba słów:"+str(len(lineTab)))

# 2.11 Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

x = "word"
y = ""
for i in range(0, len(x) - 1):
    y += x[i] + "_"
y += x[len(x) - 1]
print("#2.11: "+y)

# 2.12 Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
# Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

firstChar = ""
lastChar = ""
for word in lineTab:
    firstChar += word[0]
    lastChar += word[-1]
print("#2.12 pierwsze znaki: " + firstChar + "\n      ostatnie znaki: " + lastChar)

# 2.13 Znaleźć łączną długość wyrazów w napisie line.

print("#2.13 długość wyrazów w napisie: "+str(len(re.sub('\s', "", line))))

# 2.14 Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

longest = lineTab[0]
for x in lineTab:
    if len(x) > len(longest):
        longest = x

print("#2.14 najdłuższy wyraz: " + longest + "\n      długość tego wyrazu: "+str(len(longest)))# długość można znaleźć także: str(max(len(w) for w in lineTab))

# 2.15 Na liście L znajdują się liczby całkowite dodatnie.
# Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

print("#2.15 Napis będący ciągiem cyfr z listy L: "+''.join(map(str, L)))

# 2.16 W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

line = re.sub('GvR', "Guido van Rossum", line)
print("#2.16 Zmieniony napis: " + line)

# 2.17 Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.

print('#2.17 słowa posortowane alfabetycznie: '+str(sorted(lineTab))+"\n      słowa posortowane pod względem długości: " + str(sorted(lineTab, key=len)))

# 2.18 Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

K = 121314829415431032951723403233
print("#2.18 Liczba zer w liczbie " + str(K) + " : " + str(len(re.findall('0', str(K)))))

# 2.19 Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami.

abc = ""
for x in L:
    abc += str(x).zfill(3)
print("#2.19 Napis dopełniony zerami: " + abc)
