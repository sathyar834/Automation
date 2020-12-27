import json
import time
import boto3
client = boto3.client('organizations')

event = {
  "OUName": [
    "pyt3",
    "pyt4"
  ],
  "Name": [
    "pytSatyasleep",
    "pytSumitsleep"
  ],
  "Email": [
    "pyt1sleep@abcxyz.com",
    "pyt2sleep@abcxyz.com"
  ]
}





def Custom(event):

  response = client.list_roots(
  )
  rootId = response['Roots'][0]['Id']
  
  
  # list_of_OUNames = event["OUName"]
  # OU_IDlist=[]
  # OU_namelist=[]
  
  # for x in list_of_OUNames:
  #   responseOUID = client.create_organizational_unit(
  #   ParentId= rootId,
  #   Name=x
  #   )  
  #   OUnamefromresponse = responseOUID['OrganizationalUnit']['Name']
  #   OU_namelist.append(OUnamefromresponse)
  #   OUIDfromresponse = responseOUID['OrganizationalUnit']['Id']
  #   OU_IDlist.append(OUIDfromresponse)
  
  # print(OU_IDlist)
  # print(OU_namelist)


  # OUIdlistdict = {OU_namelist[i]: OU_IDlist[i] for i in range(len(OU_namelist))}      
  # print(OUIdlistdict)

  
  list_of_Emails = event["Email"]
  list_of_Names = event["Name"]
  Length_of_Emails = len(list_of_Emails)
  Length_of_Names = len(list_of_Names)
    
  if Length_of_Emails == Length_of_Names:
    result= zip(list_of_Emails,list_of_Names)
    

    # for x,y in zip(list_of_Emails,list_of_Names):
    #   response = client.create_account(
    #   Email=x,
    #   AccountName=y
    #   )
      
    # time.sleep(120)
    listresponse = client.list_accounts(
    )

    listmoreresponse = client.list_accounts(
      NextToken=listresponse["NextToken"]
    )

    list_of_Names = event["Name"]
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
    print(finaldict)
    keys = {k:finaldict[k] for k in (finaldict.keys() & list_of_Names)}
    print(keys)

  else:
    print("Enter the respective names for the given Email")
#  return {"rootId":rootId,"AccoundIdlist":keys}
  
Custom(event) 
  
