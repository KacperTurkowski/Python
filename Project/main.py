from Baza import *
import pandas as pd
import os.path
# Baza.py danych książek, płyt, itp.
# Baza.py powinna być zapisywana do pliku (txt, CSV, JSON).
# Operacje na bazie: wstawianie, usuwanie, wyszukiwanie, listowanie.

if not os.path.exists('.data/base.csv'):
    f = open('.data/base.csv', 'w')
    f.write("typ danych,adrestabeli")
    f.close()

df = pd.read_csv('.data/base.csv')

print("Witaj w wirtualnej bazie książek.")
temp = ""
question = """Co chciałbyś zrobić? 
    Aby wstawić objekt do biblioteki wpisz: wstawianie
    Aby usunąć obiekt z biblioteki wpisz: usuwanie
    Aby wyszukać obiekt w bibliotece wpisz: wyszukiwanie
    Aby wypisać obiekty z biblioteki wpisz: listowanie
    Aby zakończyć działanie programu wpisz: koniec
    """
while temp != "koniec":
    print(question)
    df = pd.read_csv('.data/base.csv')
    temp = input()
    if temp == "wstawianie":
        wstawianie(df)
    elif temp == "usuwanie":
        usuwanie(df)
    elif temp == "wyszukiwanie":
        wyszukiwanie(df)
    elif temp == "listowanie":
        listowanie(df)

print("Do widzenia")
