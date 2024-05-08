# Task 1: Create a Bank class with following attributes
# 1. Name
# 2. Account Number
# 3. Balance



# Task 3: Think all scenarios
# If there's sufficient balance proceed withdrawal and display amount
# If balance is not sufficient display error


# class Bank:

#     def __init__(self,name, acc_no, balance) -> None:
#         self.name = name
#         self.acc_no = acc_no
#         self.balance = balance
    
#     # Task 2: Create a display_balance() method that displays the bank balance of each object created
#     def display_balance(self):
#         print( f"Your balance is ₹{self.balance: ,}" )

#     # Task 3: Withdrawing. Think all scenarios
#     # If there's sufficient balance proceed withdrawal and display amount
#     # If balance is not sufficient display error
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f'Insufficient Balance')
#         else:
#             print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
#             self.balance -= amount
#         self.display_balance()

#     # Task 4: Depositing
#     # Add the amout specified in the holder's account
#     def deposit(self, amount):
#         if amount <= 0:
#             print(f'Invalid Amount. Please enter a valid amount')
#         self.balance += amount
#         print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
#         self.display_balance()

# amisha = Bank("Amisha",20240508,50_000)
# mathesh = Bank("Mathesh", 20240501,70_000)
# saiGanesh = Bank("Sai Ganesh",20240506, 65_000)

# # Testing
# print(f'{amisha.name} {amisha.balance} {amisha.acc_no}')

# #Using display_balance() function:

# amisha.display_balance()

# mathesh.withdraw(80000)

# saiGanesh.deposit(4000)


# class Bank1:
#     #Class Variable
#     interest_rate = 0.02

#     def __init__(self,name, acc_no, balance) -> None:
#         self.name = name
#         self.acc_no = acc_no
#         self.balance = balance
    
#     def display_balance(self):
#         print( f"Your balance is ₹{self.balance: ,}" )

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f'Insufficient Balance')
#         else:
#             print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
#             self.balance -= amount
#         self.display_balance()

#     def deposit(self, amount):
#         if amount <= 0:
#             print(f'Invalid Amount. Please enter a valid amount')
#         self.balance += amount
#         print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
#         self.display_balance()

#     def apply_interest(self):
#         interest  = self.balance*Bank1.interest_rate
#         self.balance += interest
#         print(f"An annual interest of ₹{interest:,} is applied to your account.")
#         print(self.display_balance())

# Tonika = Bank1("Tonika",20240508,50_000)
# manasa = Bank1("Manasa", 20240501,70_000)

# manasa.apply_interest()


# class Circle:
#     pi = 3.14
 
#     def __init__(self, radius):
#         self.radius = radius
 
#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius
 
#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter/2
#         return cls(radius)
 
#     def calculate_area(self):
#         return Circle.pi * self.radius**2
 
 
# # Normal function but inside class | no access to self
# print(Circle.perimeter(2))
 
# # Instance method
# circle1 = Circle(4)
# print(circle1.calculate_area())
 
# Circle.pi = 0
# # Class method - to construct the object
# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())  # 78.5

# print(Circle.pi)



class Bank:
    #Class Variable
    interest_rate = 0.02
    total_accounts = 0

    @staticmethod
    def get_total_accounts():
        return Bank.total_accounts

    @classmethod
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
        interest  = self.balance*self.interest_rate
        self.balance += interest
        print(f"An annual interest of ₹{interest:,} is applied to your account.")
        print(self.display_balance())


print(Bank.get_total_accounts())
Tonika = Bank("Tonika",128,1_00_000)
manasa = Bank("Manasa", 129,90_000)
print(Bank.get_total_accounts())


print(Bank.interest_rate)

Bank.update_interest(0.3)

print(Bank.interest_rate)




class SavingsAccount(Bank):
    interest_rate = 0.05

class CurrAccount(Bank):
    transaction_Fee = 10
    def withdraw(self, amount):
        return super().withdraw(amount+self.transaction_Fee)


sabesh = SavingsAccount("Sabesh", 131, 80_000)
tanishq = CurrAccount("Tanishq", 134, 90_000)

sabesh.apply_interest()
sabesh.display_balance()

tanishq.withdraw(1000)
tanishq.withdraw(10000)
tanishq.display_balance()
