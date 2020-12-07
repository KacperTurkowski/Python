import pandas as pd
import os.path
from Functions import *

# Baza.py danych książek, płyt, itp.
# Baza.py powinna być zapisywana do pliku (txt, CSV, JSON).
# Operacje na bazie: wstawianie, usuwanie, wyszukiwanie, listowanie.

# Jeśli nie istnieje tabela z adresami do innych tabel, to utwórz ją
if not os.path.exists('.data/base.csv'):
    f = open('.data/base.csv', 'w')
    f.write("adres_tabeli,nazwa_tabeli")
    f.close()


print("Witaj w wirtualnej Bazie danych")

question = """Co chciałbyś zrobić? 
    Aby wstawić obiekt do biblioteki wpisz: insert
    Aby usunąć obiekt z biblioteki wpisz: delete
    Aby utworzyć nową tabelę wpisz: create
    Aby usunąć tabelę wpisz: delete_table
    Aby wyszukać obiekt w bibliotece wpisz: search
    Aby wypisać obiekty z biblioteki wpisz: list
    Aby zakończyć działanie programu wpisz: end
    
    :"""

temp = ""
while True:
    # z pliku csv wyciągam adresy oraz nazwy tabel
    df = pd.read_csv('.data/base.csv')

    temp = input(question)
    temp = temp.lower()
    temp = temp.strip()
    print("\n\n\n\n\n")
    if temp == "insert":
        insert(df)
    elif temp == "create":
        create(df)
    elif temp == "delete_table":
        delete_table(df)
    elif temp == "delete":
        delete(df)
    elif temp == "search":
        search(df)
    elif temp == "list":
        to_list(df)
    elif temp == "end":
        break
    else:
        print("Proszę wybrać jedną z dostępnych opcji \n")

print("\n\n\n\n\n\n\n\n\n Do zobaczenia")
