import secrets
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

print(string.ascii_letters + string.digits + string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation

print(''.join(secrets.choice(all_chars) for i in range(8))) # astfel generam 8 simvole random din tote simbolurile

print(''.join(secrets.choice(all_chars) for i in range(20)))
# Astfel se poate de general parole
