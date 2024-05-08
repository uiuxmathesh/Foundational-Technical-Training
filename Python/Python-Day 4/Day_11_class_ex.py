# Task 1: Create a Bank class with following attributes
# 1. Name
# 2. Account Number
# 3. Balance



# Task 3: Think all scenarios
# If there's sufficient balance proceed withdrawal and display amount
# If balance is not sufficient display error


class Bank:

    def __init__(self,name, acc_no, balance) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    # Task 2: Create a display_balance() method that displays the bank balance of each object created
    def display_balance(self):
        print( f"Your balance is ₹{self.balance: ,}" )

    # Task 3: Withdrawing. Think all scenarios
    # If there's sufficient balance proceed withdrawal and display amount
    # If balance is not sufficient display error
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient Balance')
        else:
            print(f"{amount:,} has been withdrawn from {self.name}'s account successfully")
            self.balance -= amount
        self.display_balance()

    # Task 4: Depositing
    # Add the amout specified in the holder's account
    def deposit(self, amount):
        if amount <= 0:
            print(f'Invalid Amount. Please enter a valid amount')
        self.balance += amount
        print(f"Successfully deposited ₹{amount:,} into {self.name}'s account")
        self.display_balance()

amisha = Bank("Amisha",20240508,50_000)
mathesh = Bank("Mathesh", 20240501,70_000)
saiGanesh = Bank("Sai Ganesh",20240506, 65_000)

# Testing
print(f'{amisha.name} {amisha.balance} {amisha.acc_no}')

#Using display_balance() function:

amisha.display_balance()

mathesh.withdraw(80000)

saiGanesh.deposit(4000)
