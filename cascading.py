import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sql_assignment.db')
cursor = conn.cursor()

# Create categories table
cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT
)''')

# Create products table with ON DELETE CASCADE
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
)''')

conn.commit()
conn.close()
