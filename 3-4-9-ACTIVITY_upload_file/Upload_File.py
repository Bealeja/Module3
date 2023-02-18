# python manage.py runserver
import json

import requests

files = {'text': ('text.txt', open('text.txt', 'rb'))}
print(files)
response = requests.post('http://127.0.0.1:8000/our_endpoints/upload_file/', files=files)

print(response.status_code)

