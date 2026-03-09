import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: str, check:bool=True) -> subprocess.CompleatedProcess:
    # Run the commands with error checking
    print(f"\n[+] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True)
    if check and result.returncode != 0:
        print(f"[!] Command failed with exit code {result.returncode}: {cmd}")
        sys.exit(result.returncode)
    return result

def require_command(name: str) -> None:
    # Checks if command exists
    if shutil.which(name) is None:
        print(f"[!] Required command not found: {name}")
        sys.exit(1)

def main() -> None:
    for cmd in ("apt", "modprobe", "uname", "grep", "ls"):
        require_command(cmd)
    
    kernel = subprocess.check_output(["uname", "-r"], text="-r", text=True).strip()
    header_path = Path("/usr/src") / f"linux-headers-{kernel}"

    print("[*] Current kernel:", kernel)

    print("\n===== [ Step 1: Refresh package index ] =====")
    run("sudo apt update -y")

    print("\n===== [ Step 2: Install required build dependencies ] =====")
    run(f"sudo apt install -y build-essential dkms linux-headers-{kernel}")

    print("\n===== [ Step 3: Verify kernel headers ] =====")
    if headers_path.exists():
        print(f"[+] Found headers: {headers_path}")
    else:
        print(f"[!] Missing headers: {headers_path}")
        sys.exit(1)
    
    print("\n===== [ Step 4: Reinstall VirtualBox DKMS ] =====")
    run("sudo apt install --reinstall -y virtualbox-dkms")

    print("\n===== [ Step 5: Load VirtualBox kernel modules ] =====")
    run("sudo modprobe vboxdrv")
    run("sudo modprobe vboxnetflt")
    run("sudo modprobe vboxnetadp")

    print("\n===== [ Step 6: Verify device nodes ] =====")
    expected_devices = [Path("/dev/vboxdrv"), Path("/dev/vboxnetctl")]
    missing = [str(p) for p in expected_devices if not p.exists()]
    if missing:
        print("[!] Missing expected device nodes:")
        for item in missing:
            print(f"    - {item}")
        sys.exit(1)

    print("[+] VirtualBox device nodes present:")
    for item in expected_devices:
        print(f"    - {item}")

    print("\n===== [ Step 7: Next manual step in VirtualBox ] =====")
    print(
        "Open VirtualBox:\n"
        "  File -> Tools -> Network Manager\n"
        "  Host-only Networks -> Create\n"
        "  Configure:\n"
        "    IPv4 Address: 192.168.56.1\n"
        "    IPv4 Mask:    255.255.255.0\n"
        "  Then attach vboxnet0 to your VMs."
    )

    print("\n[+] Done.")


if __name__ == "__main__":
    main()