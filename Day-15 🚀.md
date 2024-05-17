# Day-15 🚀

# Abstraction in Python

The interface or abstract classes are a methodology to force the devs to implement something. 

Abstract classes will have only the required methods (obviously it won’t be imlemented). Theses methods will be implemented by the classes inheriting it.

It is like, if you inherit your father, you should show the similarities with  your father. Makes absolutely no sense right.

Let’s see an example. (The animal example, as we have did before)

```python
#Base class
class Animal:
	
	def make_sound(self):
			pass
			
#Child class	
class Dog(Animal):

	def run():
			print("Runnnnnn.....")
			

maxy = Dog()
maxy.run()
```

Here you can see  the base class in `Animal` and the child class in `Dog` . The base class have a method which is not defined yet. This is because, each animal has its own way of sounding. So it is better leave this to the child class. But there’s no rule that forces the child class to implement the method. This is where abstract classes comes into game.

To make a class abstract in python we need to import a package called `abc` (abstract base classses)

> Python for godsake doesn’t support abstraction by default.
> 

```python
from abc import ABC, abstractmethod
```

Then let’s make `Animal` class abstract

```python
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
    @abstractmethod
    def move(self):
        pass
 
 
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
 
    def move(self):
        print("Runnning... 🐕")
 
    def jump(self):
        print("Jumps 🦘")
 
 
maxy = Dog()
maxy.move()

```

Now the `Animal` class is abstract. The child class `dog`must implement every methods because, it’s gonna error up if it doesn’t implement

> Include the decorator @abstractmethod before every abstract methods in Abstract classes to make it abstract..
> 

# File handling Python

Python is capable of handling vast varieties of file. Some major file types that usually comes up are

- JSON
- CSV
- xlsx

### JSON (Javascript Object Notation):

Why we need JSON?

Any Application we use, has three layers. Frontend, Backend, Database. 

In frontend, Javascript request data needed to Backend. The backend forwards the  request to database. once after fetching records that satisfies the request it gives the records to the backend which in turn gives it as a response to the frontend’s request.

working with JSONs in Python

```python
import json #package for JSON related operations

json.dumps() #method to convert any dictionary into JSON

json.loads() #method to convert any JSON into dictionary
```

### CSV Comma Separated Values

CSVs are very popular file format used majorly in AI ML datasets

```python
import csv
csv.reader(<filename>) #Instantiates a reader object for csv file given
csv.writer(<filename>) #Instantiates a writer object for csv file given
```

### File operations

File operations in python can be done with the help of `open`  method

```python
with open(<filename>,mode,additionalArgs):
		# Your file operation here
```

The usage of `with`  ensures the auto  closing of filess once the opertion intended is done.

# Testing

## Need for testing

### Types of Testing

- Stress Testing
- Perfomance Testing
- Load Testing
- Resilient
- Regression

### Categories of Testing

![Untitled](Day-15%20%F0%9F%9A%80%202b8c7efdf7ee4b28884c9bf95ed4da7d/Untitled.png)

## Writing Tests

- Importing PyUnit package

```python
import unittest
```

- Writing a class and  Inheriting Testcase class from unittest

```python
class TestMyModule(unittest.TestCase):
```

- After this  we need to write methods to do testing. Keep in mind each method should have the word test in their name.

```python
class TestMyModule(unittest.TestCase):
	def test_add(self):
			self.assertEqual(add(1,1),2)
```