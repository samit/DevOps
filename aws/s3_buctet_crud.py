#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError


class AwsS3:
    def __init__(self, region):
        self.s3 = boto3.resource(
            's3', region_name=region) if region else boto3.resource('s3')

    def list_s3_bucket(self):
        try:
            buckets = self.s3.buckets.all()
            return [b.name for b in buckets]
        except ClientError as e:
            return e

    def create_bucket(self, bucket_name, region):
        try:
            bucket = self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": region
                }
            )
            return bucket

        except ClientError as e:
            return e



if __name__ == '__main__':
    s3 = AwsS3('ap-southeast-2')
    bucket  = s3.create_bucket('sdahalbuckets', 'ap-southeast-2')
    print(bucket)
    print(s3.list_s3_bucket())
