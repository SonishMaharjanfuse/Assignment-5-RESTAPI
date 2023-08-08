"""Connecting to database"""

import sqlite3
from models import Employee

def get_db_connection():
    connection = sqlite3.connect('data.db')
    return connection


def create_db():
    connection = get_db_connection()
    cursor = connection.execute("CREATE TABLE employee(id INT, name VARCHAR(50), department VARCHAR(20))")
    employees = cursor.fetchall()
    connection.close()
    return employees

def insert(_id, _name, _department):
    connection = get_db_connection()
    connection.execute(
            "INSERT INTO employees (id, name, department) VALUES (?, ?, ?)",
            (_id, _name, _department)
            )
    connection.comit()
    connection.close()



