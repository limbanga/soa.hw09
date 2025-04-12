from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

app = FastAPI()


class Product(BaseModel):
    product_id: UUID
    name: str
    price: float

class Order(BaseModel):
    order_id: UUID
    products: List[Product]
    order_date: datetime

@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    return order

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)