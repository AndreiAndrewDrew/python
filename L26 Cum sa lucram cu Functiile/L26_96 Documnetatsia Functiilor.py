print("Ex.1")


def mult_by_factor(value, mult=1):
    """
    Multiplicam un numar cu un multiplicator

    :param value:int
    :return value * mult
    """
    return value * mult


print("value * mult =", mult_by_factor(5, 5))

print("Ex.2")


def print_number_info(num):
    """
    Controlam daca numarul este impar sau par?

    :param num:int
    :return:Par sau Impar
    """

    if (num % 2) == 0:
        print("Numarul este par!")
    else:
        print("Numarul este impar!")

    return num


entered_num = int(input('Enter any number: '))  # Convertam in 'int'
print_number_info(entered_num)
