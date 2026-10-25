from fastapi import FastAPI,HTTPException #Import FastAPI and HTTPException
from pydantic import BaseModel #Import BaseModel from Pydantic
app = FastAPI() #Create a FastAPI instance
# --- Step 1: Define a Pydantic Model ---
class Item(BaseModel):
    id: int
    name:str
    price: float
    quantity: int
# --- Step 2: Create an In-Memory Database ---
items_db = [
    {"id": 1, "name": "Laptop", "price": 99999, "quantity": 10},
    {"id": 2, "name": "Smartphone", "price": 49999, "quantity": 25},
]
# --- Step 3: Define API Endpoints ---
@app.get("/items")
def get_items():
    return items_db
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
@app.post("/items", status_code=201)
def create_item(item: Item):
    items_db.append(item.dict())
    return item
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db[index] = updated_item.dict()
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")   
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            del items_db[index]
            return
    raise HTTPException(status_code=404, detail="Item not found")       
# --- Step 4: Run the Application ---
# To run the application, use the command:
# uvicorn main:app --reload
# Then, access the API documentation at http://
# localhost:8000/docs
# or http://localhost:8000/redoc
# for ReDoc documentation.
# You can test the endpoints using tools like Postman or curl.
# Example curl commands:
# Get all items: curl -X GET "http://localhost:8000/items"
# Get a specific item: curl -X GET "http://localhost:8000/items/1"
# Create a new item: curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"id":3,"name":"Tablet","price":29999,"quantity":15}'
# Update an item: curl -X PUT "http://localhost:8000/items/1
# -H "Content-Type: application/json" -d '{"id":1,"name":"Gaming Laptop","price":129999,"quantity":5}'
# Delete an item: curl -X DELETE "http://localhost:8000/items/1
# Note: Ensure that FastAPI and Uvicorn are installed in your Python environment.
# You can install them using pip:
# pip install fastapi uvicorn
# This code provides a simple RESTful API for managing items in an inventory.   
# It includes endpoints for creating, reading, updating, and deleting items.
