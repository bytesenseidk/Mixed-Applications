import os
import time
import pandas
import subprocess
import threading
import logging
from scapy.all import *

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WifiMonitor:
    def __init__(self, interface):
        # Initialize the monitor with a specified network interface
        self.interface = interface
        self.networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm", "Channel", "Crypto"])
        self.networks.set_index("BSSID", inplace=True)
        self.running = True

    def callback(self, packet):
        # Processes packets captured by sniff, filtering for Dot11Beacon packets
        try:
            if packet.haslayer(Dot11Beacon):
                bssid = packet[Dot11].addr2
                ssid = packet[Dot11Elt].info.decode(errors='ignore')
                dbm_signal = packet.getlayer(RadioTap).dBm_AntSignal if packet.haslayer(RadioTap) else "N/A"
                stats = packet[Dot11Beacon].network_stats()
                self.networks.loc[bssid] = [ssid, dbm_signal, stats.get("channel"), stats.get("crypto")]
        except Exception as e:
            logging.error(f"Error processing packet: {e}")

    def change_channel(self):
        # Continuously change channel of the wireless interface to scan all available channels
        try:
            ch = 1
            while self.running:
                subprocess.run(["iw", "dev", self.interface, "set", "channel", str(ch)], check=False)
                ch = (ch % 14) + 1
                time.sleep(0.5)
        except Exception as e:
            logging.error(f"Error changing channel: {e}")

    def print_all(self):
        # Periodically clears the screen and prints all detected networks
        try:
            while self.running:
                os.system("clear")
                print("Press Ctrl+C to exit.\n")
                print(self.networks)
                time.sleep(0.5)
        except Exception as e:
            logging.error(f"Error while printing networks: {e}")

    def stop_monitor_mode(interface):
        # Safely stops monitor mode and resets the interface to managed mode
        try:
            check_mode = subprocess.run(["iw", "dev", interface, "info"], capture_output=True, text=True)
            if "type monitor" in check_mode.stdout:
                stop_result = subprocess.run(["sudo", "airmon-ng", "stop", interface], capture_output=True, text=True)
                logging.info(f"Monitor mode stopped: {stop_result.stdout}")
                subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)
                subprocess.run(["sudo", "iw", interface, "set", "type", "managed"], check=True)
                logging.info(f"{interface} has been set to managed mode and brought up.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to revert {interface} to managed mode: {e}")
        except Exception as e:
            logging.error(f"Unhandled error in stopping monitor mode: {e}")

def detect_interfaces():
    # Detect wireless interfaces available on the system
    interfaces = []
    try:
        result = subprocess.run(["iw", "dev"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "Interface" in line:
                interfaces.append(line.split()[1])
    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess error during interface detection: {e}")
    except Exception as e:
        logging.error(f"General error detected during interface detection: {e}")
    return interfaces

def activate_monitor_mode(interface):
    # Activates monitor mode on the specified interface
    try:
        check_mode = subprocess.run(["iw", "dev", interface, "info"], capture_output=True, text=True)
        if "type monitor" in check_mode.stdout:
            logging.info(f"{interface} is already in monitor mode.")
            return interface
        
        activate_result = subprocess.run(["sudo", "airmon-ng", "start", interface], capture_output=True, text=True)
        print("Activating monitor mode:\n", activate_result.stdout)
        for line in activate_result.stdout.splitlines():
            if "monitor mode enabled on" in line:
                new_interface = line.split()[-1]
                if '(' in new_interface:
                    new_interface = new_interface.split('(')[0].strip()
                return new_interface
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to activate monitor mode on {interface}: {e}")
    except Exception as e:
        logging.error(f"Unhandled error during monitor mode activation: {e}")
    return None

if __name__ == "__main__":
    # Main execution block
    interfaces = detect_interfaces()
    if not interfaces:
        logging.info("No wireless interfaces detected.")
        exit(1)

    print("Detected interfaces:")
    for idx, intf in enumerate(interfaces):
        print(f"{idx+1}. {intf}")
    print(f"{len(interfaces)+1}. Exit")
    choice = int(input("Select an interface to use or Exit: "))
    if choice == len(interfaces) + 1:
        print("Exiting...")
        exit(0)

    selected_interface = interfaces[choice - 1]
    mon_interface = activate_monitor_mode(selected_interface)
    if not mon_interface:
        logging.info("Failed to enable monitor mode.")
        exit(1)

    ap = WifiMonitor(mon_interface)
    printer = threading.Thread(target=ap.print_all)
    channel_changer = threading.Thread(target=ap.change_channel)
    printer.daemon = True
    channel_changer.daemon = True

    try:
        printer.start()
        channel_changer.start()
        sniff(prn=ap.callback, iface=mon_interface, stop_filter=lambda x: not ap.running)
    except KeyboardInterrupt:
        print("\nDetected KeyboardInterrupt, stopping...")
        ap.stop_monitor_mode(selected_interface)
        os.system("clear")
        print("Exiting...")
