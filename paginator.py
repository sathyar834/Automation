import json
import boto3
client = boto3.client('iam')


def Custom():
  a=10
  print("variable",a,"is ten")
Custom()