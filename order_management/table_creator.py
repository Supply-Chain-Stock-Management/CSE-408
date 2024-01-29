import psycopg2
from psycopg2 import sql

# Database connection details
db_params = {
    'database': 'order',
    'user': 'pg',
    'password': '12345678',
    'host': 'order.cj26q4cumd9h.ap-south-1.rds.amazonaws.com',
    'port': 5432,
}

# Table creation queries
create_table_query = '''
            CREATE TABLE IF NOT EXISTS carts (
                cart_id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
# finally:
#     if conn:
#         conn.close()
print('Database connection closed.')