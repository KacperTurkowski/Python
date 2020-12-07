import pandas as pd


def wstawianie(df):
    print("Do której tabli chcesz wstawić record?")
    print("Aby wybrać tabelę wpisz jej numer, jeśli chcesz utworzyć nową tabelę wpisz \" utworz \"")
    i = 1
    for x in df['typ_danych'].values:
        print(str(i)+". "+x)
        i += 1

    temp = input("Podaj numer tabeli: ")
    i = 0
    if temp == 'utworz':
        utworz_typ(df)
        return
    try:
    
    add(df['adres_tabeli'][temp+1])


def add(address):
    df = pd.read_csv(address)
    array = [[]]
    for x in df.columns:
        print('Podaj pole dla kolumny: '+x)
        array[0].append(input())
    df = df.append(pd.DataFrame(array, columns=df.columns))
    print(df)
    df.to_csv(address, index=False)


def utworz_typ(df):
    datatype = input("Podaj nazwę tabeli: ")
    address = '.data/'+datatype + '.csv'
    df = df.append({'adres_tabeli': address, 'typ_danych': datatype}, ignore_index=True)
    df.to_csv('.data/base.csv', index=False)
    print("Wpisz nazwy kolumn dla tej tabeli")
    print("Nazwy podaj w formacie \"Parametr1,Parametr2,Parametr3,Parametr4\"")
    f = open(address, 'w')
    f.write(input())
    f.close()


def usuwanie(df):
    print("Obiekt z której tabeli chcesz usunąć?")
    print("Aby wybrać tabelę podaj jej indeks")
    i = 1
    for x in df['typ_danych'].values:
        print(str(i) + ". " + x)
        i += 1
    column = read_int("Podaj numer kolumny: ", i)
    df_new = pd.read_csv(df['adres_tabeli'][column-1])
    print(df_new)
    print("Który rekord chcesz usunąć(Proszę podać numer): ")
    row = read_int("Który rekord chcesz usunąć(Proszę podać numer): ", len(df_new.values))
    df_new = df_new[:row].append(df_new[row+1:])
    df_new.to_csv(df['adres_tabeli'][column-1], index=False)


def wyszukiwanie(df):
    temp = input("Podaj frazę do wyszukania w bazie danych: ")
    result = []

    for tables in df.values:
        df_temp = pd.read_csv(tables[0])
        for i in df_temp.columns:
            df_column_temp = pd.DataFrame(df_temp[i])
            for j in range(len(df_column_temp.values)):
                if temp in df_column_temp.values[j][0]:
                    result.append("dział: " + tables[1] + " record: " + " " + str(df_temp.values[j].tolist()))
    for i in result:
        print(i)


def listowanie(df):
    print("Jaką tabelę chcesz wylistować?")
    print("Aby wybrać tabelę podaj jej indeks")
    i = 1
    for x in df['typ_danych'].values:
        print(str(i) + ". " + x)
        i += 1
    column = int(input("Podaj nazwę: "))
    df_new = pd.read_csv(df['adres_tabeli'][column - 1])
    print(df_new)


def read_int(str, max):
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
            print("Podaj liczbę całkowitą z zakresu 0 - ", max)
    return x
