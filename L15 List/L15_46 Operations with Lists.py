greeting_str = "Hello from Python"
greeting_list = list(greeting_str)  # Operatia 'list' se face convertatsie string in listsa
print(greeting_list)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)  # Convertatsie dictionarului in lista

print(my_dict_keys)

ratings = [2.1, 3.4, 5.0, 7.3, 6.2, 3.2]
print(max(ratings))
print(min(ratings))
print(sum(ratings))

print(sum(ratings) / len(ratings))  # Valoarea Medie

my_ratings = [1.2, 2]
other_ratings = [3.2, 5.3, 7.4, 10]

all_ratings = my_ratings + other_ratings
print(all_ratings)

first_two_ratings = all_ratings[:2] # afisham primele 2 elemente
print(first_two_ratings)

middle_ratings = all_ratings[1:-1] # afisham de la al doilea pina la ultimul element
print(middle_ratings)

last_two_ratings = all_ratings[-2:] # afisham ultimele 2 elemete
print(last_two_ratings)