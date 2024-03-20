from datetime import datetime

my_datetime = datetime(2027, 7, 24, 16, 34, 54)

print(my_datetime.strftime('%d-%b-%Y'))  # 24-Jul-2027
print(my_datetime.strftime('%d-%m-%Y'))  # 24-07-2027
print(my_datetime.strftime('%d/%m/%Y'))  # 24/07/2027
print(my_datetime.strftime('%d-%b-%Y %H:%M:%S'))  # 24-Jul-2027 16:34:54

date_str = '10/12/2222'
print("Data in forama de rind(str):", date_str)

converted_date = datetime.strptime(date_str, '%d/%m/%Y')  # Convertam 'str' in date format
print("Data Convertata: ", converted_date)
