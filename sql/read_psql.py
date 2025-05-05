import psycopg2

def read_tables():
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

        # Query and display data from the customers table
        print("Customers Table:")
        cursor.execute("SELECT * FROM customers;")
        customers = cursor.fetchall()
        for row in customers:
            print(row)

        # Query and display data from the products table
        print("\nProducts Table:")
        cursor.execute("SELECT * FROM products;")
        products = cursor.fetchall()
        for row in products:
            print(row)

        # Query and display data from the transactions table
        print("\nTransactions Table:")
        cursor.execute("SELECT * FROM transactions;")
        transactions = cursor.fetchall()
        for row in transactions:
            print(row)

    except Exception as e:
        print("Error:", e)
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Call the function to read and display the tables
read_tables()