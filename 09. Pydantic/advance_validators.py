from pydantic import BaseModel, field_validator, model_validator
import datetime

class Person(BaseModel):
    name: str
    last_name: str

    @field_validator('name', 'last_name')
    def name_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Name and last name must be capitalized')
        return v
    
class User(BaseModel):
    email: str

    @field_validator('email')
    def validate_email(cls, v):
        return v.lower().strip()
    
class Product(BaseModel):
    price: float
    
    @field_validator('price', mode='before')
    def validate_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',', '').strip())
    

class DateRange(BaseModel):
    start_date: datetime.date
    end_date: datetime.date

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values['end_date'] < values['start_date']:
            raise ValueError('End date must be after start date')
        return values
