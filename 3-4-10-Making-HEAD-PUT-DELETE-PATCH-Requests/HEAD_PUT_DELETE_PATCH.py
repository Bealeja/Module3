import requests
import json

# Using Created API server
print('API CODE:')

# HEAD
response = requests.head('http://127.0.0.1:8000/our_endpoints/check_connection/')
print('This is the API headers from status 2: ', response.headers)

# OUTPUT: This is our API headers from status 2:
# {'Date': 'Wed, 08 Feb 2023 01:08:26 GMT', 'Server': 'WSGIServer/0.2 CPython/3.11.1', 'Content-Type': ...

# PUT
data = {
    'title': 'JSON File',
    'body': 'This post was inserted through the requests library in Python. This was performed using a PUT request',
    'userId': 1,
    'id': 1
}
# DUMPS: Converts Python objects to JSON String
# LOADS: Converts JSON string to Python Objects
json_data = json.dumps(data)
response = requests.put('http://127.0.0.1:8000/our_endpoints/save_json_to_file/', data=json_data)
print('This is the returned response for JSON_file generation: ', response)

# OUTPUT
# This is our JSON response text:  <Response [200]>

# DELETE
del_file = {
    "file_name": "test02"
}
json_del_file = json.dumps(del_file)
response = requests.delete('http://127.0.0.1:8000/our_endpoints/delete_file/', data=json_del_file)
print('This is the deleted file response: ', response)

# PATCH
data = {
    'updates': '\n Hello, This post was inserted through the requests library in Python as a patch file',
}
json_data = json.dumps(data)
response = requests.patch('http://127.0.0.1:8000/our_endpoints/update_file/', data=json_data)
print(response.text)

# ----------------------------------------------------


print(' ')
# Example Code
print('EXAMPLE CODE: ')

# HEAD
# This is used to retrieve the status line and header information from a specified URL.
r = requests.head('https://jsonplaceholder.typicode.com/posts/1')
print(r.headers)

# OUTPUT: {'Date': 'Wed, 16 Jun 2021 10:05:52 GMT', 'Content-Type': 'application/json;..

# PUT
# This is used to send a PUT request to the specified URL. A PUT request will update the resource specified with
# the modified information.
url = 'https://jsonplaceholder.typicode.com/posts/1'
myobj = {
    'title': 'Inserted through requests library',
    'body': 'This post was inserted through the requests library in Python. This was performed using a PUT request',
    'userId': 1,
    'id': 1
}
x = requests.put(url, data=myobj)
print(x.text)

# OUTPUT
# {
#   "title": "Inserted through requests library",
#   "body": "This post was inserted through the requests library in Python. This was performed using a PUT request",
#   "userId": "1",
#   "id": 1
# }

# DELETE
# This is used to delete a particular resource from the server.
r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

# OUTPUT
# {}

# PATCH This is similar to the ‘put’ request in that it will also modify the resource that is specified in the
# request body. The difference is that the patch request will replace the existing resource with the resource in its
# request body, whereas ‘put’ will only update the existing resource with the changed fields in the request body.
url = 'https://jsonplaceholder.typicode.com/posts/1'
myobj = {
    'title': 'Inserted through requests library',
    'body': 'This post was inserted through the requests library in Python. This was performed using a PUT request',
    'userId': 3,
    'id': 2
}
x = requests.patch(url, data=myobj)
print(x.text)
