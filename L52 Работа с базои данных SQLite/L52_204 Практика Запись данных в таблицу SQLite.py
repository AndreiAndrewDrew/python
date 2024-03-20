import sqlite3

# Creem baza de date si o deschidem cu programa 'DB Browser for SQLite'
DB_NAME = "sqlite_db1.db"  # denumirea bazei de date

# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses ( # creem un tabel nou 'courses'
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         student_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

courses = [  # creem lista din tuple, pentru insrierea datelor in db cu 'for in'
    (255, "Python Course2", 100, 30),
    (256, "JavaScript Course2", 90, 40),
    (257, "C# Course2", 80, 45),
    (258, "C++ Course2", 95, 20)
]

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT OR REPLACE INTO courses VALUES(?, ?, ?, ?)"
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()
