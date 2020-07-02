#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError


class InstanceManageMent:
    def __init__(self):
        self.ec2 = boto3.resource('ec2')

    def start_instance(self, instanceid):
        try:
            response = self.ec2.Instance(instanceid).start()
            #self.ec2.Instance.wait_until_running()
            print("Instance with instance id =%s running ", instanceid)
            return response
        except ClientError as e:
            return e

    def stop_instance(self, instanceid):
        try:
            response = self.ec2.Instance(instanceid).stop()
            #self.ec2.Instance.wait_until_stop()
            print("Instance with instance id = %s is stopped", instanceid)
            return response
        except ClientError as e:
            return e

    def allocate_and_associate_elasticIp(self, instanceid):
        try:
            response = self.ec2.meta.client.allocate_address(Domain='vpc')
            allocation_id = self.ec2.VpcAddress(response['AllocationId'])
            allocation_id.associate(InstanceId=instanceid)
            print("The elastic ip with %s is associated with instance id %s and the association id is %s \n",
                  allocation_id.public_ip, instanceid, allocation_id.association_id
                )
            print("\n")
            return allocation_id.allocation_id
        except ClientError as e:
            return e

    def disassociate_elastic_ip(self, allocationid):
        try:
            elastic_ip = self.ec2.VpcAddress(allocationid)
            elastic_ip.association.delete()
            print("Elastic ip = %s is disassociated from the instance ",
                  elastic_ip.public_ip)
            return None
        except ClientError as e:
            return e

    def release_elastic_ip(self, allocation_id):
        try:
            elastic_ip = self.ec2.VpcAddress(allocation_id)
            elastic_ip.release()
            print("The Elastic IP with ip address %s is released", allocation_id)
        except ClientError as e:
            return e

    def terminate_instance(self, instanceid):
        try:
            response = self.ec2.Instance(instanceid).terminate()
            return response
        except ClientError as e:
            return e

if __name__ == '__main__':
    mgmt = InstanceManageMent()
    instanceid = 'i-049c089b286c10e86'
    allocation_id = mgmt.allocate_and_associate_elasticIp(instanceid)
    print("disassociating ip address")
    mgmt.disassociate_elastic_ip(allocation_id)
    print("releasing Ip address")
    mgmt.release_elastic_ip(allocation_id)
    mgmt.stop_instance(instanceid)
    mgmt.start_instance(instanceid)
    mgmt.terminate_instance(instanceid)

