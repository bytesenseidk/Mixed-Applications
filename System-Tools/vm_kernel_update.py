#!/usr/bin/env python3

"""
pip install tqdm
or on Kali:
sudo apt install python3-tqdm
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path
from tqdm import tqdm


def require_command(name: str):
    if shutil.which(name) is None:
        print(f"[!] Required command not found: {name}")
        sys.exit(1)


def run(cmd: str):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[!] Command failed: {cmd}")
        sys.exit(result.returncode)


def main():

    steps = [
        "Check dependencies",
        "Update package index",
        "Install build dependencies",
        "Verify kernel headers",
        "Reinstall VirtualBox DKMS",
        "Load VirtualBox modules",
        "Verify VirtualBox devices",
        "Ensure host-only network",
    ]

    progress = tqdm(steps, desc="VirtualBox Repair", unit="step")

    for step in progress:

        progress.set_postfix_str(step)

        if step == "Check dependencies":
            for cmd in ("apt", "modprobe"):
                require_command(cmd)

        elif step == "Update package index":
            run("sudo apt update")

        elif step == "Install build dependencies":
            kernel = os.uname().release
            run(f"sudo apt install -y build-essential dkms linux-headers-{kernel}")

        elif step == "Verify kernel headers":
            kernel = os.uname().release
            headers = Path("/usr/src") / f"linux-headers-{kernel}"

            if headers.exists():
                print(f"[+] Headers found: {headers}")
            else:
                print("[!] Kernel headers missing")
                sys.exit(1)

        elif step == "Reinstall VirtualBox DKMS":
            run("sudo apt install --reinstall -y virtualbox-dkms")

        elif step == "Load VirtualBox modules":
            run("sudo modprobe vboxdrv")
            run("sudo modprobe vboxnetflt")
            run("sudo modprobe vboxnetadp")

        elif step == "Verify VirtualBox devices":
            devices = ["/dev/vboxdrv", "/dev/vboxnetctl"]

            for d in devices:
                if not Path(d).exists():
                    print(f"[!] Missing device: {d}")
                    sys.exit(1)

            print("[+] VirtualBox modules loaded")

        elif step == "Ensure host-only network":

            if shutil.which("VBoxManage"):

                result = subprocess.run(
                    "VBoxManage list hostonlyifs",
                    shell=True,
                    text=True,
                    capture_output=True,
                )

                if "vboxnet0" not in result.stdout:
                    print("[*] Creating vboxnet0...")
                    run("VBoxManage hostonlyif create")

                run(
                    "VBoxManage hostonlyif ipconfig vboxnet0 "
                    "--ip 192.168.56.1 --netmask 255.255.255.0"
                )

                print("[+] Host-only adapter configured")

            else:
                print("""
Manual Step Required:

Open VirtualBox → File → Tools → Network Manager
Create host-only network:

IPv4: 192.168.56.1
Mask: 255.255.255.0
""")


    print("\n[+] VirtualBox repair complete")


if __name__ == "__main__":
    main()
