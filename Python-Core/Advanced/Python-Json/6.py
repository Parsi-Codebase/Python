# read json file
import json

with open('data.json', 'r') as file:
    data = json.load(file)  # read + convert to dict
    print(data)
