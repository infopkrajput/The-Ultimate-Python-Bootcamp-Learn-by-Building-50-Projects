from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantity: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    
cart_data = {
    "user_id": 123,
    "items": ["laptop", "mouse", "keyboard"],
    "quantity": {"laptop": 1, "mouse": 2, "keyboard": 1}
}

cart = Cart(**cart_data)
print(cart)