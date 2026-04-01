from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to the fastAPI server !"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:str = None):
    return {"item_id":item_id, "query_string":q}



# http://127.0.0.1:8000/items/5?q=hello 
# http://127.0.0.1:8000/docs -> you can visit this server for the viewing the doc of the website you build, this is done with the help of the swagger UI
# http://127.0.0.1:8000/redoc this is an alternative option


# You already created an API that:

# Receives HTTP requests in the paths / and /items/{item_id}.
# Both paths take GET operations (also known as HTTP methods).
# The path /items/{item_id} has a path parameter item_id that should be an int.
# The path /items/{item_id} has an optional str query parameter q.