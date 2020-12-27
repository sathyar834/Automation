import json
import boto3
import time

client = boto3.client('iam')

def assumecred():
#   attachresponse = client.attach_user_policy(
#     UserName='Assume_role_user',
#     PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
#   )
#   time.sleep(25)
  response = client.create_group(
    GroupName='Assumecreds_group'
  )
assumecred()