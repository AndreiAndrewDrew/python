my_fruits = {'banana', 'apple', 'orange'}
posts_ids = {342, 345, 345, 53745, 8567, 5795}
users_inputs = {True, 'hi!', 10.5}

print(my_fruits)
print(type(my_fruits))
print(posts_ids)  # valore care se repeta se sterg in Set ramin numai valori unicale

other_fruits = {'apple', 'banana', 'orange'}
print(my_fruits == other_fruits)  # True
print(len(my_fruits))
print(len(posts_ids))
# print(posts_ids[0]) # eroare...Set nu are indexuri

# L18_65: Change objects in the set

# list_set = {[1, 2], [23, 34]}  # eroare nu putem crea un set de liste
