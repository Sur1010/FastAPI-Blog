from fastapi import FastAPI
from blog.routes import router as blog_router

app = FastAPI()

# Include routers
app.include_router(blog_router, prefix="/blog", tags=["blog"])
