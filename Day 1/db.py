import sqlite3
from sqlite3 import Error

def create_db():
    conn = None
    try:
        conn = sqlite3.connect("test1.db")
        print(sqlite3.version)
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()

create_db()
