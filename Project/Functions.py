import io
import prettytable
import pandas as pd
import os


def read_int(str, min, max):
    """funkcja wczytuje z konsoli int w przedziale (min,max) prezentując zapytanie które jest zapisane w str."""
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
    """wypisuje dane z podanego w argumencie dataframe"""
    output = io.StringIO()
    df.to_csv(output, encoding="utf-8")
    output.seek(0)
    pt = prettytable.from_csv(output, encoding="utf-8")
    print(pt)


def insert(dataframe):  # wstawianie obiektu do biblioteki
    """w tej funkcji opisana jest funkcja dodawania recordów do bazy danych"""
    write_data(dataframe['nazwa_tabeli'])  # wypisuje wszystkie możliwe tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 0, (len(dataframe.nazwa_tabeli)-1))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    df = pd.read_csv(dataframe.adres_tabeli[table_index], encoding="utf-8")  # odczytuje tabelę z odpowiedniego pliku

    array = [[]]
    for i in range(0, len(df.columns.values)):    # wypisuje wszystkie kolumny
        print(str(i+1) + ". " + df.columns[i])
        data = ''
        while data == '':
            data = input("Podaj wartość którą chcesz wpisać w tą kolumnę: ")
            data = data.strip()

        array[0].append(data)

    df = df.append(pd.DataFrame(array, columns=df.columns))  # Dodaje do dataframe nowy wiersz
    df.to_csv(dataframe.adres_tabeli[table_index], index=False, encoding="utf-8")  # zapisuje DataFrame do pliku


def removeAccents(input_text):
    """funkcja zamienia znaki z kodowania UTF-8 na ascii przy nazwach pliku"""
    strange = 'ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'

    ascii_replacements = 'UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'

    translator = str.maketrans(strange, ascii_replacements)

    return input_text.translate(translator)


def create(dataframe):  # tworzenie nowej tabeli
    """w tej funkcji opisana jest funkcja dodawania tabeli do bazy danych"""
    name = ''
    while name == '':  # Nazwa Tabeli nie może być pusta
        name = input("Podaj nazwę nowej tabeli: ")
        name = name.strip()

    asciidata = removeAccents(name)

    address = '.data/'+asciidata+'.csv'  # tworzy adres nowej tabeli
    dataframe = dataframe.append({'adres_tabeli': address, 'nazwa_tabeli': name}, ignore_index=True)  # dodaje nową tabelę do listy tabel
    dataframe.to_csv('.data/base.csv', index=False, encoding="utf-8")  # tworzy tabelę

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
    f = open(address, 'w', encoding="utf-8")
    f.write(columns[:-1])  # zapisuje bez ostatniego przecinka
    f.close()


def delete_table(dataframe):
    """w tej funkcji opisana jest funkcja usuwania tabeli z bazy danych"""
    write_data(dataframe.nazwa_tabeli)  # wypisuje tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 0, (len(dataframe.nazwa_tabeli)-1))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    table_index -= 1
    os.unlink(dataframe.adres_tabeli[table_index+1])
    dataframe = dataframe[:table_index+1].append(dataframe[table_index+2:])

    dataframe.to_csv('.data/base.csv', index=False, encoding="utf-8")


def delete(dataframe):
    """w tej funkcji opisana jest funkcja usuwania recordu z bazy danych"""
    write_data(dataframe['nazwa_tabeli'])  # wypisuje wszystkie możliwe tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 0, (len(dataframe.nazwa_tabeli)-1))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    df = pd.read_csv(dataframe.adres_tabeli[table_index], encoding="utf-8")  # odczytuje tabelę z odpowiedniego pliku
    if len(df.values) == 0:
        print("Ta tabela jest pusta")
        return
    print(df)
    if len(df.values) != 0:
        row_index = read_int("\n\n\n\n\n\nAby wybrać record wpisz jego indeks: ", 0, (len(df.values)))
    df = df[:row_index].append(df[row_index+1:])
    df.to_csv(dataframe.adres_tabeli[table_index], index=False, encoding="utf-8")


def search(dataframe):
    """w tej funkcji opisana jest funkcja wyszukiwania recordu z bazy danych"""
    temp = input("Podaj frazę do wyszukania w bazie danych: ")
    result = []

    for tables in dataframe.values:
        df_temp = pd.read_csv(tables[0], encoding="utf-8")
        for i in df_temp.columns:
            df_column_temp = pd.DataFrame(df_temp[i])
            for j in range(len(df_column_temp.values)):
                if temp in df_column_temp.values[j][0]:
                    result.append("dział: " + tables[1] + " record: " + " " + str(df_temp.values[j].tolist()))
    for i in result:
        print(i)


def to_list(dataframe):
    """w tej funkcji opisana jest funkcja wypisywania tabeli z bazy danych"""
    write_data(dataframe['nazwa_tabeli'])  # wypisuje wszystkie możliwe tabele

    if len(dataframe.nazwa_tabeli) != 0:  # Jeśli istnieją tabele
        table_index = read_int("\n\n\n\n\n\nAby wybrać tabelę wpisz jej indeks: ", 0, (len(dataframe.nazwa_tabeli)-1))
    elif len(dataframe.nazwa_tabeli) == 0:  # Jeśli nie ma tabel
        print("Brak tabel\n utwórz nową")
        return
    df = pd.read_csv(dataframe.adres_tabeli[table_index], encoding="utf-8")  # odczytuje tabelę z odpowiedniego pliku
    if len(df.values) == 0:
        print("Tabela jest pusta")
        return
    output = io.StringIO()
    df.to_csv(output, encoding="utf-8")
    output.seek(0)
    pt = prettytable.from_csv(output, encoding="utf-8")
    print(pt)

