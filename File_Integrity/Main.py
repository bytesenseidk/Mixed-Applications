import sys
from Validations import MD5, SHA1, SHA256
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('FileIntegrety.ui', self)
        self.setWindowTitle("File Integrity Checker")
        self.button_file.clicked.connect(self.set_function)
        self.button_check.clicked.connect(self.check_function)

    def set_function(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", 
                                "","All Files (*);;Python Files (*.py)", options=options)
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
