import logging

logging.basicConfig(level=logging.DEBUG, filename="logfile_1.log")

def dodawanie(skladnik_1, skladnik_2):
    wynik = skladnik_1 + skladnik_2
    return wynik
    

def odejmowanie(skladnik_1, skladnik_2):
    wynik = skladnik_1 - skladnik_2
    return wynik
    


def mnozenie(skladnik_1, skladnik_2):
    wynik = skladnik_1 * skladnik_2
    return wynik


def dzielenie(skladnik_1, skladnik_2):
    wynik = skladnik_1 / skladnik_2
    return wynik


if __name__ == "__main__":
    choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:  "))

    skladnik_1 = float(input("Podaj pierwszy skladnik: "))
    skladnik_2 = float(input("Podaj drugi skladnik: "))


    if choice == 1:
        suma = dodawanie(skladnik_1, skladnik_2)
        

        logging.debug("Dodaje %.2f i %.2f" % (skladnik_1, skladnik_2))
        logging.debug("Suma wynosi %.2f" % suma)

        print("Suma wynosi: ", suma)

    elif choice == 2:
        roznica = odejmowanie(skladnik_1, skladnik_2)

        logging.debug("Odejmuje %.2f i %.2f" % (skladnik_1, skladnik_2))
        logging.debug("Roznica wynosi %.2f" % roznica)

        print("Różnica wynosi: ", roznica)

    elif choice == 3:
        iloczyn = mnozenie(skladnik_1, skladnik_2)

        logging.debug("Mnozy %.2f i %.2f" % (skladnik_1, skladnik_2))
        logging.debug("Iloczyn wynosi %.2f" % iloczyn)

        print("Iloczyn wynosi: ", iloczyn)

    elif choice == 4:
        iloraz = dzielenie(skladnik_1, skladnik_2)

        logging.debug("Dzieli %.2f i %.2f" % (skladnik_1, skladnik_2))
        logging.debug("Iloraz wynosi %.2f" % iloraz)

        print("Iloraz wynosi: ", iloraz)
