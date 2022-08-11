import GPUtil
import psutil
import platform
import speedtest
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from datetime import datetime


class SystemScanner(object):
    def get_size(self, bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor


    def system_info(self):
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        data = {
            "System":       uname.system, 
            "Node Name":    uname.node,   
            "Release":      uname.release,
            "Version":      uname.version,
            "Architecture": uname.machine,
            "Processor":    uname.processor,
            "Boot Time": str(f"{bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")
        }
        return data


    def cpu_info(self):
        cpufreq = psutil.cpu_freq()
        data = {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "Max Frequency": str(f"{cpufreq.max:.2f} Mhz"),
            "Min Frequency": str(f"{cpufreq.min:.2f} Mhz"),
            "Current Frequency": str(f"{cpufreq.current:.2f} Mhz"),
            "Total Usage": str(f"{psutil.cpu_percent()}%")
        }
        return data
        

    def ram_info(self):
        svmem = psutil.virtual_memory()
        data = {
            "Total": self.get_size(svmem.total),
            "Available": self.get_size(svmem.available),
            "Used": self.get_size(svmem.used),
            "Percentage": str(f"{svmem.percent}%")
        }
        return data


    def gpu_info(self):
        gpus = GPUtil.getGPUs()
        data = {}
        for gpu in gpus:
            data["ID"] = gpu.id
            data["Name"] = gpu.name
            data["Load"] = f"{gpu.load*100}%"
            data["Free"] = f"{gpu.memoryFree} MB"
            data["Used"] = f"{gpu.memoryUsed} MB"
            data["Total"] = f"{gpu.memoryTotal} MB"
            data["Temp"] = f"{gpu.temperature} °C"
            data["UUID"] = gpu.uuid
        return data

    
    def disk_info(self):
        drive = psutil.disk_partitions()[0]
        disk_io = psutil.disk_io_counters()
        try:
            partition_usage = psutil.disk_usage(drive.mountpoint)
        except PermissionError:
            pass
        data = {
            "Device": drive.device,
            "Mountpoint": drive.mountpoint,
            "Filesystem": drive.fstype,
            "Total Size": self.get_size(partition_usage.total),
            "Used": self.get_size(partition_usage.used),
            "Free": self.get_size(partition_usage.free),
            "Percentage": str(f"{partition_usage.percent}%"),
            "Total Read": self.get_size(disk_io.read_bytes),
            "Total Write": self.get_size(disk_io.write_bytes)
        }
        return data
    

    def network_info(self):
        print("\nWill now do a scan, this won't take long...\n")
        scanner = psutil.net_if_addrs()
        interfaces = []
        for interface_name, _ in scanner.items():
            interfaces.append(str(interface_name))
        net_io = psutil.net_io_counters()
        speed = speedtest.Speedtest()
        data = {
            "Interface": str(interfaces[0]),
            "Download": str(f"{round(speed.download() / 1_000_000, 2)} Mbps"),
            "Upload": str(f"{round(speed.upload() / 1_000_000, 2)} Mbps"),
            "Total Bytes Sent": str(self.get_size(net_io.bytes_sent)),
            "Total Bytes Received": str(self.get_size(net_io.bytes_recv))
        }
        return data



class GUI(object):
    def __init__(self, master):
        spec = SystemScanner()
        self.methods = {
            "sys": spec.system_info(),
            "cpu":    spec.cpu_info(),
            "ram":    spec.ram_info(),
            "gpu":    spec.gpu_info(),
            "disk":   spec.disk_info(),
            "net":    spec.network_info()
        }

        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=485, height=290)

        self.system_tab = ttk.Frame(tabControl)
        tabControl.add(self.system_tab, text="System")
        tabControl.grid()

        self.cpu_tab = ttk.Frame(tabControl)
        tabControl.add(self.cpu_tab, text="CPU")
        tabControl.grid()

        self.ram_tab = ttk.Frame(tabControl)
        tabControl.add(self.ram_tab, text="RAM")
        tabControl.grid()

        self.gpu_tab = ttk.Frame(tabControl)
        tabControl.add(self.gpu_tab, text="GPU")
        tabControl.grid()

        self.disk_tab = ttk.Frame(tabControl)
        tabControl.add(self.disk_tab, text="Disk")
        tabControl.grid()

        self.net_tab = ttk.Frame(tabControl)
        tabControl.add(self.net_tab, text="Network")
        tabControl.grid()

        self.style = ttk.Style(frame)
        self.style.configure("My.TLabel", font=("Arial", 12, "bold"))
        self.style.configure("Bold.TLabel", font=("Arial", 10, "bold"))
        self.style.configure("Title.TLabel", font=("Arial", 15, "bold"))

        self.widgets()


    def widgets(self):
        # System Tab
        sys_frame_top_label = LabelFrame(self.system_tab, width=480, height=50)
        sys_frame_top_label.grid(column=0, row=0)
        sys_frame_top_label.grid_propagate(0)

        sys_top_label = Label(sys_frame_top_label, text="SYSTEM SPECIFICATIONS", style="Title.TLabel")
        sys_top_label.grid(column=1, row=0, columnspan=3, sticky=E)


        sys_label_frame = LabelFrame(self.system_tab, width=480, height=240)
        sys_label_frame.grid(column=0, row=1)
        sys_label_frame.grid_propagate(0)
                
        sys_system_label = Label(sys_label_frame, text="System: ", style="My.TLabel")
        sys_system_label.grid(column=0, row=1, sticky=W)
        sys_system_spec = Label(sys_label_frame, text=self.methods["sys"]["System"], style="Bold.TLabel")
        sys_system_spec.grid(column=1, row=1, sticky=W, padx=10, pady=2)

        sys_node_label = Label(sys_label_frame, text="Node Name: ", style="My.TLabel")
        sys_node_label.grid(column=0, row=2, sticky=W)
        sys_node_spec = Label(sys_label_frame, text=self.methods["sys"]["Node Name"], style="Bold.TLabel")
        sys_node_spec.grid(column=1, row=2, sticky=W, padx=10, pady=2)
        
        sys_rel_label = Label(sys_label_frame, text="Release: ", style="My.TLabel")
        sys_rel_label.grid(column=0, row=3, sticky=W)
        sys_rel_spec = Label(sys_label_frame, text=self.methods["sys"]["Release"], style="Bold.TLabel")
        sys_rel_spec.grid(column=1, row=3, sticky=W, padx=10, pady=2)

        sys_ver_label = Label(sys_label_frame, text="Version: ", style="My.TLabel")
        sys_ver_label.grid(column=0, row=4, sticky=W)
        sys_ver_label = Label(sys_label_frame, text=self.methods["sys"]["Version"], style="Bold.TLabel")
        sys_ver_label.grid(column=1, row=4, sticky=W, padx=10, pady=2)

        sys_arch_label = Label(sys_label_frame, text="Architecture: ", style="My.TLabel")
        sys_arch_label.grid(column=0, row=5, sticky=W)
        sys_arch_spec = Label(sys_label_frame, text=self.methods["sys"]["Architecture"], style="Bold.TLabel")
        sys_arch_spec.grid(column=1, row=5, sticky=W, padx=10, pady=2)

        sys_pro_label = Label(sys_label_frame, text="Processor: ", style="My.TLabel")
        sys_pro_label.grid(column=0, row=6, sticky=W)
        sys_pro_spec = Label(sys_label_frame, text=self.methods["sys"]["Processor"], style="Bold.TLabel")
        sys_pro_spec.grid(column=1, row=6, sticky=W, padx=10, pady=2)

        sys_boot_label = Label(sys_label_frame, text="Boot Time: ", style="My.TLabel")
        sys_boot_label.grid(column=0, row=7, sticky=W)
        sys_boot_spec = Label(sys_label_frame, text=self.methods["sys"]["Boot Time"], style="Bold.TLabel")
        sys_boot_spec.grid(column=1, row=7, sticky=W, padx=10, pady=2)


        # Central Processing Unit Tab
        cpu_frame_top_label = LabelFrame(self.cpu_tab, width=480, height=50)
        cpu_frame_top_label.grid(column=0, row=0)
        cpu_frame_top_label.grid_propagate(0)
        
        cpu_system_top_label = Label(cpu_frame_top_label, text="CENTRAL PROCESSING UNIT", style="Title.TLabel")
        cpu_system_top_label.grid(column=1, row=0, columnspan=3, sticky=N)

        
        cpu_label_frame = LabelFrame(self.cpu_tab, width=480, height=240)
        cpu_label_frame.grid(column=0, row=1)
        cpu_label_frame.grid_propagate(0)

        cpu_core_label = Label(cpu_label_frame, text="Physical Cores: ", style="My.TLabel")
        cpu_core_label.grid(column=0, row=1, sticky=W)
        cpu_core_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Physical Cores"], style="Bold.TLabel")
        cpu_core_spec.grid(column=1, row=1, sticky=W, padx=10)

        cpu_total_label = Label(cpu_label_frame, text="Total Cores: ", style="My.TLabel")
        cpu_total_label.grid(column=0, row=2, sticky=W)
        cpu_total_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Total Cores"], style="Bold.TLabel")
        cpu_total_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        cpu_max_label = Label(cpu_label_frame, text="Max Frequency: ", style="My.TLabel")
        cpu_max_label.grid(column=0, row=3, sticky=W)
        cpu_max_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Max Frequency"], style="Bold.TLabel")
        cpu_max_spec.grid(column=1, row=3, sticky=W, padx=10)

        cpu_min_label = Label(cpu_label_frame, text="Min Frequency: ", style="My.TLabel")
        cpu_min_label.grid(column=0, row=4, sticky=W)
        cpu_min_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Min Frequency"], style="Bold.TLabel")
        cpu_min_spec.grid(column=1, row=4, sticky=W, padx=10)

        cpu_cur_label = Label(cpu_label_frame, text="Current Frequency: ", style="My.TLabel")
        cpu_cur_label.grid(column=0, row=5, sticky=W)
        cpu_cur_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Current Frequency"], style="Bold.TLabel")
        cpu_cur_spec.grid(column=1, row=5, sticky=W, padx=10)

        cpu_t_usage_label = Label(cpu_label_frame, text="Total Usage: ", style="My.TLabel")
        cpu_t_usage_label.grid(column=0, row=6, sticky=W)
        cpu_t_usage_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Total Usage"], style="Bold.TLabel")
        cpu_t_usage_spec.grid(column=1, row=6, sticky=W, padx=10)


        # Random Access Memory Tab
        ram_frame_top_label = LabelFrame(self.ram_tab, width=480, height=50)
        ram_frame_top_label.grid(column=0, row=0)
        ram_frame_top_label.grid_propagate(0)
        
        ram_system_top_label = Label(ram_frame_top_label, text="RANDOM ACCESS MEMORY", style="Title.TLabel")
        ram_system_top_label.grid(column=1, row=0, columnspan=3, sticky=N)

        ram_label_frame = LabelFrame(self.ram_tab, width=480, height=240)
        ram_label_frame.grid(column=0, row=1)
        ram_label_frame.grid_propagate(0)


        ram_total_label = Label(ram_label_frame, text="Total: ", style="My.TLabel")
        ram_total_label.grid(column=0, row=1, sticky=W)
        ram_total_spec = Label(ram_label_frame, text=self.methods["ram"]["Total"], style="Bold.TLabel")
        ram_total_spec.grid(column=1, row=1, sticky=W, padx=10)

        ram_avail_label = Label(ram_label_frame, text="Available: ", style="My.TLabel")
        ram_avail_label.grid(column=0, row=2, sticky=W)
        ram_avail_spec = Label(ram_label_frame, text=self.methods["ram"]["Available"], style="Bold.TLabel")
        ram_avail_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        ram_used_label = Label(ram_label_frame, text="Used: ", style="My.TLabel")
        ram_used_label.grid(column=0, row=3, sticky=W)
        ram_used_spec = Label(ram_label_frame, text=self.methods["ram"]["Used"], style="Bold.TLabel")
        ram_used_spec.grid(column=1, row=3, sticky=W, padx=10)

        ram_per_label = Label(ram_label_frame, text="Percentage: ", style="My.TLabel")
        ram_per_label.grid(column=0, row=4, sticky=W)
        ram_per_spec = Label(ram_label_frame, text=self.methods["ram"]["Percentage"], style="Bold.TLabel")
        ram_per_spec.grid(column=1, row=4, sticky=W, padx=10)


        # Graphics Processing Unit Tab
        gpu_frame_top_label = LabelFrame(self.gpu_tab, width=480, height=50)
        gpu_frame_top_label.grid(column=0, row=0)
        gpu_frame_top_label.grid_propagate(0)
        
        gpu_system_top_label = Label(gpu_frame_top_label, text="GRAPHICS PROCESSING UNIT", style="Title.TLabel")
        gpu_system_top_label.grid(column=1, row=0, columnspan=3, sticky=N)


        gpu_label_frame = LabelFrame(self.gpu_tab, width=480, height=240)
        gpu_label_frame.grid(column=0, row=1)
        gpu_label_frame.grid_propagate(0)

        gpu_id_label = Label(gpu_label_frame, text="ID: ", style="My.TLabel")
        gpu_id_label.grid(column=0, row=1, sticky=W)
        gpu_id_spec = Label(gpu_label_frame, text=self.methods["gpu"]["ID"], style="Bold.TLabel")
        gpu_id_spec.grid(column=1, row=1, sticky=W, padx=10)

        gpu_name_label = Label(gpu_label_frame, text="Name: ", style="My.TLabel")
        gpu_name_label.grid(column=0, row=2, sticky=W)
        gpu_name_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Name"], style="Bold.TLabel")
        gpu_name_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        gpu_load_label = Label(gpu_label_frame, text="Load: ", style="My.TLabel")
        gpu_load_label.grid(column=0, row=3, sticky=W)
        gpu_load_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Load"], style="Bold.TLabel")
        gpu_load_spec.grid(column=1, row=3, sticky=W, padx=10)

        gpu_free_label = Label(gpu_label_frame, text="Free: ", style="My.TLabel")
        gpu_free_label.grid(column=0, row=4, sticky=W)
        gpu_free_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Free"], style="Bold.TLabel")
        gpu_free_spec.grid(column=1, row=4, sticky=W, padx=10)

        gpu_used_label = Label(gpu_label_frame, text="Used: ", style="My.TLabel")
        gpu_used_label.grid(column=0, row=5, sticky=W)
        gpu_used_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Used"], style="Bold.TLabel")
        gpu_used_spec.grid(column=1, row=5, sticky=W, padx=10)

        gpu_total_label = Label(gpu_label_frame, text="Total: ", style="My.TLabel")
        gpu_total_label.grid(column=0, row=6, sticky=W)
        gpu_total_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Total"], style="Bold.TLabel")
        gpu_total_spec.grid(column=1, row=6, sticky=W, padx=10)

        gpu_temp_label = Label(gpu_label_frame, text="Temp: ", style="My.TLabel")
        gpu_temp_label.grid(column=0, row=7, sticky=W)
        gpu_temp_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Temp"], style="Bold.TLabel")
        gpu_temp_spec.grid(column=1, row=7, sticky=W, padx=10)

        gpu_uuid_label = Label(gpu_label_frame, text="UUID: ", style="My.TLabel")
        gpu_uuid_label.grid(column=0, row=8, sticky=W)
        gpu_uuid_spec = Label(gpu_label_frame, text=self.methods["gpu"]["UUID"], style="Bold.TLabel")
        gpu_uuid_spec.grid(column=1, row=8, sticky=W, padx=10)


        # Disk Tab
        disk_frame_top_label = LabelFrame(self.disk_tab, width=480, height=50)
        disk_frame_top_label.grid(column=0, row=0)
        disk_frame_top_label.grid_propagate(0)
        
        disk_system_top_label = Label(disk_frame_top_label, text="DISK", style="Title.TLabel")
        disk_system_top_label.grid(column=1, row=0, columnspan=3, sticky=N)


        disk_label_frame = LabelFrame(self.disk_tab, width=480, height=240)
        disk_label_frame.grid(column=0, row=1)
        disk_label_frame.grid_propagate(0)

        disk_device_label = Label(disk_label_frame, text="Device: ", style="My.TLabel")
        disk_device_label.grid(column=0, row=1, sticky=W)
        disk_device_spec = Label(disk_label_frame, text=self.methods["disk"]["Device"], style="Bold.TLabel")
        disk_device_spec.grid(column=1, row=1, sticky=W, padx=10)

        disk_mount_label = Label(disk_label_frame, text="Mountpoint: ", style="My.TLabel")
        disk_mount_label.grid(column=0, row=2, sticky=W)
        disk_mount_spec = Label(disk_label_frame, text=self.methods["disk"]["Mountpoint"], style="Bold.TLabel")
        disk_mount_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        disk_fs_label = Label(disk_label_frame, text="Filesystem: ", style="My.TLabel")
        disk_fs_label.grid(column=0, row=3, sticky=W)
        disk_fs_spec = Label(disk_label_frame, text=self.methods["disk"]["Filesystem"], style="Bold.TLabel")
        disk_fs_spec.grid(column=1, row=3, sticky=W, padx=10)

        disk_t_size_label = Label(disk_label_frame, text="Total Size: ", style="My.TLabel")
        disk_t_size_label.grid(column=0, row=4, sticky=W)
        disk_t_size_spec = Label(disk_label_frame, text=self.methods["disk"]["Total Size"], style="Bold.TLabel")
        disk_t_size_spec.grid(column=1, row=4, sticky=W, padx=10)

        disk_used_label = Label(disk_label_frame, text="Used: ", style="My.TLabel")
        disk_used_label.grid(column=0, row=5, sticky=W)
        disk_used_spec = Label(disk_label_frame, text=self.methods["disk"]["Used"], style="Bold.TLabel")
        disk_used_spec.grid(column=1, row=5, sticky=W, padx=10)

        disk_free_label = Label(disk_label_frame, text="Free: ", style="My.TLabel")
        disk_free_label.grid(column=0, row=6, sticky=W)
        disk_free_spec = Label(disk_label_frame, text=self.methods["disk"]["Free"], style="Bold.TLabel")
        disk_free_spec.grid(column=1, row=6, sticky=W, padx=10)

        disk_per_label = Label(disk_label_frame, text="Percentage: ", style="My.TLabel")
        disk_per_label.grid(column=0, row=7, sticky=W)
        disk_per_spec = Label(disk_label_frame, text=self.methods["disk"]["Percentage"], style="Bold.TLabel")
        disk_per_spec.grid(column=1, row=7, sticky=W, padx=10)

        disk_t_read_label = Label(disk_label_frame, text="Total Read: ", style="My.TLabel")
        disk_t_read_label.grid(column=0, row=8, sticky=W)
        disk_t_read_spec = Label(disk_label_frame, text=self.methods["disk"]["Total Read"], style="Bold.TLabel")
        disk_t_read_spec.grid(column=1, row=8, sticky=W, padx=10)

        disk_t_write_label = Label(disk_label_frame, text="Total Write: ", style="My.TLabel")
        disk_t_write_label.grid(column=0, row=9, sticky=W)
        disk_t_write_spec = Label(disk_label_frame, text=self.methods["disk"]["Total Write"], style="Bold.TLabel")
        disk_t_write_spec.grid(column=1, row=9, sticky=W, padx=10)


        # # Network Tab
        net_frame_top_label = LabelFrame(self.net_tab, width=480, height=50)
        net_frame_top_label.grid(column=0, row=0)
        net_frame_top_label.grid_propagate(0)
        
        net_system_top_label = Label(net_frame_top_label, text="NETWORK", style="Title.TLabel")
        net_system_top_label.grid(column=1, row=0, columnspan=3, sticky=N)


        net_label_frame = LabelFrame(self.net_tab, width=480, height=240)
        net_label_frame.grid(column=0, row=1)
        net_label_frame.grid_propagate(0)

        net_interface_label = Label(net_label_frame, text="Interface: ", style="My.TLabel")
        net_interface_label.grid(column=0, row=0, sticky=W)
        net_interface_spec = Label(net_label_frame, text=self.methods["net"]["Interface"], style="Bold.TLabel")
        net_interface_spec.grid(column=1, row=0, sticky=W, padx=10)

        net_download_label = Label(net_label_frame, text="Download: ", style="My.TLabel")
        net_download_label.grid(column=0, row=1, sticky=W)
        net_download_spec = Label(net_label_frame, text=self.methods["net"]["Download"], style="Bold.TLabel")
        net_download_spec.grid(column=1, row=1, sticky=W, padx=10)
        
        net_upload_label = Label(net_label_frame, text="Upload: ", style="My.TLabel")
        net_upload_label.grid(column=0, row=2, sticky=W)
        net_upload_spec = Label(net_label_frame, text=self.methods["net"]["Upload"], style="Bold.TLabel")
        net_upload_spec.grid(column=1, row=2, sticky=W, padx=10)

        net_t_sent_label = Label(net_label_frame, text="Total Bytes Sent: ", style="My.TLabel")
        net_t_sent_label.grid(column=0, row=3, sticky=W)
        net_t_sent_spec = Label(net_label_frame, text=self.methods["net"]["Total Bytes Sent"], style="Bold.TLabel")
        net_t_sent_spec.grid(column=1, row=3, sticky=W, padx=10)

        net_t_recv_label = Label(net_label_frame, text="Total Bytes Received: ", style="My.TLabel")
        net_t_recv_label.grid(column=0, row=4, sticky=W)
        net_t_recv_spec = Label(net_label_frame, text=self.methods["net"]["Total Bytes Received"], style="Bold.TLabel")
        net_t_recv_spec.grid(column=1, row=4, sticky=W, padx=10)


if __name__ == "__main__":
    root = Tk()
    root.title("System Information")
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)
    GUI(root)
    root.mainloop()



    # scan = SystemScanner()
    # menu = {
    #     1: scan.system_info,
    #     2: scan.cpu_info,
    #     3: scan.ram_info,
    #     4: scan.gpu_info,
    #     5: scan.disk_info,
    #     6: scan.network_info
    # }
    # while True:
    #     os.system("cls")
    #     print(f"\n[ SYSTEM SCANNER ]\n\n"
    #         "[0] Exit\n"
    #         "[1] System Information\n"
    #         "[2] Central Processing Unit\n"
    #         "[3] Random Access Memory\n"
    #         "[4] Graphical Processing Unit\n"
    #         "[5] Disk Information\n"
    #         "[6] Network Information\n\n")
    #     try:
    #         selection = int(input("  >> "))
    #         if selection == 0:
    #             os.system("cls")
    #             print("\nThank you for using the app! Have a nice day...\n\n")
    #             _ = input("Press Enter to exit..")
    #             break

    #         os.system("cls")
    #         choice = menu[selection]

    #         for key, value in choice().items():
    #             print(f"| {key:25}| {value}".ljust(5))
    #         print("\n")
    #         _ = input("Press Enter to continue..")
    #         continue 
    #     except:
    #         os.system("cls")
    #         print("\nInvalid input! Try again..\n\n")
    #         _ = input("Press Enter to continue..")
    #         continue
