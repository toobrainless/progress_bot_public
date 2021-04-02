import requests
import json
import pprint

QIWI_TOKEN = 'some_token'
QIWI_ACCOUNT = 'some_number'

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
parameters = {'rows': '2'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments', params=parameters)
req = json.loads(h.text)
pprint.pprint(req)
