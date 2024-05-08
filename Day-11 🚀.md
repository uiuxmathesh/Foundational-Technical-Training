# Day-11 🚀

# Python Day-4 📆

Let’s continue with where we left off previously,

```python
class Car:
    def __init__(
        self, name, engine, wheels, doors
    ):  # creating object calls init (constructor)
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
    
    def horn(self):
        return f'{self.name} says Vroom Vroom'

ferrari = Car("Ferrari", "v8", 4, 2)  # object
alto = Car("Alto", "v4", 4, 4)  # object
```

In this, the `self.name` , `self.engine` , `self.wheels` , `self.doors`  are known as **Instance variable**

The good thing about classes are if we create a function inside a class, then all of the objectss can access that function. Which means, we’re writing one function that infinite number of objects of the class can make use of.

The functions that gets defined inside the classes are called methods.

In our example above, the `horn()` is the method which serves the purpose as the name says. Lol.

# Tasks on Classes and Objects

**Task 1: Create a Bank class with following attributes
1. Name
2. Account Number
3. Balance**

```python
class Bank:

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

amisha = Bank("Amisha",20240508,50_000)
mathesh = Bank("Mathesh", 20240501,70_000)
saiGanesh = Bank("Sai Ganesh",20240506, 65_000)

# Testing
print(f'{amisha.name} {amisha.balance} {amisha.acc_no}')
```

**Task 2: Create a display_balance() method that displays the bank balance of each object created**

```python
class Bank:

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    # Task 2: Create a display_balance() method that displays the bank balance of each object created
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )
        
amisha = Bank("Amisha",20240508,50_000)
mathesh = Bank("Mathesh", 20240501,70_000)
saiGanesh = Bank("Sai Ganesh",20240506, 65_000)

#Using display_balance() function:
amisha.display_balance()

```

**Task 3: Withdrawing. Think all scenarios  If there's sufficient balance proceed withdrawal and display amount. If balance is not sufficient display error and display amount**

```python
class Bank:

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    # Task 2: 
        print( f"Your balance is ₹{self.balance: ,}" )
        
    # Task 3: 
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()
        
amisha = Bank("Amisha",20240508,50_000)
mathesh = Bank("Mathesh", 20240501,70_000)
saiGanesh = Bank("Sai Ganesh",20240506, 65_000)

#Using display_balance() function:
amisha.display_balance()

#Using withdraw() function:
mathesh.withdraw(80000)
mathesh.withdraw(60000)
```

**Task 4: Depositing add the amout specified in the holder's account**

```python
class Bank:

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    # Task 2: 
        print( f"Your balance is ₹{self.balance: ,}" )
        
    # Task 3: 
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()
        
     # Task 4:
    def deposit(self, amount):
		    if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()
        
amisha = Bank("Amisha",20240508,50_000)
mathesh = Bank("Mathesh", 20240501,70_000)
saiGanesh = Bank("Sai Ganesh",20240506, 65_000)

#Using display_balance() function:
amisha.display_balance()

#Using withdraw() function:
mathesh.withdraw(80000)
mathesh.withdraw(6000)

#Using deposit function:
saiGanesh.deposit(4000)
```

## Understanding Class variable and Instance variable

In Classes the variables defined inside the classes are categorised into two types.

1. Class Variable
2. Instance Variable

### Instance variable

Instance variables are *unique to each instance of a class*. They are defined within methods and are prefixed with the `self` keyword. These variables store data that is specific to an instance, making them essential for object-oriented programming (OOP) principles like encapsulation.

In the Bank class example we discussed previously, the `name` ,`acc_no` ,`balance`  are all instance variable

### Class variable

Class variables are *shared among all instances of a class*. They are defined within the class but outside of any methods, typically near the top of the class definition. Class variables store data that is common to all instances, making them a powerful tool for managing shared state and settings.

Since we haven’t dealt with class variable yet let’s understand it by introducing the class variable in the previous example

```python
class Bank:
    #Class Variable
    interest_rate = 0.02

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

```

Here,  the `interest_rate` is a class variable because the interest rate is same for all the account holders. There’s no one in a bank having different interest rate than all others.

### More on Variable Types

[Class vs. Instance Variables in Python](https://medium.com/@pouyahallaj/class-vs-instance-variables-in-python-5573e71c99b5)

### Let’s dive into  tasks to manipulate class variables

**Task 5:  Write a method inside the `Bank` class so that it applies the interest to  the account holder. `apply_interest()`** 

```python

class Bank:
    #Class Variable
    interest_rate = 0.02

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

    def apply_interest(self):
        interest  = self.balance*Bank1.interest_rate
        self.balance += interest
        print(f"An annual interest of ₹{interest:,} is applied to your account.")
        print(self.display_balance())

Tonika = Bank("Tonika",20240508,50_000)
manasa = Bank("Manasa", 20240501,70_000)

manasa.apply_interest()
```

## Types of Methods in Classes

In python classes, the methods defined inside the function are broadly classified into three main types.

1. Instance Method
2. Class Method
3. Static Method

### Instance Methods

Instance methods are the most common type of methods in Python classes. They are associated with instances of a class and have access to both instance-specific data (attributes) and class-level data. Here’s an example of an instance method:

In our bank example, all the methods that we defined as of now are Instance method

### Class Methods

Class methods are defined using the `@classmethod` decorator. They are bound to the class and can access and modify class-level attributes. Class methods take the class itself as their first argument, typically named `cls` 

Let’s understand this by some examples

```python
class Circle:
    pi = 3.14
 
    def __init__(self, radius):
        self.radius = radius
 
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)
 
    def calculate_area(self):
        return Circle.pi * self.radius**2
        
circle_from_dia = Circle.from_diameter(10)
print(circle_from_dia.calculate_area())  # 78.5
```

Here, in this example if you see closely you can notice that `from_diameter()` is a Class method which takes two arguments `(cls, diameter)` . This particular method can be invoked by Saying `Circle.from_diameter()` and then you pass the diameter as a argument. You can ask that why we haven’t passed any arguments for `cls` parameter. It is because, just like the `self` keyword in *instance methods,* the `cls` keyword takes it value from class that calls it.

### Static Methods

Static methods are defined using the `@staticmethod` decorator. They do not have access to the instance or class state and are not bound to either. Static methods behave like regular functions but are scoped within the class for organization. Here's an example:

```python
class Circle:
    pi = 3.14
 
    def __init__(self, radius):
        self.radius = radius
 
    @staticmethod
    def perimeter(radius):
        return 2 * Circle.pi * radius
 
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)
 
    def calculate_area(self):
        return Circle.pi * self.radius**2
 
 
# Normal function but inside class | no access to self
print(Circle.perimeter(2))
 
# Instance method
circle1 = Circle(4)
print(circle1.calculate_area())
```

As you can see here `perimeter(radius)` is just like any other normal function which doesn’t have any self or cls keyword in its argument list. To access this method we don’t need any object at all. We can explicity call  the function with the class name like `Circle.perimeter()` and pass the  argument directly

### More on Method Types ⬇️

[Instance Methods, Static Methods, and Class Methods in Python: A Comprehensive Guide](https://medium.com/@avijit.bhattacharjee1996/instance-methods-static-methods-and-class-methods-in-python-a-comprehensive-guide-9163de3f4a47)

Let’s understand these concepts better by carrying out the following tasks

**Task 6: Create a method to get the total number of accounts that the bank has.**

```python
class Bank:
    interest_rate = 0.02
    total_accounts = 0 #Creating a Class Variable for storing no. of. acc. 

    @staticmethod
    def get_total_accounts(): #Writing a static method which does't take any arguments but returns, total no. of. acc. at present in the bank
        return Bank.total_accounts

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        Bank.total_accounts += 1 #Incrementing class variable total_accounts each time bank when the object is created.
    
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

    def apply_interest(self):
        interest  = self.balance*Bank1.interest_rate
        self.balance += interest
        print(f"An annual interest of ₹{interest:,} is applied to your account.")
        print(self.display_balance())

print(Bank.get_total_accounts())
Tonika = Bank("Tonika",128,1_00_000)
manasa = Bank("Manasa", 129,90_000)
print(Bank.get_total_accounts())
```

**Task 7: Writing a method to update the interest rate. Remeber interest rate is a class variable**

```python
class Bank:
    #Class Variable
    interest_rate = 0.02
    total_accounts = 0

    @staticmethod
    def get_total_accounts():
        return Bank.total_accounts

    @classmethod # Creating a class method which updates the class inteerest_rate of the class variable
    def update_interest(cls, x):
        cls.interest_rate = x

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        Bank.total_accounts += 1
    
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

    def apply_interest(self):
        interest  = self.balance*Bank1.interest_rate
        self.balance += interest
        print(f"An annual interest of ₹{interest:,} is applied to your account.")
        print(self.display_balance())

print(Bank.interest_rate)
Bank2.update_interest(0.3)
print(Bank.interest_rate)
```

# Access Specifiers

Access Specifiers are common in every  programming language. There are three acceess specifiers in Python

1. **Public** 
    
    All variables are by default defined as public.
    
2. **Private**
    
    We can make any variable private by giving two undrscores `_` before the variable name. 
    
    Example, `__variableName = value`
    
    The private variables can only be accessed with in the class it is defined.
    
3. **Protected**
    
    We can make any variable protected by giving single undrscore `_` before the variable name. 
    
    Example, `_variableName = value`
    
    The protected variables can only be accessed with in the class it is defined and those which inherits this class.
    

Variables and Methods with public access specifiers allows to be accessed anywhere with help of objects.

### **General rule of thumb:**

- Keep all the Class variable and Instance variable private
- Access Class variable and Instance variable via the methods in the class.

### More on Access Specifiers

[Access Modifiers and Name Mangling in Python](https://sahanlksk.medium.com/access-modifiers-and-name-mangling-in-python-3c732b894ca)

# Inheritance

# **What Is Inheritance?**

The method of inheriting the properties of parent class into a child class is known as inheritance. It is an OOP concept. The following are the benefits of inheritance.

1. Code reusability- we do not have to write the same code, again and again, we can just inherit the properties we need in a child class.
2. It represents a real-world relationship between parent class and child class.
3. It is transitive in nature. If a child class inherits properties from a parent class, then all other sub-classes of the child class will also inherit the properties of the parent class.

Below is a simple example of inheritance in Python.

```python
class Parent():
def first(self):
print('first function')class Child(Parent):
def second(self):
print('second function')ob= Child()
ob.first()
ob.second()
```

## **Sub-classing**

Calling a constructor of the parent class by mentioning the parent class name in the declaration of the child class is known as sub-classing. A child class identifies its parent class by sub-classing.

Let’s understand inheritance by doing tasks.

We know that each bank has atleast two types of account. Savings and Normal. The interest rate, transaction fee and other some features may differ from one another.

Now that we have a Bank class already create SavingsAccount and CurrentAccount classes which has to do the following:

### More on Inheritance ⬇️

[Inheritance In Python](https://medium.com/edureka/inheritance-in-python-eab5c0456b7)

**Task 7: SavingsAccount should have a interest_rate of 0.05**

```python
class Bank:
    #Class Variable
    interest_rate = 0.02
    total_accounts = 0

    @staticmethod
    def get_total_accounts():
        return Bank.total_accounts

    @classmethod # Creating a class method which updates the class inteerest_rate of the class variable
    def update_interest(cls, x):
        cls.interest_rate = x

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        Bank.total_accounts += 1
    
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

    def apply_interest(self):
        interest  = self.balance*Bank1.interest_rate
        self.balance += interest
        print(f"An annual interest of ₹{interest:,} is applied to your account.")
        print(self.display_balance())

class SavingsAccount(Bank):
    interest_rate = 0.05

sabesh = SavingsAccount("Sabesh", 131, 80_000)
sabesh.apply_interest()
sabesh.display_balance()
```

**Task 8: For every transaction in CurrentAccount a transaction of charge of 10 has to be debitted** 

```python
class Bank:
    #Class Variable
    interest_rate = 0.02
    total_accounts = 0

    @staticmethod
    def get_total_accounts():
        return Bank.total_accounts

    @classmethod # Creating a class method which updates the class inteerest_rate of the class variable
    def update_interest(cls, x):
        cls.interest_rate = x

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        Bank.total_accounts += 1
    
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

    def apply_interest(self):
        interest  = self.balance*Bank1.interest_rate
        self.balance += interest
        print(f"An annual interest of ₹{interest:,} is applied to your account.")
        print(self.display_balance())

class SavingsAccount(Bank):
    interest_rate = 0.05

class CurrAccount(Bank):
    transaction_Fee = 10
    def withdraw(self, amount):
        return super().withdraw(amount+self.transaction_Fee)
 
 
sabesh = SavingsAccount("Sabesh", 131, 80_000)
sabesh.apply_interest()
sabesh.display_balance()

tanishq = CurrAccount("Tanishq", 134, 90_000)
tanishq.withdraw(1000)
tanishq.withdraw(10000)
tanishq.display_balance()
```

# Magic Methods

Magic methods in python also know as *Dunder Methods* or *Special Methods* are predefined methods in python that have double underscores (or “dunders”) at the beginning and end of their names. These methods specific behaviours for built-in operations or funcitonalitites in Python. By implementing Dunder methods, you can customize the behaviour of your objects and make them work seamlessly with python’s language comstructs

More on **Dunder or Magic  Methods ⬇️**

[Dunder methods in Python, really crazy functions](https://nitesh-yadav.medium.com/dunder-methods-in-python-really-crazy-functions-3455ecb6472d)

Here are some examples of using built-in ‘Dunder methods’ in python

### Example 1:

Let’s  see the `Cat` class and manipulating `Dunder` operations inside a class. 

In this program we have a cat class and two instances of that class `pichu` ,`snowbell` .   If we try to print `pichu`  it  prints a weird and random string which can be anything but not human readable.

```python
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
 
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
```

So, if you want to `print(pichu)` and doesn’t want to get that weird output, then you need to override the `__str__` method so that it returns something meaningful.

The reason we’re overriding `__str__` method is because, this method returns a string representation of the object and is invoked by the built-in `str()` function or when an object is printed. It provides a human-readable representation of the object.

Let’s see how we can change them so that returns something meaningfull

```python
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
```

Now if you do the same thing there will be a awesome message displayed to you. 

### Example 2:

Let’s take same example. this time we also need  to print the representation of object with   `repr()` . 

```python
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu)
```

If we do this, again we’ll be getting a weird text. Let’s fix that.  This time we know which method to modify. Obviously `__repr__` it is. Let’s do that.

```python
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
        
    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"
 
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu)
```

Now we have again got a nice string.

> **Note:** `__repr__` method is primarily used for debugging
> 

### Example 3:

For one final time let’s use the same Cat class. This time we want to add the two objects `pichu` ,`snowbell`

```python
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
 
    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"
 
 
    # Polymorphism:  Method overriding
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu + snowbell)
```

This time instead of a human readable text we get a error saying unable to add the two objects

To address this issue we might need to overwrite the `__add__` method which is responsible for adding two objects. Let’s do that.

```python
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
 
    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"
 
    def __add__(self, other):
        return self.__speed + other.__speed
 
    # Polymorphism:  Method overriding
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu + snowbell)
```

# Module Imports

Import the module by using the `import` statement:

```python
import mymodule
```

if you want to import a particular method or class from a module you can use `from` 

```python
from mymodule import myFunction
```

You can also *alias* the module during import

```python
from mymodule import myFunction as func
```

To import  a module that exists in a different file let say *components,* then you can use

```python
from components.mymodule import myFunction
```

# Exception Handling

Exception handling in Python is a process of resolving errors that occur in a program. This involves catching exceptions, understanding what caused them, and then responding accordingly. Exceptions are errors that occur at runtime when the program is being executed. They are usually caused by invalid user input or code that is invalid in Python. Exception handling allows the program to continue to execute even if an error occurs.

General syntax

```python
try:
   # code that may cause an exception
except ExceptionType as e:
   # code to handle the exception
else:
   # code to execute if no exceptions were raised
finally:
   # code that will always be executed, regardless of exceptions

```

Let’s see some example

**Example 1**

```python
def math_divide(n1, n2):
    try:
        result = n1 / n2

    # Specific message
    except ZeroDivisionError:
        return "You cannot divide by zero! 💀"
    else:
        # When no error
        print("Division was successful ✅")
    finally:
        # No matter
        print("Operation done 😊✌️")

    return result

# Runtime error
print(math_divide(10, 5))
print(math_divide(10, 0))  # Execution stops
print(math_divide(15, 3))
```

> **Note:** We can also generate errors under certain conditions by writing the error in `raise` statement
> 

Example 2:

```python
def divide_eggs(n1, n2):
    try:
        if n1 < 0:
            raise ValueError("Eggs cannot be negative 🤭")
        if n2 < 0:
            raise ValueError("People cannot be negative 🤭")

        # Code is shield 🛡️
        result = n1 / n2

    # Specific message
    except ZeroDivisionError:
        return "You cannot divide by zero! 💀"
    except ValueError as e:
        return f"Invalid number: {e}"
    else:
        # When no error
        print("Division was successful ✅")
    finally:
        # No matter
        print("Operation done 😊✌️")

    return result

# Runtime error
print(divide_eggs(10, -5))
print(divide_eggs(-10, 5))
print(divide_eggs(10, 5))
print(divide_eggs(10, 0))  # Execution stops
print(divide_eggs(15, 3))
```