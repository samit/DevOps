#!/usr/bin/python3
from get_pid_list import GetPid
import subprocess
__all__ = ["PerProcessUsageInfo", "get_per_process_mem", "get_per_process_cpu"]

_instance  = None
def _get_instance():
    global _instance
    if _instance is None:
        _instance = PerProcessUsageInfo()
    return _instance

def get_per_process_mem():
    return _get_instance().get_mem_info()

def get_per_process_cpu():
    return _get_instance().get_cpu_info()

class PerProcessUsageInfo(object):
    def __init__(self, pidlist = GetPid().get_pid()):
        self.pidlist = pidlist
    
    def get_mem_info(self):
        return self.get_mem_usage(self.pidlist)
    __call__  = get_mem_info

    @staticmethod
    def get_mem_usage(pids):
        mem_pid = dict()
        d_keys = ['State', 'VmRss', 'VmPeak', 'VmHWM', 'VmSwap', 'Vctxt', 'Nvctxt','Command']

        for pid in pids:
            command = open("/proc/"+pid+"/cmdline").read()
            with open("/proc/"+pid+"/status") as status:
                line = status.readlines()
                vmrss = ''.join([x.strip().split(":")[1] for x in line if x.startswith("VmRSS") ]).replace("\t","")
                state = ''.join([x.strip().split(":")[1] for x in line if x.startswith("State") ]).replace("\t","")
                vmpeak = ''.join([x.strip().split(":")[1] for x in line if x.startswith("VmPeak")]).replace("\t","")
                vmhwm = ''.join([x.strip().split(":")[1] for x in line if x.startswith("VmHWM") ]).replace("\t","")
                vmswap = ''.join([x.strip().split(":")[1] for x in line if x.startswith("VmSwap")]).replace("\t","")
                vctxt = ''.join([x.strip().split(":")[1] for x in line if x.startswith("voluntary_ctxt_switches")]).replace("\t","")
                nvctxt = ''.join([x.strip().split(":")[1] for x in line if x.startswith("nonvoluntary_ctxt_switches")]).replace("\t","")
                d_val = [state, vmrss,vmpeak,vmhwm,vmswap,vctxt,nvctxt,command]
                try:
                    mem_pid[pid] = dict(zip(d_keys,d_val))
                except:
                    pass
        return mem_pid





    def get_cpu_info(self):
        return self.get_cpu_pid(self.pidlist)
    __call__  = get_cpu_info
    @staticmethod
    def get_cpu_pid(pids):
        hertz = subprocess.getoutput("getconf CLK_TCK")
        uptime = subprocess.getoutput("cat /proc/uptime").strip().split()[0]
        cpu_pid = dict()
        for pid in pids:
            try:
                with open("/proc/"+pid+"/stat", 'r') as statfile:
                    pidstat = statfile.read().strip().split()
                utime=pidstat[13] # CPU time Spent in user code
                stime=pidstat[14] #CPU time spent in Kernal COde
                cutime=pidstat[15] #Waited-for children's CPU time spent in user code (in clock ticks)
                cstime = pidstat[16] # Waited-for children's CPU time spent in kernel code (in clock ticks)
                starttime=pidstat[21] #Time when the process started, measured in clock ticks
                total_time = float(utime)+float(stime)+float(cstime)+float(cutime)
                seconds = float(uptime) -(float(starttime)/(float(hertz)))
                cpu_usage = 100 * ((total_time/float(hertz))/seconds)
                cpu_usage = "{:.2f}".format(cpu_usage)
                cpu_pid.update({pid:float(cpu_usage)})
            except Exception:
                pass
        return cpu_pid


    



