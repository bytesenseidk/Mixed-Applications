import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 802, 296)
        self.setWindowTitle("Number System Converter")
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        # self.setWindowIcon(QtGui.QIcon("logo.ico"))
        self.initUI()


    def initUI(self):
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 271))
        
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)

        self.tab_binary = QWidget()
        self.tab_binary.setObjectName("tab_binary")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_binary), "Binary")

        self.toplabel_binary = QtWidgets.QLabel(self)
        self.toplabel_binary.setObjectName("toplabel_binary")
        self.toplabel_binary.setGeometry(QtCore.QRect(280, 0, 251, 41))
        font1 = QtGui.QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.toplabel_binary.setFont(font1)
        self.toplabel_binary.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabel_binary.setText("Binary")

        self.entry_binary = QtWidgets.QLineEdit(self)
        self.entry_binary.setObjectName("entry_binary")
        self.entry_binary.setGeometry(QtCore.QRect(150, 60, 571, 31))
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.entry_binary.setFont(font2)
        self.entry_binary.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entry_binary.setText("")
        
        self.label_binary = QtWidgets.QLabel(self)
        self.label_binary.setObjectName("label_binary")
        self.label_binary.setGeometry(QtCore.QRect(20, 60, 121, 31))
        font3 = QtGui.QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_binary.setFont(font3)
        self.label_binary.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_binary.setText("Binary:")

        self.entry_decimal = QtWidgets.QLineEdit(self)
        self.entry_decimal.setObjectName("entry_decimal")
        self.entry_decimal.setGeometry(QtCore.QRect(150, 100, 571, 31))
        self.entry_decimal.setFont(font2)
        self.entry_decimal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entry_decimal.setText("")

        self.label_decimal = QtWidgets.QLabel(self)
        self.label_decimal.setObjectName("label_decimal")
        self.label_decimal.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_decimal.setFont(font3)
        self.label_decimal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_decimal.setText("Decimal:")

        self.button_binary = QtWidgets.QPushButton(self)
        self.button_binary.setObjectName("button_binary")
        self.button_binary.setGeometry(QtCore.QRect(350, 160, 101, 51))
        self.button_binary.setFont(font3)
        self.button_binary.setText("Convert")
        
        self.tabWidget.addTab(self.tab_binary, "")
        self.tab_hexa = QWidget()
        self.tab_hexa.setObjectName("tab_hexa")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hexa), "Hexa")

        self.label_decimal_hexa = QtWidgets.QLabel(self)
        self.label_decimal_hexa.setObjectName("label_decimal_hexa")
        self.label_decimal_hexa.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_decimal_hexa.setFont(font3)
        self.label_decimal_hexa.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_decimal_hexa.setText("Decimal:")
        
        self.entry_hexa = QtWidgets.QLineEdit(self)
        self.entry_hexa.setObjectName(u"entry_hexa")
        self.entry_hexa.setGeometry(QtCore.QRect(150, 60, 571, 31))
        self.entry_hexa.setFont(font2)
        self.entry_hexa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entry_hexa.setText("")
        
        self.toplabel_hexa = QtWidgets.QLabel(self)
        self.toplabel_hexa.setObjectName("toplabel_hexa")
        self.toplabel_hexa.setGeometry(QtCore.QRect(280, 0, 251, 41))
        self.toplabel_hexa.setFont(font1)
        self.toplabel_hexa.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabel_hexa.setText("Hexadecimal")
        
        self.button_hexa = QPushButton(self)
        self.button_hexa.setObjectName("button_hexa")
        self.button_hexa.setGeometry(QtCore.QRect(350, 160, 101, 51))
        self.button_hexa.setFont(font3)
        self.button_hexa.setText("Convert")
        
        self.label_hexa = QtWidgets.QLabel(self)
        self.label_hexa.setObjectName("label_hexa")
        self.label_hexa.setGeometry(QtCore.QRect(20, 60, 121, 31))
        self.label_hexa.setFont(font3)
        self.label_hexa.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_hexa.setText("Hex:")
        
        self.entry_decimal_hexa = QtWidgets.QLineEdit(self)
        self.entry_decimal_hexa.setObjectName("entry_decimal_hexa")
        self.entry_decimal_hexa.setGeometry(QtCore.QRect(150, 100, 571, 31))
        self.entry_decimal_hexa.setFont(font2)
        self.entry_decimal_hexa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entry_decimal_hexa.setText("")
        
        self.tabWidget.addTab(self.tab_hexa, "")
        self.tab_octal = QWidget()
        self.tab_octal.setObjectName("tab_octal")
        
        self.label_decimal_octal = QtWidgets.QLabel(self)
        self.label_decimal_octal.setObjectName("label_decimal_octal")
        self.label_decimal_octal.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_decimal_octal.setFont(font3)
        self.label_decimal_octal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_decimal_octal.setText("Decimal:")
        
        self.entry_octal = QtWidgets.QLineEdit(self)
        self.entry_octal.setObjectName("entry_octal")
        self.entry_octal.setGeometry(QtCore.QRect(150, 60, 571, 31))
        self.entry_octal.setFont(font2)
        self.entry_octal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entry_octal.setText("")
        
        self.toplabel_octal = QtWidgets.QLabel(self)
        self.toplabel_octal.setObjectName("toplabel_octal")
        self.toplabel_octal.setGeometry(QtCore.QRect(280, 0, 251, 41))
        self.toplabel_octal.setFont(font1)
        self.toplabel_octal.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabel_octal.setText("Octadecimal")
        
        self.button_octal = QtWidgets.QPushButton(self)
        self.button_octal.setObjectName("button_octal")
        self.button_octal.setGeometry(QtCore.QRect(350, 160, 101, 51))
        self.button_octal.setFont(font3)
        self.button_octal.setText("Convert")
        
        self.label_octal = QtWidgets.QLabel(self)
        self.label_octal.setObjectName("label_octal")
        self.label_octal.setGeometry(QtCore.QRect(20, 60, 121, 31))
        self.label_octal.setFont(font3)
        self.label_octal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_octal.setText("Octal:")
        
        self.entry_decimal_octal = QtWidgets.QLineEdit(self)
        self.entry_decimal_octal.setObjectName("entry_decimal_octal")
        self.entry_decimal_octal.setGeometry(QtCore.QRect(150, 100, 571, 31))
        self.entry_decimal_octal.setFont(font2)
        self.entry_decimal_octal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entry_decimal_octal.setText("")

        self.tabWidget.addTab(self.tab_octal, "")
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_octal), "Octal")

        # QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
