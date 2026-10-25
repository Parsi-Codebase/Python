# write to json file
import json

data = {
    "name": "Charlie",
    "age": 35,
    "city": "Delhi"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
