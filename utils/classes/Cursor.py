import sqlite3


class Cursor:
    """THIS IS THE CONTEXT MANAGER FOR EXECUTING SQL QUERIES ON THE PROGRAM DATABASE"""
    def __init__(self):
        self.connection = sqlite3.connect('data.db')  # 'data.db' is the database file for the program
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
