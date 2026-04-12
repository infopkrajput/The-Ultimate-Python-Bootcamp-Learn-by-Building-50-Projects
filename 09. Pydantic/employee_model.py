from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int = Field(..., description="The employee's unique identifier"),
    name: str = Field(..., min_length=2, max_length=50, description="The employee's full name",examples="Pushpendra Kumar"),
    department: Optional[str] = Field(default='General', description="The employee's department"),
    salary: float = Field(..., ge=10000, description="The employee's salary", examples=50000.0),
    
class User(BaseModel):
    email: str = Field(..., regex=r'^\S+@\S+\.\S+$', description="The user's email address", examples="john.doe@example.com"),
    phone: Optional[str] = Field(default=None, regex=r'^\+?\d{10,15}$', description="The user's phone number", examples="+1234567890"),
    age: Optional[int] = Field(default=None, ge=0, le=150, description="The user's age", examples=30),
    