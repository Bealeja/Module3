import json

# DUMPS: Converts Python objects to JSON String
# LOADS: Converts JSON string to Python Objects

#JSON DATA
data = '{"name":"joe", "lastname":"Doe", "age":18}'
data_parsed = json.loads(data)

print('DATA TYPE: ', type(data))
print('PARSED DATA TYPE: ', type(data_parsed))
print('LAST NAME: ', data_parsed['lastname'])
print(' ')
# Different way of moving from python to JSON
sample_data_01 = {"name": "John", "lastname": "Doe", "age": 24}

sample_data_01_json = json.dumps(sample_data_01)
print('JSON DATA TYPE: ', type(sample_data_01_json))
print('EXAMPLE DATA TYPE: ', sample_data_01_json)
print(' ')

sample_data_02 = {
    "name": "John",
    "age": 24,
    "married": True,
    "divorced": False,
    "children": ("Bruce"),
    "cars": [
        {"model": "corolla", "year": 2020},
    ]
}

print('JSON DATA: ', json.dumps(sample_data_02))
print('JSON FORMATTED INDEXED: ', json.dumps(sample_data_02, indent=4))
print('JSON FORMATTED INDEXED WITH SEPERATORS: ', json.dumps(sample_data_02, indent=4, separators=(". ", " = ")))
print(' ')
