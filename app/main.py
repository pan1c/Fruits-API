import contextlib
import logging

import uvicorn
from fastapi import FastAPI

from app import config  # Import configuration settings
from app.db import init_db  # Function to initialize the database
from app.logger import setup_logging  # Function to set up logging
from app.modules.fruit.router import router as fruit_router  # Fruit API router

# Set up logging configuration
setup_logging()
logger = logging.getLogger(__name__)


# Define the application's lifespan events (startup and shutdown)
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up application...")
    logger.info(f"Using database URL: {config.DATABASE_URL}")
    await init_db()  # Initialize the database connection
    logger.info("Application started successfully")
    logger.info("API docs: /docs, /redoc | Server: http://localhost:8000")
    yield  # Application runs here
    logger.info("Shutting down application...")


# Create FastAPI application instance with custom docs URLs and lifespan handler
app = FastAPI(
    title="Fruit API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Include the fruit router under the /api/v1 path with the "fruits" tag
app.include_router(fruit_router, prefix="/api/v1", tags=["fruits"])

# Run the application using Uvicorn if this file is executed directly
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
