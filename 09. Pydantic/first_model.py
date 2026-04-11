from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
input_data = {
    "id": 1, 
    "name": "Raj",
    "is_active": True
}

user = User(**input_data)
print(user)

# if we give any wrong type of data in input_data, it will raise a validation error
# for example, if we give a string instead of an integer for the id field, it will raise a validation error
