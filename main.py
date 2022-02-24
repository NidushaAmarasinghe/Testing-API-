import requests
import os

API = os.environ.get('SD_API')

req = requests.post(API+'/logo?name='+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
