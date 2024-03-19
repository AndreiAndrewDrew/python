print("Ex.1")
my_number = 22.4

if type(my_number) is int:
    print(type(my_number), my_number, "is integer")
else:
    print(type(my_number), my_number, "is not an integer")

print("Ex.2")

my_phone = {
    'price': 300,
    'brand': 'Motorola'
}

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")
