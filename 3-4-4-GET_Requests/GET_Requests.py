import requests

# This method is used to execute a GET request on the specified URL.
requests.get = ()

URL = 'https://www.google.com'

# Below the URL, define and make a request and then store the response into a variable called ‘res’.
res = requests.get(url=URL)

# Running this snippet makes a GET request to Google!
print(res)

# In most situations, you would like to know if your request went through or not. To confirm, you need a response
# status code returned between 200 and 299. Ideally, you would like it to be 200 on the dot.
if res.status_code == 200:
    print(res.headers)
else:
    print(res.status_code)

# Since you will write more code, it’s a good idea to organise it. You can organise existing code into a class,
# where you can store all the GET request logic that you will use.

class GetRequests:
    def make_get_request(self, url):
        res = requests.get(url=url)

        if res.status_code == 200:
            print(res.headers)
        else:
            print(res.status_code)


urls = {'google': 'https://www.google.com'}

my_get = GetRequests()
my_get.make_get_request(urls['google'])
