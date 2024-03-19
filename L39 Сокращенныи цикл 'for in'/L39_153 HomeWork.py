print("Sarcina 1. Creem dict nou cu keiele Majuskule:")
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}

new_dict = {key.upper(): value for key, value in my_dict.items()}

print(new_dict)

print("Sarcina 2. Creeem lista noua cu lungimea mai mare de 3:")

my_list = ['Andrew', 'Anastasion', 'Jon', 'Ted']

new_dict = [elem for elem in my_list if len(elem) > 3]

print(my_list)
print(new_dict)
