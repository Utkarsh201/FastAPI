# crud.py
from fastapi import APIRouter
from mongo import get_db       # Import your DB connection
from schema import Item        # Import your Pydantic schema

# Create the router for this specific file
router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/{item_id}")
async def read_item(item_id: int):
    db = get_db()
    item = await db.items.find_one({"id": item_id}, {"_id": 0})
    
    if item:
        return item
    return {"error": "No such item where present"}

@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    db = get_db()
    update_result = await db.items.update_one(
        {"id": item_id},
        {"$set": item.model_dump()}
    )
    
    if update_result.matched_count:
        return {"message": "Item updated", "item": item.model_dump()}
    return {"error": "No such item where present"}

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    db = get_db()
    deleted_item = await db.items.find_one_and_delete({"id": item_id}, {"_id": 0})
    
    if deleted_item:
        return {"message": "Item deleted", "item": deleted_item}
    return {"error": "No such element exists"}

@router.post("/")
async def insert_item(item: Item):
    db = get_db()
    
    existing = await db.items.find_one({"id": item.id})
    if existing:
        return {"error": "Item with this id already exists"}
    
    await db.items.insert_one(item.model_dump())
    return {"message": "Item created", "item": item.model_dump()}