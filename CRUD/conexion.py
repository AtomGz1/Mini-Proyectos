import mysql.connector

class BaseDatos:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = '',
            user = '',
            password = '',
            database = ''
        )
        self.cursor = self.connection.cursor()
