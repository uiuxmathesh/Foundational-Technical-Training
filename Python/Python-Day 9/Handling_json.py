import json
 
data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
    ]
}
 
 
print(type(data))  # dict
# Dict -> JSON
 
data_json = json.dumps(data, indent=4)
print(data_json)
print(type(data_json))  # string
 
print(data["employees"])
print(data["employees"][0])
# print(data_json["employees"]]) # error ❌
 
 
def dbl(x):
    return x * 2
 
 
sport = {"name": "Dhoni", "dbl": lambda x: x * 2}
 
print(dbl(4))
print(sport["dbl"](4))
print(sport["dbl"])
print(sport["name"])
print(type(sport))
 
# sport_json = json.dumps(sport) # ❌ not JSON serializable
 
 
student_json = """
{
    "name": "Tonika",
    "gender": "female"
}
 
"""
 
student = json.loads(student_json)  # convert to dict
print(type(student))
print(student)
print(student["name"])
 
# json.dumps  -> dumps as JSON
# json.loads  -> loads into dict
 
 
bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""
 
 
# Task 1 (normal for loop)
# All Active user's balance should increase by 10%
# Final Output should be JSON format