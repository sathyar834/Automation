import json
import boto3
from flask import Flask,jsonify,request

client = boto3.client('organizations')

app=Flask(__name__)

@app.route("/checkguard",methods=["POST"])

def default_configuration():
  event= request.get_json(force=True)
# List roots
  response = client.list_roots(
  )
  rootId = response['Roots'][0]['Id']

#  Create Core OU
  Core = client.create_organizational_unit(
    ParentId= rootId,
    Name='API_Core'
  )
  CoreID = Core['OrganizationalUnit']['Id']
  print(CoreID)

 # Create Custom OU
  Custom = client.create_organizational_unit(
    ParentId= rootId,
    Name='API_Custom'
  )
  CustomID = Custom['OrganizationalUnit']['Id']
  print(CustomID)


#Create Accounts
  EmailCore_1 = event["EmailforVDSS"]
  EmailCore_2 = event["EmailforVDMS"]
  EmailCore_3 = event["EmailforCentral"]
  EmailCore_4 = event["EmailforLogging"]
  EmailCustom_1 = event["EmailforMissionApp"]

  VDSSresponse = client.create_account(
  Email=EmailCore_1,
  AccountName='VDSS'
  )
  VDMSresponse = client.create_account(
  Email=EmailCore_2,
  AccountName='VDMS'
  )
  Centralresponse = client.create_account(
  Email=EmailCore_3,
  AccountName='Central'
  )
  Loggingresponse = client.create_account(
  Email=EmailCore_4,
  AccountName='Logging'
  )

  Missionappresponse = client.create_account(
  Email=EmailCustom_1,
  AccountName='Missionapp'
  )


  #list all the accounts
  response = client.list_accounts(
  )

  AccountName = response['Accounts']
  for y in AccountName:
    for x in y.keys():
      if y[x] == "Central":
        for a in y.keys():
          print("Name",y["Name"])
          CentralId = y["Id"]
          print(CentralId)
          break
        break
  for y in AccountName:
    for x in y.keys():
      if y[x] == "VDMS":
        for a in y.keys():
          print("Name",y["Name"])
          VDMSId = y["Id"]
          print(VDMSId)
          break
        break
  for y in AccountName:
    for x in y.keys():
      if y[x] == "VDSS":
        for a in y.keys():
          print("Name",y["Name"])
          VDSSId = y["Id"]
          print(VDSSId)
          break
        break
  for y in AccountName:
    for x in y.keys():
      if y[x] == "Logging":
        for a in y.keys():
          print("Name",y["Name"])
          LoggingId = y["Id"]
          print(LoggingId)
          break
        break
  for y in AccountName:
    for x in y.keys():
      if y[x] == "Missionapp":
        for a in y.keys():
          print("Name",y["Name"])
          MissionappId = y["Id"]
          print(MissionappId)
          break
        break

#Move accounts to Organization
  response = client.move_account(
    AccountId=CentralId,
    SourceParentId=rootId,
    DestinationParentId=CoreID
  )
  response = client.move_account(
    AccountId=VDMSId,
    SourceParentId=rootId,
    DestinationParentId=CoreID
  )
  response = client.move_account(
    AccountId=VDSSId,
    SourceParentId=rootId,
    DestinationParentId=CoreID
  )
  response = client.move_account(
    AccountId=LoggingId,
    SourceParentId=rootId,
    DestinationParentId=CoreID
  )

  response = client.move_account(
    AccountId=MissionappId,
    SourceParentId=rootId,
    DestinationParentId=CustomID
  )

#create a Service control policy
  response = client.create_policy(
    Content= "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Allow\",\"Action\":[\"s3:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement2\",\"Effect\":\"Allow\",\"Action\":[\"cloudwatch:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement3\",\"Effect\":\"Allow\",\"Action\":[\"cloudtrail:DescribeAlarmsForMetric\",\"cloudtrail:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement4\",\"Effect\":\"Allow\",\"Action\":[\"config:*\"],\"Resource\":[\"*\"]}]}",
    Description='Allow S3_CloudWatch_CloudTrail_AWSConfig',
    Name='LoggingAccountSCP',
    Type='SERVICE_CONTROL_POLICY',
  )
  Loggingpolicyid= response['Policy']['PolicySummary']['Id']
  print(Loggingpolicyid)

  response = client.create_policy(
    Content= "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Allow\",\"Action\":[\"codecommit:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement2\",\"Effect\":\"Allow\",\"Action\":[\"cloudformation:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement11\",\"Effect\":\"Allow\",\"Action\":[\"guardduty:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement12\",\"Effect\":\"Allow\",\"Action\":[\"organizations:*\"],\"Resource\":[\"*\"]},{\"Sid\":\"Statement13\",\"Effect\":\"Allow\",\"Action\":[\"kms:*\"],\"Resource\":[\"*\"]}]}",
    Description='Allows CodeCommit_Cloudformation_Guardduty_Organization_KMS',
    Name='CentralAccountSCP',
    Type='SERVICE_CONTROL_POLICY',
  )
  Centralpolicyid= response['Policy']['PolicySummary']['Id']
  print(Centralpolicyid)

# Attach the policy to Logging account
  attachresponse = client.attach_policy(
    PolicyId= Loggingpolicyid,
    TargetId= LoggingId
  )

#Attach the policy to a Central account
  attachresponse = client.attach_policy(
    PolicyId= Centralpolicyid,
    TargetId= CentralId
  )

if __name__ == "__main__":
  app.run(debug=True)
