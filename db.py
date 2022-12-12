import connection
conn = connection.get_connection()

# create new database 'microclimate_system'
def create_db():
    try:
        cursor = conn.cursor()
        query = "CREATE DATABASE microclimate_system"
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


