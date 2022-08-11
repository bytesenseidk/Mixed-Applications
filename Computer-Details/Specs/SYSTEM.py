import platform


class SystemInformation(object):
    def __init__(self):
        self.system = platform.uname()
        self.data = {
            "System":    self.system.system,
            "Node":      self.system.node,
            "Release":   self.system.release,
            "Version":   self.system.version,
            "Machine":   self.system.machine,
            "Processor": self.system.processor
            }
    
    
    def __str__(self):
        return str(f"System:     {self.data['System']}\n"
                   f"Node Name:  {self.data['Node']}\n"
                   f"Release:    {self.data['Release']}\n"
                   f"Version:    {self.data['Version']}\n"
                   f"Machine:    {self.data['Machine']}\n"
                   f"Processor:  {self.data['Processor']}")

