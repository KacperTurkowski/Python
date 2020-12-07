import pandas as pd
import os

def read_int(str, min, max):
    check = False
    while not check:
        x = input(str)
        check = True
        try:
            x = int(x)
        except ValueError:
            check = False
        if check and not (0 <= x <= max):
            check = False
        if not check:
            print("Podaj liczbę całkowitą z zakresu: ", min, " - ", max)
    return x


def write_data(df):
    for i in range(0, len(df.values)):    # wypisuje wszystkie możliwe tabele
        print(str(i+1) + ". " + df[i])


def insert(dataframe):  # wstawianie obiektu do biblioteki
    write_data(dataframe['nazwa_tabeli'])  # wypisuje wszystkie możliwe tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 1, (len(dataframe.nazwa_tabeli)))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    df = pd.read_csv(dataframe.adres_tabeli[table_index-1])  # odczytuje tabelę z odpowiedniego pliku

    array = [[]]
    for i in range(0, len(df.columns.values)):    # wypisuje wszystkie kolumny
        print(str(i+1) + ". " + df.columns[i])
        data = ''
        while data == '':
            data = input("Podaj wartość którą chcesz wpisać w tą kolumnę: ")
            data = data.strip()

        array[0].append(data)

    df = df.append(pd.DataFrame(array, columns=df.columns))  # Dodaje do dataframe nowy wiersz
    df.to_csv(dataframe.adres_tabeli[table_index-1], index=False)  # zapisuje DataFrame do pliku


def create(dataframe):  # tworzenie nowej tabeli
    name = ''
    while name == '':  # Nazwa Tabeli nie może być pusta
        name = input("Podaj nazwę nowej tabeli: ")
        name = name.strip()
    address = '.data/'+name+'.csv'  # tworzy adres nowej tabeli
    dataframe = dataframe.append({'adres_tabeli': address, 'nazwa_tabeli': name}, ignore_index=True)  # dodaje nową tabelę do listy tabel
    dataframe.to_csv('.data/base.csv', index=False)  # tworzy tabelę

    columns = ""
    question = """Podaj nowej nazwę kolumny 
    (Jeśli dodałeś już wszystkie tabele wpisz end)
    :"""
    temp = ''
    while temp != "end":
        temp = input(question)
        temp = temp.strip()  # usuwam spację
        if temp != "" and temp != "end":  # nazwa kolumny nie może byc pusta
            columns += temp + ','

    # zapis do pliku
    f = open(address, 'w')
    f.write(columns[:-1])  # zapisuje bez ostatniego przecinka
    f.close()


def delete_table(dataframe):
    write_data(dataframe.nazwa_tabeli)  # wypisuje tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 1, (len(dataframe.nazwa_tabeli)))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    table_index -= 1
    os.unlink(dataframe.adres_tabeli[table_index])
    dataframe = dataframe[:table_index].append(dataframe[table_index+1:])

    dataframe.to_csv('.data/base.csv', index=False)



def delete(dataframe):
    write_data(dataframe['nazwa_tabeli'])  # wypisuje wszystkie możliwe tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 1, (len(dataframe.nazwa_tabeli)))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    df = pd.read_csv(dataframe.adres_tabeli[table_index - 1])  # odczytuje tabelę z odpowiedniego pliku
    if len(df.values) == 0:
        print("Ta tabela jest pusta")
        return
    print(df)
    if len(df.values) != 0:
        row_index = read_int("\n\n\n\n\n\nAby wybrać record wpisz jego indeks: ", 0, (len(dataframe.nazwa_tabeli)))
    df = df[:row_index].append(df[row_index+1:])
    df.to_csv(dataframe.adres_tabeli[table_index - 1], index=False)


def search(dataframe):
    temp = input("Podaj frazę do wyszukania w bazie danych: ")
    result = []

    for tables in dataframe.values:
        df_temp = pd.read_csv(tables[0])
        for i in df_temp.columns:
            df_column_temp = pd.DataFrame(df_temp[i])
            for j in range(len(df_column_temp.values)):
                if temp in df_column_temp.values[j][0]:
                    result.append("dział: " + tables[1] + " record: " + " " + str(df_temp.values[j].tolist()))
    for i in result:
        print(i)


def to_list(dataframe):
    write_data(dataframe['nazwa_tabeli'])  # wypisuje wszystkie możliwe tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 1, (len(dataframe.nazwa_tabeli)))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    df = pd.read_csv(dataframe.adres_tabeli[table_index - 1])  # odczytuje tabelę z odpowiedniego pliku
    if len(df.values) == 0:
        print("Tabela jest pusta")
        return
    print(df)
