# a = 10
# b = 10
# c = 10
 
 
# Multiple variable assignment
a = b = c = 10
print(a, b, c)
 
 
# Unpacking / Destructuring
# poojitha, shivam, samar = ("Black current", "Choco chip", "Butterscotch") # Tuple
poojitha, shivam, samar = "Black current", "Choco chip", "Butterscotch"  # Tuple
 
print(poojitha)
print(shivam)
print(samar)
 
movies = ["Mission Impossible", "JJK", "Avengers Infinity War"]
# mathesh = movies[0]
# nandhini = movies[1]
# devesh  = movies[2]
 
mathesh, nandhini, devesh = movies
print(mathesh, nandhini, devesh)
 
 
# t1, t2, t3 = [100, 200, 300, 400]
# print(t1, t2, t3)  # ❌
 
 
# t1, t2, t3, _ = [100, 200, 300, 400]
# print(t1, t2, t3)  # _ -> skip
 
 
# t1, _ , t2, t3, = [100, 200, 300, 400]
# print(t1, t2, t3)  # 100 300 400
 
# * -> Unpacking operator
# t1, t2, *t3 = [100, 200, 300, 400, 60, 40, 30]
# print(t1, t2, t3)  # 100 200 [300, 400, 60, 40, 30]
 
 
# * -> Unpacking operator
t1, t2, *t3 = (100, 200, 300, 400, 60, 40, 30)
print(t1, t2, t3)  # 100 200 [300, 400, 60, 40, 30]
 
 
# Task 1
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
 
# For each point find the distance from origin
 
# Task 1.1 - for loop
 
# distances = []
# for cord in coordinates:
#     x = cord[0]
#     y = cord[1]
#     d = (x**2 + y**2) ** 0.5
#     distances.append(d)
 
# print(distances)
 
# Task 1.2 - for loop + unpacking
 
# distances = []
# for cord in coordinates:
#     x, y = cord
#     d = (x**2 + y**2) ** 0.5
#     distances.append(d)
 
# print(distances)
 
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distances = []
for x, y in coordinates:
    d = (x**2 + y**2) ** 0.5
    distances.append(round(d, 2))
 
print(distances)
 
 
# Task 1.3 - unpacking + list comprehension
 
 
distances = [round((x**2 + y**2) ** 0.5, 2) for x, y in coordinates]
print(distances)
# Output
# [6.4, 1.414, 11.66, 13.45]
 
 
# t1, t2, *z1, t3 = (100, 200, 300, 400, 60, 40, 30)
t1, t2, *_, t3 = (100, 200, 300, 400, 60, 40, 30)
print(t1, t2, t3)
 
# Copy
marks1 = [70, 80, 60]
# marks2 = [*marks1] # copy - 1. slice    2. .copy()
marks2 = [*marks1, 75, 68]
marks3 = [100, 60, *marks1, 75, 68]
print(marks2)
print(marks3)
 
# Merging multiple lists
t1 = [80, 90]
t2 = [50, 60]
t3 = [*t1, *t2]  # t1 + t2
 
print(t3)
 
# t3 = [80, 90, 50, 60]
 
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
 
# Dict - No duplicate keys