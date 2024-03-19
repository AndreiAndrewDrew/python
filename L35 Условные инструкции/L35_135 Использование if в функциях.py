print("Varianta.1")


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return " Unul din argumente nu e cifra intreaga"

    if a > b:
        return f" {a} este mai mare ca {b}"

    if a < b:
        return f" {a} este mai mic ca {b}"

    return f" Ambele numere sunt egale cu {a}"

n_info=nums_info(12,34.3)
print(n_info)


print("Varianta.2 de functie cu 'elif' si 'else'")


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = " Unul din argumente nu e cifra intreaga"
    elif a > b:
        info = f" {a} este mai mare ca {b}"
    elif a < b:
        info = f" {a} este mai mic ca {b}"
    else:
        info = f" Ambele numere sunt egale cu {a}"
    return info


print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(-10, -3))
print(nums_info(2, 6))
print(nums_info(3, 3))
