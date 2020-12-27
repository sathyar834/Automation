import json
import boto3
from flask import Flask,jsonify,request
client = boto3.client('organizations')

# event = {
#   "List of Ids of Account": [
#     "784725266810",
#     "865615574130"
#   ],
#   "List of Ids of respective Destination Account": [
#     "ou-oblp-vav4uc7y",
#     "ou-oblp-t5inrbmb"
#   ],
#   "DescriptionSCP": [
#     "SCPguardpyt",
#     "SCPguardtestpyt2"
#   ],
#   "SCPName": [
#     "flaskscp3test",
#     "flaskscp2test"
#   ],
#   "Document":["scp_policy","duplicatepolicy"]
# }

# event = {
#   "List of SCP Policy Ids": [
#     "p-9njznm1p",
#     "p-9njznm1p"
#   ],
#   "List of SCP Target Ids": [
#     "105553713263",
#     "715921394743"
#   ]
# }

def global_variables_for_moving_accounts():
  event= request.get_json(force=True)
  global AccountId
  global SourceId
  global DestinationId
  AccountId = event["Enter the Ids of Accounts which you want to move"]
  DestinationId = event["Enter the Ids of respective Destination Account"]
  SourceId = event["Enter the Ids of respective Source Account"]

def global_variables_to_create_scp():
  event= request.get_json(force=True)
  global SCP_Description
  global SCP_Name
  global Document_name
  SCP_Description = event["Enter the List of Descriptions for SCP"]
  SCP_Name = event["Enter the List of Names for SCP"]
  Document_name = event["Enter the List of available Json Document Name"]

def global_variables_to_attach_scp():
  event= request.get_json(force=True)
  global SCP_PolicyId
  global SCP_TargetId
  SCP_PolicyId = event["Enter the List of SCP Policy Ids that you want to attach"]
  SCP_TargetId = event["Enter the List of respective Account Ids for the Policies chosen"]

def move_account():
  global_variables_for_moving_accounts()
  for a,b,c in zip(AccountId,SourceId,DestinationId):
    Moveresponse = client.move_account(
      AccountId= a,
      SourceParentId= b,
      DestinationParentId= c
    )

def create_scp_policy():
  global_variables_to_create_scp()

  for a,b,c in zip(Document_name,SCP_Description,SCP_Name):
    if a == "scp_policy":
      with open('scp_policy.json') as f:
        data = json.load(f)
    elif a == "duplicatepolicy":
      with open('duplicatepolicy.json') as f:
        data = json.load(f)
    else:
      print("error occured")
    create_scp_response = client.create_policy(
    Content= data,
    Description= b,
    Name= c,
    Type='SERVICE_CONTROL_POLICY',
    )



def list_scp_policy():
  list_scp_response = client.list_policies(
    Filter='SERVICE_CONTROL_POLICY',
  )
  listscpstatus = list_scp_response["Policies"]

  scpNamelist =[]
  scpIdslist =[]
  for y in listscpstatus:
    for x in y.keys():
      for a in y.keys():
        Names = y["Name"]
        scpNamelist.append(Names)
        Ids = y["Id"]
        scpIdslist.append(Ids)
        break
      break
  scpdict = {scpNamelist[i]: scpIdslist[i] for i in range(len(scpNamelist))}
  return {"SCP Policies":scpdict}

def attach_scp_policy():
  global_variables_to_attach_scp()
  for x,y in zip(SCP_PolicyId,SCP_TargetId):
    attachresponse = client.attach_policy(
      PolicyId= x,
      TargetId= y
    )
  print("policy attached")
# create_scp_policy()
# attach_scp_policy()

