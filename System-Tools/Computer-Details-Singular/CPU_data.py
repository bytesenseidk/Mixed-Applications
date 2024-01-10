import psutil
import cpuinfo
from tabulate import tabulate


def cpu_info():
    frequency = psutil.cpu_freq()
    processor = cpuinfo.get_cpu_info()['brand_raw']
    data = {
        "Physical Cores":   [psutil.cpu_count(logical=False)],
        "Total Cores":      [psutil.cpu_count(logical=True)],
        "Max Frequency":    [frequency.max],
        "Min Frequency":    [frequency.min],
        "Current Frequency":  [frequency.current]
    }
    core_usage = lambda: '\n'.join([f'Core {i+1}: {percentage}%' for i, 
            percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1))]).split('\n')
    
    cores_0_headers = [header[0] for header in [core.split(':') for core in core_usage()][:8]]
    cores_0_data = [value[1] for value in [core.split(':') for core in core_usage()][:8]]
    cores_1_headers = [header[0] for header in [core.split(':') for core in core_usage()][-8:]]
    cores_1_data = [value[1] for value in [core.split(':') for core in core_usage()][-8:]]

    return [processor, data, [cores_0_headers, cores_0_data], [cores_1_headers, cores_1_data]]
    
if __name__ == "__main__":
    processor, data, cores_0, cores_1 = cpu_info()
    print(f'\t\t [ {processor} ]\n')
    print(tabulate(data, headers="keys"))
    print(f'{"\t"*4} [ USAGE ]')
    print(tabulate(cores_0, tablefmt='row'))
    print(tabulate(cores_1, tablefmt='row'))
    
