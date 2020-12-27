import json
import time
import boto3

stsclient = boto3.client('sts')

def assumerole():
  anotheraccountresponse = stsclient.assume_role(
    RoleArn="arn:aws:iam::689020024752:role/OrganizationAccountAccessRole",
    RoleSessionName='master_to_acess_VLG',
  )
  credentials=anotheraccountresponse['Credentials']
  print(credentials)

  # s3_resource=boto3.resource(
  #   's3',
  #   aws_access_key_id=credentials['AccessKeyId'],
  #   aws_secret_access_key=credentials['SecretAccessKey'],
  #   aws_session_token=credentials['SessionToken'],
  # )

  # for bucket in s3_resource.buckets.all():
  #   print(bucket.name)

  iamclient = boto3.client(
    'iam',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
  )

  # groupresponse = iamclient.create_group(
  #   GroupName='Admin_VLG'
  # )
  # print(groupresponse)

  Userresponse = iamclient.create_user(
    UserName='Assume_role_user',
  )

  attachresponse = iamclient.attach_user_policy(
    UserName='Assume_role_user',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
  )
  time.sleep(10)

  Accesskeyresponse = iamclient.create_access_key(
    UserName='Assume_role_user'
  )
  print(Accesskeyresponse)

assumerole()