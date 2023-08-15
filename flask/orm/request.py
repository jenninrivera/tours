import requests
import json
headers = {
    'content-type': "application/json",
    }
url = 'http://127.0.0.1:5555'
new_user = {'name':'test'}

r = requests.post(f'{url}/users', data=json.dumps(new_user), headers=headers)
print(r.json())