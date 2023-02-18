import json

# Step 1: Format the following as JSON with indent 4:

data_01 = { "color": "black", "Year of first registration": 2008, "brand": "bmw"}
data_02 = { "Name": "Lyra", "Last name": "Doe", "year of birth": 1987 }
data_03 = { "Name": "Lyra", "Last name": "Doe", "year of birth": 1987, "car": [{ "color": "black", "Year of first registration": 2008, "brand": "bmw"}]}

print(json.dumps(data_01, indent=4))
print(json.dumps(data_02, indent=4))
print(json.dumps(data_03, indent=4))
