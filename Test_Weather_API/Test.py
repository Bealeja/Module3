import requests

API_Key = "a70562b06dd8986413ddb15946b19c92"

location_dict = {
    "Lake_District": [54.4609, -3.0886],
    "Corfe_Castle": [50.6395, -2.0566],
    "Cotswolds": [51.8330, -1.8433],
    "Cambridge": [52.2053, 0.1218],
    "Bristol": [51.4545, -2.5879],
    "Oxford": [51.7520, -1.2577],
    "Norwich": [52.6309, 1.2974],
    "Stone_Henge": [51.1789, -1.8262],
    "Watergate_Bay": [50.4429, -5.0553],
    "Birmingham": [52.4862, -1.8904]
}

print(location_dict["Oxford"][1])

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"



res = requests.get(url=URL)

print(res)
print(res.headers)
print(res.text)
print(res)
