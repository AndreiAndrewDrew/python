import math


def calc_factorial(num):  # Exemplu de functei recursiva
    if type(num) is not int:
        raise TypeError("Number must be integer!!!")
    if num <= 0:
        raise ValueError("Number must be positive!!!")
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num  # recursie


print(calc_factorial(4))  # fuunctie proprie
print(math.factorial(4))  # acealasi rezultata cu functia 'factorial' din modul 'math'

# print(math.factorial('abc'))
# print(math.factorial(-10))
