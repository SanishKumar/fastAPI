from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    id: Optional[int] = None
    
my_posts = [{"title": "Post 1", "content": "Content of post 1", "published": True, "rating": 5, "id": 1},
            {"title": "Post 2", "content": "Content of post 2", "published": False, "rating": 3, "id": 2}]

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/posts")
def get_posts():
    return {"message": my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post.dict())
    return {"data": post_dict}
# title str, content str