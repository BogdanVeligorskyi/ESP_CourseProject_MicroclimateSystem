import connection
conn = connection.get_connection()

# create rooms table
def create_rooms_table():
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE Rooms (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(20), width FLOAT, length FLOAT, height FLOAT, square FLOAT) 
        """
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()

# insert new room to rooms table
def insert_to_rooms_table(name, width, length, height, square):
    try:
        cursor = conn.cursor()
        query = """
               INSERT INTO Rooms (name, width, length, height, square) VALUES (%s, %s, %s, %s, %s) 
               """
        val = (name, width, length, height, square)
        cursor.execute(query, val)
        conn.commit()
    finally:
        conn.close()

# delete room from rooms table
def delete_from_rooms_table(id):
    try:
        cursor = conn.cursor()
        query = """
               DELETE FROM Rooms WHERE id = %d
               """
        cursor.execute(query, id)
        conn.commit()
    finally:
        conn.close()
