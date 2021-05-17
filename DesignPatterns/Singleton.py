import sqlite3

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Quiz(metaclass=Singleton):
    connection = None
    def __init__(self):
        self.cursor, self.connection = self.connect()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS TableName (time TEXT, day INT, comment TEXT)")

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Database.db")
            self.cursor = self.connection.cursor()
        return self.connection, self.cursor


if __name__ == "__main__":
    instance_0 = Quiz()
    instance_1 = Quiz()
    print(f"First Instance:  {instance_0}")
    print(f"Second Instance: {instance_1}")
