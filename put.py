from fastapi import FastAPI
from pydantic import BaseModel
# Declare the body using standard Python types, thanks to Pydantic.
# pydantic is a data validation library for python

# use fastapi dev put.py to run the file 

app = FastAPI()

class Item(BaseModel):
    name : str
    price : int
    is_offer : bool | None

@app.get("/")
def read_root():
    return {"Hello":"World"}
# these read_root, read_item, update_item are basically callback function just like in the case of nodejs

@app.get("/items/{items_id}")
def read_item(item_id:int, q:str | None = None):
    return {"item_name":item.name, "item_id":item_id}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"item_name":item.name, "item_id":item_id}

# http://127.0.0.1:8000/docs

