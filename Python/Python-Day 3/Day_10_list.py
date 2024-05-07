
# Task 1 : Finding the distance between given coordinates and origin
coordinates = [(5,4) , (1,1), (6,10), (9,10)]

distance = [ round(((x**2 + y**2)**0.5),2) for (x,y) in coordinates]


print(distance)

person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    "sport": "football",
}

print(person["address"]["city"])
print(person.get("address").get("goals")) #Searching inside nested dictionary that doesn't exist throws error
print(person.get("stats",{"goals":0}).get("goals")) #Adding a default condition

employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
#Task 1: Update each employees experience to 1
for employee in employees:
    employee["experience"] = employee.get("experience",0) + 1
    print(employee)


# Task 2: Senior 5 or more, Mid-Level 3 to 5, Junior < 3

for employee in employees:
    experience = employee.get("experience")
    if experience < 3:
        employee["status"] = "Junior"
    elif experience < 5:
        employee["status"] = "Mid-Level"
    else:
        employee["status"] = "Senior"
    
    print(employee)

#Task 3 Merging two lists using unpacking operator

t1 = [80, 90]
t2 = [30, 50]

t3 =  [*t1, *t2]
print(t3)

# Unpacking -> ** Dict
movie = {"name": "John wick", "year": 2014}
 
# Copy
mv1 = {**movie, "actor": "Keanu Reeves"}
mv2 = {**movie, "actor": "Keanu Reeves", "year": 2015}
mv3 = {"actor": "Keanu Reeves", "year": 2015, **movie}
print(mv1)
print(mv2)
print(mv3)
print(movie)