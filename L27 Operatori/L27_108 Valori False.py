print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(range(0)))
print(bool(''))

print(not not {})  # spoate in loc de functaie "bool"
# sa folosim operantul "not not"

my_list = [1, 2]

if len(my_list) > 0:  # Astfel nu e acceptabil de scris
    print("Lista are elemente!")
else:
    print("Lista NU are elemente")

if my_list:  # Verianta acceptabila de scris, python automat controleaza daca e true
    print("Lista are elemente!")
else:
    print("Lista NU are elemente")
