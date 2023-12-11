import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class Navigations(object):
    def host_page(self):
        self.close()
        self.host_screen = HostScreen()
        screens.addWidget(self.host_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
        
        
    """,
    def register_page(self):
        self.close()
        self.signup_screen = SignUpScreen()
        screens.addWidget(self.signup_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    

    def welcome_page(self, username):
        self.close()
        self.ap_screen = APScreen(username)
        screens.addWidget(self.ap_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    """
    def update_netspeed(self):
        self.lcd_download.display(5)
        self.lcd_upload.display(4)
    
    def exit(self):
        sys.exit()
        


class HostScreen(QMainWindow, Navigations):
    def __init__(self):
        super(HostScreen, self).__init__()
        loadUi('page_template.ui', self)
        screens.setWindowTitle("Network Tool")
        #self.login_button.clicked.connect(self.login)
        #self.signup_button.clicked.connect(self.register_page)
        self.exit_btn.clicked.connect(self.exit)
        self.update_netspeed()
        
"""
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
            self.feedback_label.setText(e)


class APScreen(QMainWindow, Navigations):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(APScreen, self).__init__()
        loadUi('Screens/APScreen.ui', self)
        screens.setWindowTitle("Login System | Welcome")
        self.welcome_label.setText(f"Welcome {self.username}")
        self.logout_button.clicked.connect(self.host_page)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()

        
class SignUpScreen(QMainWindow, Navigations):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi('Screens/SignUpScreen.ui', self)
        screens.setWindowTitle("Login System | Sign Up")
        self.create_button.clicked.connect(self.sign_up)
        self.login_button.clicked.connect(self.host_page)
        self.exit_button.clicked.connect(self.exit)  
        
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screens = QtWidgets.QStackedWidget()
    login_window = HostScreen()
    
    screens.addWidget(login_window)
    screens.setFixedHeight(600)
    screens.setFixedWidth(800)
    screens.show()
    sys.exit(app.exec_())