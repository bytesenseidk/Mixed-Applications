import sys
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable


class MainWindow(QMainWindow):
    score = 0
    streak = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 590, 467)
        self.setWindowTitle("Binary Trainer")
        self.initUI()
        self.decimal_string, self.binary_string = self.question()
        self.binary_question.setText(self.binary_string)


    def initUI(self):
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setObjectName("top_label")
        self.top_label.setGeometry(QtCore.QRect(40, 0, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Extra Expanded ExtraBold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.top_label.setFont(font)
        self.top_label.setText("Binary Trainer")

        self.score_label = QtWidgets.QLabel(self)
        self.score_label.setObjectName("score_label")
        self.score_label.setGeometry(QtCore.QRect(80, 70, 101, 16))
        font1 = QtGui.QFont()
        font1.setFamily("Inconsolata Extra Expanded ExtraBold")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.score_label.setFont(font1)
        self.score_label.setText("Score:")
        self.score_count = QtWidgets.QLabel(self)
        self.score_count.setObjectName("score_count")
        self.score_count.setGeometry(QtCore.QRect(190, 70, 61, 16))
        self.score_count.setFont(font1)
        self.score_count.setText(str(MainWindow.score))

        self.streak_label = QtWidgets.QLabel(self)
        self.streak_label.setObjectName("streak_label")
        self.streak_label.setGeometry(QtCore.QRect(330, 70, 121, 16))
        self.streak_label.setFont(font1)
        self.streak_label.setText("Streak:")
        self.streak_count = QtWidgets.QLabel(self)
        self.streak_count.setObjectName("streak_count")
        self.streak_count.setGeometry(QtCore.QRect(460, 70, 61, 16))
        self.streak_count.setFont(font1)
        self.streak_count.setText(str(MainWindow.streak))

        self.convertion_label = QtWidgets.QLabel(self)
        self.convertion_label.setObjectName("convertion_label")
        self.convertion_label.setGeometry(QtCore.QRect(140, 120, 301, 20))
        self.convertion_label.setFont(font1)
        self.convertion_label.setText("Convertion Table:")
        self.convertion_table = QtWidgets.QLabel(self)
        self.convertion_table.setObjectName("convertion_table")
        self.convertion_table.setGeometry(QtCore.QRect(30, 140, 521, 31))
        font2 = QtGui.QFont()
        font2.setFamily("Inconsolata Extra Expanded ExtraBold")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.convertion_table.setFont(font2)
        self.convertion_table.setText("128  64   32   16   8   4   2   1")

        self.split_line = QtWidgets.QLabel(self)
        self.split_line.setObjectName("split_line")
        self.split_line.setGeometry(QtCore.QRect(20, 170, 551, 20))
        self.split_line.setFont(font2)
        self.split_line.setText("_______________________________________________________________________________________________")

        self.binary_question = QtWidgets.QLabel(self)
        self.binary_question.setObjectName("binary_question")
        self.binary_question.setGeometry(QtCore.QRect(20, 230, 551, 21))
        self.binary_question.setFont(font2)
        self.binary_question.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_question.setText("")

        self.octet_input_1 = QtWidgets.QLineEdit(self)
        self.octet_input_1.setObjectName("octet_input_1")
        self.octet_input_1.setGeometry(QtCore.QRect(120, 310, 81, 32))
        self.octet_input_1.setFont(font2)
        self.octet_input_1.setMaxLength(3)
        self.octet_input_1.setAlignment(QtCore.Qt.AlignCenter)
        self.octet_input_1.setText("")
        self.octet_input_2 = QtWidgets.QLineEdit(self)
        self.octet_input_2.setObjectName("octet_input_2")
        self.octet_input_2.setGeometry(QtCore.QRect(210, 310, 81, 32))
        self.octet_input_2.setFont(font2)
        self.octet_input_2.setMaxLength(3)
        self.octet_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.octet_input_2.setText("")

        self.octet_input_3 = QtWidgets.QLineEdit(self)
        self.octet_input_3.setObjectName("octet_input_3")
        self.octet_input_3.setGeometry(QtCore.QRect(300, 310, 81, 32))
        self.octet_input_3.setFont(font2)
        self.octet_input_3.setMaxLength(3)
        self.octet_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.octet_input_3.setText("")
        self.octet_input_4 = QtWidgets.QLineEdit(self)
        self.octet_input_4.setObjectName("octet_input_4")
        self.octet_input_4.setGeometry(QtCore.QRect(390, 310, 81, 32))
        self.octet_input_4.setFont(font2)
        self.octet_input_4.setMaxLength(3)
        self.octet_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.octet_input_4.setText("")

        self.check_button = QtWidgets.QPushButton(self)
        self.check_button.setObjectName("check_button")
        self.check_button.setGeometry(QtCore.QRect(230, 360, 131, 41))
        font3 = QtGui.QFont()
        font3.setFamily("Inconsolata Extra Expanded Black")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.check_button.setFont(font3)
        self.check_button.setText("Check")
        self.check_button.clicked.connect(self.verify)

        self.result_feedback = QtWidgets.QLabel(self)
        self.result_feedback.setObjectName("result_feedback")
        self.result_feedback.setGeometry(QtCore.QRect(220, 270, 151, 21))
        self.result_feedback.setFont(font2)
        self.result_feedback.setAlignment(QtCore.Qt.AlignCenter)
        self.result_feedback.setText("")


    def question(self):
        num_string = self.q_decimal()
        bin_string = self.q_binary(num_string)
        return num_string, bin_string


    def q_decimal(self):
        octet_1 = random.randint(0, 255)
        octet_2 = random.randint(0, 255)
        octet_3 = random.randint(0, 255)
        octet_4 = random.randint(0, 255)
        return f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"

    def q_binary(self, decimal_string):
        binary_string = ""
        for num in decimal_string.split("."):
            binary_string += str("{0:08b}.".format(int(num)))
        return binary_string[:-1]


    def verify(self):
        octet_1 = self.octet_input_1.text()
        octet_2 = self.octet_input_2.text()
        octet_3 = self.octet_input_3.text()
        octet_4 = self.octet_input_4.text()
        result_string = f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"
        if self.decimal_string == result_string:
            MainWindow.score += 1
            MainWindow.streak += 1
            self.result_feedback.setText("Correct")
            self.score_count.setText(str(MainWindow.score))
            self.streak_count.setText(str(MainWindow.streak))
            self.result_feedback.setText("")
        else:
            MainWindow.streak = 0
            self.result_feedback.setText("Incorrect")
            self.streak_count.setText(str(MainWindow.streak))
            self.result_feedback.setText("")
        self.decimal_string, self.binary_string = self.question()
        self.binary_question.setText(str(self.binary_string))
        self.octet_input_1.setText("")
        self.octet_input_2.setText("")
        self.octet_input_3.setText("")
        self.octet_input_4.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
