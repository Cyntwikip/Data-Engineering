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
