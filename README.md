# python-publish-module

This script will create a new module in the TFCB private registry, create a new version for the module, and then upload the code for the module to the registry.  Documentation for the API can be found here:
https://www.terraform.io/cloud-docs/api-docs/private-registry/modules#create-a-module-with-no-vcs-connection

To run the script set your TFCB access token to an environment variable called TOKEN and then, set the variables to appropriate values at the top of the script.  The URL for the API is set to the default TFCB API, but could be easily changed to work with TFE as well.  

