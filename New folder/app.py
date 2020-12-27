from flask import Flask,jsonify,request
import json
import boto3

client = boto3.client('iam')

app=Flask(__name__)

@app.route("/addgroup",methods=["POST"])


def create_group():

  req= request.get_json(force=True)
  name = req['Group_Name']
  response = client.create_group(
    GroupName= name
  )
  return response
if __name__ == "__main__":
  app.run(debug=True)
