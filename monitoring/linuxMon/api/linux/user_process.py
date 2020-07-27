#!/usr/bin/python3
import subprocess
__all__ = ["UserProcess", "get_user_process"]

_instance  = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = UserProcess()
    return _instance

def get_user_process():
    return _get_instance().get_user_process_count()

class UserProcess(object):
    """ Read /etc/passwd file get the list of users and return the 
    dict containing users and process run by associated users
    """
    def __init__(self, path='/etc/passwd'):
        self.path = path
    
    def get_user_process_count(self):
        return self.get_count(self.read(self.path))
    __call__ = get_user_process_count

    @staticmethod
    def read(passwdfile):
        users = []
        with open(passwdfile, 'r') as passwd:
            for line in passwd.readlines():
                users.append(line.split(":")[0])
        return users
    @staticmethod
    def get_count(users):
        user_pid = dict()
        for user in users:
            user_pid.update({user:subprocess.getoutput("ps -u "+user+"|tail -n+2|wc -l")})
        return user_pid

