# Set your TFCB/TFE access token to an environment variable called TOKEN prior to running.  
# The code for your module should be in a tarball stored in the location referenced by the code variable

import requests
import os

org = "swhashi"
module_name = "apitest"
module_provider = "aws"
version = "1.0.0"
code = "../terraform-aws-apitest/module.tar.gz"

def create_module(org, module_name, module_provider):
    "Create a new module in the registry"
    api_url = 'https://app.terraform.io/api/v2/organizations/{0}/registry-modules'.format(org)
    payload={"data": { "type": "registry-modules", "attributes": {"name": module_name, "provider": module_provider, "registry-name": "private"}}}
    response = requests.post(api_url, headers={'Content-Type':'application/vnd.api+json', 'Authorization': 'Bearer {}'.format(os.environ.get('TOKEN'))}, json=payload)
    print('The response from the API to the module creation request was:\n{}\n\n'.format(response.json()))
    return response;

def create_module_version(org, module_name, module_provider, version):
    "Create a new module version for an existing module"
    api_url = 'https://app.terraform.io/api/v2/organizations/{0}/registry-modules/private/{1}/{2}/{3}/versions'.format(org, org, module_name, module_provider)
    payload={"data": { "type": "registry-modules-versions", "attributes": {"version": version}}}
    response = requests.post(api_url, headers={'Content-Type':'application/vnd.api+json', 'Authorization': 'Bearer {}'.format(os.environ.get('TOKEN'))}, json=payload)
    print('The response from the API to the version creation request was\n{}\n'.format(response.json()))
    return response;
    
def upload_module_version(url, code):
    "Upload a new module version to the module registry"
    data = open(code, 'rb').read()
    response = requests.put(url, data=data, headers={'Content-Type': 'application/octet-stream'})
    print('The response from the API to the version upload request was\n{}\n'.format(response))
    return response; 

#Create the new module
create_module(org, module_name, module_provider)

#Create a new version for the module
url=create_module_version(org, module_name, module_provider, version).json()['data']['links']['upload']

#Upload the code for the module to the URL provided by the version creation API
upload_module_version(url, code)
