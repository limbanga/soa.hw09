from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    user_id: UUID
    username: str
    email: str
    address: Address

@app.post("/users/", response_model=User )
async def create_user(user: User):
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)