# python manage.py runserver

import requests

# Formulate our GET request and direct it to your server’s URL:
response = requests.get(url='http://127.0.0.1:8000/our_endpoints/server_time')

print(response.text)