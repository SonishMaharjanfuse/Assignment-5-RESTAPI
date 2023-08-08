"""Main py"""

from fastapi import FastAPI
from database import insert, create_db
from models import Employee

app = FastAPI()

@app.on_event("startup")
async def startup():
    create_db()

# @app.get("/employees/")
# async def get_employee():
#     passimport


@app.post("/employees")
async def add_employee(employee: Employee):
    insert(employee.id, employee.name, employee.department)
    return {"message": "Employee added successfully"}

# @app.delete("/employee/{employee_id}")
# async def delete_employee():
#     pass

# @app.put("/employees/{empoyee_id}/{column}/{new_value}")
# async def update_employee():
#     pass