import json
import boto3
client = boto3.client('organizations')



def Custom():
    response = client.create_account(
        Email='pyt@pytabc.com',
        AccountName='pythonaccount',
        IamUserAccessToBilling='ALLOW'
    )
    print(response)
    return response
Custom()