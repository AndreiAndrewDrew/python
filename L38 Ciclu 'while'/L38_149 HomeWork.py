while True:
    first_num = int(input("Introduceti primul numar:"))
    second_num = int(input("Introduceti al doilea nr:"))
    res = first_num / second_num
    print("Rezultatul impartsirei:", res)
    answer = input("Doriti sa continuatsi? yes or no: ")
    if answer == 'no':
        break
