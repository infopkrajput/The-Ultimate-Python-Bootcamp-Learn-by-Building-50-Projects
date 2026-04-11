from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product1 = User(id=1, name="Laptop", price=999.99)
print(product1)

product2 = User(id=2, name="Smartphone", price=499.99, in_stock=False)
print(product2) 