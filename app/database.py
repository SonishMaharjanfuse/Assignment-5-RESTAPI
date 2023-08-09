"""Creating the database for the RESTAPI project."""
import sqlite3


def create_table():
    """ Function to create the table.
    """
    connection = sqlite3.connect("./data.db")
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
