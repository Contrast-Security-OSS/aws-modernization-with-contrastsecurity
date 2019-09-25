import json, yaml, os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

parameters = list()
with open('./contrast_security.yaml') as src:
    config = yaml.safe_load(src)

stack_name = "ContrastSecurityWorkshopVPC"

credentials = config['api']
url = credentials['url']
api_key = credentials['api_key']
service_key = credentials['service_key']
user_name = credentials['user_name']

parameters.append({"ParameterKey": "StackNameVPC","ParameterValue": stack_name})
parameters.append({"ParameterKey": "ContrastURL","ParameterValue": url})
parameters.append({"ParameterKey": "ContrastApiKey","ParameterValue": api_key})
parameters.append({"ParameterKey": "ContrastServiceKey","ParameterValue": service_key})
parameters.append({"ParameterKey": "ContrastUserName","ParameterValue": user_name})

with open ('./contrast-aws-workshop-ecs-parameters.json', 'w') as dest:
    json.dump(parameters,dest, indent=4, sort_keys=True)
