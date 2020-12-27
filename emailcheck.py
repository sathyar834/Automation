import boto3
import json
import time

client = boto3.client('organizations')

Emaillist = ["sathyar834@xxx.com"]
Name_list = ["Central"]
ListAWS = ["dfsf@xxx.com","sathyar834@xxx.com", "dsfsdf@xxx.com"]
paginator = client.get_paginator('list_create_account_status')

def email():
#   Existing_emails = list_existing_email()
#   global_variables_for_account()
#   Length_of_Emails = len(list_of_Emails)
#   Length_of_Names = len(list_of_Names)

#   if Length_of_Emails == Length_of_Names:
#     for mail,name in zip(list_of_Emails,list_of_Names):
#       for awsmail in Existing_emails:
#         if mail == awsmail:
#           status = "Invalid email"
#           return("The email already exist!")
#           break
#         else:
#           status = "Valid email"
#       if status == "Valid email":
#         cresponse = client.create_account(
#           Email= mail,
#           AccountName= name,
#           IamUserAccessToBilling='ALLOW'
#         )
#         return("Account created successfully")
#       elif status == "Invalid email":
#         cresponse = client.create_account(
#           Email= mail,
#           AccountName= name,
#           IamUserAccessToBilling='ALLOW'
#         )
#         response = client.list_create_account_status(
#           States=[
#               'FAILED'
#           ],
#           MaxResults=20
#         )
#         nextresponse = client.list_create_account_status(
#           States=[
#               'FAILED'
#           ],
#           NextToken = response["NextToken"],
#           MaxResults=20
#         )
#         nextresponse2 = client.list_create_account_status(
#           States=[
#               'FAILED'
#           ],
#           NextToken = nextresponse["NextToken"],
#           MaxResults=20
#         )
#         status = response["CreateAccountStatuses"]
#         nextstatus = nextresponse["CreateAccountStatuses"]
#         nextstatus2 = nextresponse2["CreateAccountStatuses"]

#         Namelist =[]
#         Failurelist =[]
#         for y in status:
#           for x in y.keys():
#             for a in y.keys():
#               Names = y["AccountName"]
#               Namelist.append(Names)
#               Failure = y["FailureReason"]
#               Failurelist.append(Failure)
#               break
#             break

#         Namelistmore = []
#         Failurelistmore = []
#         for y in nextstatus:
#           for x in y.keys():
#             for a in y.keys():
#               Names = y["AccountName"]
#               Namelistmore.append(Names)
#               Failure = y["FailureReason"]
#               Failurelistmore.append(Failure)
#               break
#             break

#         Namelistmore2 = []
#         Failurelistmore2 = []
#         for y in nextstatus2:
#           for x in y.keys():
#             for a in y.keys():
#               Names = y["AccountName"]
#               Namelistmore2.append(Names)
#               Failure = y["FailureReason"]
#               Failurelistmore2.append(Failure)
#               break
#             break

#         res = {Namelist[i]: Failurelist[i] for i in range(len(Namelist))}
#         resmore = {Namelistmore[i]: Failurelistmore[i] for i in range(len(Namelistmore))}
#         resmore2 = {Namelistmore2[i]: Failurelistmore2[i] for i in range(len(Namelistmore2))}
#         finaldict = dict(list(res.items()) + list(resmore.items()) + list(resmore2.items()))
#         print(finaldict)
#         for key in finaldict:
#           for name,mail in zip(list_of_Names,list_of_Emails):
#             if name == key:
#               return finaldict[key]
#             else:
#               continue
#       else:
#         return("Code error")
email()