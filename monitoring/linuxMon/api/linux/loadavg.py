#!/usr/bin/python3

__all__ = ["LoadAvg", "get_load_avg"]
_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = LoadAvg()
    return _instance

def get_load_avg():
    return _instance.get_load_avg_data()


class LoadAvg(object):
    """ Read /proc/loadavg and returns the dict data containing
    the load average for last 1, 5 , 15 minutes.
    If the averages are 0.0, then your system is idle.
    If the 1 minute average is higher than the 5 or 15 minute averages, then load is increasing.
    If the 1 minute average is lower than the 5 or 15 minute averages, then load is decreasing.
    If they are higher than your CPU count, then you might have a performance problem (it depends).
"""
    def __init__(self, path='/proc/loadavg'):
        self.path = path
    
    def get_load_avg_data(self):
        return self.parse_loadavg(self.read(self.path))
    __call__ = get_load_avg_data

    @staticmethod
    def read(path):
        with open(path, 'r') as loadavgfile:
            loadavg = loadavgfile.read().split()
        return loadavg[:-2]
    @staticmethod
    def parse_loadavg(loadavg):
        load_data = dict()
        load_data.update({"1Min":loadavg[0],"5Min":loadavg[1], "15Min":loadavg[2]})
        return load_data
