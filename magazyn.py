# Program powinien poprawnie działać jeżeli przy pierwszym uruchomieniu programu pliki magazyn.csv i magazyn_sprzedaz.csv będą puste a w pliku zmienne.csv bedą dwie wartości 0

from magazyn_funkcje import get_items, add_item, sell_item, lista_sprzedanych_towarów, get_value,  show_revenue, dostepne_towary
from magazyn_funkcje import export_items_to_csv, export_sales_to_csv, load_items_from_csv, load_sold_items_from_csv, check_item,cena_itema_w_magazynie
import csv



def zapis_zmiennych():                  # funkcja zapisuje zmienne koszt_calkowity oraz zyski w pliku zmienne.csv

    with open('zmienne.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

        writer.writerow([koszt_calkowity])
        writer.writerow([zyski])


def odczyt_zmiennych():                  # funkcja wczytuje zmienne koszt_calkowity oraz zyski z pliku zmienne.csv
    with open('zmienne.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            row = float(row[0])
            zmienne.append(row)

zmienne = []



odczyt_zmiennych()

wybor = -1

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
    print("--------------------")
    print()


    wybor = int(input("Wybierz działanie (1 - 9):  "))

    if wybor == 1:
        item_name = ''
        item_quantity = ''
        item_price = ''
        print("Wybrałeś dodanie towaru - add")
        while len(item_name) < 3:
            
            item_name = input("Item name: ")
            if len(item_name) < 3:
                print("Nazwa musi składać sie z conajmniej 3 liter.")
            


        print(check_item(item_name))     # wywołanie funkcji check_item  zwraca 0 jesli dodawanego towaru nie ma w magazynie i 1 kiedy juz jest w magazynie
        
        if check_item(item_name) == 0:
            print("Tego towaru nie ma jeszcze w magazynie")

            # Tu pisać kod jeśli towaru nie ma w magazynie

            while item_quantity.isnumeric() == False:

                try:
                    item_quantity = input("Item quantity: ")   # item_quantity = int(input("Item quantity: "))
                except:
                    print("Podaj prawidłową liczbę. ")
            
            item_quantity = int(item_quantity)

            item_unit = input("Item unit of measure: (L, kg, pcs) ")

            while isinstance(item_price, int) == False  and isinstance(item_price, float) == False:   # item_price = string 

                try:
                    item_price = input("Item price: ")
                    item_price = float(item_price)
                except:
                    print("Podaj prawidłową liczbę. ")



        elif check_item(item_name) == 1:
            print("Towar o tej nazwie jest już na stanie magazynowym")

            # Tu pisać kod jeśli towar jest w magazynie

            while item_quantity.isnumeric() == False:

                try:
                    item_quantity = input("Item quantity: ")   # item_quantity = int(input("Item quantity: "))
                except:
                    print("Podaj prawidłową liczbę. ")
            
            item_quantity = int(item_quantity)

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
        print("Wybrałeś sprzedaż z magazynu - Sell")
        print("Dostępne towary: ")
        dostepne_towary()           # wywołanie funkcji: dostepne_towary

        nazwa_towaru = input("Podaj nazwe towaru na sprzedaż: ")

        sprzedana_ilosc = int(input("Ilość towaru na sprzedaż: "))

        sell_item(nazwa_towaru, sprzedana_ilosc)
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
