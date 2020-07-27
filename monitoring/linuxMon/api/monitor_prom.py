#!/usr/bin/python3
from prometheus_client import start_http_server
from prometheus_client.core import HistogramMetricFamily,CounterMetricFamily, GaugeMetricFamily, REGISTRY, SummaryMetricFamily
import time
import logging
from  linux.user_process import UserProcess
from  linux.cpucore_data import CPUUsage
from linux.loadavg import LoadAvg
from linux.uptime import  Uptime
from linux.disk_stats import DiskStats
from linux.meminfo import MemInfo
from linux.proc_snmp import ProcNetSnmp
from linux.proc_netstat import ProcNetNetstat
from linux.proc_net_dev import ProcNetDev
logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(levelname)s/%(processName)s] %(message)s')
logger = logging.getLogger(__name__)

class MyCustumMonitor(object):
    def __init__(self):
        logger.info("Server started at port 8000")
        start_http_server(8000)
    
    def collect(self):
        user_process_count  = UserProcess().get_user_process_count()
        metric = HistogramMetricFamily("Users_Linux_box", "Number_of_process_run")
        for k,v in user_process_count.items():
            metric.add_sample("Number_of_process_run", value = int(v), labels={"users":k})
        yield metric
        cpu_usage = CPUUsage().get_cpu_percentage()
        cpu_metric = GaugeMetricFamily("cpu_cores", "percentage_used_per_core")
        for k, v in cpu_usage.items():
            cpu_metric.add_sample("percentage_used_per_core", value=float(v),labels={"cpucore":k})
        yield cpu_metric
        loadavg = LoadAvg().get_load_avg_data()
        load_metric = CounterMetricFamily("load_average", "load_avg_1M_5M_15M")
        for k,v in loadavg.items():
            load_metric.add_sample("load_avg_1M_5M_15M", value=float(v), labels={"load_avg":k})
        yield load_metric

        uptime = Uptime().get()
        uptime_metrics = SummaryMetricFamily("Uptime_data", "uptime_in_days")
        for k,v in uptime.items():
            uptime_metrics.add_sample("uptime_in_seconds", value=v, labels={"uptime_data_in_seconds":k})
        yield uptime_metrics

        disk_stat = DiskStats().get_proc_diskstat()
        disk_stat_metrics = SummaryMetricFamily("disk_part", "disk_stat_summary")
        for key,val in disk_stat.items():
            for k,v in val.items():
                disk_stat_metrics.add_sample("disk_stat_summary", value=float(v), labels={key:k})
        yield disk_stat_metrics

        mem_info = MemInfo().get_mem_info()
        mem_info_metrics = SummaryMetricFamily("memory_info","mem_info_summary_kB")
        for k,v in mem_info.items():
            mem_info_metrics.add_sample("mem_info_summary_kB", value=float(v), labels={"mem_info":k} )
        yield mem_info_metrics

        proc_net_snmp = ProcNetSnmp().get_net_snmp()
        proc_net_snmp_metrics = SummaryMetricFamily("proc_net_snmp_summary", "proc_net_snmp")
        for key,val in proc_net_snmp.items():
            for k,v in val.items():
                proc_net_snmp_metrics.add_sample("proc_net_snmp", value=float(v), labels={key:k})
        yield proc_net_snmp_metrics
        proc_net_netstat = ProcNetNetstat().get_net_netstat()
        proc_net_netstat_metrics = SummaryMetricFamily("proc_net_netstat_summary", "proc_net_netstat")
        for key,val in proc_net_netstat.items():
            for k,v in val.items():
                proc_net_netstat_metrics.add_sample("proc_net_netstat", value=float(v), labels={key:k})
        yield proc_net_netstat_metrics

        proc_net_dev = ProcNetDev().proc_net_dev()
        proc_net_dev_metrics = SummaryMetricFamily("device_stat", "proc_net_dev_summary")
        for key,val in proc_net_dev.items():
            for k,v  in val.items():
                proc_net_dev_metrics.add_sample("proc_net_dev_summary", value=float(v), labels={key:k})
        yield proc_net_dev_metrics


if __name__ == '__main__':
   REGISTRY.register(MyCustumMonitor())
   while True:
       time.sleep(1)
