import requests
import pandas # am intsalat packetul 'pandas' de pe 'pypi.org'


my_request = requests.get("https://www.python.org")

print(my_request)
print(my_request.text)  # ne intorce in forma de text, pagina html
print(my_request.status_code)  # 200 - ce inseamna ca serverul reusit nia aintors zaprosu nostru
