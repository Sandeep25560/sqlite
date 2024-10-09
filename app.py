import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('sql_assignment.db')
cursor = conn.cursor()

# Creating tables
cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY, 
    customer_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY, 
    product_name TEXT)''')

# Modifying the orders table to include product_name along with product_id
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY, 
    customer_id INTEGER, 
    product_id INTEGER,
    product_name TEXT,   -- Adding product_name as a column
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY, 
    supplier_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS product_suppliers (
    product_id INTEGER, 
    supplier_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY, 
    employee_name TEXT, 
    department_id INTEGER, 
    manager_id INTEGER,
    salary REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY, 
    department_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY, 
    author_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY, 
    book_title TEXT, 
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY, 
    category_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY, 
    user_name TEXT, 
    email TEXT UNIQUE NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER, 
    course_name TEXT, 
    department_id INTEGER,
    PRIMARY KEY (course_id, department_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY, 
    student_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER, 
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id))''')

# Committing the table creation
conn.commit()

# Inserting data into the customers table
cursor.execute("INSERT INTO customers (customer_name) VALUES (?)", ('John Doe',))
cursor.execute("INSERT INTO customers (customer_name) VALUES (?)", ('Jane Smith',))

# Inserting data into the products table
cursor.execute("INSERT INTO products (product_name) VALUES (?)", ('Laptop',))
cursor.execute("INSERT INTO products (product_name) VALUES (?)", ('Smartphone',))

# Inserting data into the orders table (with product_id, product_name, and order_date)
cursor.execute("INSERT INTO orders (customer_id, product_id, product_name, order_date) VALUES (?, ?, ?, ?)", (1, 1, 'Laptop', '2024-10-01'))
cursor.execute("INSERT INTO orders (customer_id, product_id, product_name, order_date) VALUES (?, ?, ?, ?)", (2, 2, 'Smartphone', '2024-10-05'))

# Inserting data into the suppliers and product_suppliers tables
cursor.execute("INSERT INTO suppliers (supplier_name) VALUES (?)", ('Supplier A',))
cursor.execute("INSERT INTO suppliers (supplier_name) VALUES (?)", ('Supplier B',))
cursor.execute("INSERT INTO product_suppliers (product_id, supplier_id) VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO product_suppliers (product_id, supplier_id) VALUES (?, ?)", (2, 2))

# Inserting data into the employees table
cursor.execute("INSERT INTO employees (employee_name, department_id, manager_id, salary) VALUES (?, ?, ?, ?)", ('Alice', 1, None, 50000))
cursor.execute("INSERT INTO employees (employee_name, department_id, manager_id, salary) VALUES (?, ?, ?, ?)", ('Bob', 2, 1, 45000))

# Inserting data into the departments table
cursor.execute("INSERT INTO departments (department_name) VALUES (?)", ('HR',))
cursor.execute("INSERT INTO departments (department_name) VALUES (?)", ('Engineering',))

# Inserting data into the authors and books tables
cursor.execute("INSERT INTO authors (author_name) VALUES (?)", ('Author 1',))
cursor.execute("INSERT INTO authors (author_name) VALUES (?)", ('Author 2',))
cursor.execute("INSERT INTO books (book_title, author_id) VALUES (?, ?)", ('Book 1', 1))
cursor.execute("INSERT INTO books (book_title, author_id) VALUES (?, ?)", ('Book 2', 2))

# Inserting data into the categories table
cursor.execute("INSERT INTO categories (category_name) VALUES (?)", ('Electronics',))
cursor.execute("INSERT INTO categories (category_name) VALUES (?)", ('Books',))

# Inserting data into the users table
cursor.execute("INSERT INTO users (user_name, email) VALUES (?, ?)", ('Cherry', 'user1@example.com'))
cursor.execute("INSERT INTO users (user_name, email) VALUES (?, ?)", ('Sandy', 'user2@example.com'))

# Inserting data into the courses table
cursor.execute("INSERT INTO courses (course_id, course_name, department_id) VALUES (?, ?, ?)", (1, 'Math 101', 1))
cursor.execute("INSERT INTO courses (course_id, course_name, department_id) VALUES (?, ?, ?)", (2, 'Science 101', 2))

# Inserting data into the students table
cursor.execute("INSERT INTO students (student_name) VALUES (?)", ('Sandeep',))
cursor.execute("INSERT INTO students (student_name) VALUES (?)", ('Anudeep',))

# Inserting data into the student_courses table
cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (2, 2))

# Committing the inserts
conn.commit()

# Closing the connection
conn.close()
