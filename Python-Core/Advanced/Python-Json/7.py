# Read API Response
import json

response = '''
{
  "id": 101,
  "title": "Python JSON Tutorial",
  "tags": ["python", "json", "tutorial"],
  "published": true
}
'''

# Convert to Python object
post = json.loads(response)

# Access data
print(post["title"])
print(post["tags"][1])
