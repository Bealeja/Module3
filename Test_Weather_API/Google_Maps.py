import requests

# API KEY
api_file = open("api_key.txt", "r")
api_key = api_file.read()
api_file.close()

# home address input
home = "Lake District National Park"

# Work Address Input
work = "Corfe Castle"

# Base URL
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)

# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

# print the total travel time
print("\nThe total travel time from home to work is: ", time)


#Using Google places API

url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={api_key}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)