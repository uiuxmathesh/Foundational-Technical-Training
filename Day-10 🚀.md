# Day-10 🚀

# Python Day-3 📆

# Set (contd..)

- To add one item to a set use the `add()` method.
    
    **Example**
    
    Add an item to a set, using the `add()` method:
    
    ```python
    thisset = {"apple", "banana", "cherry"}
    thisset.add("orange")
    print(thisset)
    ```
    

### Add Sets

- To add items from another set into the current set, use the `update()` method.
    
    **Example**
    
    Add elements from `tropical` into `thisset`:
    
    ```python
    thisset = {"apple", "banana", "cherry"}
    tropical = {"pineapple", "mango", "papaya"}
    thisset.update(tropical)
    print(thisset)
    ```
    

### Add Any Iterable

- The object in the `update()` method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
    
    **Example**
    
    Add elements of a list to at set:
    
    ```python
    thisset = {"apple", "banana", "cherry"}
    mylist = ["kiwi", "orange"]
    thisset.update(mylist)
    print(thisset)
    ```
    

### Remove Item

- To remove an item in a set, use the `remove()`, or the `discard()` method.
    
    **Example**
    
    Remove "banana" by using the `remove()` method:
    
    ```python
    thisset = {"apple", "banana", "cherry"}
    thisset.remove("banana")
    print(thisset)
    ```
    
    **Note:** If the item to remove does not exist, `remove()` will raise an error.
    
    **Example**
    
- Remove "banana" by using the `discard()` method:
    
    ```python
    thisset = {"apple", "banana", "cherry"}
    thisset.discard("banana")
    print(thisset)
    ```
    
    **Note:** If the item to remove does not exist, `discard()` will **NOT** raise an error.
    

## **Other important Methods in Sets:**

1. `union()`
2. `intersection()`
3. `difference()`
4. `symmetric_difference()` 
5. `issubset()`
6. `issuperset()` 

# Python Assignation Techniques

Let us say we need to assign three variables namely `a` `b` `c` each with same value, let’s say 10.

### 1. Way 1 (Traditional Assignment)

- We can typically do this by,

```python
a = 10
b = 10
c = 10
```

This is the one way and traditional way of doing it.

### 2. Way 2 (Pythonic Assignment)

```python
a = b = c = 10
```

This is another and simpler way of doing it.

### 3. Way 3 (Unpacking)

- Let’s say we have three guys `mathesh` ,`mohammed` ,`manoj` and each of them having their personal favorite movies `"Mission Impossible"` , `"Fast & Furious"` , `"GI Joe"` . We cannot assign them as shown above as each of them are having different values to be assigned. But we do have a way to assign them in a pythonic way
    
    ```python
    mathesh,mohammed,manoj = ["Mission Impossible", "Fast & Furious", "GI Joe"]
    ```
    
- This way of assigning multiple variables all at once  is  called **“Unpacking”**
- Here since we have used list for storing the values to be assigned it is called “List Unpacking”.
- This same thing can be done with tuple and sets
    
    ```python
    mathesh,mohammed,manoj = ("Mission Impossible", "Fast & Furious", "GI Joe")
    mathesh,mohammed,manoj = {"Mission Impossible", "Fast & Furious", "GI Joe"}
    ```
    
    The above code does the same thing.
    

- But here araises a problem. What if you have more values to unpack then you need. Then python shows error
    
    For example,
    
    ```python
    a,b,c = [1,2,3,4]
    ```
    
- In this scenario we have 3 variables but 4 values to unpack. This will throw an error. We can solve this by two ways.
    - First is, omitting a value. How can we do that
        
        ```python
        a,b,c,_ = [1,2,3,4]
        ```
        
        The above code assigns a = 1, b = 2, c = 3 and omits 4. This is because we used underscore `_`  which basically skips that particular value.
        
        We can omit any value we wish to.
        
        ```python
        a,b._,c = [1,2,3,4] #omits 3
        a,_, b,c = [1,2,3,4] #omits 2
        ```
        
    
    - The second way of doing so is using `*` operator which is know as unpacking operator
        
        ```python
        a,b,*c = [1,2,3,4]
        ```
        
        This statement assigns, a = 1, b = 2, and then creates a list out of the remaining values, which is then assigned to c.
        
        unpacking operator can be used in first, last, middle or any part of the variable list
        

> **Note:** No matter which unpacking technique you’re using, it always returns the remaining element as list
> 

# Tasks on Dictionary

**Task 1: Finding the distance between given coordinates and origin**

Method 1: for-loop

```python
coordinates = [(5,4) , (1,1), (6,10), (9,10)]
distance = []
for coordinate in coordinates:
		x = coordinate[0]
		y = coordinate[1]
		distance.append(round(((x**2 + y**2)**0.5),2))

print(distance)
```

Method  2: Unpacking + for-loop

```python
coordinates = [(5,4) , (1,1), (6,10), (9,10)]
distance = []
for x,y in coordinates:
		distance.append(round(((x**2 + y**2)**0.5),2))

print(distance)
```

Method 3: Unpacking + List comprehension

```python
coordinates = [(5,4) , (1,1), (6,10), (9,10)]

distance = [ round(((x**2 + y**2)**0.5),2) for (x,y) in coordinates]

print(distance)
```

## Difference between `[]` notation and `.get()` method in dictionary

Both the `[]` notation and `.get()` method is used for accessing the dicitonary items. But while using the `[]` notation and key specified inside the notation is not found, then it throws an error, whereas the `.get()` method returns `None` type.

Hence, we can say that it is safer to use `.get()` method to avoid errors.

Let’s see a practical example

```python
person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    "sport": "football",
}

print(person["address"]["goals"]) #This throws error
print(person.get("address").get("goals")) #This returns 'Nonetype' object
print(person.get("stats").get("goals")) #In this we are accessing a 'Nonetype' Object to get a key: value pair. So it throws error
print(person.get("stats",{"goals":0}).get("goals")) #.get() method accepts two parameter. One is the key to be searched. Another is the default value which has to be returned when the key is not found. This solves the previous error
```

**Task 2: Update each employees experience by 1**

```python
employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
for employee in employees:
    employee["experience"] = employee.get("experience",0) + 1
    print(employee)
```

**Task 3: Assign a status key to each employee and provide their value as Senior 5 or more, Mid-Level 3 to 5, Junior < 3**

```python
for employee in employees:
    experience = employee.get("experience")
    if experience < 3:
        employee["status"] = "Junior"
    elif experience < 5:
        employee["status"] = "Mid-Level"
    else:
        employee["status"] = "Senior"
    
    print(employee)
```

**Task 4: Merging two lists using unpacking operator**

```python
t1 = [80, 90]
t2 = [30, 50]

t3 =  [*t1, *t2]
print(t3)
```

## Unpacking Dictionary

To unpack a dictionary we need to use the unpacking operator `*` two times.

```python
movie = {"name": "John wick", "year": 2014}
 
mv1 = {**movie, "actor": "Keanu Reeves"}
mv2 = {**movie, "actor": "Keanu Reeves", "year": 2015}
mv3 = {"actor": "Keanu Reeves", "year": 2015, **movie}
print(mv1)
print(mv2)
print(mv3)
print(movie)
```

> **Note:** emember that in dicitonaries the keys should be unique. So in unpacking two or more dictionaries to create a new one, if a key is repeated, then the last occurence of the key’s value will be assigned to the key overwriting the previous one.
> 

## Functions in Python

The purpose of functions  in any programming language is to keep the logic in one-place

Let’s say we have the code like

```python
a = 10
b = 20
print("The sum is ", a+b)

a1 = 40
b1 = 30
print("The sum is ", a1+b1)

a2 = 50
b2 = 70
print("The sum is ", a2+b2)
```

If you look closely the same logic of addition operation is applied three times in the same code. What if we find a way to make this code a lot more robust.

So here’s how we can write the code using function.

```python
def add(a,b):
	return f'The sum is {a+b}'

print(add(10,20))
print(add(40,30))
print(add(50,70))
```

Now that we have know functions can help clean our code by having the logic in one place, let’s start learning functions by understanding the syntax of function definition in python

```python
def functionName(parameter1, parameter2...parametern):
	statements here
```

### Parts of Functions

1. Function Declaration/Definition
2. Function name
3. Parameters (optional)
4. Function body

Let’s understand all these by writing a simple function for driving test.

```python
def driving_test(name, age, car="Dezire"):
    if age >= 18:
        return f"{name} eligible for driving. You will be tested
          in {car}"
    else:
        return "Try again after few years 👶🍼"
```

Now that, we have created the function, we need to use the function in our program. We can do that by calling out the function name. This process is called function calling

```python
print(driving_test("John", 20, "Amaze"))
```

The above code will display the output of, 

*“John eligible for driving. You will be tested in Amaze”*

## Types of arguments in Functions

1. **Positional argument**
- In this type the arguments passed to the function are exactly in the order of how the parameter they are associated with is defined in the function
- For example, let’s see in the above function of `driving_test(name,age,car)`  what happens if we change the order in which we pass the arguments
    
    ```python
    print(driving_test( 20, "John", "Amaze"))
    ```
    
- This will throw an error for the type comparison statement as it tries to compare the equality of a string and integer.
1. **Keyword argument**
- In this type the arguments passed  to the function are labelled in the function call. By doing so, we can avoid the chaos that arise due to the changed order of arguments.
- This method ensures that no matter, which order you are giving the  argument to the function, they are interpreted correctly as they are intended to
- For example, let’s see the same scenario mentioned above with keyword argument.
    
    ```python
    print(driving_test( age=20, car="Amaze", name="John"))
    ```
    
- We can also use a combination of Positional as well as keyword argument.

> **Note:** Be sure to keep the order of their occurence as positional argument cannot appear after keyword argument
> 

## Tasks in Functions

Consider the following list of dictionaries.

```python
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

```

**Task 1: Add Book Function: Write a function `add_book(library, new_book)`**

```python
def add_book(library, book):
     library.append(book)

print(library_list)

book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}

add_book(library_list,book)
print(library_list)
```

**Task 2: Search Books by Author Function: Write a function `search_by_author(library, author_name)` which returns a list of books from a specified author that are in the library**

```python
def search_by_author(library, author_name):
     books = []
     for book in library:
          if book.get("author") == author_name:
               books.append(book)
     return books

print(search_by_author(library_list,"Mark Lutz"))
```

**Task 3: Check Out Book Function: Write a function `check_out_book(library, title)` that** 

- **Marks a book as not available if it exists in the library and also available, so that a user can check out**
- **Returns it is not available in the library if the book is unavailable**
- **Returns that the library doesn’t have that book if all the previous cases fails**

```python
def check_out_book(library, title):
     isBookExists = False
     for book in library:
          if book.get("title") == title:
            isBookExists = True
            if book.get("available") == True:
			           book["available"] = False
                 return f'{title} Book is available'
            else:
                 return f'{title} Book is not available'
     if isBookExists == False:
            return f'{title} book does not exist in our library'
               
print(check_out_book(library_list, "Automate the Boring Stuff with Python"))

print()

```

**Task 4: Calculate average rating in the following dictionaries**

```python
#Given Movies list with dictionaries inside 
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
```

```python
# The following function takes a movie's dictionary and returns its average rating
def avg_rating(movie):
     print(movie)
     ratings = movie.get("ratings")
     ratings = sum(ratings)/len(ratings)
     print(ratings)
     return ratings
 
 # The following function takes list of movies with each movie represented in a dicctionary and creates a new key "avg_ratings" and asssign the average rating with the help of the abive function
 def rate_movies(movies):
     print(movies)
     for movie in movies:
          movie["avg_ratings"] = avg_rating(movie)
  
 rate_movies(movies)
```

We can pass arbitrary arguments inside a function by defining the function with `*args` 

let’s see  how we can do that

```python
def own_max(a,*nums):
     max = a
     for num in nums:
          if num > max:
               max = num
     return max

print(own_max(1,3,4,5,77,90))
```

In this example, the `*nums` is the thing we talked about. It recieves all the additional parameters and encapsulates them into tuple

# Introduction to OOPS in Python

Object-Oriented-Programming shortly known as OOP is a type of programming paradigm that helps modeling our problems as real-world objects and assists in making meaningful solutions

In OOPs there are two things that we frequently come across:

1. Class
2. Objects

### Class:

Classes are the fundamental building blocks of OOPs which  provides a foundation upon which the objects can be built on

### Objects:

Objects are working are things that are built using the class and have various propeerties based on the classs and its own

Let’s say we’re going to implement OOP for cars

Every car has the following things:

1. Engine
2. Wheels
3. Make
4. Doors

If the car is called as  class, then these are the things that are known as properties of the  class. Let’s see how we can build a car with this information in our hand

```python
class Car: #Creating a class called car
	def __init__(self, name, engine, wheels, doors): #This is constructor function which is used for creating neew objects of this class.
			self.name = name
			self.engine = engine
			self.wheels = wheels
	    self.doors = doors
```

Now that we have blueprint for the Cars, let’s manufacture some cars by creating object for that Cars class.

```python
ferrari = Car("Ferrari","v8",4,2) # Whenever the cars function is called it invokes the  __init__ method in Car class which is called as constructor. The "self" in the Constructor is referring to the thing that is calling the constructor. In our case it is "ferrari"
alto = Car("Alto","v8",4,4)

print(ferrari.name, ferrari.wheels)
```