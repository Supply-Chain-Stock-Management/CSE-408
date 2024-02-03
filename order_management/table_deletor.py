import psycopg2
from decouple import config

def delete_cart_table():
    try:
        # Read configuration from config.env
        # Database connection details
        db_params = {
            'dbname': config('DB_NAME'),
            'user': config('DB_USER'),
            'password': config('DB_PASSWORD'),
            'host': config('DB_HOST'),
            'port': config('DB_PORT'),
        }
        # Connect to the AWS PostgreSQL database
        connection = psycopg2.connect(**db_params)

        # Create a cursor
        cursor = connection.cursor()

        # Define the SQL statement for dropping the carts table
        drop_table_query = 'DROP TABLE IF EXISTS carts;'

        # Execute the SQL statement
        cursor.execute(drop_table_query)

        # Commit the changes
        connection.commit()

        print('Cart table deleted successfully.')


    except Exception as e:
        print('Error:', e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    delete_cart_table()
