"""Create the skeleton for the data base to be store.
"""
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    """Create the skeleton requirement for Employeee.

    Args:
        BaseModel (object): helper function for class
    """
    name: str
    department: str


class Employee(EmployeeCreate):
    """determine skeleton for id.

    Args:
        EmployeeCreate (class): parent class
    """

    id: int
