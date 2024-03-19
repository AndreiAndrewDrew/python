import re


# Controlam email-u
def chek_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "VALID" if email_check_pattern.fullmatch(email) else "Not VALID"
    return (email, validation_result)


# Valid
print(chek_email('ab.1@gmail.com'))
print(chek_email('ab_1@gmail.com'))
print(chek_email('ab_1@gmail.com'))
print(chek_email('ab._1@gmail.com'))
# Invalid
print(chek_email('ab._1gmail.com'))
print(chek_email('ab._1@gmailcom'))
print(chek_email('@gmail.com'))
print(chek_email('ab._1@'))
