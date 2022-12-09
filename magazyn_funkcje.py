import csv
from datetime import date
from datetime import datetime

items = []


sold_items = []

def get_items():                        # funkcja wyświetla listę towarów w magazynie
    print("Name\t\t\tQuantity\tUnit\tUnit Price (GBP)\tDate and time")
    print("----\t\t\t--------\t----\t----------------\t------------------")
   
    for i in items:
        if len(i['name']) > 7:
            print("%s\t\t%.2f\t\t%s\t%.2f\t\t\t%s"  % (i["name"], i["quantity"], i["unit"], i["unit_price"], i["date_and_time"]))

        else:
            print("%s\t\t\t%.2f\t\t%s\t%.2f\t\t\t%s"  % (i["name"], i["quantity"], i["unit"], i["unit_price"], i["date_and_time"]))



def lista_sprzedanych_towarów():        # wyświetla listę sprzedanych towarów

    print("Name\t\t\tQuantity\tUnit\tUnit Price (GBP)\tDate and time")
    print("----\t\t\t--------\t----\t----------------\t------------------")

    for x in sold_items:
        print("%s\t\t\t%d\t\t%s\t%.2f\t\t\t%s"  % (x["name"], x["quantity"], x["unit"], x["unit_price"],x["date_and_time"]))
        

def check_item(item_name):
    licznik = 0
    for slownik in items:

        if slownik['name'] == item_name:
            licznik = licznik + 1
            #slownik['quantity'] = slownik['quantity'] + item_quantity
        else:
            pass
    return licznik


def cena_itema_w_magazynie(item_name):

    for slownik in items:

        for k, v in slownik.items():
            if v == item_name:
                cenka = slownik["unit_price"]
            

    return cenka


def add_item(item_name, item_quantity, item_unit, item_price):     # dodanie nowego słownika do listy items, trzeba udoskonalić bo dodaje kolejny towar o takiej samej nazwie a tak nie może być

    licznik = 0
    now = datetime.now()
    for slownik in items:

        if slownik['name'] == item_name:
            licznik = licznik + 1
            slownik['quantity'] = slownik['quantity'] + item_quantity
            slownik['date_and_time'] = now.strftime("%d/%m/%Y    %H:%M")
        else:
            pass

    if licznik == 0:
        items.append({
        "name": item_name,
        "quantity": item_quantity,
        "unit": item_unit,
        "unit_price": item_price,
        "date_and_time": now.strftime("%d/%m/%Y    %H:%M")
        })

def jaka_cena():


    pass

def sell_item(nazwa_towaru, sprzedana_ilosc, cena_sprzedazy):       # funkcja odejmuje ze stanu magazynowego towar np. milk w ilości określonej przez wprowadzoną liczbę
    now = datetime.now()

    for slownik in items:

        for klucz, wartosc in slownik.items():
            if wartosc == nazwa_towaru:
                if slownik["quantity"] >= sprzedana_ilosc:


                    slownik["quantity"] -= sprzedana_ilosc
                    # w sold_items jest juz slownik z 'name' = nazwa_towaru to tylko odejmuje sprzedana_ilosc od wartosci ktora już jest
                    

                    sold_items.append({
                        "name": nazwa_towaru,
                        "quantity": sprzedana_ilosc,
                        "unit": slownik["unit"],       
                        "unit_price": cena_sprzedazy,          # * slownik['cena_sprzedazy'] może trzeba bedzie podac cene sprzedazy jako argument funkcji
                        "date_and_time": now.strftime("%d/%m/%Y    %H:%M")
                    })

                    print("Successfully sold %d %s of %s" % (sprzedana_ilosc, slownik["unit"], nazwa_towaru))


                elif slownik["quantity"] < sprzedana_ilosc:
                    print("Nie masz tylu sztuk na magazynie !!!")
                
                

def get_value():        # funkcja zlicza wartość przedmiotów aktualnie znajdujących się w magazynie - na liście items
    
    suma = 0
    for slownik in items:
        suma = suma + slownik["quantity"] * slownik["unit_price"]
    return suma
    
    
def show_revenue():  #  funkcja zlicza wartość sprzedanych przedmiotów z listy sold_items.

    suma_2 = 0
    for slownik in sold_items:
        suma_2 = suma_2 + slownik["quantity"] * slownik["unit_price"]
    return suma_2
    
def export_items_to_csv():          # funkcja eksportuje / zapisuje do pliku magazyn.csv całą zawartość listy items.

    with open('magazyn.csv', 'w', newline='', encoding="utf-8") as csvfile:

        fieldnames = ['name', 'quantity', 'unit', 'unit_price', 'date_and_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for slownik in items:
            writer.writerow({
                'name': slownik['name'], 
                'quantity': slownik['quantity'], 
                'unit': slownik['unit'], 
                'unit_price': slownik['unit_price'],
                'date_and_time': slownik['date_and_time']
                })
      

def export_sales_to_csv():          # funkcja eksportuje / zapisuje do pliku magazyn_sprzedaz.csv całą zawartość listy sold_items.

    with open('magazyn_sprzedaz.csv', 'w', newline='', encoding="utf-8") as csvfile:

        fieldnames = ['name', 'quantity', 'unit', 'unit_price', 'date_and_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for slownik in sold_items:
            writer.writerow({
                'name': slownik['name'], 
                'quantity': slownik['quantity'], 
                'unit': slownik['unit'], 
                'unit_price': slownik['unit_price'], 
                'date_and_time': slownik['date_and_time']
                })


def load_items_from_csv():  

    items.clear()

    with open('magazyn.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
   

    for slownik in items:
        for klucz in slownik.keys():

            try:
                slownik[klucz] = float(slownik[klucz])
            except:
                slownik[klucz] = str(slownik[klucz])


def load_sold_items_from_csv():

    sold_items.clear()

    with open('magazyn_sprzedaz.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sold_items.append(row)

    for slownik1 in sold_items:
        for klucz in slownik1.keys():

            try:
                slownik1[klucz] = float(slownik1[klucz])
            except:
                slownik1[klucz] = str(slownik1[klucz])


def dostepne_towary():

    dost_tow = []
    
    for slownik in items:

        dost_tow.append({
                            "name": slownik['name'],
                            "quantity": slownik['quantity'],   
                        })

    lp = 1
    for i in dost_tow:

        print("%d. %s  -->  %d sztuk"  % (lp, i["name"], i["quantity"]))
        lp = lp + 1

def wydruk_items():
    for i in items:
        print(i)


def wydruk_sold_items():
    for i in sold_items:
        print(i)
# funkcja wczytuje przy pomocy modułu csv.DictReader wczyta dane z pliku CSV i zastąpi nimi zawartość listy items. 
# Wskazówka: użyj metody list.clear(), [items.clear() ] żeby wyczyścić listę items, przed załadowaniem danych.    
