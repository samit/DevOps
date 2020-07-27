#!/usr/bin/python3

__all__ = ["ProcNetSnmp", "get_proc_net_snmp"]
_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = ProcNetSnmp()
    return _instance

def get_proc_net_snmp():
    return _get_instance().get_net_snmp()

class ProcNetSnmp(object):
    def __init__(self, path='/proc/net/snmp'):
        self.path = path
    
    def get_net_snmp(self):
        return self.get_snmp(self.path)
    
    __call__ = get_net_snmp

    @staticmethod
    def get_snmp(snmp):
        key_data = None
        key_val = None
        snmp_data = dict()
        with open(snmp, "r") as sfile:
            for line in sfile:
                if not line.strip():
                    continue
                key, val = line.split(":",1)
                val = val.split()
                if key_data !=key:
                    key_data = key
                    key_val = val
                else:
                    val = [v for v in val]
                    snmp_data[key_data] = dict(zip(key_val, val))
        return snmp_data