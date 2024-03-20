import time

# start_time = time.time()  # 1710918109.5125718 intorce data curenta in secunde, dupa '.' sunt milesecunde
#
# print(time.ctime())  # Wed Mar 20 09:03:25 2024 , in forma citibila
#
# print(time.ctime(1123213213))  # converteaza din secunde in data citabila
# print("Pauza de 2.5 secunde;")
# time.sleep(2.5)
#
# end_time = time.time()
#
# print(end_time-start_time) # afisham diferentsa = 2.5014662742614746 aprox. 2.5 secunde

# exemplu 2

start_time2 = time.time()

my_range = list(range(50_000_000))  # convertam in lista un interval pina la 50.000.000
print(my_range[100_000])  # Afisham elementul al 100.000

end_time2 = time.time()

print("Total duration of the operation (secunde):", end_time2 - start_time2) # 7.126104354858398
