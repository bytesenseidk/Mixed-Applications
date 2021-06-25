#!/usr/bin/python3
import os
import time

os.system("clear")
print("Fetching updates...")
time.sleep(2)
os.system("sudo apt update -y")

os.system("clear")
print("Updating system...")
time.sleep(2)
os.system("sudo apt upgrade -y")

os.system("clear")
print("Upgrading distro...")
time.sleep(2)
os.system("sudo apt dist-upgrade -y")

os.system("clear")
print("Removing temporary packages...")
time.sleep(2)
os.system("sudo apt autoremove -y")

os.system("clear")
print("System now fully upgraded!")


""" Make script global runnable:

chmod +x script_name.py  -> Make script executable
mv script_name.py /bin/running_name  -> Copies the file to your bin folder

now this script could be executed everywhere with the given name, in this case:
"sudo running_name"
"""
