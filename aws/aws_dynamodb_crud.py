#!/usr/bin/python
from pprint import pprint
import boto3
import json
from datetime import datetime
from botocore.exceptions import ClientError
# Install awscli using pip
# Create the IAM user from AWS IAM console and provide programatic access and AdminAccess permission/or
# Permission to end point(DynamoDB).
# Download AWS access key and secret key
# Issue aws configure and provice access key, secret key and region


class Dynamodb:
    """ A demo class implementation that one can use to perform CRUD operation on Dynamo DB Table """

    def __init__(self):
        self.ec2 = boto3.resource('dynamodb')

    def create_table(self, tablename):
        db = self.ec2
        table = db.create_table(
            TableName=tablename,
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'last_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        table.meta.client.get_waiter('table_exists').wait(TableName=tablename)
        return table

    def put_item_in_table(self, tablename):
        """ Function that writes data to DynamoDB table """
        db = self.ec2
        table = db.Table(tablename)
        with open('users.json', 'r') as user_data:
            records = json.load(user_data)
            for user in records:
                item = {
                    "username": user['username'],
                    "first_name": user["first_name"],
                    "last_name": user["last_name"],
                    "age":  str(user["age"]),
                    "account_type": user["account_type"]
                }
                response = table.put_item(

                    TableName=tablename,
                    Item=item
                )

        return response['Item']

    def get_item(self, tablename, uname, lname):
        """Function that query DB table based on supplied Key"""
        db = self.ec2
        table = db.Table(tablename)
        response = table.get_item(
            Key={
                "username": uname,
                "last_name": lname
            }
        )
        return response

    def update_item_and_add_new_attr(self, tablename, uname, lname, age, sex):
        """Function that update and add new entry to existing table """
        db = self.ec2
        table = db.Table(tablename)
        response = table.update_item(
            Key={
                "username": uname,
                "last_name": lname
            },
            UpdateExpression="SET age = :val1, sex = :val2",
            ExpressionAttributeValues={
                ':val1': age,
                ':val2': sex
            }
        )
        return response

    def delete_table_item(self, tablename, uname, lname):
        """ Function that perfroms delete operations on table  """
        db = self.ec2
        table = db.Table(tablename)
        response = table.delete_item(
            Key={
                "username": uname,
                "last_name": lname
            }
        )
        return response


if __name__ == '__main__':
    db = Dynamodb()
    print("creating table user")
    tablename = 'users'
    user_table = db.create_table(tablename)
    print(user_table.item_count)
    print(db.put_item_in_table(tablename))
    uname = "sdahal"
    lname = "Dahal"
    pprint(db.get_item(tablename, uname, lname))
    age = '16'
    sex = "M"
    pprint(db.update_item_and_add_new_attr(tablename, uname, lname, age, sex))
    pprint(db.get_item(tablename, uname, lname))
    pprint(db.delete_table_item(tablename, uname, lname))
