import glob
import json
import os
# arr = os.listdir(r'C:\Users\Sathya R\Desktop\VS Code Scripts')
arr_txt = [x for x in os.listdir(r'C:\Users\Sathya R\Desktop\VS Code Scripts') if x.endswith(".json")]
# print(arr_txt)

f = open(r'C:\Users\Sathya R\Desktop\New folder (2)\scp_policy.json')
data = json.load(f)
data1 = json.dumps(data, indent=4)
print(data1)
# txtfiles = []
# for file in glob.glob(r'C:\Users\Sathya R\Desktop\VS Code Scripts\*.json'):
#   txtfiles.append(file)
# print(txtfiles)