from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Company(BaseModel):
    name: str
    parent: Optional[Address] = None
    
class Employee(BaseModel):
    name: str
    company: Optional[Company] = None
    
    
class TextContent(BaseModel):
    text: str = "Default text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str
    
class Article(BaseModel):
    title: str
    section: List[Union[TextContent, ImageContent]]
    
class Country(BaseModel):
    name: str
    code: str
    
class State(BaseModel):
    name: str
    country: Country
    
class City(BaseModel):
    name: str
    state: State
    
class Address(BaseModel):
    street: str
    city: City
    postal_code: str
    
class Organization(BaseModel):
    name: str
    address: Address
    branches: List[Address] = []