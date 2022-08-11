import psutil


class CentralProcessingUnit(object):
    def __init__(self):
        self.frequency = psutil.cpu_freq()
        self.data = {
            "Physical Cores": psutil.cpu_count(logical=False)
            "Total Cores":  psutil.cpu_count(logical=True),
            "Max Frequency":  self.frequency.max,
            "Min Frequency":  self.frequency.min,
            "Current Frequency":  self.frequency.current
            }
    
    
    def __str__(self):
        return str(f"Physical Cores:     {self.data['Physical Cores']}\n"
                   f"Total Cores:        {self.data['Total Cores']}\n"
                   f"Max Frequency:      {self.data['Max Frequency']}\n"
                   f"Min Frequency:      {self.data['Min Frequency']\n"
                   f"Current Frequency:  {self.data['Current Frequency']}\n"
                   f"CPU Usage:          {[print(f'Core {i+1}: {percentage}%') for i, percentage  in enumerate(psutil.cpu_percent(percpu=True, interval=1))][0]}")

