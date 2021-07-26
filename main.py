import os
from pymongo import MongoClient
import pymongo
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from bson import ObjectId
load_dotenv()

user_name = os.environ.get('PYMONGO_USER')
password = os.environ.get('PYMONGO_PASSWORD')

app = FastAPI()

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = f"mongodb+srv://{user_name}:{password}@cluster0.zvd6g.mongodb.net/fastapidb?retryWrites=true&w=majority"

# Create a connection using MongoClient. db used is fastapidb
client = MongoClient(CONNECTION_STRING)
fastapidb = client["fastapidb"]

# A Pydantic model for an Item


class Item(BaseModel):
    id: int
    text: str


@app.get("/items")
async def read_items():
    items = list(fastapidb["items_collection"].find({}, {"_id": 0}))
    return {"message": "All items", "items": items}


@app.get("/item/{item_id}")
async def read_item(item_id: str):
    item = list(fastapidb["items_collection"].find(
        {"_id": ObjectId(item_id)}, {"_id": 0}))
    return {"item_id": item_id, "item": item}


@app.post("/item/{item_id}")
async def save_item(item_id: str, item: Item):
    result = list(fastapidb["items_collection"].insert_one(
        {"text": item.text}))
    return "Insert a single document: inserted id: " + str(result.inserted_id) + ", acknowledged: " + str(result.acknowledged)


@app.put("/item/{item_id}")
async def modify_item(item_id: str, item: Item):
    result = list(fastapidb["items_collection"].update_one(
        {"_id": ObjectId(item_id)}, {"$set": {"text": item.text}}))
    return "Upsert one: acknowledged: " + str(result.acknowledged) + ", matched_count: " + str(result.matched_count) + ", modified_count: " + str(result.modified_count) + ", upserted_id: " + str(result.upserted_id) + ", raw_result: " + str(result.raw_result)


@app.delete("/item/{item_id}")
async def delete_item(item_id: str, item: Item):
    result = list(fastapidb["items_collection"].delete_one(
        {"_id": ObjectId(item_id)}))
    return {"item_id": item_id}
