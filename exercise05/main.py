from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import List, Optional

app = FastAPI()

class TaskDetail(BaseModel):
    detail_id: UUID
    description: str
    deadline: datetime  # Nên thêm timezone nếu có thể

class Task(BaseModel):
    task_id: UUID
    title: str
    created_at: datetime  # Nên thêm timezone nếu có thể
    details: List[TaskDetail]

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    current_time = datetime.now(timezone.utc)  # Sử dụng timezone UTC
    for detail in task.details:
        if detail.deadline.tzinfo is None:
            # Nếu deadline không có timezone, giả sử nó là UTC
            deadline = detail.deadline.replace(tzinfo=timezone.utc)
        else:
            deadline = detail.deadline
            
        if deadline <= current_time:
            raise HTTPException(status_code=400, detail="Deadline must be in the future.")
    return task

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)