import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bookstore API",
    description="A simple REST API for a bookstore",
    version="1.0.0",
    debug=True  # Enable debug mode
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
async def root():
    logger.debug("Root endpoint called")
    return {
        "message": "Welcome to the Bookstore API",
        "documentation": "/docs",
        "endpoints": {
            "books": "/api/books",
            "book_by_id": "/api/books/{book_id}"
        }
    }

# Include routers
app.include_router(books.router, prefix="/api", tags=["books"])

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting the application in debug mode")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 