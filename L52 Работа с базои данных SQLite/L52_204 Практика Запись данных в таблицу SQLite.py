import sqlite3

DB_NAME = "sqlite_db1.db"  # denumirea bazei de date

# Adaugara datelor in tabelul 'courses'
courses = [  # creem lista din tuple, pentru Insrierea datelor in db cu 'for in'
    (255, "Python Course2", 100, 30),
    (256, "JavaScript Course2", 90, 40),
    (257, "C# Course2", 80, 45),
    (258, "C++ Course2", 95, 20)
]

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT OR REPLACE INTO courses VALUES(?, ?, ?, ?)"  # 'REPLACE' daca exista asa 'id' il reinscriem
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()
