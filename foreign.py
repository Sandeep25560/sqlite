import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sql_assignment.db')
cursor = conn.cursor()

# Create authors table
cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT
)''')

# Create books table with foreign key referencing authors
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    book_title TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
)''')

conn.commit()
conn.close()
