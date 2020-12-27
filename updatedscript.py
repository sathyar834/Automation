import json
import time
import boto3
from flask import Flask,jsonify,request

client = boto3.client('organizations')


def list_roots():
  global rootId
  rootId_response = client.list_roots(
  )
  rootId = rootId_response['Roots'][0]['Id']
  return {"RootId":rootId}

# event = {
#   "OU_Parent":["r-oblp"],
#   "OUName":["flaskOU"],
#   "OUParent":["r-oblp"],
#   "Name":["pytSumit","testapi2"]
# }


def global_variables_to_create_ou():
  event= request.get_json(force=True)
  global list_of_OUNames
  global list_of_ParentId
  list_of_OUNames = event["Enter the list of names on which the OU has to be created"]
  list_of_ParentId = event["Enter the Id of the parent where the OU has to be created"]

def global_variables_to_list_ou():
  event= request.get_json(force=True)
  global OU_parentId_list
  OU_parentId_list = event["Enter the Id of the parent OU whose child OUs you want to list"]

def global_variables_for_account():
  event= request.get_json(force=True)
  global list_of_Emails
  global list_of_Names
  list_of_Emails = event["Enter the list of Emails to create account"]
  list_of_Names = event["Enter the names for the respective Emails to create account"]

def create_organizational_units():
  global_variables_to_create_ou()
  for x,y in zip(list_of_ParentId,list_of_OUNames):
    Create_OU_response = client.create_organizational_unit(
    ParentId= x,
    Name=y
    )
    time.sleep(10)

def list_organizational_units():
  global_variables_to_list_ou()
  OUnames_list = []
  OUId_list = []
  for x in OU_parentId_list:
    list_OU_response = client.list_organizational_units_for_parent(
      ParentId=x,
    )
    NameofOU = list_OU_response["OrganizationalUnits"]
    for y in NameofOU:
      for x in y.keys():
        for a in y.keys():
          Names = y["Name"]
          OUnames_list.append(Names)
          Ids = y["Id"]
          OUId_list.append(Ids)
          break
        break
  print(OUnames_list)
  print(OUId_list)

  OUdict = {OUnames_list[i]: OUId_list[i] for i in range(len(OUnames_list))}
  print(OUdict)
  # keys = {k:OUdict[k] for k in (OUdict.keys() & list_of_OUNames)}
  # print(keys)
  return {"Organizational units":OUdict}

def list_accounts():
  # global_variables_for_account()
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

  res = {Namelist[i]: Idslist[i] for i in range(len(Namelist))}
  # print(res)
  resmore = {Namelistmore[i]: Idslistmore[i] for i in range(len(Namelistmore))}
  # print(resmore)
  finaldict = dict(list(res.items()) + list(resmore.items()))
  print(finaldict)
  return{"Accounts":finaldict}
  # keys = {k:finaldict[k] for k in (finaldict.keys() & list_of_Names)}
  # print(keys)

def list_existing_email():
  listresponse = client.list_accounts(
  )

  listmoreresponse = client.list_accounts(
    NextToken=listresponse["NextToken"]
  )

  AccountEmail = listresponse['Accounts']
  AccountEmailmore = listmoreresponse['Accounts']

  Emaillist =[]
  for y in AccountEmail:
    for x in y.keys():
      for a in y.keys():
        Email = y["Email"]
        Emaillist.append(Email)
        break
      break

  Emaillistmore =[]
  for y in AccountEmailmore:
    for x in y.keys():
      for a in y.keys():
        Email = y["Email"]
        Emaillistmore.append(Email)
        break
      break

  final_email_list = Emaillist + Emaillistmore
  return final_email_list

def create_account():
  Existing_emails = list_existing_email()
  global_variables_for_account()
  Length_of_Emails = len(list_of_Emails)
  Length_of_Names = len(list_of_Names)

  if Length_of_Emails == Length_of_Names:
    for mail,name in zip(list_of_Emails,list_of_Names):
      for awsmail in Existing_emails:
        if mail == awsmail:
          status = "Invalid email"
          Invalid_mail = mail
          return("The email",Invalid_mail,"already exist!")
          break
        else:
          status = "Valid email"
      if status == "Valid email":
        cresponse = client.create_account(
          Email= mail,
          AccountName= name,
          IamUserAccessToBilling='ALLOW'
        )
        return("Account created successfully")
      
  else:
    return("Enter the respective names for the given Email")
    time.sleep(10)


