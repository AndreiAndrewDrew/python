def increase_persone_age(person):
    print("ID 'person':", id(person))
    person['name'] = 'New_Andrew'
    person['age'] += 1
    return person


person_one = {
    'name': 'Andrew',
    'age': 36
}
print("Dict. 'person_one'", person_one)
print("Id 'person_one'", id(person_one))

increase_persone_age(person_one)  # Chemam functia pentru dict. 'person_one'
print("Valoare cheie 'name':", person_one['name'])
print("Valoare cheie 'age':", person_one['age'])

# astfel functia 'increase_persone_age' a modifcat cheia 'age'
# din Dict. 'person_one', dar id-rile al 'persone' si 'persone_one'
# sunt egale
