import sqlite3
# Creem baza de date si o deschidem cu programa 'DB Browser for SQLite'
DB_NAME = "sqlite_db1.db"
# Create new table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses ( # creem un tabel nou 'courses'
        id integer PRIMARY KEY,
        title text NOT NULL,
        student_qty integer,
        reviews_qty integer
    );"""
    sqlite_conn.execute(sql_request)