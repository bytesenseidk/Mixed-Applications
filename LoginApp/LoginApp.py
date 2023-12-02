import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from UserBank import *


class Navigations(object):
    def login_page(self):
        self.close()
        self.login_screen = LoginScreen()
        screens.addWidget(self.login_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
        
    def register_page(self):
        self.close()
        self.signup_screen = SignUpScreen()
        screens.addWidget(self.signup_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    
    def welcome_page(self, username):
        self.close()
        self.welcome_screen = WelcomeScreen(username)
        screens.addWidget(self.welcome_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
        
    def exit(self):
        self.closeDb()
        sys.exit()
        
    def closeDb(self):
        self.database.cursor.close()
        self.database.connection.close()


class LoginScreen(QMainWindow, Navigations):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('Screens/LoginScreen.ui', self)
        screens.setWindowTitle("Login System | Login")
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.register_page)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()
        
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user_data = self.database.get_account(username)
        try:
            if user_data["username"] == username and self.database.verify_password(user_data["password"], password):
                self.welcome_page(username)
            else:
                self.feedback_label.setText("Invalid username or password")
        except Exception as e:
            self.feedback_label.setText("Invalid username or password")


class WelcomeScreen(QMainWindow, Navigations):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('Screens/WelcomeScreen.ui', self)
        screens.setWindowTitle("Login System | Welcome")
        self.welcome_label.setText(f"Welcome {self.username}")
        self.logout_button.clicked.connect(self.login_page)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()

        
class SignUpScreen(QMainWindow, Navigations):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi('Screens/SignUpScreen.ui', self)
        screens.setWindowTitle("Login System | Sign Up")
        self.create_button.clicked.connect(self.sign_up)
        self.login_button.clicked.connect(self.login_page)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()


    def _validate_input(self, username, password, v_password):
        user_len = lambda username: "True" if len(username) > 5 and len(username) < 15 else "Min. 6 & Max. 16 characters in usernames."
        same_pass = lambda password, v_password: "True" if password == v_password else "Passwords do not match!"
        pass_len = lambda password: "True" if len(password) > 7 and len(password) < 63 else "Min. 8 & Max. 64 characters in passwords"
        user_exist = ""
        conditions = [user_len(username), same_pass(password, v_password), pass_len(password)]
        for condition in conditions:
            if condition != "True":
                self.feedback_label.setText(condition)
                return False
        return True
        

    def sign_up(self):
        username = self.username_input.text()
        password = self.password_input.text()
        v_password = self.confirm_password_input.text()
        if self._validate_input(username, password, v_password):
            user_data = self.database.get_account(username)
            if user_data["username"] is None:
                self.database.save_account(username, password)
                self.login_page()
            else:
                self.feedback_label.setText("Username already exists!")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screens = QtWidgets.QStackedWidget()
    login_window = LoginScreen()
    
    screens.addWidget(login_window)
    screens.setFixedHeight(600)
    screens.setFixedWidth(800)
    screens.show()
    sys.exit(app.exec_())