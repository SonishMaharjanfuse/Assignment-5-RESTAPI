# models.py

from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    department: str

class Employee(EmployeeCreate):
    id: int
