import requests
response = requests.get('https://catfact.ninja/fact')
print(response.status_code)

#OUTPUT
#200