import psycopg2
from psycopg2 import sql
from decouple import config

# Database connection details
db_params = {
    'dbname': config('DB_NAME'),
    'user': config('DB_USER'),
    'password': config('DB_PASSWORD'),
    'host': config('DB_HOST'),
    'port': config('DB_PORT'),
}

# Table creation queries
create_table_query = '''
            CREATE TABLE IF NOT EXISTS carts (
                cart_id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        '''

# Connect to the database and execute the queries
try:
    conn = psycopg2.connect(**db_params)
    print("here")
    with conn.cursor() as cursor:
        cursor.execute(create_table_query)
    conn.commit()
    print('Tables created successfully.')
except Exception as e:
    print('Error:', e)
finally:
    if conn:
        conn.close()
print('Database connection closed.')