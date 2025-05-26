from pydantic import BaseModel


# Input schema for creating a fruit
class FruitIn(BaseModel):
    fruit: str
    color: str


# Output schema for returning a fruit
class FruitOut(BaseModel):
    id: int
    fruit: str
    color: str

    model_config = {"from_attributes": True}  # Enable ORM to schema conversion
