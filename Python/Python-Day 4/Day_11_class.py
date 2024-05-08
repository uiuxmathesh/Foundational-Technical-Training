# Idea
# Object Oriented Programming
# Modeling our problem as real-world objects
 
# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors
 
 
#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2
 
 
# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4
 
 
#  Car -> blueprint | Class blueprint object
 
 
# Class should start with capital letter
class Car:
    def __init__(self, name, engine, wheels, doors):
        # creating object calls init (constructor)
        # instance variable - self
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
 
    # instance method
    def horn(self):
        return f"{self.name} says Vroom Vroom!!!"
 
 
ferrari = Car("Ferrari", "v8", 4, 2)  # object (instance)
alto = Car("Alto", "v4", 4, 4)  # object
 
# print(ferrari["name"]) # ❌ error
print(type(ferrari), type("cool"))  # <class '__main__.Car'> <class 'str'>
print(ferrari.name, ferrari.wheels)
 
print(ferrari.horn())
print(alto.horn())
 
 
# Task 1
# Bank Account
# 1. acc_no
# 2. name
# 3. balance
 
 
class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
 
    def display_balance(self):
        return f"Your balance is: ₹{self.balance:,}"
 
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
 
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"
 
 
# Object / Instance -> Bank (class)
amisha = Bank(123, "Amisha", 50_000)
mathesh = Bank(124, "Mathesh", 70_000)
sai_ganesh = Bank(125, "Sai ganesh", 65_000)
 
 
print(amisha.name)
 
# Task 2
print(amisha.display_balance())  # Your balance is: ₹50,000
print(mathesh.display_balance())
print(sai_ganesh.display_balance())
 
 
# Task 3 - Tricky | Clue: Think all scenarios
print(mathesh.withdraw(10_000))  # Success. Your balance is: ₹60,000
print(mathesh.display_balance())  # Your balance is: ₹60,000
print(mathesh.withdraw(90_000))
 
# Task 4
print(sai_ganesh.deposit(10_000))  # Success. Your balance is: ₹75,000
print(sai_ganesh.display_balance())  # Your balance is: ₹75,000
 
 
# Encapsulation: properties + action (logic) + access
class Bank1:
    # Class variable | All your instance share the class variable
    interest_rate = 0.02
 
    def __init__(self, acc_no, name, balance):
        # instance variable
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
 
    def display_balance(self):
        return f"Your balance is: ₹{self.balance:,}"
 
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
 
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"
 
    def apply_interest(self):
        accumulated_interest_amt = self.balance * Bank1.interest_rate
        self.balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"
 
 
tonika = Bank1(126, "Tonika", 1_50_000)
manasa = Bank1(127, "Manasa", 80_000)
 
print(Bank1.interest_rate)
 
# Task 4
# After 1 year
tonika.apply_interest()
manasa.apply_interest()
 
print(tonika.display_balance())
print(manasa.display_balance())
 
 
# @staticmethod vs @classmethod | Both decorators
# super charge to the normal method
# @staticmethod
# Normal function
 
# @classmethod
 
 
# perimeter  2 * pi * r
 
 
class Circle:
    # class variable | common methods across instance
    pi = 3.14
 
    def __init__(self, radius):
        self.radius = radius
 
    # staticmethod -> no cls, self | normal function
    @staticmethod
    def perimeter(radius):
        return 2 * Circle.pi * radius
 
    # Common methods across instance | modify the class variable
    @classmethod
    def from_diameter(cls, diameter):
        # to construct the object
        radius = diameter / 2
        # print(cls.pi)
        return cls(radius)
 
    def calculate_area(self):
        return Circle.pi * self.radius**2
 
 
# Normal function but inside class | no access to self
print(Circle.perimeter(2))
 
# Instance method
circle1 = Circle(4)
print(circle1.calculate_area())
 
 
# Class method - to construct the object
circle_from_dia = Circle.from_diameter(10)  # 10 -> dia
print(circle_from_dia.calculate_area())  # 78.5
 
 
# get_total_no_accounts(), update_interest_rate()
 
 
class Bank2:
    # Class variable | All your instance share the class variable
    interest_rate = 0.02
    no_of_accounts = 0
 
    def __init__(self, acc_no, name, balance):
        # instance variable
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        Bank2.no_of_accounts += 1
 
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank2.no_of_accounts} accounts"
 
    @classmethod
    def update_interest_rate(cls, new_interest_rate):
        cls.interest_rate = new_interest_rate
 
    def display_balance(self):
        return f"Your balance is: ₹{self.balance:,}"
 
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
 
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"
 
    def apply_interest(self):
        accumulated_interest_amt = self.balance * Bank2.interest_rate
        self.balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"
 
 
sneha = Bank2(128, "Sneha", 1_00_000)
siva = Bank2(129, "Siva", 90_000)
 
 
# print(Bank2.get_total_no_accounts())
Bank2.update_interest_rate(0.10)
 
print(sneha.apply_interest())
print(sneha.display_balance())  # 110,000
print(Bank2.get_total_no_accounts())
 
 
class Bank3:
    # Class variable | All your instance share the class variable
    __interest_rate = 0.02
    __no_of_accounts = 0
 
    def __init__(self, acc_no, name, balance):
        # instance variable
        self.__acc_no = acc_no
        self.__name = name
        self.__balance = balance
        Bank3.__no_of_accounts += 1
 
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank3.__no_of_accounts} accounts"
 
    @classmethod
    def update_interest_rate(cls, new_interest_rate):
        cls.__interest_rate = new_interest_rate
 
    def display_balance(self):
        return f"Your balance is: ₹{self.__balance:,}"
 
    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
 
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"
 
    def apply_interest(self):
        accumulated_interest_amt = self.__balance * Bank3.__interest_rate
        self.__balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"
 
 
divya = Bank3(130, "Divya", 1_00_000)
priya = Bank3(131, "Priya", 90_000)
 
 
# divya.__balance = -800000  # should not be allowed ❌
 
# private
# print(divya.__balance)  # internal usage
 
 
print(divya.apply_interest())
print(divya.display_balance())
# Access specifiers
 
# 1. Private    -> __balance (double underscore)
# 2. Protected  -> _balance  (single underscore)
# 3. Public     -> balance   (no underscore)
 
 
# Conventions
 
# 1. Privatize all instance & class variables
# 2. Access to instance & class variable - through - public - methods
 
 
# Inheritance
class Animal:
    def __init__(self, name):
        self._name = name
 
    # methods / attributes
    def speak(self):
        return "Some sound"
 
 
class Dog(Animal):
    def __init__(self, name, speed):
        super().__init__(name)  # Base class constructor
        self.__speed = speed
 
    def run(self):
        return "🐶 wags tail!!"
 
    # Polymorphism:  Method overriding
    def speak(self):
        return "Woof!! 🐕"
 
    def speed_bonus(self):
        return f"{self._name} is running at {self.__speed * 2}Km/hr"
 
 
toby = Animal("toby")
print(toby.speak())
# print(toby.run())
 
maxy = Dog("maxy", 20)
# print(maxy._name)
print(maxy.run())
print(maxy.speak())
# print(maxy.__speed)
print(maxy.speed_bonus())
 
 
class Bank4:
    # Class variable | All your instance share the class variable
    _interest_rate = 0.02
    __no_of_accounts = 0
 
    def __init__(self, acc_no, name, balance):
        # instance variable
        self.__acc_no = acc_no
        self.__name = name
        self._balance = balance
        Bank4.__no_of_accounts += 1
 
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank4.__no_of_accounts} accounts"
 
    @classmethod
    def update_interest_rate(cls, new_interest_rate):
        cls._interest_rate = new_interest_rate
 
    def display_balance(self):
        return f"Your balance is: ₹{self._balance:,}"
 
    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
 
    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"
 
    def apply_interest(self):
        accumulated_interest_amt = self._balance * self._interest_rate
        self._balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"
 
 
# SavingsAccount -  interest_rate -> 0.05
# Task  5
# class SavingsAccount(Bank4):
#     _interest_rate = 0.05
 
#     # method overriding
#     def apply_interest(self):
#         accumulated_interest_amt = self._balance * SavingsAccount._interest_rate
#         self._balance += accumulated_interest_amt
#         return f"Interest received. ₹{accumulated_interest_amt}"
 
 
class SavingsAccount(Bank4):
    _interest_rate = 0.05
 
 
sabesh = SavingsAccount(131, "Sabesh", 80_000)
priya = Bank3(131, "Priya", 1_00_000)
 
 
print(sabesh.apply_interest())  # 5%
print(sabesh.display_balance())
 
print(priya.apply_interest())  # 2%
print(priya.display_balance())
 
 
# # Task 6
# # withdraw - per_transaction_fee - 10 Rupee
class CurrentAccount(Bank4):
    per_transaction_fee = 10
 
    # Polymorphism: method overloading
    def withdraw(self, amount):
        total_amount = amount + CurrentAccount.per_transaction_fee
        return super().withdraw(total_amount)
 
 
tanishq = CurrentAccount(132, "Tanishq", 90_000)
 
print(tanishq.withdraw(1_000))
print(tanishq.withdraw(10_000))
print(tanishq.display_balance())
 
# common across objects - class variable  (cls)         - no. of eyes
# unique across objects - instance variable (self)      - size of nose