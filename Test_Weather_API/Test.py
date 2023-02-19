import requests
import json

# Create dictionary of location and lat, long (Done)

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
lat = location_dict["Lake_District"][0]
lon = location_dict["Lake_District"][1]

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"

response = requests.get(url=URL)

# Example Test
#print(location_dict["Oxford"][1])
#print(response)
#print(response.headers)
#print(response.text)

# Identify Critical Weather Features needed to display for assignment

# co-ord
## lat and long,

# weather
## main
## description

# main
## temp
## feel_like
## temp_min
## temp_max
## humidity

# wind
## speed

#sys
## name

# Get Extracts by converting from JSON to python

jsonResponse = response.json()

#Example 2
print(jsonResponse)
jsonObject = json.dumps(jsonResponse, indent=4)
print(jsonObject)
print(jsonResponse["name"])

print("These are the listed info parameters: ")


# Display to Console

# Create API calls depending on each feature

# Create best route for the day call

# Create best route for the future (if possible) call
