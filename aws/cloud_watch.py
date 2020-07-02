#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError
import json


class AwsCloudWatch:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')

    def create_cloud_watch_alarm(self, **kwargs):
        try:
            response = self.cloudwatch.put_metric_alarm(
                AlarmName=kwargs['metrics']['AlarmName'],
                ComparisonOperator=kwargs['metrics']['ComparisonOperator'],
                EvaluationPeriods=kwargs['metrics']['EvaluationPeriods'],
                MetricName=kwargs['metrics']['MetricName'],
                Namespace=kwargs['metrics']['Namespace'],
                Period=kwargs['metrics']['Period'],
                Statistic=kwargs['metrics']['Statistic'],
                Threshold=kwargs['metrics']['Threshold'],
                ActionsEnabled=kwargs['metrics']['ActionsEnabled'],
                AlarmActions=kwargs['metrics']['AlarmActions'],
                AlarmDescription=kwargs['metrics']['AlarmDescription'],
                Dimensions=kwargs['metrics']['Dimensions'],
                Unit=kwargs['metrics']['Unit']
            )
            return response
        except ClientError as e:
            return e

    def disable_alarm(self, *AlarmNames):
        try:
            response = self.cloudwatch.disable_alarm_action(
                AlarnNames=AlarmNames)
            return response
        except ClientError as e:
            return e

    def delete_alarm(self, *AlarmNames):
        try:
            response = self.cloudwatch.delete_alarms(AlarmNames=AlarmNames)
            return response
        except ClientError as e:
            return e


if __name__ == '__main__':
    cw = AwsCloudWatch()
    with open('cloudwatch.json', 'r') as cwfile:
        records = json.load(cwfile)
    metric_alarm = cw.create_cloud_watch_alarm(metrics=records)
    print(metric_alarm)
    alarmnames = ['Application CPU Utilization',
                  'Application Memory Utilization']
    disable_alarm = cw.disable_alarm(alarmnames)
    print("Response for disable alarm function is ", disable_alarm)
    dle_alarm = cw.delete_alarm(alarmnames)
    print("response from delete alarm is", dle_alarm)
