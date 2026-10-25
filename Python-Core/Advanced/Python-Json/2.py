import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into json:
y=json.dumps(x)
print(y) # the result is a json string