from fastapi import FastAPI, HTTPException
from models import StockItem
from typing import List
from crud import get_items, add_item, update_item, delete_item

app = FastAPI()

@app.get("/stock/", response_model=List[StockItem])
def read_items():
    return get_items()

@app.post("/stock/", response_model=StockItem)
def create_item(item: StockItem):
    return add_item(item)

@app.put("/stock/{item_id}", response_model=StockItem)
def modify_item(item_id: int, item: StockItem):
    return update_item(item_id, item)

@app.delete("/stock/{item_id}")
def remove_item(item_id: int):
    return delete_item(item_id)
