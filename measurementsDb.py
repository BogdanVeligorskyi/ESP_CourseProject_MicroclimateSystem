import connection
conn = connection.get_connection()


# create measurements table
def create_measurements_table():
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE Measurements (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        sensor_id INTEGER, value FLOAT, date_time VARCHAR(20),
        FOREIGN KEY (sensor_id) REFERENCES Sensors (id)) 
        """
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


# insert measurement from sensor to measurements table
def insert_to_measurements_table(sensor_id, value, date_time):
        cursor = conn.cursor()
        query = """
               INSERT INTO Measurements (sensor_id, value, date_time) VALUES(%s, %s, %s) 
               """
        val = (sensor_id, value, date_time)
        cursor.execute(query, val)
        conn.commit()


# delete measurement from sensors table
def delete_from_sensors_table(id):
    try:
        cursor = conn.cursor()
        query = """
               DELETE FROM Measurements WHERE id = %s
               """
        cursor.execute(query, id)
        conn.commit()
    finally:
        conn.close()
