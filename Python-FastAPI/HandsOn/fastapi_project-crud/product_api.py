from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- Step 1: Define a Pydantic Model ---
class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

# --- Step 2: In-memory Database (list) ---
items = [
    {"id": 1, "name": "Laptop", "price": 75000, "quantity": 5},
    {"id": 2, "name": "Mouse", "price": 800, "quantity": 20},
]

# --- Step 3: GET - Read all items ---
@app.get("/items")
def get_items():
    return {"items": items}

# --- Step 4: GET - Read single item by ID ---
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# --- Step 5: POST - Create a new item ---
@app.post("/items")
def create_item(new_item: Item):
    # Check for duplicate ID
    for item in items:
        if item["id"] == new_item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(new_item.dict())
    return {"message": "Item added successfully", "item": new_item}

# --- Step 6: PUT - Update existing item ---
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item.dict()
            return {"message": "Item updated successfully", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")

# --- Step 7: DELETE - Remove an item ---
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
