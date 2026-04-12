from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    
address = Address(street="123 Main St", city="Mathura", zip_code="123456")

user = User(id=1, name="Raj", email="raj@example.com", address=address)


user_data = {
    "id": 2,
    "name": "Mahesh",
    "email": "mahesh@example.com",
    "address": {
        "street": "456 Elm St",
        "city": "Mathura",
        "zip_code": "654321"
        }
}

user2 = User(**user_data)

print(user)

print(user2)