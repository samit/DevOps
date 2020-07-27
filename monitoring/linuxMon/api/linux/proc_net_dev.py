#!/usr/bin/python3
__all__ = ["ProcNetDev", "get_proc_net_dev"]

_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = ProcNetDev()
    return _instance

def get_proc_net_dev():
    return _get_instance().proc_net_dev()


class ProcNetDev(object):
    def __init__(self, path='/proc/net/dev'):
        self.path = path
    
    def proc_net_dev(self):
        return self.parse_proc_net_dev(self.path)
    
    __call__ = proc_net_dev

    @staticmethod
    def parse_proc_net_dev(netdev):
        ifaces = dict()
        with open(netdev, "r") as netfile:
            lines = netfile.readlines()
            headerline = lines[1]
            _, recv, tx = headerline.split("|")
            recv = map(lambda x: "rx_"+x , recv.split())
            tx = map(lambda x:"tx_"+x, tx.split())
            columns = [x for x in recv] + [y for y in  tx]
            for line in lines[2:]:
                iface, data = line.split(":")
                ifacedata = dict(zip(columns, data.split()))
                ifaces.update({iface:ifacedata})
        return ifaces


