import sqlite3

# This function returns a database connection
def get_db():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row  # This makes rows behave like dictionaries
    return conn

# Function to initialize the database
def init_db():
    db = get_db()
    # Create the books table if it doesn't exist
    db.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_year INTEGER NOT NULL
        );
    ''')
    db.commit()
    db.close()
