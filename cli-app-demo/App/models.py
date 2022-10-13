import datetime
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, DateTime


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fname: str
    lname: str
    age: int
    salary: int
    datejoin: DateTime = Field(default_factory=DateTime)
