import requests
import json

location = {
    "Location": "Oxford"
}
json_location = json.dumps(location)
response = requests.get('http://127.0.0.1:8000/wa_api/getlocationdata/', data=json_location)
returned_data = json.loads(response.text)
indented_data = json.dumps(returned_data, indent=4)
print(indented_data)


