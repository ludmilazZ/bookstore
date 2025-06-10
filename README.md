# Bookstore API

A REST API for a bookstore built with FastAPI. This project is for educational purposes only, demonstrating various design patterns and best practices in Python API development.

## Project Structure
```
app/
├── core/
│   └── config.py
├── models/
│   └── book.py
├── repositories/
│   └── book_repository.py
├── routers/
│   └── books.py
└── main.py
```

## Setup

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Run the following command:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing the API

### Using a Web Browser
Simply open `http://localhost:8000/api/books` in your web browser.

### Using Insomnia
1. Create a new request in Insomnia
2. Set the HTTP method to `GET`
3. Set the URL to `http://localhost:8000/api/books`
4. Add the following headers:
   - `Accept: application/json`
   - `Content-Type: application/json`

## Endpoints

### Books
- `GET /api/books`: Get all books
- `GET /api/books/{book_id}`: Get a specific book
- `POST /api/books`: Create a new book
- `PUT /api/books/{book_id}`: Update a book
- `DELETE /api/books/{book_id}`: Delete a book

### Example Book Object
```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925,
  "price": 19.99,
  "in_stock": true
}
```

## API Construction and Design Patterns

This project is built for educational purposes to demonstrate various design patterns and architectural principles in Python API development. Here are the main patterns and principles used:

### 1. Repository Pattern
- Separates data access logic from business logic
- Abstracts the data source (currently in-memory, could be changed to database)
- Provides a clean interface for data operations

### 2. Model-View-Controller (MVC) Pattern
- Models: Define data structure (Pydantic models)
- Controllers: Handle HTTP requests (FastAPI routers)
- Views: JSON responses (handled by FastAPI)

### 3. Dependency Injection
- FastAPI's dependency injection system
- Makes the code more testable and maintainable

### 4. Data Transfer Object (DTO) Pattern
- Separates input/output models from internal models
- `BookCreate`: For creating new books
- `Book`: For complete book data including ID

### 5. Factory Pattern
- Used in the repository for creating book objects
- Encapsulates object creation logic

### 6. Single Responsibility Principle
- Each module has a single responsibility:
  - `models/`: Data structure definition
  - `repositories/`: Data access
  - `routers/`: Request handling
  - `core/`: Configuration

### 7. Open/Closed Principle
- The code is open for extension but closed for modification
- New features can be added without changing existing code
- Example: Adding new filters to GET /books endpoint

### 8. Interface Segregation
- Clean separation of concerns
- Each interface (router, repository, model) has specific responsibilities

### 9. Error Handling Pattern
- Consistent error handling across the application
- Proper error status codes and messages

### 10. Configuration Pattern
- Centralized configuration
- Environment-based settings

## Benefits of this Architecture

1. **Maintainability**: Easy to modify and extend
2. **Testability**: Components can be tested in isolation
3. **Scalability**: Easy to add new features
4. **Separation of Concerns**: Clear boundaries between components
5. **Code Reusability**: Components can be reused in other parts of the application

## Note
This project is for educational purposes only. It demonstrates various design patterns and best practices but is not intended for production use. In a real-world scenario, you would need to add:
- Database integration
- Authentication and authorization
- Input validation
- Logging
- Testing
- CI/CD pipeline
- And other production-ready features 