import connection
conn = connection.get_connection()


# create sensors table
def create_sensors_table():
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE Sensors (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        room_id INTEGER, model_id INTEGER, active INTEGER,
        FOREIGN KEY (room_id) REFERENCES Rooms (id),
        FOREIGN KEY (model_id) REFERENCES Models (id)) 
        """
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


# insert new sensor to sensors table
def insert_to_sensors_table(room_id, model_id, active):
    try:
        cursor = conn.cursor()
        query = """
               INSERT INTO Sensors (room_id, model_id, active) VALUES(%s, %s, %s) 
               """
        val = (room_id, model_id, active)
        cursor.execute(query, val)
        conn.commit()
    finally:
        conn.close()


# delete sensor from sensors table
def delete_from_sensors_table(id):
    try:
        cursor = conn.cursor()
        query = """
               DELETE FROM Sensors WHERE id = %s
               """
        cursor.execute(query, id)
        conn.commit()
    finally:
        conn.close()
