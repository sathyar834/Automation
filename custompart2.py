from flask import Flask,jsonify,request
import json
import boto3
client = boto3.client('organizations')

app=Flask(__name__)

@app.route("/CreateSCP",methods=["POST"])



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
#     "pytguardSCptest",
#     "pytguardscpcustom2"
#   ]
# }


def Move_Account():
  event= request.get_json(force=True)


  response = client.list_roots(
  )
  rootId = response['Roots'][0]['Id']
  
  AccId = event["List of Ids of Account"]
  DesId = event["List of Ids of respective Destination Account"]

  resultMove = zip(AccId,DesId)

  # for a,b in zip(AccId,DesId):
  #   Moveresponse = client.move_account(
  #     AccountId= a,
  #     SourceParentId=rootId,
  #     DestinationParentId= b
  #   )
  
  listresponse = client.list_accounts(
  )

  listmoreresponse = client.list_accounts(
    NextToken=listresponse["NextToken"]
  )

  AccountName = listresponse['Accounts']
  AccountNamemore = listmoreresponse['Accounts']


  
  Namelist =[]
  Idslist =[]
  for y in AccountName:
    for x in y.keys():
      for a in y.keys():
        Names = y["Name"]
        Namelist.append(Names)
        Ids = y["Id"]
        Idslist.append(Ids)
        break
      break
  # print(Namelist)
  # print(Idslist)
  
  Namelistmore =[]
  Idslistmore =[]
  for y in AccountNamemore:
    for x in y.keys():
      for a in y.keys():
        Names = y["Name"]
        Namelistmore.append(Names)
        Ids = y["Id"]
        Idslistmore.append(Ids)
        break
      break
  # print(Namelistmore)
  # print(Idslistmore)

  res = {Namelist[i]: Idslist[i] for i in range(len(Namelist))}
  # print(res)
  resmore = {Namelistmore[i]: Idslistmore[i] for i in range(len(Namelistmore))}
  # print(resmore)
  finaldict = dict(list(res.items()) + list(resmore.items()))
  # print(finaldict)

  event= request.get_json(force=True)
  with open('scp_policy.json') as f:
    data = json.load(f)
 
 
  SCP_Description = event["DescriptionSCP"]
  SCP_Name = event["SCPName"]
  resultMove = zip(SCP_Description,SCP_Name)
 
  PolicySCPId = []

  for a,b in zip(SCP_Description,SCP_Name):
    response = client.create_policy(
    Content= data,
    Description= a,
    Name= b,
    Type='SERVICE_CONTROL_POLICY',
    )
    Custompolicyid= response['Policy']['PolicySummary']['Id']
    PolicySCPId.append(Custompolicyid)
  print(PolicySCPId)
  return {"PolicyID":PolicySCPId}
 
if __name__ == "__main__":
  app.run(debug=True)

