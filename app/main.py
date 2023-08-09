"""The main file to execute the FASTAPI."""

import sqlite3
from fastapi import FastAPI, HTTPException
from models import EmployeeCreate
from database import create_table


app = FastAPI()


@app.on_event("startup")
async def startup():
    """On starting the app the table will be created.
    """
    create_table()


@app.get("/employees/")
async def get_employees():
    """FETCH all the data from table employee.

    Returns:
        list: data from table
    """
    connection = sqlite3.connect("./data.db")
    cursor = connection.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    connection.close()
    return employees


@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    """GET the data of certain employee

    Args:
        employee_id (int): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    connection = sqlite3.connect("./data.db")
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
    """Create the new entry form user.

    Args:
        employee (EmployeeCreate): _description_

    Returns:
        _type_: _description_
    """
    connection = sqlite3.connect("./data.db")
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
    """ Delete the data from the table matching the employee_id.

    Args:
        employee_id (int): Id of the employee to be delete

    Returns:
        dict: Message of delete.
    """
    connection = sqlite3.connect("./data.db")
    connection.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    connection.commit()
    connection.close()
    return {"message": f"Employee with ID {employee_id} deleted"}


@app.put("/employees/{employee_id}/{column}/{new_value}")
async def update_employee(employee_id: int, column: str, new_value: str):
    """Update the data matching the employee id.

    Args:
        employee_id (int): Employee id
        column (str): Constrain to be updated
        new_value (str): Message

    Returns:
        _type_: _description_
    """
    connection = sqlite3.connect("./data.db")
    connection.execute(
        f"UPDATE employees SET {column}=? WHERE id=?", (new_value, employee_id)
    )
    connection.commit()
    connection.close()
    return {"message": f"Employee with ID {employee_id} updated"}
