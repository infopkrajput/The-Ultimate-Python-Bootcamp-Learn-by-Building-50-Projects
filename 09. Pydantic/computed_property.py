from pydantic import BaseModel, Field, computed_field

class Product(BaseModel):
    name: str
    price: float
    discount: float = 0.0
    quantity: int

    @computed_field
    def discounted_price(self) -> float:
        return self.price * (1 - self.discount)
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * (1 - self.discount) * self.quantity
    
class Booking(BaseModel):
    User_id: int
    room_id: int
    nights: int = Field(..., gt=1)
    rate_per_night: float = Field(..., gt=0)
    
    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(User_id=1, room_id=101, nights=3, rate_per_night=150.0)
print(f"Booking Total Cost: ${booking.total_cost:.2f}")

product = Product(name="Laptop", price=999.99, discount=0.1, quantity=2)
print(f"Product: {product.name}")
print(f"Original Price: ${product.price:.2f}")
print(f"Discounted Price: ${product.discounted_price:.2f}")
print(f"Total Price: ${product.total_price:.2f}")
print(f"Discount: {product.discount * 100}%")