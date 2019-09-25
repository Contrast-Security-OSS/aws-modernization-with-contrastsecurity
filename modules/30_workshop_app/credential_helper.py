import json, yaml, os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

parameters = list()
with open('./contrast_security.yaml') as src:
    config = yaml.safe_load(src)

vpc_stack_name = "ModernizationVPC"
desired_count = "1"

credentials = config['api']
url = credentials['url']
api_key = credentials['api_key']
service_key = credentials['service_key']
user_name = credentials['user_name']

parameters.append({"ParameterKey": "VPCstack","ParameterValue": vpc_stack_name})
parameters.append({"ParameterKey": "ContrastURL","ParameterValue": url})
parameters.append({"ParameterKey": "ContrastApiKey","ParameterValue": api_key})
parameters.append({"ParameterKey": "ContrastServiceKey","ParameterValue": service_key})
parameters.append({"ParameterKey": "ContrastUserName","ParameterValue": user_name})
parameters.append({"ParameterKey": "DesiredCount", "ParameterValue": desired_count})

with open ('./ecs-parameters.json', 'w') as dest:
    json.dump(parameters,dest, indent=4, sort_keys=True)
