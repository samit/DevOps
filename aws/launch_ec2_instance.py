#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError
from pprint import pprint
import os


class LaunchEc2Instance:
    def __init__(self):
        self.ec2 = boto3.resource('ec2')

    def create_key_pair_for_ssh(self, dirname, private_key_file_name, key_name):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        else:
            path = os.path.join(dirname, private_key_file_name)
            try:
                key_pair = self.ec2.create_key_pair(KeyName=key_name)
                print("key pair created with name = %s", key_pair.name)
                with open(path, 'w') as filename:
                    filename.write(key_pair.key_material)
                    return key_pair
            except ClientError as e:
                return e

    def launch_instance(self, userdata, **kwargs):
        instance = self.ec2.create_instances(
            ImageId = kwargs['ImageId'],
            MinCount = kwargs['MinCount'],
            MaxCount = kwargs['MaxCount'],
            InstanceType = kwargs['InstanceType'],
            KeyName = kwargs['KeyName'],
            SubnetId = kwargs['SubnetId'],
            SecurityGroupIds = kwargs['SecurityGroupIds'],
            UserData = userdata
        )
        return instance


if __name__ == '__main__':
    li = LaunchEc2Instance()
    #print(li.create_key_pair_for_ssh("aws_key", "first_key.pem", "my_first_key"))
    ImageId = 'ami-088ff0e3bde7b3fdf'
    MinCount = 1
    MaxCount = 1
    InstanceType = 't1.micro'
    KeyName = 'my_first_key'
    SubnetId = 'subnet-006278503c676ebb5'
    SecurityGroupIds = ['sg-0f4f66a1a8a59b97b',]
    UserData ='''#!/bin/bash
    yum update -y
    yum install python3 -y
    '''
    li.launch_instance(
        UserData,
        ImageId=ImageId,
        MinCount=MinCount,
        MaxCount=MaxCount,
        InstanceType=InstanceType,
        KeyName = KeyName,
        SecurityGroupIds=SecurityGroupIds,
        SubnetId = SubnetId,
        )
