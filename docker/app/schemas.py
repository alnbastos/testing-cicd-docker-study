from pydantic import BaseModel

class Animals(BaseModel):
    name: str
    species: str
    average_weight_kg: float
    country_origin: str
    average_age: int
    photo: str

