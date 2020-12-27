import json
import boto3
client = boto3.client('organizations')

def xxx():
  with open('guard.json') as f:
    data = json.load(f)
    data1 = json.dumps(data, indent=4)

  response = client.create_policy(
    Content= str(data1),
    Description="Landing zone guardrail",
    Name="vscodeguardrail",
    Type='SERVICE_CONTROL_POLICY'
  )
  guardpolicyid = response['Policy']['PolicySummary']['Id']
  print(guardpolicyid)

xxx()