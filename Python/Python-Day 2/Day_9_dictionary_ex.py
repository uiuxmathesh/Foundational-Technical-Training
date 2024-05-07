books = [
    {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {
        "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {
        "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {
        "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]

result_books = []
for book in books:
    if book['rating'] >= 4.7:
        result_books.append(book["title"])

print(result_books)

highly_rated_books = [book["title"] for book in books if book["rating"] >= 4.7 ]

print(highly_rated_books)

# Tuple
 
 
# Tuple - Immutable
person_list = ["Sanjana", "India", 20]
person = ("Sanjana", "India", 20, 20)
 
print(person[0], person[2])
 
# person_list[0] = "Sneha"
# person[0] = "Sneha"  # ❌
print(person[0], person[2])
 
# Modification is not allowed
# List vs Tuples
# Remove -> .pop(), .remove()  - ❌
# Add -> .append() , .insert() - ❌
 
# Methods
print(person.count(20))  # 2
print(person.index("India"))  # 1
 
# index vs find
# index - error if not found | find - -1  if not found


colors = ["red", "blue", "red", "blue", "green","pink"]

color_set = {color for color in colors}

print(color_set)


color_set2 = set()

for color in colors:
    color_set2.add(color)