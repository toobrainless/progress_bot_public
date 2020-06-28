import requests
import json
import pprint

QIWI_TOKEN = 'b54133f0bb4500328dae755a7bb55556'
QIWI_ACCOUNT = '+79173922879'

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
parameters = {'rows': '2'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments', params=parameters)
req = json.loads(h.text)
pprint.pprint(req)
