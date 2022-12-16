# Program powinien poprawnie działać jeżeli przy pierwszym uruchomieniu programu pliki magazyn.csv i magazyn_sprzedaz.csv będą puste a w pliku zmienne.csv bedą dwie wartości 0

from magazyn_funkcje import get_items, add_item, sell_item, lista_sprzedanych_towarów,  show_revenue, dostepne_towary, jaka_cena_zakupu
from magazyn_funkcje import export_items_to_csv, export_sales_to_csv, load_items_from_csv, load_sold_items_from_csv, check_item, cena_itema_w_magazynie
from magazyn_funkcje import sprawdzam_cene_sprzedazy, ile_sztuk_w_magazynie, czy_towar_w_magazynie, dostepni_klienci, czy_klient_na_liscie
import csv


def zapis_zmiennych():                  # funkcja zapisuje zmienne koszt_calkowity oraz zyski w pliku zmienne.csv

    with open('zmienne.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

        writer.writerow([koszt_calkowity])
        writer.writerow([zyski])


def odczyt_zmiennych():                  # funkcja wczytuje zmienne koszt_calkowity oraz zyski z pliku zmienne.csv
    with open('zmienne.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            row = float(row[0])
            zmienne.append(row)


zmienne = []


odczyt_zmiennych()

wybor = ''
koszt_calkowity = zmienne[0]
zyski = zmienne[1]


# Ładowanie danych z plików wraz ze startem programu

load_items_from_csv()
load_sold_items_from_csv()


while wybor != 9:
    print()
    print()
    print("--------------------")
    print("1. Dodaj towar - Add")
    print("2. Sprzedaj - Sell")
    print("3. Wyświetl liste towarów w magazynie - show")
    print("4. Wyświetl liste sprzedanych towarów")
    print("5. Zestawienie finansowe")
    print("6. Zapis stanu magazynu i sprzedanych towarów - opcja")
    print("7. Wczytuje stan magazynu z pliku magazyn.csv - opcja")
    print("8. Wczytuje sprzedane towary z pliku magazyn_sprzedaz.csv - opcja")
    print("9. Wyjście z programu ")
    print("0. Baza klientów")
    print("------------------")
    print()

    wybor = ''
    while isinstance(wybor, int) == False:

        try:
            wybor = input("Wybierz działanie (0 - 9):  ")
            if int(wybor) >= 0 and int(wybor) <= 9:
                wybor = int(wybor)
            else:
                print("Wpisałeś liczbę całkowitą z poza zakresu 1 - 9")
        except:
            print("Wpisałeś bzdury")

    if wybor == 1:
        item_name = '1'
        item_price = ''
        item_unit = ''

        print("Wybrałeś dodanie towaru - add")

        while item_name[0].isnumeric() == True or len(item_name) <= 3:

            try:
                item_name = input("Item name: ")
                if len(item_name) == 0:
                    item_name = '1'
                    print(
                        "Zerowa dlugosc nazwy towaru. Czy nacisnąłeś Enter ?? Cwaniaczku")

                elif len(item_name) <= 3:
                    print("Nazwa towaru musi mieć co najmniej 4 znaki")

                elif item_name[0].isnumeric() == True:
                    print("Nazwa towaru nie może rozpoczynać się od cyfry. ")

                elif len(item_name) == None:
                    print("dlugosc nazwy towaru wynosi none")

                elif len(item_name) == True:
                    print("True")

                elif len(item_name) == False:
                    print("False")
            except:
                print("kij ci w oko")

        # wywołanie funkcji check_item  zwraca 0 jesli dodawanego towaru nie ma w magazynie i 1 kiedy juz jest w magazynie
        print(check_item(item_name))

        if check_item(item_name) == 0:
            print("Tego towaru nie ma jeszcze w magazynie")

            # Tu pisać kod jeśli towaru nie ma w magazynie

            item_quantity = ''

            while isinstance(item_quantity, int) == False:
                try:
                    # item_quantity = int(input("Item quantity: "))
                    item_quantity = input("Item quantity: ")
                    if int(item_quantity) > 0:
                        item_quantity = int(item_quantity)
                    else:
                        print("Podaj dodatnią ilość sztuk np: 1, 20 lub 50")

                except:
                    print("Podaj prawidłową liczbę. ")

            # można zrobić zeby długosc była przynajmniej 1 znak i ten znak nie może być cyfrą (tylko literą alfabetu)

            while len(item_unit) < 1 or len(item_unit) > 6:
                try:
                    item_unit = input(
                        "Item unit of measure: (L, unit, kg, pcs, bottle, box, jar etc ...) ")
                    if len(item_unit) > 7:
                        print("Za długa nazwa jednostki!")
                except:
                    print("Co ty robisz?")

            # item_price = string
            while isinstance(item_price, int) == False and isinstance(item_price, float) == False:

                try:
                    item_price = input("Item price: ")
                    if float(item_price) > 0.01:
                        item_price = float(item_price)
                    else:
                        print("Cena zakupu musi być wyższa niż 0.01")
                except:
                    print("Podaj prawidłową liczbę, np: 5 lub 5.1 ")

        elif check_item(item_name) == 1:
            print("Towar o tej nazwie jest już na stanie magazynowym")

            # Tu pisać kod jeśli towar jest w magazynie
            item_quantity = ''

            while isinstance(item_quantity, int) == False:
                try:
                    item_quantity = input("Item quantity: ")
                    if int(item_quantity) > 0:
                        item_quantity = int(item_quantity)
                    else:
                        print("Podaj dodatnią ilość sztuk np: 1, 20 lub 50")
                except:
                    print("Podaj prawidłową liczbę. ")

            item_unit = ''
            item_price = cena_itema_w_magazynie(item_name)

        koszt_calkowity = koszt_calkowity + (item_quantity * item_price)
        add_item(item_name, item_quantity, item_unit, item_price)
        get_items()

        # zapis w pliku magazyn.csv
        export_items_to_csv()
        zyski = round(show_revenue() - koszt_calkowity, 2)
        zapis_zmiennych()

    elif wybor == 2:

        ncs = ''
        zmiana_ceny = ''
        sprzedana_ilosc = ''
        nazwa_towaru = ''
        nazwa_klienta = ''

        print("Wybrałeś sprzedaż z magazynu - Sell")
        print("Dostępne towary: ")
        dostepne_towary()           # wywołanie funkcji: dostepne_towary

        while czy_towar_w_magazynie(nazwa_towaru) == False:

            try:
                nazwa_towaru = input("Podaj nazwe towaru na sprzedaż: ")
                if czy_towar_w_magazynie(nazwa_towaru) == False:
                    print("Tego towaru nie ma w magazynie. ")
                elif czy_towar_w_magazynie(nazwa_towaru) == True:
                    print()
                    print("OK. Sprzedajemy :)) ")
                    print()
            except:
                print("Tego towaru nie ma w magazynie.")

        while isinstance(sprzedana_ilosc, int) == False:
            try:
                sprzedana_ilosc = input("Ilość towaru na sprzedaż: ")
                if int(sprzedana_ilosc) > 0:
                    sprzedana_ilosc = int(sprzedana_ilosc)
                else:
                    print("Podaj dodatnią ilość sztuk np: 1, 20 lub 50")
            except:
                print("Wpisz dodatnią liczbę np: 100")

        # tu pisze kod który sprawdza czy w magazynie jest wystarczaja ca liczba sztuk na sprzedaż

        while ile_sztuk_w_magazynie(nazwa_towaru) < sprzedana_ilosc:
            print("Nie masz wystarczającej ilości towaru o nazwie: ", nazwa_towaru,
                  " W magazynie pozostało ", ile_sztuk_w_magazynie(nazwa_towaru), " sztuk.")

            sprzedana_ilosc = ''

            while isinstance(sprzedana_ilosc, int) == False:
                try:
                    sprzedana_ilosc = input(
                        "Ile sztuk towaru %s chcesz sprzedać? " % nazwa_towaru)
                    if int(sprzedana_ilosc) > 0:
                        sprzedana_ilosc = int(sprzedana_ilosc)
                    else:
                        print("Podaj dodatnią ilość sztuk np: 1, 20 lub 50")
                except:
                    print("Wpisz dodatnią liczbę np: 100")

        # drukuje cene sprzedazy jeśli była jz sprzedaż dla danego towaru
        print("Poprzednia cena sprzedaży: ",
              sprawdzam_cene_sprzedazy(nazwa_towaru))

        #print("Nowa cena sprzedaży wynosi: ", zmiana_ceny_sprzedazy(nazwa_towaru))

        #ncs1 = zmiana_ceny_sprzedazy(nazwa_towaru)

        while zmiana_ceny != 'y' and zmiana_ceny != 'n':
            try:
                zmiana_ceny = input(
                    "Czy chcesz ustalić / zmienić cenę sprzedaży? (y / n) ")

                if zmiana_ceny == 'y':

                    # ncs = string
                    while isinstance(ncs, int) == False and isinstance(ncs, float) == False:
                        try:
                            # ncs - nowa cena sprzedazy
                            ncs = input("Podaj nową cenę sprzedaży: ")
                            if float(ncs) > 0.01:
                                ncs = float(ncs)
                            else:
                                print("Cena sprzedaży musi być większa niż zero")
                        except:
                            print("Podaj prawidłową liczbę, np: 5 lub 5.2 ")

                    while jaka_cena_zakupu(nazwa_towaru) >= ncs:
                        print("Cena sprzedaży nie może być mniejsza od ceny zakupu")
                        print("Cena zakupu towaru o nazwie: ", nazwa_towaru, " wynosi ", jaka_cena_zakupu(
                            nazwa_towaru), "wpisz wyższą cenę sprzedaży.")

                        ncs = ''

                        while isinstance(ncs, int) == False and isinstance(ncs, float) == False:
                            try:
                                ncs = input("Podaj nową cenę sprzedaży: ")
                                if float(ncs) > 0.01:
                                    ncs = float(ncs)
                                else:
                                    print(
                                        "Cena sprzedaży musi być większa niż cena zakupu ...")
                            except:
                                print("Podaj prawidłową liczbę, np: 5 lub 5.3 ")

                elif zmiana_ceny == 'n':
                    if sprawdzam_cene_sprzedazy(nazwa_towaru) == None:

                        while isinstance(ncs, int) == False and isinstance(ncs, float) == False:
                            try:
                                ncs = input("Podaj cenę sprzedaży: ")
                                if float(ncs) > 0.01:
                                    ncs = float(ncs)
                                else:
                                    print(
                                        "Cena sprzedaży musi być większa niż zero")
                            except:
                                print("Podaj prawidłową liczbę, np: 5 lub 5.4 ")

                        while jaka_cena_zakupu(nazwa_towaru) >= ncs:
                            print(
                                "Cena sprzedaży nie może być mniejsza od ceny zakupu")
                            print("Cena zakupu towaru o nazwie: ", nazwa_towaru, " wynosi ", jaka_cena_zakupu(
                                nazwa_towaru), "wpisz wyższą cenę sprzedaży.")

                            ncs = ''

                            while isinstance(ncs, int) == False and isinstance(ncs, float) == False:
                                try:
                                    ncs = input("Podaj cenę sprzedaży: ")
                                    if float(ncs) > 0.01:
                                        ncs = float(ncs)
                                    else:
                                        print(
                                            "Cena sprzedaży musi być większa niż cena zakupu ...")
                                except:
                                    print(
                                        "Podaj prawidłową liczbę, np: 5 lub 5.5 ")

                    elif sprawdzam_cene_sprzedazy(nazwa_towaru) != None:
                        ncs = sprawdzam_cene_sprzedazy(nazwa_towaru)

            except:
                print("Wyberz y lub n")

        dostepni_klienci()

        while czy_klient_na_liscie(nazwa_klienta) == False:
            try:
                nazwa_klienta = input("Podaj nazwę klienta: ")
                if czy_klient_na_liscie(nazwa_klienta) == False:
                    print("Tego klienta nie ma na liście klientów!")
                elif czy_klient_na_liscie(nazwa_klienta) == True:
                    print()
                    print("Towar sprzedany firmie: ", nazwa_klienta)
                    print()
            except:
                print("Co Ty robisz ???")

        sell_item(nazwa_towaru, sprzedana_ilosc, ncs, nazwa_klienta)
        print()
        print("---------------------------------")
        print("Stan magazynu:")
        print()
        get_items()
        # zapis w obu plikach (magazyn.csv i magazyn_sprzedaż.csv)
        export_items_to_csv()
        export_sales_to_csv()
        zyski = round(show_revenue() - koszt_calkowity, 2)
        zapis_zmiennych()

    elif wybor == 3:
        print("Wyświetla listę towarów w magazynie.")
        get_items()

    elif wybor == 4:
        print("Wyświetla listę sprzedanych towarów")
        lista_sprzedanych_towarów()

    elif wybor == 5:                                    # Wydatki, przychody i zyski
        zyski = show_revenue() - koszt_calkowity
        print()
        print("------------------------")
        print("Koszt wszystkich zakupionych towarów: ", koszt_calkowity, " GBP")
        print()
        print("Przychód ze sprzedaży towarów: ", show_revenue(), " GBP")
        print()
        print("Zyski ze sprzedaży towarów: ", round(zyski, 2), " GBP")
        print()
        print()

    elif wybor == 6:
        print("Zapis stanu magazunu do pliku magazyn.csv ")
        print("Zapis sprzedanych towarów do pliku magazyn_sprzedaz.csv")
        export_items_to_csv()
        export_sales_to_csv()

    elif wybor == 7:
        print("Wczytuje dane z pliku magazyn.csv   i zastąpi nimi zawartość listy items. ")
        load_items_from_csv()

    elif wybor == 8:
        print("Wczytuje dane z pliku magazyn_sprzedaz.csv  i zastąpi nimi zawartość listy sold_items.")
        load_sold_items_from_csv()

    elif wybor == 9:
        print("Wybrałeś wyjście z programu. Bye bye. ")

    elif wybor == 0:
        print("Wyceń towary w magazynie.")
