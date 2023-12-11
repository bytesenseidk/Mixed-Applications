import sys
import Login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Email Manager | Login")
        self.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.initUi()
        
    def initUi(self):
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setObjectName("top_label")
        self.top_label.setGeometry(QtCore.QRect(0, 0, 800, 100))
        title_font = QtGui.QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)
        title_font.setWeight(75)
        self.top_label.setFont(title_font)
        self.top_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_label.setText("Email Manager")
        
        self.email_label = QtWidgets.QLabel(self)
        self.email_label.setObjectName("email_label")
        self.email_label.setGeometry(QtCore.QRect(350, 120, 100, 30))
        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(True)
        label_font.setWeight(75)
        self.email_label.setFont(label_font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setText("Email")
        
        self.email_input = QtWidgets.QLineEdit(self)
        self.email_input.setObjectName("email_input")
        self.email_input.setGeometry(QtCore.QRect(200, 150, 400, 30))
        input_font = QtGui.QFont()
        input_font.setPointSize(14)
        input_font.setBold(True)
        input_font.setWeight(50)
        self.email_input.setFont(input_font)
        self.email_input.setMaxLength(100)
        
        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setObjectName("password_label")
        self.password_label.setGeometry(QtCore.QRect(345, 200, 110, 30))
        self.password_label.setFont(label_font)
        self.password_label.setStyleSheet("")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setText("Password")

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setObjectName("password_input")
        self.password_input.setGeometry(QtCore.QRect(200, 230, 400, 30))
        self.password_input.setFont(input_font)
        self.password_input.setMaxLength(100)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.signin_button = QtWidgets.QPushButton(self)
        self.signin_button.setObjectName("signin_button")
        self.signin_button.setGeometry(QtCore.QRect(350, 280, 100, 50))
        button_font = QtGui.QFont()
        button_font.setPointSize(18)
        button_font.setBold(True)
        button_font.setWeight(75)
        self.signin_button.setFont(button_font)
        self.signin_button.setText("Login")
        self.signin_button.clicked.connect(self.login)
        
        self.status_label = QtWidgets.QLabel(self)
        self.status_label.setObjectName("status_label")
        self.status_label.setGeometry(QtCore.QRect(245, 400, 300, 30))
        self.status_label.setFont(label_font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setFont(label_font)
    
    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        try:
            user = Login.Login(email, password)
            test = user.login()
            if test:
                self.status_label.setText("Login Successful")
        except Exception as e:
            self.status_label.setText("Invalid Email or Password")
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
