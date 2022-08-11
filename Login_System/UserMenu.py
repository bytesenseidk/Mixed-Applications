import os
import time
import sqlite3
from Database import Database

class UserMenu(object):
    def __init__(self, username=None):
        self.username = username
        self.options = {
            "0": self.exit,
            "1": self.print_data,
            "2": self.add_data,
            "3": self.delete_data
        }
        # self.db = Database(self.username)

    def personal_data(self):
        pass

    def exit(self):
        print("Exitting..")
        # self.db.cursor.close()
        # self.db.connection.close()
        time.sleep(1)

    def print_data(self):
        # self.db.read_data()
        print("printing data")
        time.sleep(1)

    def add_data(self):
        os.system("cls")
        print("[ ADD DATA ]")
        data_name = input("Enter name  >> ")
        data_desc = input("Enter description  >> ")
        # self.db.add_data(data_name, data_desc)
        print("\n\nData added..")
        time.sleep(1)


    def delete_data(self):
        print("Deleting data")


    def menu(self):
        os.system("cls")
        print("[ USER MENU ]\n"
              f"[ SIGNED IN: {self.username} ]\n"
              "[0] EXIT\n"
              "[1] PRINT DATA\n"
              "[2] ADD DATA\n"
              "[3] DELETE DATA\n")
        try:
            selection = input("  >> ")
            method = self.options[selection]
            method()
        except:
            self.menu()


if __name__ == "__main__":
    UserMenu().menu()
