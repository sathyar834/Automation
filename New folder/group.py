import json
import boto3
client = boto3.client('iam')

def satya():
    response = client.create_group(
        GroupName='Admin'
    )
satya()