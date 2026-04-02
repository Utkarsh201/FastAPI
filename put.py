from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
# Declare the body using standard Python types, thanks to Pydantic.
# pydantic is a data validation library for python

# use fastapi dev put.py to run the file 

app = FastAPI()

class Item(BaseModel):
    id : int
    name : str
    price : int
    is_offer : bool | None


arr:List[Item] = []
# this is going to be an array where i can store my item  

@app.get("/")
def read_root():
    return {"Hello":"World"}
# these read_root, read_item, update_item are basically callback function just like in the case of nodejs

# In FastAPI endpoint functions,  the return value is what gets sent back to the client as the HTTP response body (usually JSON)

@app.get("/items/{item_id}")
def read_item(item_id:int, q:str | None = None):
    for idx, item in enumerate(arr):
        if item.id == item_id:
            return {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "is_offer": item.is_offer,
            }
    return {"error" : "No such item where present"}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    for idx, item in enumerate(arr):
        if item.id == item_id:
            arr[idx] = Item(
                id=item_id,
                name=item.name,
                price=item.price,
                is_offer=item.is_offer,
            )
            return {"message": "Item updated", "item": arr[idx]}
    return {"error" : "No such item where present"}


@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    for idx, item in enumerate(arr):
        if item.id == item_id:
            val = arr.pop(idx)
            return {"message": "Item deleted", "item": val}
    return {"error":"No such element exists"}

@app.post("/items")
def insert_item(item:Item):
    for existing in arr:
        if existing.id == item.id:
            return {"error": "Item with this id already exists"}
    arr.append(item)
    return {"message": "Item created", "item": item}

