import logging

logging.basicConfig(level=logging.DEBUG, filename="logfile_1.log")

def add(item_1, item_2):
    result = item_1 + item_2
    return result
    

def sub(item_1, item_2):
    result = item_1 - item_2
    return result
    


def multi(item_1, item_2):
    result = item_1 * item_2
    return result


def div(item_1, item_2):
    result = item_1 / item_2
    return result

if_number = False
 
item_1_float = False
item_2_float = False

item_1_int = False
item_2_int = False

if __name__ == "__main__":

    while if_number == False:

        choice = input("Give the operation using the correct number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division:  ")
        if_number = choice.isnumeric()
        

        if if_number == True:
            choice = int(choice)


    while item_1_float == False:   

        try:
            item_1 = float(input("Enter the first item: "))
            item_1_float = isinstance(item_1, float)            # True if item_1 is float
        except:
            pass

    while item_2_float == False:   
        try:
            item_2 = float(input("Enter the second item: "))    
            item_2_float = isinstance(item_2, float)            # True if item_2 is float
        except:
            pass

    if choice == 1:
        sum = add(item_1, item_2)
                
        logging.debug("Addition %.2f and %.2f" % (item_1, item_2))
        logging.debug("The sum is: %.2f" % sum)

        print("The sum is: ", sum)

    elif choice == 2:
        diff = sub(item_1, item_2)

        logging.debug("Subtraction %.2f and %.2f" % (item_1, item_2))
        logging.debug("The difference is: %.2f" % diff)

        print("The difference is: ", diff)

    elif choice == 3:
        ratio = multi(item_1, item_2)

        logging.debug("Multiplication %.2f and %.2f" % (item_1, item_2))
        logging.debug("The ratio is: %.2f" % ratio)

        print("The ratio is: ", ratio)

    elif choice == 4:
        quotient = div(item_1, item_2)

        logging.debug("Division %.2f i %.2f" % (item_1, item_2))
        logging.debug("The quotient is: %.2f" % quotient)

        print("The quotient is: ", quotient)

    
        
# Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:
# 1. Sprawdzaj, czy podana wartość na pewno jest liczbą.
# 2. W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.