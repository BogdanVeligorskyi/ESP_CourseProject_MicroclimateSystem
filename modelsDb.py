import connection
conn = connection.get_connection()


# create models of sensors table
def create_models_table():
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE Models (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(15), measure VARCHAR(20), range_min FLOAT, range_max FLOAT) 
        """
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


# insert new model to the models table
def insert_to_models_table(name, measure, range_min, range_max):
    try:
        cursor = conn.cursor()
        query = """
               INSERT INTO Models (name, measure, range_min, range_max) VALUES(%s, %s, %s, %s) 
               """
        val = (name, measure, range_min, range_max)
        cursor.execute(query, val)
        conn.commit()
    finally:
        conn.close()


# delete model from models table
def delete_from_models_table(id):
    try:
        cursor = conn.cursor()
        query = """
               DELETE FROM Models WHERE id = %d
               """
        cursor.execute(query, id)
        conn.commit()
    finally:
        conn.close()


# update model info in models table
def update_in_models_table(id, name, measure, range_min, range_max):
    try:
        cursor = conn.cursor()
        query = """
               UPDATE Models SET name=%s, measure=%s, range_min=%s, range_max=%s WHERE id=%s 
               """
        val = (name, measure, range_min, range_max, id)
        cursor.execute(query, val)
        conn.commit()
    finally:
        conn.close()

