import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

client = None
db = None

async def connectDB():
    # initlaliza the mongo connection 
    global client, db
    
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME")
    
    if not mongo_uri or not db_name :
        raise ValueError("Connection value to the mongoDb are not present")
    
    client = AsyncIOMotorClient(mongo_uri)
    db = client[db_name]
    
    print("Sucessfully connected to MONGODB, {db.name}")
    
async def closeDB():
    # close the connection of the DB
    global client
    if client:
        client.close()
        print("Mongo Connection Closed")

def get_db():
    return db
    