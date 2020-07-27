#!/usr/bin/python3

__all__ = ["CpuInfo", "get_cpu_info",  "get_processors"]

_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = CpuInfo()
    return _instance

def get_cpu_info():
    return _get_instance().get_cpu_info()

def get_processors():
    return _get_instance().get_processor_count()

class CpuInfo(object):
    def __init__(self, path='/proc/cpuinfo'):
        self.path = path
    
    def get_cpu_info(self):
        return self.get_model(self.read_cpufile(self.path))

    __call__ = get_cpu_info
    
    @staticmethod
    def read_cpufile(cpufile):
        with open(cpufile, "r") as cpu:
            info = cpu.readlines()
        return info
    
    @staticmethod
    def get_model(info):
        cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
        return cpuinfo[0]
    
    def get_processor_count(self):
        return self.get_count(self.read_cpufile(self.path))
    __call__ = get_processor_count
    @staticmethod
    def get_count(info):
        return len([x.strip().split(":")[1] for x in info if "processor"  in x])

