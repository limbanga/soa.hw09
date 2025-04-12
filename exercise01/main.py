from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

app = FastAPI()

class Event(BaseModel):
    id: UUID = uuid4()
    name: str
    timestamp: datetime = datetime.now()

@app.post("/events/", response_model=Event)
async def create_event(event: Event):
    return event

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)