## Introduction to SQL and PostgreSQL

### Introduction to SQL
SQL (Structured Query Language) is a standard language used to interact with relational databases. It allows you to create, read, update, and delete data stored in tables. SQL is widely used in applications to manage structured data efficiently.

### Introduction to PostgreSQL
PostgreSQL is an advanced, open-source relational database management system (RDBMS) that supports SQL and additional features like JSON, full-text search, and advanced indexing. It is known for its reliability, extensibility, and compliance with SQL standards.

### Nuances in PostgreSQL Syntax
- **Auto-Increment**: PostgreSQL uses `SERIAL` for auto-incrementing primary keys instead of `AUTO_INCREMENT` (used in MySQL).
- **Computed Columns**: PostgreSQL supports `GENERATED ALWAYS AS` for computed columns, but the expression must reference columns within the same table.
- **Case Sensitivity**: PostgreSQL treats unquoted identifiers as lowercase, so `ColumnName` is equivalent to `columnname` unless quoted as `"ColumnName"`.

> **Note**: While SQL is a standard language, different database systems (e.g., PostgreSQL, MySQL, SQL Server) have slight variations in syntax and features. Always refer to the documentation for the specific database you are using.

---

## Basic Syntax
Here are some common SQL commands:
- **Create a Table**:
  ```sql
  CREATE TABLE table_name (
      column_name data_type constraints
  );
  ```
  ```sql
  CREATE TABLE customers (
      customer_id SERIAL PRIMARY KEY,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50) NOT NULL,
      email VARCHAR(100) UNIQUE NOT NULL
  );
  ```
- **Insert Data**:
  ```sql
  INSERT INTO table_name (column1, column2)
  VALUES (value1, value2);
  ```
  ```sql
  INSERT INTO customers (first_name, last_name, email) 
  VALUES ('John', 'Doe', 'john.doe@example.com');
    ```
- **Select Data**:
  ```sql
  SELECT column1, column2 
  FROM table_name 
  WHERE condition;
  ```
  ```sql
  SELECT first_name, last_name 
  FROM customers 
  WHERE email = 'john.doe@example.com';
  ```
- **Delete Data**:
  ```sql
  DELETE FROM table_name WHERE condition;
  ```
  ```sql
  DELETE FROM customers 
  WHERE email = 'john.doe@example.com';
  ```

---

## Installing PostgreSQL
1. Download and install PostgreSQL from the [official website](https://www.postgresql.org/download/).
2. During installation, set up a username and password for the PostgreSQL superuser (default username is `postgres`).

---

## Running the SQL Script
To execute the provided `sample.sql` file:
1. Open a terminal.
2. Run the following command:
   ```bash
   psql -U postgres -d your_database_name -f sample.sql
   ```
   Replace `your_database_name` with the name of your database.

---

### Sample Commands Inside `psql`
Here are some useful commands to use within the `psql` interactive terminal:
- **Connect to a Database**:
  ```sql
  \c your_database_name
  ```
- **List All Databases**:
  ```sql
  \l
  ```
- **List All Tables**:
  ```sql
  \dt
  ```
- **Describe a Table**:
  ```sql
  \d table_name
  ```
- **Exit `psql`**:
  ```sql
  \q
  ```

---

### Example Workflow
1. Install PostgreSQL,
2. Run the `sample.sql` file to:
    - create a database (e.g., `data_eng_db`) and connect automatically
    - create tables
    - insert sample data
   ```bash
   psql -f sample.sql
   ```
3. Open `psql` and query the data:
   ```bash
   psql -U postgres -d data_eng_db
   SELECT * FROM customers;
   ```

---

### Using Python to Read PostgreSQL Tables

You can use the provided Python script (`read_psql.py`) to connect to your PostgreSQL database and read data from the tables.

#### Prerequisites
1. Install the `psycopg2` library:
   ```bash
   pip install psycopg2
   ```
2. Update the database credentials in the script:
   - Replace `your_database_name`, `your_username`, and `your_password` with your PostgreSQL details.

#### Running the Script
1. Save the script as `read_psql.py`.
2. Run the script:
   ```bash
   python read_psql.py
   ```
3. The script will display the contents of the `customers`, `products`, and `transactions` tables.

#### Example Output
```plaintext
Customers Table:
(1, 'John', 'Doe', 'john.doe@example.com')

Products Table:
(1, 'Laptop', 999.99)

Transactions Table:
(1, 1, 1, 1, 999.99, '2023-10-01 12:00:00')
```

Make sure your PostgreSQL server is running and the tables are populated with data before executing the script.

---

### Quick Introduction to JOINs and CTEs

#### JOINs
A **JOIN** in SQL is used to combine rows from two or more tables based on a related column. Common types of JOINs include:
- **INNER JOIN**: Returns rows with matching values in both tables.
- **LEFT JOIN**: Returns all rows from the left table and matching rows from the right table.
- **RIGHT JOIN**: Returns all rows from the right table and matching rows from the left table.

Example:
```sql
SELECT customers.first_name, products.product_name
FROM transactions
JOIN customers ON transactions.customer_id = customers.customer_id
JOIN products ON transactions.product_id = products.product_id;
```

#### Common Table Expressions (CTEs)
A **CTE** is a temporary result set defined within a SQL query. It improves readability and can be reused within the query.

Example:
```sql
WITH customer_sales AS (
    SELECT customer_id, SUM(quantity) AS total_quantity
    FROM transactions
    GROUP BY customer_id
)
SELECT c.first_name, cs.total_quantity
FROM customers c
JOIN customer_sales cs ON c.customer_id = cs.customer_id;
```

CTEs are especially useful for breaking down complex queries into smaller, manageable parts.

---

### Using JOIN and CTE in SQL with Python

The `read_join_psql.py` script demonstrates how to use a Common Table Expression (CTE) and a JOIN to fetch aggregated data from a PostgreSQL database.

#### SQL Query Explanation
The script uses the following SQL query:
```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(quantity) AS total_quantity
    FROM transactions
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    cs.total_quantity
FROM customers c
JOIN customer_sales cs
ON c.customer_id = cs.customer_id;
```

1. **CTE (`customer_sales`)**:
   - Aggregates the total quantity of products purchased by each customer from the `transactions` table.
2. **JOIN**:
   - Combines the `customers` table with the aggregated data (`customer_sales`) using the `customer_id` column.

#### Running the Script
1. Ensure the database is populated with the required tables and sample data.
2. Run the script:
   ```bash
   python read_join_psql.py
   ```

#### Example Output
```plaintext
Customer Sales:
Customer ID: 1, Name: John Doe, Total Quantity: 5
Customer ID: 2, Name: Jane Smith, Total Quantity: 7
Customer ID: 3, Name: Alice Johnson, Total Quantity: 7
```

This script is useful for analyzing customer purchase behavior by combining and aggregating data from multiple tables.

---
