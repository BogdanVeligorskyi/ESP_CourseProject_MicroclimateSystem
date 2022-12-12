import pymysql.cursors

# establishing connection with database
def get_connection():
    conn = pymysql.connect(host='192.168.0.104',
                           user='Bogdan',
                           password='***',
                           db='microclimate_system',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn
