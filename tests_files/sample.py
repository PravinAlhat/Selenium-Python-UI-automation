from utilities.configurations import *
from utilities.payload import *
from utilities.variables import *
import requests
import json

config = getconfig(GlobalVariables.properties_file)
payload = json.dumps(addObjects())

add_object = requests.post(url=config['API']['endpoint'], data=payload, headers=GlobalVariables.headers)
add_object_response = add_object.json()
assert add_object.status_code == GlobalVariables.SUCCESS
if add_object_response['id']:
    id_to_delete = add_object_response['id']

delete_object = requests.delete(url=config['API']['delete_endpoint'].replace('id', id_to_delete), headers=GlobalVariables.headers)
delete_object_response = delete_object.json()
assert delete_object.status_code == GlobalVariables.SUCCESS
assert delete_object_response['message'] == 'Object with id = {} has been deleted.'.format(id_to_delete)
