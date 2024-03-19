import csv

with open('test.csv', 'w') as csv_file:  # creem fisierul 'test.csv'
    writer = csv.writer(csv_file)  # creem obiect dela clasa 'csv'
    writer.writerow(['user_id', 'user_name', 'comment_qty'])
    writer.writerow([111, 'Andrew', 32])
    writer.writerow([122, 'Vasile', 544])
    writer.writerow([1124, 'Ion', 678])

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file) # creem obiectul 'reader' din claasa 'csv'
    print(reader)
    print(type(reader))
    for line in reader: # executam iteratie pentru fiecare rind
        print(line)

    print(reader.line_num)
