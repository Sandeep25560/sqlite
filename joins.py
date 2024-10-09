import sqlite3

conn = sqlite3.connect('sql_assignment.db')
cursor = conn.cursor()

# a) Inner Join
cursor.execute('''SELECT customers.customer_name, orders.product_name 
                  FROM customers
                  INNER JOIN orders ON customers.customer_id = orders.customer_id''')
rows = cursor.fetchall()
print("Inner Join: Customers and Products")
for row in rows:
    print(row)

# b) Left Join
cursor.execute('''SELECT customers.customer_name, orders.product_name 
                  FROM customers
                  LEFT JOIN orders ON customers.customer_id = orders.customer_id''')
rows = cursor.fetchall()
print("\nLeft Join: All Customers and Their Orders (including no orders)")
for row in rows:
    print(row)

# c) Right Join
cursor.execute('''SELECT products.product_name, suppliers.supplier_name 
                  FROM products
                  LEFT JOIN product_suppliers ON products.product_id = product_suppliers.product_id
                  LEFT JOIN suppliers ON product_suppliers.supplier_id = suppliers.supplier_id''')
rows = cursor.fetchall()
print("\nRight Join (Simulated): Products and Suppliers (including products without suppliers)")
for row in rows:
    print(row)

# e) Self Join
cursor.execute('''SELECT e1.employee_name AS employee, e2.employee_name AS manager
                  FROM employees e1
                  LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id''')
rows = cursor.fetchall()
print("\nSelf Join: Employees and Their Managers")
for row in rows:
    print(row)

# f) Cross Join
cursor.execute('''SELECT products.product_name, customers.customer_name
                  FROM products
                  CROSS JOIN customers''')
rows = cursor.fetchall()
print("\nCross Join: All combinations of Products and Customers")
for row in rows:
    print(row)

# g) Natural Join
cursor.execute('''SELECT customers.customer_name, orders.order_id, orders.order_date
                  FROM customers, orders
                  WHERE customers.customer_id = orders.customer_id''')
rows = cursor.fetchall()
print("\nNatural Join (Simulated): Customers and Their Orders")
for row in rows:
    print(row)

# h) Join with Aggregation
cursor.execute('''SELECT customers.customer_name, COUNT(orders.product_id) AS total_orders
                  FROM customers
                  LEFT JOIN orders ON customers.customer_id = orders.customer_id
                  GROUP BY customers.customer_name''')
rows = cursor.fetchall()
print("\nJoin with Aggregation: Total Number of Products Ordered by Each Customer")
for row in rows:
    print(row)

# i) Multiple Joins
cursor.execute('''SELECT customers.customer_name, products.product_name, orders.order_date
                  FROM customers
                  INNER JOIN orders ON customers.customer_id = orders.customer_id
                  INNER JOIN products ON orders.product_id = products.product_id''')
rows = cursor.fetchall()
print("\nMultiple Joins: Order Details (Customer Name, Product Name, and Order Date)")
for row in rows:
    print(row)

conn.close()
