import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="35.169.16.216",
        user="root",
        password="Srii@773",
        database="atirath"
    )


