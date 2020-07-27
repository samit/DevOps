#!/usr/bin/python3

__all__ = ["MemInfo", "get_mem_info"]

_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = MemInfo()
    return _instance

def get_mem_info():
    return _get_instance().get_mem_info()

class MemInfo(object):
    def __init__(self, path='/proc/meminfo'):
        self.path = path
    
    def get_mem_info(self):
        return self.read_memfile(self.path)

    __call__ = get_mem_info
    
    @staticmethod
    def read_memfile(memfile):
        mem_dict = dict()
        with open(memfile, "r") as mem:
            for line in mem.readlines():
                mem_dict.update({line.split(":")[0]: line.split(":")[1].strip().replace("kB","")})
        return mem_dict
