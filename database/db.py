import sqlite3

DATABASE = "database.db"

def get_connection():
    return sqlite3.connect(DATABASE)