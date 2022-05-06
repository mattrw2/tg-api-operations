import requests
import base64
import json
import config

"""
from tg import *
tg = TG()
tg.get_token()
c = tg.get_project_children(3075732)

"""

class TG:

    def __init__(self):
        self.access_token = None
        self.base_url = 'https://api.teamgantt.com/v1/'

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.access_token
        }

    def get_project_children(self, project_id):

        url = f'projects/{project_id}/children?is_flat_list=true'

        r = requests.get(self.base_url+url, headers=self.headers)
        return json.loads(r.content)

    
    def get_todays(self):

        url = 'tasks?today'

        r = requests.get(self.base_url+url, headers=self.headers)
        return json.loads(r.content)
    
    def get_token(self):

        token_url = 'https://auth.teamgantt.com/oauth2/token'
        content_type = 'application/x-www-form-urlencoded'
        client_id = config.client_id
        client_secret = config.client_secret
        username = config.username
        password = config.password

        message_bytes = f'{client_id}:{client_secret}'.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        auth_header = f'Basic {base64_message}'

        grant_type = f'grant_type=password&username={username}&password={password}'

        headers = {
            'Authorization': auth_header, 
            'Content-Type': content_type,
            }

        r = requests.post(token_url, data= grant_type, headers=headers)

        token =  json.loads(r.content)['access_token']

        self.access_token = f'Bearer {token}'
        self.headers['Authorization'] = self.access_token

        
