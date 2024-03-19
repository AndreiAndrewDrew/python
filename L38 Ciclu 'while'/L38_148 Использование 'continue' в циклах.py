import random

random_num = random.randint(1, 10)  # generam random un nr de la 1 la 10
while True:
    num = int(input("Ghiceste nr. de la 1 la 10:"))
    if num != random_num:
        print("Mai incearca...")
        continue
    print("Felicitari!!! Ai ghicit!!!")
    break


