from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True
    created_at: datetime
    tags: List[str] = []
    
    model_config = ConfigDict(
                              json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )
    
user = User(
    id=1,
    name="Raj",
    email="raj@example.com",
    address=Address(
        street="123 Main St",
        city="Agra",
        zip_code="12345"),
    created_at=datetime(2024, 6, 1, 12, 0, 0),
    is_active=False,
    tags=["premium", "subscriber"]
)


python_dict = user.model_dump()

print("Printing User Object:")
print(user)

print("*" * 30)
print("Printing Python Dictionary:")
print(python_dict)


json_string = user.model_dump_json()

print("*" * 30)
print("Printing JSON String:")
print(json_string)

