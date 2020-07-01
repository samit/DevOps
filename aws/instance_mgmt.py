#!/usr/bin/python3
import boto3

class InstanceManageMent:
    def __ini__(self):
        self.ec2 = boto3.resource('ec2')
    def start_instance(self):
        pass
    def stop_instance(self):
        pass
    def modify_instance(self):
        pass
    def allocate_n_associate_elasticIp(self):
        pass
    def disassociate_elastic_ip(self):
        pass
    def release_elastic_ip(self):
        pass
    def terminate_instance(self):
        pass
    def create_snapshot_instance(self):
        pass
    def attach_ebs_vol(self):
        pass
    def detach_ebs_vol(self):
        pass
    