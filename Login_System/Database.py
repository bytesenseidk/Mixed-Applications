import os
import sys
import sqlite3
import datetime


class MetaSingleton(type):
    """ Insures only a single connection to the database is available at the time. """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def __init__(self, username=None):
        self.cursor, self.connection = self.connect()
        self.table_name = username
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (time_added TEXT, data_name TEXT, data_desc TEXT)")
        
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Database_file.db")
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection
    
    def insert_data(self, data_name, data_desc):
        """ Inserts data into our table. """
        time_added = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.cursor.execute(f"INSERT INTO {self.table_name} (time_added, data_name, data_desc) VALUES(?,?,?)", (time_added, data_name, data_desc))
        self.connection.commit()

    def read_data(self):
        """ Reads data from our table. """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor.fetchall():
            print(row)


if __name__ == "__main__":
    database = Database()
    database.insert_data()
    database.read_data()
    if sys.exit():
        database.cursor.close()
        database.connection.close()

