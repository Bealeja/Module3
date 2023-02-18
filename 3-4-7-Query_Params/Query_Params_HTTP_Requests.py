import requests

# Query parameters are used in GET requests as a form of customisation by passing values through the parameter string
# or, in other words, parameterising the GET request. What’s more, it helps retrieve specific data and performs
# actions based on user inputs.
#
# One way to do so is to pass data to params. You can pass params as a dictionary, list, or tuple. So, for example,
# passing a list to the params parameter of the GET request modifies the results that come back

requests.get(
    'https://samples.openweathermap.org/data/2.5/',
    params=[('q', 'Chicago, USA')],
)

query = {'q': 'stream', 'order': 'length', 'min_width': '5000', 'min_height': '300'}
req = requests.get('https://flickr.com/en/photos/', params=query)

print(req.url)

# OUTPUT:

# https://flickr.com/en/photos/?q=stream&min_width=5000&min_height=300&order=length
