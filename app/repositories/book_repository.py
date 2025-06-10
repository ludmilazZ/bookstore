from typing import List, Optional
from app.models.book import Book

class BookRepository:
    def __init__(self):
        self.books = [
            Book(
                id=1,
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                year=1925,
                price=19.99,
                in_stock=True
            ),
            Book(
                id=2,
                title="To Kill a Mockingbird",
                author="Harper Lee",
                year=1960,
                price=15.99,
                in_stock=True
            ),
            Book(
                id=3,
                title="1984",
                author="George Orwell",
                year=1949,
                price=12.99,
                in_stock=False
            )
        ]

    def get_all(self) -> List[Book]:
        return self.books

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.id == book_id), None)

    def create(self, book: Book) -> Book:
        # Validate that the book doesn't already exist
        if any(b.id == book.id for b in self.books):
            raise ValueError(f"Book with id {book.id} already exists")
        self.books.append(book)
        return book

    def update(self, book_id: int, book_data: Book) -> Optional[Book]:
        book = self.get_by_id(book_id)
        if book:
            for key, value in book_data.dict().items():
                if key != 'id':  # Don't update the id
                    setattr(book, key, value)
        return book

    def delete(self, book_id: int) -> bool:
        book = self.get_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False 