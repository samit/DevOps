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

    def delete_bucket(self, bucket_name):
        try:
            print("Deleting bucket with bucket name", bucket_name)
            self.s3.Bucket(bucket_name).delete()
        except ClientError as e:
            print(e)

    def upload_file_to_s3(self, bucket_name, filename):
        try:
            response = self.s3.meta.client.upload_file(
                './users.json', bucket_name, filename)
            return response
        except ClientError as e:
            return e

    def get_acl_for_s3bucket(self, bucket_name):
        try:
            return self.s3.Bucket(bucket_name).Acl()
        except ClientError as e:
            return e

    def set_acl_for_log_delevery_group(self, **aclpolicy):
        """ To grant access to Amazon S3 to write server access logs to the bucket, 
            under S3 log delivery group, choose Log Delivery.
            If a bucket is set up as the target bucket to receive access logs, 
            the bucket permissions must allow the Log Delivery group write access
            to the bucket. When you enable server access logging on a bucket, 
            the Amazon S3 console grants write access to the Log Delivery group 
            for the target bucket that you choose to receive the logs.  """

        try:
            pass
        except ClientError as e:
            return e


if __name__ == '__main__':
    s3 = AwsS3('ap-southeast-2')
    bucket = s3.create_bucket('sdahalbuckets', 'ap-southeast-2')
    print(bucket)
    print(s3.list_s3_bucket())
    s3.delete_bucket('sdahalbuckets')
