my_list = [1, 2]
other_list = ['a', 'b']
my_dict = {}

my_dict1 = {
    'a': 5,
    'b': 4
}
my_dict2 = {
    'b': 4,
    'a': 5
}

print(my_list or other_list)  # intorce prima valoare Adevarate '[1,2]'
print(len(my_list) > 0 or other_list)  # Prima valoare este 'True'
print(len(my_list) < 0 or other_list)  # ['a','b']
print(my_list and other_list)  # ['a','b']

print(my_list and my_dict)  # {} - dictionar gol
print(bool(my_list and my_dict))  # False

my_list and print("List is not empty!")

print(len(my_dict1) and len(my_dict2))
(my_dict1 and my_dict2) and print("Dictionary is equals")
