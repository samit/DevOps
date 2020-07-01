#!/usr/bin/python3
import boto3
from pprint import pprint
class Ec2Instance:
    def __init__(self, resource):
        self.resource = resource
    
    def get_ec2_resource(self):
        ec2 = boto3.resource(self.resource)
        return ec2

    def create_vpc(self, cidr_block, **create_tags):
        ec2 = self.get_ec2_resource()
        vpc = ec2.create_vpc(CidrBlock = cidr_block)
        vpc.create_tags(Tags=[create_tags])
        vpc.wait_until_available()
        return vpc
    
    def create_and_attach_igw(self, vpc):
        ec2 = self.get_ec2_resource()
        ig = ec2.create_internet_gateway()
        vpc.attach_internet_gateway(InternetGatewayId=str(ig.id))
        return ig.id
    
    def create_subnet(self, cidr_block, vpcid):
        ec2 = self.get_ec2_resource()
        subnet = ec2.create_subnet(CidrBlock = cidr_block, VpcId = vpcid)
        return subnet.id
    
    def create_route_table(self, vpc , dest_cidr_block, igwid):
        route_table = vpc.create_route_table()
        route_table.create_route(
            DestinationCidrBlock = dest_cidr_block,
            GatewayId = igwid
        )
        return route_table
    
    def associate_route_table_to_subnet(self, subnetid, route_table):
        return route_table.associate_with_subnet(SubnetId=subnetid)
    
    def create_sec_group(self, grpname, desc, vpcid, cidrip, ipproto,fromport,toport):
        ec2 = self.get_ec2_resource()
        sec_group = ec2.create_security_group(GroupName=grpname, Description=desc, VpcId=vpcid)
        sec_group.authorize_ingress(
            CidrIp = cidrip,
            IpProtocol = ipproto,
            FromPort = fromport,
            ToPort = toport
        )
        return sec_group

    
if __name__ == '__main__':
    ec2 = Ec2Instance('ec2')
    vpc_cidr = "192.168.0.0/16"
    vpc  = ec2.create_vpc(vpc_cidr, Key="Name",Value="my_vpc")
    igw = ec2.create_and_attach_igw(vpc)
    subnet_cidr = '192.168.1.0/24'
    vpcid = vpc.id
    subnet_id = ec2.create_subnet(subnet_cidr, vpcid)
    print(subnet_id)
    dest_cidr_block = '0.0.0.0/0'
    route_table = ec2.create_route_table(vpc, dest_cidr_block, igw)
    pprint(route_table)
    ass_rt_to_subnet = ec2.associate_route_table_to_subnet(subnet_id,route_table)
    pprint(ass_rt_to_subnet)
    grpname = "my-sec-group"
    desc = "securoty group for my-vpc"
    sec_cidr = '0.0.0.0/0'
    ipproto = 'icmp'
    fromPort = 80
    toport = 80
    sec_grp = ec2.create_sec_group(grpname,desc,vpcid,sec_cidr,ipproto,fromPort,toport)
    pprint(sec_grp)


    

        




    