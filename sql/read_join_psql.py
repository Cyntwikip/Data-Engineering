import psycopg2

def fetch_customer_sales():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname="data_eng_db",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # SQL query with CTE and JOIN
        query = """
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
        """

        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()

        # Display the results
        print("Customer Sales:")
        for row in results:
            print(f"Customer ID: {row[0]}, Name: {row[1]} {row[2]}, Total Quantity: {row[3]}")

    except Exception as e:
        print("Error:", e)
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Call the function to fetch and display customer sales
fetch_customer_sales()