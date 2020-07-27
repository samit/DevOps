#!/usr/bin/python3
from time import sleep
# A python script that read /proc/stat file to
# get the CPU usage percentage information for each CPU 
#core.

__all__ = ["CPUUsage", 'get_cpu_data', 'get_cpu_usage']

_instance = None 

def _get_instance():
    global _instance
    if _instance is None:
        _instance = CPUUsage()
    return _instance

def get_cpu_data():
    return _get_instance().get_proc_stat()

def get_cpu_usage():
    return _get_instance().get_cpu_percentage()



class CPUUsage(object):
    def __init__(self, path="/proc/stat"):
        self.path = path
    
    def get_proc_stat(self):
        return self.parse_proc_stat(self.read_proc_stat(self.path))
    __call__ = get_proc_stat

    def get_cpu_percentage(self):
        cpu_data_prev = self.get_proc_stat()
        sleep(2)
        cpu_data_current = self.get_proc_stat()
        return self.get_percent(cpu_data_current, cpu_data_prev)
    
    __call__ = get_cpu_percentage

    

    @staticmethod
    def read_proc_stat(proc_stat):
        with open(proc_stat) as cpustat:
            return cpustat.readlines()

    @staticmethod
    def parse_proc_stat(cpustat):
        cpu_data = dict()
        for line in cpustat:
            if line.startswith("cpu"):
                cpu_core = [line.split()[0]]+[float(x) for x in line.split()[1:]]
                cpu_id,user,nice,system,idle,iowait,irq,softrig,steal,guest,guest_nice = cpu_core
                cpu_idle = idle+iowait
                cpu_non_idle = user+nice+system+irq+softrig+steal
                total = cpu_idle + cpu_non_idle
                cpu_data.update({cpu_id:{'total':total, 'idle':cpu_idle}})
        return cpu_data


    @staticmethod
    def get_percent(cpu_prev, cpu_current):
        cpu_load = dict()
        for cpu in cpu_prev:
            current_total = cpu_current[cpu]['total']
            current_idle = cpu_current[cpu]['idle']
            prev_total = cpu_prev[cpu]['total']
            prev_idle = cpu_prev[cpu]['idle']
            total_delta = current_total - prev_total
            idle_delta = current_idle -prev_idle
            cpu_percentage = (total_delta -idle_delta)/total_delta*100
            cpu_percentage = "{:.2f}".format(cpu_percentage)
            cpu_load.update({cpu:cpu_percentage})
        return cpu_load


    


    


