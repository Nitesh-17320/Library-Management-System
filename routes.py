from flask import Blueprint, request, jsonify
from models import Book  
from database import get_db  

# Define the Blueprint
api_routes = Blueprint('api_routes', __name__)

# Route to get all books with pagination
@api_routes.route("/books", methods=["GET"])
def get_books():
    db = get_db()
    query = "SELECT * FROM books"
    params = []

    title = request.args.get("title")
    author = request.args.get("author")

    # Add search filters if title or author are provided
    if title:
        query += " WHERE title LIKE ?"
        params.append(f"%{title}%")
    if author:
        query += " AND author LIKE ?" if title else " WHERE author LIKE ?"
        params.append(f"%{author}%")
    
    # Pagination: Get 'page' and 'per_page' query parameters from the URL, with defaults
    page = request.args.get("page", 1, type=int)  # Default to page 1
    per_page = request.args.get("per_page", 10, type=int)  # Default to 10 items per page

    # Calculate offset for pagination
    offset = (page - 1) * per_page

    # Add LIMIT and OFFSET to the query
    query += " LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    # Execute the query and fetch the books
    books = db.execute(query, params).fetchall()
    db.close()

    # Convert books to a list of dictionaries and return as JSON
    return jsonify([dict(book) for book in books])

# Route to get a single book by ID
@api_routes.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.get_by_id(book_id)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Route to create a new book
@api_routes.route('/books', methods=['POST'])
def create_book():
    data = request.json  # Get the data from the request
    Book.create(data['title'], data['author'], data['published_year'])  # Create a book
    return jsonify({"message": "Book created"}), 201

# Route to update an existing book
@api_routes.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    Book.update(book_id, data['title'], data['author'], data['published_year'])  # Update the book
    return jsonify({"message": "Book updated"})

# Route to delete a book
@api_routes.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    Book.delete(book_id)  # Delete the book
    return jsonify({"message": "Book deleted"})
