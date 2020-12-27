
import json
import boto3


client = boto3.client('organizations')

def move_ac():
  try:
    Moveresponse = client.move_account(
      AccountId= "640338191567",
      SourceParentId="ou-oblp-vav4uc7y",
      DestinationParentId= "ou-oblp-t1ps2psp"
    )
  except client.exceptions.SourceParentNotFoundException as e:
    raise e
  except client.exceptions.TooManyRequestsException as e:
    raise e
  except client.exceptions.ConcurrentModificationException as e:
    raise e
  except client.exceptions.AccountNotFoundException as e:
    raise ("AccountNotFound")
move_ac()