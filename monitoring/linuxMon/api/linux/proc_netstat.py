#!/usr/bin/python3

__all__ = ["ProcNetNetstat", "get_proc_net_netstat"]

_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = ProcNetNetstat()
    return _instance

def get_proc_net_netstat():
    return _get_instance().get_net_netstat()

class ProcNetNetstat(object):
    def __init__(self, path="/proc/net/netstat"):
        self.path = path
    
    def get_net_netstat(self):
        return self.get_netstat(self.path)
    
    __call__ = get_net_netstat

    @staticmethod
    def get_netstat(netstat):
        key_data = None
        key_val = None
        netstat_data = dict()
        with open(netstat, "r") as netfile:
            for line in netfile:
                if not line.strip():
                    continue
                key, val = line.split(":", 1)
                val = val.split()
                if key !=key_data:
                    key_data = key
                    key_val = val
                else:
                    val = [v for v in val]
                    netstat_data[key] = dict(zip(key_val,val))
        return netstat_data
                    
