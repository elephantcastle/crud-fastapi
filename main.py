from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# A Pydantic model for an Item
class Item(BaseModel):
    id: int
    text: str

@app.get("/items")
async def read_items():
    return {"message": "All items"}

@app.get("/item/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

@app.post("/item/{item_id}")
async def save_item(item_id: str, item:Item):
    return {"item_id": item_id}

@app.put("/item/{item_id}")
async def modify_item(item_id: str, item:Item):
    return {"item_id": item_id}
@app.delete("/item/{item_id}")
async def delete_item(item_id: str, item:Item):
    return {"item_id": item_id}