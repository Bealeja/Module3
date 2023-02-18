import requests

API_key = "a70562b06dd8986413ddb15946b19c92"

URL = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=a70562b06dd8986413ddb15946b19c92"

URL_LL = "https://api.openweathermap.org/data/2.5/weather?lat=54.4609&lon=3.0886&appid=a70562b06dd8986413ddb15946b19c92"

res = requests.get(url=URL_LL)

print(res)
print(res.headers)
print(res.text)
