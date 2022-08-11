import os
import sqlite3
import datetime
from argon2 import PasswordHasher

    
class MetaSingleton(type):
    """ Insures only a single connection to the database is available at the time. """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.cursor, self.connection = self.connect()
        self.table_name = "Users"
        self.time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (user_id int, username TEXT, password TEXT, created TEXT)")
        self.hasher = PasswordHasher()
        
    def connect(self):
        """ Makes sure to make a connection to the database, if no connection is active. """
        if self.connection is None:
            self.connection = sqlite3.connect("UserBank.db")
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection
    
    def get_account(self, username):
        """ Fetches the account from the database. """
        self.connection.commit()
        data = self.cursor.execute(f"SELECT * FROM {self.table_name}").fetchall()
        user_data = {"user_id": None, "username": None, "password": None, "created": None}
        for account in data:
            if username in account:
                for index, key in enumerate(user_data):
                    user_data[key] = account[index]
                return user_data
        return user_data
        
    def save_account(self, username, password):
        """ Saves the account to the database. """
        password = self.hasher.hash(password)
        try:
            user_id = self.cursor.execute(f"SELECT MAX(user_id) FROM {self.table_name}").fetchone()[0] + 1
        except:
            user_id = 0
        created = self.time
        self.cursor.execute(f"INSERT INTO {self.table_name} (user_id, username, password, created) VALUES(?,?,?,?)", (user_id, username, password, created))
        self.connection.commit()
        print(f"Account {username} created successfully!")
    
    def verify_password(self, hashed_pass, password):
        return self.hasher.verify(hashed_pass, password)
