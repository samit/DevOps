#!/usr/bin/python3
import boto3
from pprint import pprint
#filter = [{'Name': 'instance-state-name', 'Values': [value]}]
#filters = [{'Name': 'tag:fqdn', 'Values': ['sdahal.local']}]
# filters = [{'Name': 'tag:Role', 'Values': ['sdahal.local']}]

#


class ListEc2Instance:
    """Class to get all instance and filter instance by tag name /role/state
     """

    def __init__(self):
        self.ec2 = boto3.resource('ec2')

    def list_all_instance(self):
        for instance in self.ec2.instances.all():
            return instance

    def list_instance_by_filters(self, filters):
        filters = filters
        instance = self.ec2.instances.filter(Filters=filters)
        return instance


if __name__ == '__main__':
    instance_list = ListEc2Instance()
    all_instance = instance_list.list_all_instance()
    if all_instance is not None:
        print(
            "Id:{0}\nPlatform:{1}\nType:{2}\nPublic Ivp4:{3}\nAMI:{4}\nState:{5}\nTags:{6}".format(
                all_instance.id, all_instance.platform, all_instance.instance_type, all_instance.public_ip_address, all_instance.image.id, all_instance.state, all_instance.tags
            )
        )
    else:
        print("There are no instances Please launch instances")
    filters = [{'Name': 'tag:fqdn', 'Values': ['sdahal.local']}]

    filter_inst = instance_list.list_instance_by_filters(filters)
    for i in filter_inst:
        print(i.id)
