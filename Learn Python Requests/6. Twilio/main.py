import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.twilio.com/2010-04-01/Accounts/AC6f93cbe2be6aacbd7c5f52351814591e/Messages.json'

auth = HTTPBasicAuth('AC6f93cbe2be6aacbd7c5f52351814591e', '7a66aa1513f26415a75083a8ee559edc')

message = input('What do you want to say? ')

data = {'To' : '+17025966918', 'From' : '+17026088140', 'Body' : message}

r = requests.post(url, auth=auth, data=data)

print(r.text)