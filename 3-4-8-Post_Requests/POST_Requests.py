# The POST method requests a dynamic resource (resources that are constantly modified), so it submits large amounts
# of data as parameters to be processed. The parameter can contain any amount of text, meaning the POST method can be
# used to upload large text and binary files (

import requests

urls = {'google': 'https://www.google.com',
        'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers', 'post')}}


# In the below code, you created a class that contained a single method—make_post_request. This method makes
# a POST request with three parameters: URL, data, and headers. Then, you started formulating your request. You
# specified data and headers, although notice that the headers are fake and the User-Agent is made up: the request is
# from Python but the code states that the request comes from a custom name User-Agent

class PostRequest:
    @classmethod
    def make_post_request(self, url, data=None, headers=None):
        return requests.post(url=url, data=data, headers=headers)


pr = PostRequest()

headers_post = {'User-Agent': 'My User Agent 1.0'}
data = {'Something': 'Anything'}

resp = pr.make_post_request(url=urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][2], data=data,
                            headers=headers_post)

print(gr.print_response_headers(resp.headers))
print("STATUS_CODE: ", resp.status_code)
print(resp.text)
print(resp.url)

# For a form
data = {'first_name': 'Ana', 'last_name': 'Storm', 'age': '24'}

# If you wanted to send data a different way, say by uploading a file through a POST request, you could do this:
data = {'dir':'/uploads/', 'submit':'Submit'}
files = {'file':('my_picture.jpg', open('my_picture.jpg', 'rb'))}
r = requests.post(url=urls['google'], data=data, files=files)

#OUTPUT:
# None
# STATUS_CODE:  200
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "Something": "Anything"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "18",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "Godzilla",
#     "X-Amzn-Trace-Id": "Root=1-60c9fe2e-3ab12dc94824e257395bd208"
#   },
#   "json": null,
#   "origin": "197.92.136.164",
#   "url": "https://httpbin.org/post"
# }
#
# https://httpbin.org/post

