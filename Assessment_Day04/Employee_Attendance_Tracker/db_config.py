import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mdfaizu*18",
        database="emp_atd"
    )