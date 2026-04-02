from contextlib import asynccontextmanager # 1. Added for startup/shutdown
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# 2. Import the functions you built in database.py
from mongo import connectDB, closeDB, get_db

from crud import router as item_router

# 3. Define the lifespan to connect when the app starts, and close when it stops
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await connectDB()
    # The word 'yield' basically means "Pause this function here,
    yield # Your FastAPI app runs during this yield
    print("Shutting down...")
    await closeDB()
# why are we using the closeDB function ?
# Python creates an invisible "Event Loop" to manage all these background tasks. Motor (your MongoDB driver) must run on the exact same Event Loop as FastAPI. If you run connectDB() globally at the top of your file, Python tries to connect before FastAPI has finished building its Event Loop. They get out of sync, and Python will throw errors at you.
# The lifespan function guarantees that FastAPI is fully awake, the Event Loop is perfectly set up, and it is 100% safe to plug in your database.

# Declare the body using standard Python types, thanks to Pydantic.
# pydantic is a data validation library for python


# 4. Tell FastAPI to use your lifespan function
app = FastAPI(lifespan=lifespan)

app.include_router(item_router)


# # --- Test Route ---
# @app.get("/test-db")
# async def ping_database():
#     """A quick route to test if the database is successfully connected."""
#     db = get_db()
#     if db is not None:
#         # db.name dynamically gets the name of the database from your .env
#         return {"status": "success", "message": f"Connected to MongoDB database: {db.name}"}
#     return {"status": "error", "message": "Database is not connected!"}


@app.get("/")
def read_root():
    return {"message":"Server is running"}