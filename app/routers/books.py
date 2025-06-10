from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.book import Book, BookCreate
from app.repositories.book_repository import BookRepository

router = APIRouter()
book_repository = BookRepository()

@router.get("/books", response_model=List[Book])
async def get_books(
    in_stock: Optional[bool] = Query(None, description="Filter by stock availability"),
    author: Optional[str] = Query(None, description="Filter by author name"),
    min_price: Optional[float] = Query(None, description="Minimum price"),
    max_price: Optional[float] = Query(None, description="Maximum price")
):
    try:
        books = book_repository.get_all()
        
        # Apply filters if provided
        if in_stock is not None:
            books = [book for book in books if book.in_stock == in_stock]
        if author:
            books = [book for book in books if author.lower() in book.author.lower()]
        if min_price is not None:
            books = [book for book in books if book.price >= min_price]
        if max_price is not None:
            books = [book for book in books if book.price <= max_price]
            
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving books: {str(e)}")

@router.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    try:
        if book_id < 1:
            raise HTTPException(status_code=400, detail="Book ID must be positive")
            
        book = book_repository.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
        return book
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving book: {str(e)}")

@router.post("/books", response_model=Book, status_code=201)
async def create_book(book: BookCreate):
    try:
        # Validate book data
        if book.year < 0:
            raise HTTPException(status_code=400, detail="Year cannot be negative")
        if book.price < 0:
            raise HTTPException(status_code=400, detail="Price cannot be negative")
            
        # Convert BookCreate to Book by adding an id
        new_book = Book(
            id=len(book_repository.books) + 1,
            **book.dict()
        )
        return book_repository.create(new_book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating book: {str(e)}")

@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookCreate):
    try:
        if book_id < 1:
            raise HTTPException(status_code=400, detail="Book ID must be positive")
            
        # Validate book data
        if book.year < 0:
            raise HTTPException(status_code=400, detail="Year cannot be negative")
        if book.price < 0:
            raise HTTPException(status_code=400, detail="Price cannot be negative")
            
        updated_book = book_repository.update(book_id, Book(**book.dict()))
        if not updated_book:
            raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
        return updated_book
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating book: {str(e)}")

@router.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    try:
        if book_id < 1:
            raise HTTPException(status_code=400, detail="Book ID must be positive")
            
        if not book_repository.delete(book_id):
            raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting book: {str(e)}") 