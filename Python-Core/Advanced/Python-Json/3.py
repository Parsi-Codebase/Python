import json
#Converting Python Object → JSON String
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
# Python dictionary
data = {
    "name": "Bob",
    "age": 28,
    "skills": ["C#", "Python"]
}

# Convert to JSON string
json_string = json.dumps(data)

print(json_string)
print(type(json_string))  # str
#Formatting JSON Output (Pretty Print)
#You can make JSON output more readable using 
# indent and sort_keys.
print(json.dumps(data, indent=4, sort_keys=True))