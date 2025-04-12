from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Optional

app = FastAPI()
class Author(BaseModel):
    author_id: UUID
    name: str
    email: Optional[str]

class Comment(BaseModel):
    comment_id: UUID
    content: str
    created_at: datetime
    author: Author

class BlogPost(BaseModel):
    post_id: UUID
    title: str
    content: str
    published_at: datetime
    tags: List[str]
    comments: List[Comment]

@app.post("/blogposts/", response_model=BlogPost)
async def create_blog_post(blog_post: BlogPost):
    return blog_post

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)