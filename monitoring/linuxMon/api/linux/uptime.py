#!/usr/bin/python3
from datetime import timedelta
__all__ = ["Uptime", 'get_uptime']
_instance = None
def _get_instance():
    global _instance
    if _instance is None:
        _instance = Uptime()
    return _instance

def get_uptime():
    return _get_instance().get()


class Uptime(object):
    def __init__(self, path='/proc/uptime'):
        self.path = path
    def get(self):
        return self.get_uptime_data(self.path)
    __call__ = get
    
    @staticmethod
    def get_uptime_data(uptimepath):
        uptime_data = dict()
        with open(uptimepath, 'r') as upfile:
            line = upfile.read().split()
            uptime_data.update({"systemuptime":float(line[0]), "time_spent_idle_process": float(line[1])})
        return uptime_data
