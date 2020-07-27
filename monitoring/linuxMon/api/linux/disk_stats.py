#!/usr/bin/python3
__all__ = ["DiskStats", "get_disk_stat"]
_instance = None
def _get_instance():
    global _instance
    if _instance is None:
        _instance = DiskStats()
    return _instance

def get_disk_stat():
    return _get_instance().get_proc_diskstat()
#https://www.kernel.org/doc/Documentation/ABI/testing/procfs-diskstats
#according to my kernerl version 18 field if your kernel version is 5.5 or above
#add flush_req_completed, time_spent_flushing on column disk
columns_disk = ['major_dev_num', 'minor_dev_num', 'device', 'reads', 
                'reads_merged', 'sectors_read', 'ms_reading', 'writes', 
                'writes_merged', 'sectors_written', 'ms_writing', 
                'current_ios', 'ms_doing_io', 'weighted_ms_doing_io',
                'discard_completed','discard_merged','sectors_discarded',
                'time_spent_discarding']


class DiskStats(object):
    def __init__(self, path='/proc/diskstats'):
        self.path = path
    
    def get_proc_diskstat(self):
        return self.read_and_parse_disk_stat(self.path)
    __call__ = get_proc_diskstat

    @staticmethod
    def read_and_parse_disk_stat(diskstat):
        response = {}
        with open(diskstat, 'r') as statfile:
            for line in statfile.readlines():
                if line =='':
                    continue
                row = line.split()
                if len(row) == len(columns_disk):
                    col = columns_disk
                else:
                    continue
                try:
                    data = dict(zip(col,row))
                    response[data['device']] = dict((k, int(v)) for k,v in data.items() if k !='device')

                except Exception as e:
                    print(e)
            return response



