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


if __name__ == "__main__":
    choice = int(input("Give the operation using the correct number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division:  "))

    item_1 = float(input("Enter the first item: "))
    item_2 = float(input("Enter the second item: "))


    if choice == 1:
        sum = add(item_1, item_2)
        

        logging.debug("Addition %.2f and %.2f" % (item_1, item_2))
        logging.debug("The sum is: %.2f" % sum)

        print("The sum is: ", sum)

    elif choice == 2:
        diff = sub(item_1, item_2)

        logging.debug("Subtraction %.2f and %.2f" % (item_1, item_2))
        logging.debug("The difference is: %.2f" % diff)

        print("he difference is: ", diff)

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
