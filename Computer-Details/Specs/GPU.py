import GPUtil


class CpuInfo(object):
    def __init__(self):
        self.gpu = GPUtil.getGPUs()
        self.gpu_list = []
        
