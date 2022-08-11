import psutil
from SizeConverter import GetSize


class RandomAccessMemory(object):
    def __init__(self):
        memory = psutil.virtual_memory()
        self.data = {
            "Total":      memory.total,
            "Available":  memory.available,
            "Used":       memory.used,
            "Percentage": memory.percent
            }
    
    
    def __str__(self):
        return str(f"Total RAM:     {GetSize(self.data['Total'])}\n"
                   f"Available RAM: {GetSize(self.data['Available'])}\n"
                   f"Used RAM:      {GetSize(self.data['Used'])}\n"
                   f"Percantage:    {str(GetSize(self.data['Percentage'])).strip('B')}%")

