#!/usr/bin/python3
import requests

payload = {'username':'chris', 'password':'azerty'}
r = requests.post('https://httpbin.org/post', data=payload)
headers = r.headers
text = r.json()
url = r.url
print(f'{r.status_code:.<8}{r.ok}')
print(text['form'])

