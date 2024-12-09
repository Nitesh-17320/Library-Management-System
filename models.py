from database import get_db

class Book:
    @staticmethod
    def get_by_id(book_id):
        db = get_db()
        book = db.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
        db.close()
        return dict(book) if book else None

    @staticmethod
    def create(title, author, published_year):
        db = get_db()
        db.execute("INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)",
                   (title, author, published_year))
        db.commit()
        db.close()

    @staticmethod
    def update(book_id, title, author, published_year):
        db = get_db()
        db.execute("UPDATE books SET title = ?, author = ?, published_year = ? WHERE id = ?",
                   (title, author, published_year, book_id))
        db.commit()
        db.close()

    @staticmethod
    def delete(book_id):
        db = get_db()
        db.execute("DELETE FROM books WHERE id = ?", (book_id,))
        db.commit()
        db.close()
