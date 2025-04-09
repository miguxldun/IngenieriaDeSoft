from pydantic import BaseModel

class StockItem(BaseModel):
    id: int
    name: str
    quantity: int
