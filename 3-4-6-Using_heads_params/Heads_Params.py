# You might have noticed in the example before the exercise that the headers were printed out in one line,
# making it difficult to read.  Remember, headers are a way to transmit additional information with an HTTP request,
# and being able to easily read the information they store is valuable.
import requests


class GetRequests:
    @classmethod
    def print_response_headers(self, response_headers):
        for key, value in response_headers.items():
            print(key, ": ", value)

    @classmethod
    def make_get_request(self, url):
        res = requests.get(url=url)

        if res.status_code == 200:
            self.print_response_headers(res.headers)
        else:
            self.print_response_headers(res.status_code)

    # Return to the Requests.py file and modify the make_get_request to only return the response, then add a condition to
    # the request based on the optional parameter params.
    #
    # You’ll learn more about params and their various types later this week. For now, you should know that params allow
    # us to pass information or instructions along with HTTP methods.

    @classmethod
    def make_get_request(self, url, params=None):
        return requests.get(url=url, params=params)

    # **
    @classmethod
    def make_get_request(self, url, params=None, headers=None):
        return requests.get(url=url, params=params, headers=headers)


# Expand your URL dictionary to include additional URLs you will use for testing and demonstrating requests.

urls = {'google': 'https://www.google.com',
        'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers')}}

gr = GetRequests()
resp = gr.make_get_request(urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][0])
print(resp)

# OUTPUT:
# <Response [200]>

# Next, you will set headers and parameters, and then modify them to see what happens.

# **

params_get = {'freeform': 'Something is HERE'}
headers_get = {'content-type': 'application/json'}

# Next, formulate a new request where params and headers will be defined:

gr = GetRequests()
resp = gr.make_get_request(urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][1], params=params_get,
                           headers=headers_get)
print(gr.print_response_headers(resp.headers))
print(resp.content)
print(resp.url)

# The defined params and headers are passed to the class method make_get_request. The class method takes in the three
# arguments:
#
# 1. a constructed address with the path
# 2. the parameters
# 3. the headers.

# OUTPUT:

# Date :  Wed, 16 Jun 2021 13:10:52 GMT
# Content-Type :  application/json
# Content-Length :  105
# Connection :  keep-alive
# Server :  gunicorn/19.9.0
# freeform :  Something is HERE
# Access-Control-Allow-Origin :  *
# Access-Control-Allow-Credentials :  true
# None
# b'{\n  "Content-Length": "105", \n  "Content-Type": "application/json", \n  "freeform": "Something is HERE"\n}\n'
# https://httpbin.org/response-headers?freeform=Something+is+HERE

# If you wanted multiple param and multiple headers, you could just expand param and headers further like this:

params = {'freeform': 'Something is HERE', 'test': 'test'}
headers = {'content-type': 'application/json', 'test': 'test'}
