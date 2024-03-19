print("Ex.1")
my_number = 0.0
# exemlpu de ternarnii
print(my_number, "is Integer") if type(my_number) is int else print(my_number, "is Float")

# facem acceaiesh numai clasik cu 'if' si 'else'
if type(my_number) is int:
    print(my_number, "is Integer")
else:
    print(my_number, "is Float")

print("Ex.2")
product_qty = 2

print("Product in stock" if product_qty > 0 else "Out of stock")

print("Ex.3")
temp = +24
weather = "hot" if temp > 18 else "cold"
print(weather)
