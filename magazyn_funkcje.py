import csv
from datetime import date
from datetime import datetime

items = []
klienci = []

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

    print("Name\t\t\tQuantity\tUnit\tUnit Price (GBP)\tDate and time\t\tKlient")
    print("----\t\t\t--------\t----\t----------------\t------------------\t---------")

    for x in sold_items: # x - jest słownikiem sprzedanego towaru
        if len(x['name']) > 7:

            print("%s\t\t%d\t\t%s\t%.2f\t\t\t%s\t%s"  % (x["name"], x["quantity"], x["unit"], x["unit_price"], x["date_and_time"], x['klient']))
        else:
            print("%s\t\t\t%d\t\t%s\t%.2f\t\t\t%s\t%s"  % (x["name"], x["quantity"], x["unit"], x["unit_price"], x["date_and_time"], x['klient']))

        

def check_item(item_name):          # funkcja sprawdza czy dany towar (item_name) istnieje w magazynie ( lista items)
    licznik = 0
    for slownik in items:

        if slownik['name'] == item_name:
            licznik = licznik + 1
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

def jaka_cena_zakupu(nazwa_towaru):

    for slownik in items:
        for k, v in slownik.items():
            if v == nazwa_towaru:
                return slownik['unit_price']



   

def sell_item(nazwa_towaru, sprzedana_ilosc, ncs, nazwa_klienta):       # funkcja odejmuje ze stanu magazynowego towar np. milk w ilości określonej przez wprowadzoną liczbę
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
                        "unit_price": ncs,          # * slownik['cena_sprzedazy'] może trzeba bedzie podac cene sprzedazy jako argument funkcji
                        "date_and_time": now.strftime("%d/%m/%Y    %H:%M"),
                        "klient": nazwa_klienta

                    })

                    print("Successfully sold %d %s of %s firmie %s" % (sprzedana_ilosc, slownik["unit"], nazwa_towaru, nazwa_klienta))


                elif slownik["quantity"] < sprzedana_ilosc:
                    print("Nie masz tylu sztuk na magazynie !!!")
                
                

def ile_sztuk_w_magazynie(nazwa_towaru):

    for slownik in items:
        for klucz, wartosc in slownik.items():
            if wartosc == nazwa_towaru:
                #print(slownik['quantity'])
                return slownik['quantity']

    
    
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

        fieldnames = ['name', 'quantity', 'unit', 'unit_price', 'date_and_time', 'klient']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for slownik in sold_items:
            writer.writerow({
                'name': slownik['name'], 
                'quantity': slownik['quantity'], 
                'unit': slownik['unit'], 
                'unit_price': slownik['unit_price'], 
                'date_and_time': slownik['date_and_time'],
                'klient': slownik['klient']
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



def czy_towar_w_magazynie(nazwa_towaru):

    towary_w_magazynie = []

    for slownik in items:
        towary_w_magazynie.append(slownik['name'])

    if nazwa_towaru in towary_w_magazynie:
        return True 

    if nazwa_towaru not in towary_w_magazynie:
        return False


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


def sprawdzam_cene_sprzedazy(nazwa_towaru):

    cena = 0
    
    for slownik in sold_items:
        for k, v in slownik.items():
            if v == nazwa_towaru:
                cena = slownik['unit_price']
   
    if cena > 0:
        return cena        
    elif cena == 0:
        return print("Nie było jeszcze sprzedaży tego towaru.")

def dostepni_klienci():

    klienci.clear()

    with open('firmy.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            rowek = row[0]
            klienci.append(rowek)

    licz = 1
    for klient in klienci:

        print("%d. %s  " % (licz, klient))
        licz = licz + 1

def czy_klient_na_liscie(nazwa_klienta):

    if nazwa_klienta in klienci:
        return True
    elif nazwa_klienta not in klienci:
        return False