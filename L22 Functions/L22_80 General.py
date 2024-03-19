def sum(a, b):
    c = a + b
    print("Suma a + b =", c)


a = 3
b = 8
sum(a, b)
sum(23, 24)
print(type(sum))  # calasa function


def my_function(a, b):
    a = a + 1
    c = a + b
    return c


res = my_function(12, 3)
print("Rez. funct. 'my_function:'", res)
