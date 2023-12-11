"""
Accesspoint scan
Host info
Interface scanner
ip_locator
Network speed
Service name finder
GUI:
    - Host Info & Interface scanner & IP Locator
    - Network Speed & Service Name Finder
    - AP Scanner
"""
import sys
import time
import threading 
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from netspeed import *


class Navigations(object):
    def host_page(self):
        self.close()
        self.host_screen = HostScreen()
        screens.addWidget(self.host_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
        
        
    
    def network_page(self):
        self.close()
        self.network_screen = NetworkScreen()
        screens.addWidget(self.network_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    

    def ap_page(self):
        self.close()
        self.ap_screen = APScreen(username)
        screens.addWidget(self.ap_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    
    def subprocesses(self):
        netspeed_thread = threading.Thread(target=self.update_netspeed)
        netspeed_thread.start()

    def update_netspeed(self):
        net_speed = Network_Details().return_data()
        self.lcd_download.display(net_speed[0])
        self.lcd_upload.display(net_speed[1])
    
    def exit(self):
        sys.exit()
        


class HostScreen(QMainWindow, Navigations):
    def __init__(self):
        super(HostScreen, self).__init__()
        loadUi('page_template.ui', self)
        
        self.exit_btn.clicked.connect(self.exit)
        
        self.subprocesses()
            

        

class APScreen(QMainWindow, Navigations):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(APScreen, self).__init__()
        loadUi('Screens/APScreen.ui', self)
        self.exit_button.clicked.connect(self.exit)

        
class NetworkScreen(QMainWindow, Navigations):
    def __init__(self):
        super(NetworkScreen, self).__init__()
        loadUi('Screens/NetworkScreen.ui', self)
        self.exit_button.clicked.connect(self.exit)  
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screens = QtWidgets.QStackedWidget()
    login_window = HostScreen()
    screens.setWindowTitle("Network Tool")
    screens.addWidget(login_window)
    screens.setFixedHeight(600)
    screens.setFixedWidth(800)
    screens.show()
    sys.exit(app.exec_())
