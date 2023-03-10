import requests
import json
import ee

# Parameters for URL
APIKey = "a70562b06dd8986413ddb15946b19c92"
Units = "metric"

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
Lat = location_dict["Lake_District"][0]
Lon = location_dict["Lake_District"][1]

# API URL
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Lon}&appid={APIKey}&units={Units}"

# FUNCTION 1: Produce Weather Data for a set location

# Request GET and Conversion to JSON
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?lat=51.752&lon=-1.2577&appid=a70562b06dd8986413ddb15946b19c92&units=metric")
jsonResponse = response.json()
print(" ")

# Display to Console
print('Here is the information for the location you have specified: \n'
      f'Name of Location: {jsonResponse["name"]}\n'
      f'Longitude: {jsonResponse["coord"]["lon"]}\n'
      f'Latitude: {jsonResponse["coord"]["lat"]}\n'
      f'Weather: {jsonResponse["weather"][0]["main"]}\n'
      f'Weather Description: {jsonResponse["weather"][0]["description"]}\n'
      f'Temperature (Celcius): {jsonResponse["main"]["temp"]}\n'
      f'Feels Like (Celcius): {jsonResponse["main"]["feels_like"]}\n'
      f'Temp Min (Celcius): {jsonResponse["main"]["temp_min"]}\n'
      f'Temp Max (Celcius): {jsonResponse["main"]["temp_max"]}\n'
      f'Humidity: {jsonResponse["main"]["humidity"]}%\n'
      f'Wind Speed (m/s): {jsonResponse["wind"]["speed"]}\n'
      f'Clouds: {jsonResponse["clouds"]["all"]}%\n'
      )

# Create API calls depending on each feature
# Location Weather (with google image)
# Item List
# Best Path and duration of Journey
# Google Map

# FUNCTION 2: PRODUCE BEST ROUTE BASED ON WEATHER

# Create best route for the day call
# calculate: Weather, Feels like, Wind Speed, Clouds for all locations
# for key in locations dict
# get request latitude long values
# add name of dict location, lat, long, Weather, Feels like, Wind Speed, Clouds to an array, ranking = 0
rating_dict = {}

for key in location_dict:
    Lat_dict = location_dict[str(key)][0]
    Lon_dict = location_dict[str(key)][1]
    url_dict = f"https://api.openweathermap.org/data/2.5/weather?lat={Lat_dict}&lon={Lon_dict}&appid={APIKey}&units={Units}"

    response = requests.get(url=url_dict)
    jsonResponse = response.json()

    rating_dict[str(key)] = [jsonResponse["coord"]["lat"],
                             jsonResponse["coord"]["lon"],
                             jsonResponse["weather"][0]["description"],
                             jsonResponse["main"]["feels_like"],
                             jsonResponse["wind"]["speed"],
                             jsonResponse["clouds"]["all"]
                             ]

new_sorted_by_lat_lon = sorted(rating_dict.items(), key=lambda x: x[1][0])
print("Sorted by latitude: \n", new_sorted_by_lat_lon)
print(" ")
new_sorted_by_clouds = sorted(rating_dict.items(), key=lambda x: x[1][5])
print("Sorted by best weather: \n", new_sorted_by_clouds)

# Create Google API call for the location and a calculation of the best path. Return the journey time



