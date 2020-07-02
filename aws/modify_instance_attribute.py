#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError
from instance_mgmt import InstanceManageMent


class ModifyInstanceAttribute:
    """ Modify instance attributes just by passing attribute and value for attribute and value read aws docs """
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def modify_attribute(self, **attribute):
        print(self.ec2)
        try:
            print("stopping instances")
            self.ec2.stop_instances(InstanceIds=[attribute['InstanceId']])
            #waiter = self.ec2.get_waiter('instance-stopped')
            #waiter.wait(InstanceIds=[attribute['InstanceId']])
            print("Modifying instance attribute")
            self.ec2.modify_instance_attribute(
                InstanceId=attribute['InstanceId'],
                Attribute=attribute['Attribute'],
                Value=attribute['Value']
            )
            print("Starting instances")
            response = self.ec2.start_instances(InstanceIds=[attribute['InstanceId']])
            return response
        except ClientError as e:
            return e
            


if __name__ == '__main__':
            modification = ModifyInstanceAttribute()
            InstanceId = 'i-049c089b286c10e86'
            Attribute = 'instanceType'
            Value = 't2.small'
            modification.modify_attribute(InstanceId=InstanceId, Attribute=Attribute, Value=Value)
