my_img = ('1920', '1080')
print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("Incorrect image formatting")

print("Sarcina 1...La fel folosind 'if' si 'else'")

my_img = ('3840', '2160')
if len(my_img) == 2 :
    print(f"{my_img[0]}x{my_img[1]}")
else:
    print("Incorrect image formatting")

print("Sarcina 2")

my_string = "Este un commentariu scurt12345"

print("String is Long") if len(my_string) >30 else print("String is Short")

