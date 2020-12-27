#!/usr/bin/env python3
# CFW/aws/connections.py

"""
Establishing AWS Connection for all AWS Resources
"""
from __future__ import print_function
import botocore.exceptions
import boto3
import logging

region = 'us-east-1'

"""
Function: get_connect(servicename,region,serviceconnectiontype)
Return: client
Example: get_connect('s3',us-east-1,client)
"""
def get_connect(servicename,region,serviceconnectiontype):
    if serviceconnectiontype == 'client':
        try:
            client = boto3.client(servicename,region_name=region)
            return client
        except botocore.exceptions.ClientError as e:
            return e
        except botocore.exceptions.ParamValidationError as e:
            raise ValueError('The parameters you provided are incorrect: {}'.format(e))
        except botocore.exceptions.NoCredentialsError as e:
            raise ValueError('Unable to find user credentials to proceed: {}'.format(e))
    elif serviceconnectiontype == 'resource':
        try:
             client = boto3.resource(servicename,region_name=region)
             return client
         # TODO: Handle right exception
        except client.meta.client.exceptions as e:
            return e
        except botocore.exceptions.ParamValidationError as e:
            raise ValueError('The parameters you provided are incorrect: {}'.format(e))
    else:
        print("Something Went Wrong in connections.py" )
        exit()


def get_account(args=None):
    try:
        sts = get_connect('sts',region,'client')
        response = sts.get_caller_identity()["Account"]
        #print(response)
        return response
     #TODO: Handle right exception   
    except botocore.exceptions as e:
            raise ValueError('Unable to find user credentials to proceed: {}'.format(e))