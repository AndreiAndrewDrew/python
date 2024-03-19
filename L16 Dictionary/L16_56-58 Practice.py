my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['price'] = 70
my_disk['brand'] = 'Samsung'

print(my_disk)
print(id(my_disk))

print(my_disk.items())
print(my_disk.keys())
print(list(my_disk.keys()))

new_disk = my_disk.copy()  # copiem dictonarul

new_disk['type'] = 'ssd'  # adaugam o pereche noua
print(my_disk)
print(new_disk)
print("Lungimea my_disk=", len(my_disk))
print("Lungimea new_disk=", len(new_disk))

my_list = [['first', 0], ['second', True]]  # creem o lista din liste
my_dict = dict(my_list)  # Convertam lista in dictionar
print(my_dict)
