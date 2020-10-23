import re

line = """Guido van Rossum (GvR) (ur. 31 stycznia 1956 r. w Haarlem)
    holenderski programista
twórca języka   programowania Python."""

L = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 99, 101, 199, 999]

K = 121314829415431032951723403233

# 2.10 Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami
# (spacja, tabulacja, newline).

print("#2.10 Liczba słów:" + str(len(line.split(None))))

# 2.11 Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

x = "word"
y = x[0]
for i in range(1, len(x)):
    y += "_" + x[i]
print("#2.11: " + y)

# 2.12 Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
# Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

firstChar = ""
lastChar = ""
for word in line.split(None):
    firstChar += word[0]
    lastChar += word[-1]
print("#2.12 pierwsze znaki: " + firstChar + "\n      ostatnie znaki: " + lastChar)

# 2.13 Znaleźć łączną długość wyrazów w napisie line.

print("#2.13 długość wyrazów w napisie: " + str(len(re.sub('\s', "", line))))

# 2.14 Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

longest = sorted(line.split(None), key=len, reverse=True)[0]
print("#2.14 najdłuższy wyraz: "+longest+"\n      długość tego wyrazu: "+str(len(longest)))

# 2.15 Na liście L znajdują się liczby całkowite dodatnie.
# Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

print("#2.15 Napis będący ciągiem cyfr z listy L: " + ''.join(map(str, L)))

# 2.16 W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

print("#2.16 Zmieniony napis: " + re.sub('GvR', "Guido van Rossum", line))

# 2.17 Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.

print('#2.17 słowa posortowane alfabetycznie: ' + str(sorted(line.split(None))) + "\n      słowa posortowane pod względem długości: " + str(sorted(line.split(None), key=len)))

# 2.18 Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

print("#2.18 Liczba zer w liczbie " + str(K) + " : " + str(len(re.findall('0', str(K)))))

# 2.19 Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami.

print("#2.19 Napis dopełniony zerami: " + ''.join(map(str, [str(x).zfill(3) for x in L])))
