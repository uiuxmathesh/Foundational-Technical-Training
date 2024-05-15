from json import loads, dumps
from pprint import pprint
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

#Task 1
# All Active user's balance should increase by 10%
# Final Output should be JSON format

#converting Text to Dictionary
bank_dict = loads(bank_data)

for user in bank_dict:
    if user["isActive"]:
        user["balance"] += user["balance"] * 0.1


#converting Dictionary to JSON

bank_json = dumps(bank_dict, indent=2)

print(bank_json)

