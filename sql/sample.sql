-- Create the database only if it does not exist
DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_database WHERE datname = 'data_eng_db'
    ) THEN
        CREATE DATABASE data_eng_db;
    END IF;
END
$$;

-- Connect to the database
--\connect data_eng_db user=postgres host=localhost port=5432
\c data_eng_db

-- Drop the customers table if it exists
DROP TABLE IF EXISTS customers;

-- Create the customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Drop the products table if it exists
DROP TABLE IF EXISTS products;

-- Create the products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Drop the transactions table if it exists
DROP TABLE IF EXISTS transactions;

-- Create the transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample data into customers
INSERT INTO customers (first_name, last_name, email, phone) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321'),
('Alice', 'Johnson', 'alice.johnson@example.com', '1122334455');

-- Insert sample data into products
INSERT INTO products (product_name, price, stock) VALUES
('Laptop', 999.99, 10),
('Smartphone', 499.99, 20),
('Headphones', 49.99, 50);

-- Insert sample data into transactions
INSERT INTO transactions (customer_id, product_id, quantity, total_price) VALUES
(1, 1, 1, 999.99), -- John Doe buys 1 Laptop
(2, 2, 2, 999.98), -- Jane Smith buys 2 Smartphones
(3, 3, 3, 149.97); -- Alice Johnson buys 3 Headphones

-- Query to verify the data
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM transactions;