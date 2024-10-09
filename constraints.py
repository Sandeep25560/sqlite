import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sql_assignment.db')
cursor = conn.cursor()

# a) Unique Constraint
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT,
    email TEXT UNIQUE NOT NULL
)''')

# b) Check Constraint
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL CHECK (price > 0)
)''')

# c) Primary Key and Consistency
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER,
    course_name TEXT,
    department_id INTEGER,
    PRIMARY KEY (course_id, department_id)
)''')

# d) Foreign Key and Consistency
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)
)''')

# e) Not Null Constraint
cursor.execute('''
CREATE TABLE IF NOT EXISTS users_not_null (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
)''')

# f) Adding a Check Constraint to an Existing Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    salary REAL CHECK (salary > 0)
)''')

# g) Composite Key Constraint
# This has already been defined above.

conn.commit()
conn.close()

print("All tables created successfully with specified constraints.")
