def my_fun(a, b):
    a = a + 1
    c = a + b
    print("Id 'a':", id(a))
    print("Id 'b':", id(b))
    return c


num_one = 10
num_two = 5

res = my_fun(num_one, num_two)
print("Rez. funct. 'my_fun':", res)
print(num_one)
print(num_two)
print(id(num_one)) # 'num_one' are id diferit de 'a',a fost modificat in interiorul funuctiei
print(id(num_two)) # 'num_two' are id egal cu 'b' din functie
