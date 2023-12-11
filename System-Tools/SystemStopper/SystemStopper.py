import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 526, 220)
        self.setWindowTitle("System Stopper")
        
        self.font_1 = QtGui.QFont()
        self.font_1.setFamily("Microsoft YaHei UI")
        self.font_1.setBold(False)
        self.font_1.setWeight(75)
        self.font_1.setPointSize(14)

        self.font_2 = QtGui.QFont()
        self.font_2.setFamily("Rockwell Extra Bold")
        self.font_2.setBold(True)
        self.font_2.setWeight(75)

        self.initUI()
    

    def initUI(self):
        self.label_top = QtWidgets.QLabel(self)
        self.label_top.setObjectName("label_top")
        self.label_top.setGeometry(QtCore.QRect(80, 0, 351, 51))
        self.font_2.setPointSize(24)
        self.label_top.setFont(self.font_2)
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setText("System Stopper")
        
        
        self.entry_minutes = QtWidgets.QLineEdit(self)
        self.entry_minutes.setObjectName("entry_minutes")
        self.entry_minutes.setGeometry(QtCore.QRect(170, 70, 171, 31))
        self.font_2.setPointSize(14)
        self.font_2.setBold(False)
        self.font_2.setWeight(50)
        self.entry_minutes.setFont(self.font_2)
        self.entry_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.entry_minutes.setText("")
        self.entry_minutes.setPlaceholderText("Default = Now")
        

        self.radio_shutdown = QtWidgets.QRadioButton(self)
        self.radio_shutdown.setObjectName("radio_shutdown")
        self.radio_shutdown.setGeometry(QtCore.QRect(350, 66, 141, 17))
        self.radio_shutdown.setText("Shutdown")
        self.radio_shutdown.setFont(self.font_1)
        self.radio_shutdown.setChecked(True)
        
        self.radio_restart = QtWidgets.QRadioButton(self)
        self.radio_restart.setObjectName("radio_restart")
        self.radio_restart.setGeometry(QtCore.QRect(350, 86, 141, 17))
        self.radio_restart.setText("Restart")
        self.radio_restart.setFont(self.font_1)
        
        
        self.label_minutes = QtWidgets.QLabel(self)
        self.label_minutes.setObjectName("label_minutes")
        self.label_minutes.setGeometry(QtCore.QRect(28, 70, 141, 31))
        self.font_2.setPointSize(16)
        self.label_minutes.setFont(self.font_2)
        self.label_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minutes.setText("Minutes:")
        
        self.label_activation = QtWidgets.QLabel(self)
        self.label_activation.setObjectName("label_activation")
        self.label_activation.setGeometry(QtCore.QRect(90, 110, 331, 31))
        self.font_2.setPointSize(12)
        self.label_activation.setFont(self.font_2)
        self.label_activation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_activation.setText("")
        
        
        self.button_activate = QtWidgets.QPushButton(self)
        self.button_activate.setObjectName("button_activate")
        self.button_activate.setGeometry(QtCore.QRect(180, 160, 151, 51))
        self.button_activate.setText("Activate")
        self.button_activate.setFont(self.font_2)
        self.button_activate.setFocus(True)
        self.button_activate.clicked.connect(self.activate)
    

    def activate(self):
        method = None
        try:
            timer_period = int(self.entry_minutes.text())
        except:
            timer_period = 0
        if self.radio_shutdown.isChecked():
            method = "Shutdown"
            os.system(f"shutdown -s -t {timer_period * 60}")
        else:
            method = "Restarting"
            os.system(f"shutdown -r -t {timer_period * 60}")
        if timer_period == 1:
            self.label_activation.setText(f"{method} in {timer_period} minute..")
        else:
            self.label_activation.setText(f"{method} in {timer_period} minutes..")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: lightgrey;")
    window.setWindowIcon(QtGui.QIcon("shutdown_logo.ico"))
    window.show()
    sys.exit(app.exec_())