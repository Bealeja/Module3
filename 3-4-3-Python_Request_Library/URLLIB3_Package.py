import urllib.request as urlb

response_url = urlb.urlopen('https://api.publicapis.org/entries')

print(response_url)

#OUTPUT
#<http.client.HTTPResponse object at 0x00000275F522EEE0>

print(response_url.info())

#OUTPUT
# Access-Control-Allow-Origin: *
# Content-Type: application/json
# Date: Fri, 18 Jun 2021 18:16:01 GMT
# Server: Caddy
# X-Rate-Limit-Duration: 1
# X-Rate-Limit-Limit: 10.00
# X-Rate-Limit-Request-Forwarded-For: 102.39.128.155
# X-Rate-Limit-Request-Remote-Addr: 172.17.0.1:35808
# Connection: close
# Transfer-Encoding: chunked

print(response_url.read())
# "Category":"Weather"},{"API":"weather-api","Description":"A RESTful free API to check the weather","Auth":"",
# "HTTPS":true,"Cors":"no","Link":"https://github.com/robertoduessmann/weather-api", "Category":"Weather"},
# {"API":"Weatherbit","Description":"Weather","Auth":"apiKey","HTTPS":true,"Cors":"unknown",
# "Link":"https://www.weatherbit.io/api", "Category":"Weather"},{"API":"weatherstack","Description":"Real-Time
# \\u0026 Historical World Weather Data API","Auth":"apiKey","HTTPS":true,"Cors":"unknown",
# "Link":"https://weatherstack.com/", "Category":"Weather"}]}\n'

import pprint

response_url = urlb.urlopen('https://api.publicapis.org/entries')

html = response_url.read()
pprint.pprint(html)

response_url.close()

# OUTPUT
# b'th":"apiKey","HTTPS":true,"Cors":"yes","Link":"https://www.visualcrossing.co'
#  b'm/weather-api","Category":"Weather"},{"API":"weather-api","Description":"A R'
#  b'ESTful free API to check the weather","Auth":"","HTTPS":true,"Cors":"no","Li'
#  b'nk":"https://github.com/robertoduessmann/weather-api","Category":"Weather"},'
#  b'{"API":"Weatherbit","Description":"Weather","Auth":"apiKey","HTTPS":true,"Co'
#  b'rs":"unknown","Link":"https://www.weatherbit.io/api","Category":"Weather"},{'
#  b'"API":"weatherstack","Description":"Real-Time \\u0026 Historical World We'
#  b'ather Data API","Auth":"apiKey","HTTPS":true,"Cors":"unknown","Link":"https:'
#  b'//weatherstack.com/","Category":"Weather"}]}\n')