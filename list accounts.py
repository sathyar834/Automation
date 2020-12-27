import boto3
import json
client = boto3.client('organizations')

def lambda_handler():
    response = client.list_accounts(
    )
    print(response)
lambda_handler()