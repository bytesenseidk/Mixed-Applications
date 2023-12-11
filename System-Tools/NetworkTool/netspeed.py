import psutil
import speedtest

class Network_Details(object):
    def __init__(self):
        self.scanner = psutil.net_if_addrs()
        self.speed = speedtest.Speedtest()
        self.interfaces = self.interface()[0]

    def interface(self):
        interfaces = []
        for interface_name, _ in self.scanner.items():
            interfaces.append(str(interface_name))
        return interfaces
    
    def return_data(self):
        down = float(str(f"{round(self.speed.download() / 1_000_000, 2)}"))
        up = float(str(f"{round(self.speed.upload() / 1_000_000, 2)}"))
        return down, up

  