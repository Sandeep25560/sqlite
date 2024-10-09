import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sql_assignment.db')
cursor = conn.cursor()

# Create customers table
cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
)''')

# Create orders table with foreign key referencing customers
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)''')

# Try inserting an order with a non-existent customer_id (this will cause a foreign key violation)
try:
    cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (?, ?)", (999, '2024-10-10'))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Foreign key violation: {e}")

conn.close()
