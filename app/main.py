"""main.py"""
from fastapi import FastAPI, HTTPException
from models import EmployeeCreate
from database import create_table
import sqlite3

app = FastAPI()


@app.on_event("startup")
async def startup():
    create_table()


@app.get("/employees/")
async def get_employees():
    connection = sqlite3.connect("data.db")
    cursor = connection.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    connection.close()
    return employees


@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    connection = sqlite3.connect("data.db")
    cursor = connection.execute(
        "SELECT * FROM employees WHERE id=?", (employee_id,)
        )
    employee = cursor.fetchone()
    connection.close()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees/")
async def add_employee(employee: EmployeeCreate):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO employees (name, department) VALUES (?, ?)",
        (employee.name, employee.department)
    )
    connection.commit()
    connection.close()
    return {"message": "Employee added successfully"}


@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    connection = sqlite3.connect("data.db")
    connection.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    connection.commit()
    connection.close()
    return {"message": f"Employee with ID {employee_id} deleted"}


@app.put("/employees/{employee_id}/{column}/{new_value}")
async def update_employee(employee_id: int, column: str, new_value: str):
    connection = sqlite3.connect("data.db")
    connection.execute(
        f"UPDATE employees SET {column}=? WHERE id=?", (new_value, employee_id)
    )
    connection.commit()
    connection.close()
    return {"message": f"Employee with ID {employee_id} updated"}
