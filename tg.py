import requests
import base64
import json
import config as config
import pandas as pd

class TG:

    base_url = 'https://api.teamgantt.com/v1/'
    token_url = 'https://auth.teamgantt.com/oauth2/token'

    def __init__(self):
        self.access_token = None
        self.refresh_token = None

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.access_token
        }

        self.get_token()

    def get_company_users_as_data_frame(self, company_id):
        url = f'{self.base_url}companies/{company_id}/users'
        r = requests.get(url,headers=self.headers)
        return pd.DataFrame(json.loads(r.content))
    
    def generate_tasks(self, project_id, how_many):
        url = 'tasks'

        for i in range(how_many):
            data = {'project_id': project_id, 'name': f'Task {i+200}'}
            requests.post(self.base_url+url, headers=self.headers, json=data)

    
    def generate_projects(self, company_id, how_many):

        url = 'projects'

        for i in range(how_many):
            data = {'company_id': company_id, 'name': f'Proj {i}'}
            requests.post(self.base_url+url, headers=self.headers, json=data)
    
    
    def get_project_children(self, project_id):

        url = f'projects/{project_id}/children?is_flat_list=true'

        r = requests.get(self.base_url+url, headers=self.headers)
        return json.loads(r.content)

    
    def post_new_labels(self, labels, company_id):

        url= f'{self.base_url}companies/{company_id}/resources/company'
        responses = []

        for label in labels:
            data = {'name':label}
            r = requests.post(url,headers=self.headers,json=data)
            responses.append(r)

        return responses

    
    def post_user(self, company_id):

        url = f'companies/{company_id}/users'

        data = {
                "can_invite": True,
                "is_guest": False,
                "permissions": "edit",
                "email_address": "matt+test111022a@teamgantt.com",
                "first_name": "C",
                "integrations": None,
                "last_name": "D",
                "status": "active",
                "time_zone": None
            }
        return requests.post(self.base_url+url, headers=self.headers, json=data)

    def get_todays(self):

        url = 'tasks?today'

        r = requests.get(self.base_url+url, headers=self.headers)
        return json.loads(r.content)
    
    def get_token(self):

        token_url = self.token_url
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

        res = json.loads(r.content)
        self.res = res
        
        token =  res['access_token']
        self.refresh_token = res['refresh_token']


        self.access_token = f'Bearer {token}'
        self.headers['Authorization'] = self.access_token