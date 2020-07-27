#!/usr/bin/python3

import os 

__all__ = ["GetPid", "get_pid_list"]
_instance = None
def _get_instance():
    global _instance
    if  _instance is None:
        _instance = GetPid()
    return _instance

def get_pid_list():
    return _get_instance().get_pid()

class GetPid(object):
    def __init__(self, path='/proc'):
        self.path = path
    
    def get_pid(self):
        return self.get_list(self.path)
    
    __call__ = get_pid

    @staticmethod
    def get_list(pidpath):
        return [x for x in os.listdir(pidpath) if x.isdigit()]