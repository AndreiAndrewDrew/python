def increase_person_age(person):
    person_copy = person.copy()  # creem copie obiectului 'person'
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 3
}

new_person = increase_person_age(person_one)
print("Valoarea cheiei 'age' din dict 'person_one':", person_one['age'])
print("Valoarea cheiei 'age' din dict 'new_person':", new_person['age'])

# Astefel cu ajutorul functiei se face copie la dictionarul transmis in ea,
# si pplus se modifica cheia 'age' in dictionarul nou creat 'new_person'.
