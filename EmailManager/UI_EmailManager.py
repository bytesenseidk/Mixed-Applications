import sys
import Login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow

class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('LoginScreen.ui', self)
        self.setWindowTitle("Email Manager | Login")
        self.login_button.clicked.connect(self.login)

    def login(self):
        self.email = self.email_input.text()
        password = self.password_input.text()
        try:
            user = Login.Login(self.email, password)
            success = user.login()
            if success:
                self.close()
                self.welcome_screen = WelcomeScreen(self.email)
                self.welcome_screen.show()
        except Exception as e:
            self.feedback_label.setText("Invalid Email or Password")
            print(e)


class WelcomeScreen(QMainWindow):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('WelcomeScreen.ui', self)
        self.setWindowTitle("Email Manager | Welcome")
        self.welcome_label.setText(f"Welcome {self.username}")
        self.logout_button.clicked.connect(self.logout)
        
    def logout(self):
        self.close()
        self.login_screen = LoginScreen()
        self.login_screen.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())
