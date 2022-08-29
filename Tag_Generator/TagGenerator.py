import sys, os, random, win32clipboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(300, 300, 580, 400)
        self.setWindowTitle("Tag Generator")
        
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        
        self.font_element = QtGui.QFont()
        self.font_element.setPointSize(16)
        self.font_element.setBold(True)
        self.font_element.setWeight(75)

        self.font_tags = QtGui.QFont()
        self.font_tags.setPointSize(12)
        self.font_tags.setBold(True)
        self.font_tags.setWeight(75)

        self.initUI()

        self.tag_list = self.read_tags()
        self.lcd_tagCount.display(int(len(self.tag_list)))


    def initUI(self):
        self.button_add = QtWidgets.QPushButton(self)
        self.button_add.setObjectName("button_add")
        self.button_add.setGeometry(QtCore.QRect(10, 10, 111, 81))
        self.button_add.setFont(self.font_element)
        self.button_add.setText("Add Tags")
        self.button_add.clicked.connect(self.add_tags)
        
        self.button_generate = QtWidgets.QPushButton(self)
        self.button_generate.setObjectName("button_generate")
        self.button_generate.setGeometry(QtCore.QRect(10, 100, 111, 81))
        self.button_generate.setFont(self.font_element)
        self.button_generate.setText("Generate")
        self.button_generate.clicked.connect(self.generate)
        
        self.button_copy = QtWidgets.QPushButton(self)
        self.button_copy.setObjectName("button_copy")
        self.button_copy.setGeometry(QtCore.QRect(440, 100, 131, 81))
        self.button_copy.setFont(self.font_element)
        self.button_copy.setText("Copy Tags")
        self.button_copy.clicked.connect(self.copy_tags)
        
        self.label_tagCount = QtWidgets.QLabel(self)
        self.label_tagCount.setObjectName("label_tagCount")
        self.label_tagCount.setGeometry(QtCore.QRect(430, 0, 141, 31))
        self.label_tagCount.setFont(self.font_element)
        self.label_tagCount.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tagCount.setText("Tag Counter:")
        
        self.lcd_tagCount = QtWidgets.QLCDNumber(self)
        self.lcd_tagCount.setObjectName("lcd_tagCount")
        self.lcd_tagCount.setGeometry(QtCore.QRect(440, 30, 131, 41))
        self.lcd_tagCount.setSmallDecimalPoint(False)
        self.lcd_tagCount.setDigitCount(7)
        self.lcd_tagCount.setProperty("value", 0.0)
        self.lcd_tagCount.setObjectName("lcdNumber")
        self.lcd_tagCount.setStyleSheet("QLCDNumber { color: black }")
        self.lcd_tagCount.display(0)
        
        self.spin_tagAmount = QtWidgets.QSpinBox(self)
        self.spin_tagAmount.setObjectName("spin_tagAmount")
        self.spin_tagAmount.setGeometry(QtCore.QRect(360, 120, 71, 41))
        self.spin_tagAmount.setFont(self.font_element)
        self.spin_tagAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_tagAmount.setMinimum(1)
        self.spin_tagAmount.setMaximum(999)
        self.spin_tagAmount.setValue(30)
        
        self.label_include = QtWidgets.QLabel(self)
        self.label_include.setObjectName("label_include")
        self.label_include.setGeometry(QtCore.QRect(150, 0, 141, 31))
        self.label_include.setFont(self.font_element)
        self.label_include.setAlignment(QtCore.Qt.AlignCenter)
        self.label_include.setText("Include:")
        
        self.check_pythonprogramming = QtWidgets.QCheckBox(self)
        self.check_pythonprogramming.setObjectName("check_pythonprogramming")
        self.check_pythonprogramming.setGeometry(QtCore.QRect(140, 90, 191, 21))
        self.check_pythonprogramming.setFont(self.font_tags)
        self.check_pythonprogramming.setText("pythonprogramming")
        
        self.check_programming = QtWidgets.QCheckBox(self)
        self.check_programming.setObjectName("check_programming")
        self.check_programming.setGeometry(QtCore.QRect(140, 70, 191, 21))
        self.check_programming.setFont(self.font_tags)
        self.check_programming.setText("programming")
        
        self.check_gaming = QtWidgets.QCheckBox(self)
        self.check_gaming.setObjectName("check_gaming")
        self.check_gaming.setGeometry(QtCore.QRect(140, 50, 191, 21))
        self.check_gaming.setFont(self.font_tags)
        self.check_gaming.setText("gaming")
        
        self.check_machinelearning = QtWidgets.QCheckBox(self)
        self.check_machinelearning.setObjectName("check_machinelearning")
        self.check_machinelearning.setGeometry(QtCore.QRect(140, 110, 191, 21))
        self.check_machinelearning.setFont(self.font_tags)
        self.check_machinelearning.setText("machinelearning")
        
        self.check_python = QtWidgets.QCheckBox(self)
        self.check_python.setObjectName("check_python")
        self.check_python.setGeometry(QtCore.QRect(140, 30, 191, 21))
        self.check_python.setFont(self.font_tags)
        self.check_python.setText("python")

        self.check_python_genius = QtWidgets.QCheckBox(self)
        self.check_python_genius.setObjectName("check_python_genius")
        self.check_python_genius.setGeometry(QtCore.QRect(140, 150, 191, 21))
        self.check_python_genius.setFont(self.font_tags)
        self.check_python_genius.setText("python_genius")
        
        self.check_hacking = QtWidgets.QCheckBox(self)
        self.check_hacking.setObjectName("check_hacking")
        self.check_hacking.setGeometry(QtCore.QRect(140, 130, 191, 21))
        self.check_hacking.setFont(self.font_tags)
        self.check_hacking.setText("hacking")

        self.text_tags = QtWidgets.QTextEdit(self)
        self.text_tags.setObjectName("text_tags")
        self.text_tags.setGeometry(QtCore.QRect(10, 190, 561, 191))
    

    def set_tags(self):
        add_tags = []
        tags = [
            self.check_pythonprogramming, self.check_python_genius, self.check_programming,
            self.check_gaming, self.check_machinelearning, self.check_python, self.check_hacking]
        for tag in tags:
            if tag.isChecked():
                name = "#" + str(tag.text())
                add_tags.append(name)
        return add_tags
        
    
    def read_tags(self):
        tags = []
        try:
            with open("tag_list.txt", "r") as file:
                for word in file.read().split(" "):
                    for added in tags:
                        if word == added:
                            continue
                    tags.append(word)
        except Exception as E:
            return E
        return tags
    

    def generate(self):
        tags = []
        result = ""
        amount = self.spin_tagAmount.value()
        checked_tags = self.set_tags()
        for tag in checked_tags:
            tags.append(tag)
        while len(tags) <= amount:
            word = random.choice(self.tag_list)
            if word not in tags:
                tags.append(word)
        for word in tags:
            result += word + " "
        self.text_tags.setText(result)
    

    def copy_tags(self):
        tags = self.text_tags.toPlainText()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(tags)
        win32clipboard.CloseClipboard()
        self.text_tags.setText("Tags copied to clipboard!")
    

    def add_tags(self):
        tags = []
        start_dir = str(Path.home())
        fname, *_ = QFileDialog.getOpenFileName(self, 'Choose Text File', start_dir)
        try:
            with open(fname, "r") as file:
                for word in file.read().split(" "):
                    for added in tags:
                        if word == added:
                            continue
                    tags.append(word.strip("\n"))
        except Exception as E:
            return E
        try:
            with open("tag_list.txt", "a+") as file:
                for word in file.read().split(" "):
                    for added in tags:
                        if word == added:
                            continue
                    file.write(word + " ")
        except Exception as E:
            return E


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
