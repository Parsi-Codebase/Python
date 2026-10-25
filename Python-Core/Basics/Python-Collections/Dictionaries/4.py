employee = {
    "id": 101,
    "name": "John",
    "department": "IT",
    "salary": 75000
}

print("Employee ID:", employee["id"])
print("Name:", employee["name"])
print("Department:", employee["department"])
print("Salary:", employee["salary"])

# Update salary
employee["salary"] = 80000

# Add new property
employee["location"] = "Hyderabad"

print("\nUpdated Employee:")

for key, value in employee.items():
    print(key, ":", value)