# blog/routes.py

from fastapi import APIRouter, HTTPException
from typing import List
from blog.schemas import BlogCreate, Blog

router = APIRouter()

# Mock database for demonstration purposes
fake_db = []

@router.get("/", response_model=List[Blog])
async def read_blogs():
    return fake_db

@router.post("/", response_model=Blog)
async def create_blog(blog: BlogCreate):
    # Mock logic to create a blog entry
    new_blog = Blog(id=len(fake_db) + 1, title=blog.title, content=blog.content)
    fake_db.append(new_blog)
    return new_blog

@router.get("/{blog_id}", response_model=Blog)
async def read_blog(blog_id: int):
    # Mock logic to get a blog by ID
    for blog in fake_db:
        if blog.id == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.put("/{blog_id}", response_model=Blog)
async def update_blog(blog_id: int, blog: BlogCreate):
    # Mock logic to update a blog by ID
    for index, existing_blog in enumerate(fake_db):
        if existing_blog.id == blog_id:
            updated_blog = Blog(id=existing_blog.id, title=blog.title, content=blog.content)
            fake_db[index] = updated_blog
            return updated_blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/{blog_id}", response_model=Blog)
async def delete_blog(blog_id: int):
    # Mock logic to delete a blog by ID
    for index, blog in enumerate(fake_db):
        if blog.id == blog_id:
            del fake_db[index]
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

