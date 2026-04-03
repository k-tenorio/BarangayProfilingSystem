import mysql.connector

def connect_db(host=None, user=None, password=None, database=None):
    if host is None:
        host = "localhost"
    if user is None:
        user = "root"
    if password is None:
        password = ""
    if database is None:
        database = "barangay_profiling"

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )





