from pydantic import BaseModel

class Item(BaseModel):
    id : int
    name : str
    price : int
    is_offer : bool | None
    