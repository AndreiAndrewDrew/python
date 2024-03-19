import re
print("Sarcina: Crearea a functiilore de control a emailului si parolei Userului")


def chek_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "Valid" if email_check_pattern.fullmatch(email) else "NOT Valid"
    return print(f"Emailul: {email}, ==> {validation_result}")


def chek_password(password):
    # r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    password_regexp = r"^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*[_.].*)[0-9a-zA-Z_.]{8,}$"
    password_check_pattern = re.compile(password_regexp)
    validation_result = "Valid" if password_check_pattern.fullmatch(password) else "NOT Valid"
    return print(f"Parola: {password} ==> {validation_result}")


while True:
    user_email = input("Introduceti email-ul : ")
    user_password = input("Introduceti prola(minimum 8 simb.): ")
    chek_password(user_password)
    chek_email(user_email)
    answer = input("Continnue? Yes(Enter) or No(n): ")
    if answer == 'n':
        break
