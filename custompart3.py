from flask import Flask,jsonify,request
import json
import boto3
client = boto3.client('organizations')

# event = {
#   "List of SCP Policy Ids": [
#     "p-pn9eaoz0",
#     "p-pn9eaoz0"
#   ],
#   "List of SCP Target Ids": [
#     "105553713263",
#     "308042207821"
#   ]
# }

app=Flask(__name__)

@app.route("/attachSCP",methods=["POST"])


def custompart3(event):

  SCP_PolicyId = event["List of SCP Policy Ids"]
  SCP_TargetId = event["List of SCP Target Ids"]

  resultSCP = zip(SCP_PolicyId,SCP_TargetId)
 
#   for x,y in zip(SCP_PolicyId,SCP_TargetId):
#     attachresponse = client.attach_policy(
#       PolicyId= x,
#       TargetId= y
#     )
  print(SCP_PolicyId)
  return SCP_PolicyId

custompart3(event)