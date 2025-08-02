import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="54.225.203.231",
        user="root",
        password="Srii@773",
        database="atirath"
    )

