# database.py

import sqlite3

def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT
        )
        """
    )
    connection.commit()
    connection.close()
