from pprint import pprint as pprint
from math import*
library_list = [

    {

        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True

    },

    {

        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True

    },

    {

        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False

    },

    {

        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True

    },

    {

        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False

    },

]

book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}
# # Task 1
# # Add Book Function: Write a function add_book(library, new_book)

def add_book(library, book):
     library.append(book)


print(library_list)
add_book(library_list,book)
print(library_list)

# # Task 2
# # Search Books by Author Function: Write a function search_by_author(library, author_name)

def search_by_author(library, author_name):
     books = []
     for book in library:
          if book.get("author") == author_name:
               books.append(book)
     return books

print(search_by_author(library_list,"Mark Lutz"))

# # Task 3
# # Check Out Book Function: Write a function check_out_book(library, title) that marks a book as not available if it exists and is available in the library.

def check_out_book(library, title):
     isBookExists = False
     for book in library:
          if book.get("title") == title:
            isBookExists = True
            if book.get("available") == True:
                 return f'{title} Book is available'
            else:
                 return f'{title} Book is not available'
     if isBookExists == False:
            return f'{title} book does not exist in our library'
               
print(check_out_book(library_list, "Automate the Boring Stuff with Python"))

print()

# Task 4
# Calculate average rating in the following dictionaries
movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]
print(movies)

def avg_rating(movie):
     print(movie)
     ratings = movie.get("ratings")
     ratings = sum(ratings)/len(ratings)
     print(ratings)
     return ratings

def rate_movies(movies):
     print(movies)
     for movie in movies:
          movie["avg_ratings"] = avg_rating(movie)
        
rate_movies(movies)
pprint(movies)

print(max(1,4,77,90))

def own_max(a,*nums):
     max = a
     for num in nums:
          if num > max:
               max = num
     return max

print(own_max(1,3,4,5,77,90))