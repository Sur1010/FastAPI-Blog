# test_blog.py
import pytest
from fastapi.testclient import TestClient
from main import app
from blog.schemas import BlogCreate, Blog
from typing import List

client = TestClient(app)

@pytest.mark.asyncio
async def test_read_blogs():
    response = client.get("/blog/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list
    assert all('id' in blog and 'title' in blog and 'content' in blog for blog in response.json())  # Check structure

@pytest.mark.asyncio
async def test_create_blog():
    blog_data = {"title": "New Blog", "content": "This is a new blog post."}
    response = client.post("/blog/", json=blog_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == blog_data["title"]
    assert response_data["content"] == blog_data["content"]
    assert "id" in response_data

@pytest.mark.asyncio
async def test_read_blog():
    # First, create a blog to ensure we have one to read
    blog_data = {"title": "Another Blog", "content": "This is another blog post."}
    create_response = client.post("/blog/", json=blog_data)
    blog_id = create_response.json()["id"]

    # Now read the blog
    response = client.get(f"/blog/{blog_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == blog_id
    assert response_data["title"] == blog_data["title"]
    assert response_data["content"] == blog_data["content"]

@pytest.mark.asyncio
async def test_update_blog():
    # First, create a blog to ensure we have one to update
    blog_data = {"title": "Update This Blog", "content": "Content to be updated."}
    create_response = client.post("/blog/", json=blog_data)
    blog_id = create_response.json()["id"]

    # Now update the blog
    updated_data = {"title": "Updated Blog", "content": "Updated content."}
    response = client.put(f"/blog/{blog_id}", json=updated_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == blog_id
    assert response_data["title"] == updated_data["title"]
    assert response_data["content"] == updated_data["content"]

@pytest.mark.asyncio
async def test_delete_blog():
    # First, create a blog to ensure we have one to delete
    blog_data = {"title": "Delete This Blog", "content": "Content to be deleted."}
    create_response = client.post("/blog/", json=blog_data)
    blog_id = create_response.json()["id"]

    # Now delete the blog
    response = client.delete(f"/blog/{blog_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == blog_id
    assert response_data["title"] == blog_data["title"]
    assert response_data["content"] == blog_data["content"]

    # Try to read the deleted blog
    response = client.get(f"/blog/{blog_id}")
    assert response.status_code == 404
