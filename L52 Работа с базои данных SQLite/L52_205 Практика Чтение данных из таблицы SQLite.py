import sqlite3

DB_NAME = "sqlite_db1.db"  # denumirea bazei de date

print("\nCitim datele din tabelul 'courses' in forma de Tuple:")
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses"
    sql_cursor = sqlite_conn.execute(sql_request) # execute() ne intorce curosrul, ne trebuie iteratii
    for record in sql_cursor:
        print(record) # toate cimpurile
        # print(record[1]) # numai cimpul 'title', din tuple al doilea element
        # print(record[0]) # numai cimpul 'id'

print("\nCitim datele din tabelul 'courses' in forma de Lista de Tuple:")
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses"
    sql_cursor = sqlite_conn.execute(sql_request) # execute() ne intorce curosrul, ne trebuie iteratii
    records = sql_cursor.fetchall()
    print(records)

print("\nCitim datele din tabelul 'courses' in forma de Lista de Tuple cu filtru 'WHERE reviews_qty>40':")
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=40"
    sql_cursor = sqlite_conn.execute(sql_request) # execute() ne intorce curosrul, ne trebuie iteratii
    records = sql_cursor.fetchall()
    print(records)