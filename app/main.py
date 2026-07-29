from fastapi import FastAPI
from .database import Base, engine
from . import models
from .routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management REST API",
    description="REST API built with FastAPI",
    version="1.0.0"
)

# Include all API routes
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to User Management REST API"
    }