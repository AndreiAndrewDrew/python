happy_smiles = []

happy_smiles.append(':)')
happy_smiles.append(':D')
happy_smiles.append(';)')

print(happy_smiles)
print(len(happy_smiles))

u_inputs = [True, 'Hi!', ':D', 10.5]

u_inputs.pop()  # se sterge ultimul element din lista
print(u_inputs)

u_inputs.pop(0)  # se ssterge elementul cu indexul '0'
print(u_inputs)

remove_element = u_inputs.pop()

print(remove_element)
print(u_inputs)

list_ids = [123, 3423, 588, 345]
list_ids.sort()  # Sorteaza crescator lista cu nr intregi
print(list_ids)

list_ids.sort(reverse=True)  # Sorteaza descrescator lista cu nr intregi
print(list_ids)
