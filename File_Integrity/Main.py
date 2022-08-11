import sys
from Validations import MD5, SHA1, SHA256
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 805, 423)
        self.setWindowTitle("File Integrity Checker")
        self.initUI()

    def initUI(self):
        self.label_top = QtWidgets.QLabel(self)
        self.label_top.setObjectName("label_top")
        self.label_top.setGeometry(QtCore.QRect(20, 0, 771, 41))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Ultra Expanded SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_top.setFont(font)
        self.label_top.setText("File Integrity Checker")

        self.file_entry = QtWidgets.QLineEdit(self)
        self.file_entry.setObjectName("file_entry")
        self.file_entry.setGeometry(QtCore.QRect(180, 70, 451, 32))

        self.button_file = QtWidgets.QPushButton(self)
        self.button_file.setObjectName("button_file")
        self.button_file.setGeometry(QtCore.QRect(300, 110, 211, 34))
        font1 = QtGui.QFont()
        font1.setFamily("Inconsolata Ultra Expanded SemiBold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.button_file.setFont(font1)
        self.button_file.setText("Choose File")
        self.button_file.clicked.connect(self.set_function)

        self.hash_entry = QtWidgets.QLineEdit(self)
        self.hash_entry.setObjectName("hash_entry")
        self.hash_entry.setGeometry(QtCore.QRect(180, 200, 451, 32))

        self.button_check = QtWidgets.QPushButton(self)
        self.button_check.setObjectName("button_check")
        self.button_check.setGeometry(QtCore.QRect(320, 320, 171, 34))
        self.button_check.setFont(font1)
        self.button_check.setText("Check")
        self.button_check.clicked.connect(self.check_function)

        self.hash_choice = QtWidgets.QComboBox(self)
        self.hash_choice.addItem("")
        self.hash_choice.addItem("")
        self.hash_choice.addItem("")
        self.hash_choice.setObjectName("hash_choice")
        self.hash_choice.setGeometry(QtCore.QRect(360, 160, 91, 31))
        self.hash_choice.setItemText(0, "MD5")
        self.hash_choice.setItemText(1, "SHA1")
        self.hash_choice.setItemText(2, "SHA256")

        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setObjectName("label_result")
        self.label_result.setGeometry(QtCore.QRect(280, 240, 251, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Inconsolata Ultra Expanded SemiBold")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_result.setFont(font2)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setText("")

        self.log_box = QtWidgets.QCheckBox(self)
        self.log_box.setObjectName("log_box")
        self.log_box.setGeometry(QtCore.QRect(640, 70, 81, 31))
        self.log_box.setFont(font1)
        self.log_box.setText("Log")


    def set_function(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            self.file_entry.setText(file_name)


    def check_function(self):
        hashes = {"MD5": MD5,
                  "SHA1": SHA1,
                  "SHA256": SHA256
        }
        file, hash_sum = self.file_entry.text(), str(self.hash_entry.text()).strip()
        hash = str(self.hash_choice.currentText())
        generated_hash_temp = hashes[hash]
        generated_hash = str(generated_hash_temp(file)).strip()
        if hash_sum == generated_hash:
            result = "Match!"
        else:
            result = "No Match!"
        if self.log_box.isChecked():
            with open("Integrity_log.txt", "a") as logger:
                logger.write(f"File: {str(file.split('/')[-1])}\nGenerated Hash: {generated_hash}\nOrigional Hash: {hash_sum}\nResult: {result}\n{'-'*30}\n\n")
        self.label_result.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
