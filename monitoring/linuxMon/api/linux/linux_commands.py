#!/usr/bin/python3
# runs different commands like mpstat, iostat, and
# return json data
# Please install systat and enable it .
import os
import subprocess
__all__ = ["GetLinuxCommands", "get_iostat_extended", "get_iostat_cpu", "get_mpstat_all","get_pid_stat_d"]

_instance = None

def _get_instance():
    global _instance 
    if _instance is None:
        _instance = GetLinuxCommands()
    return _instance

def get_iostat_extended():
    return _get_instance().get_iostat_xd()

def get_iostat_cpu():
    return _get_instance().get_iostat_c()

def get_mpstat_all():
    return _get_instance().get_mpstat()

def get_pid_stat_d():
    return _get_instance().get_pidstat()


class GetLinuxCommands(object):
    def __init__(self):
        self.__init__
    
    def get_iostat_xd(self):
        return os.system("iostat -xd -o JSON")
    
    __call__ = get_iostat_xd

    def get_iostat_c(self):
        return os.system("iostat -c -o JSON")
    
    def get_mpstat(self):
        return os.system("mpstat -P ALL -o JSON")
    
    __call__ = get_mpstat

    def get_pidstat(self):
        return self.parse_pidstat()
    
    __call__ = get_pidstat

    @staticmethod
    def parse_pidstat():
        pid_data = subprocess.getoutput("pidstat -d")
        filter_data = list(filter(lambda x:x !='', pid_data.split('\n')))
        rows, col = filter_data[1], filter_data[2:]
        rows = rows.split()
        rows[0] = "time"
        for line in col:
            yield(dict(zip(rows, line.split())))







