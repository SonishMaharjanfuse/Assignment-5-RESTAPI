# Creating the Employee Class

from pydantic import BaseModel

class Employee(BaseModel):
    id :int
    name: str
    department: str


