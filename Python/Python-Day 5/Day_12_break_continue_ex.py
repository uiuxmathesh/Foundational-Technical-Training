# break -> stop loop
# continue -> skip one iteration
# return -> exits out of function
 
 
def print_nums():
    for num in range(1, 10):
        if num == 6:
            break
 
        print(num)
    print("Execution continues 🎊")
 
 
def skip_even():
    for num in range(1, 10):
        if num % 2 == 0:
            continue
        print(num)
    print("Execution continues 🎊")
 
 
# Task 1: Find the first negative value
def first_negative(numbers):
    # Your students will fill this in
    result = "No negative numbers is in the list"
    for num in numbers:
        if num < 0:
            result = f"The first negative number is {num}"
            break
    return result        
 
if __name__ == "__main__":
    # print_nums()
    # skip_even()
    # Test case
    print(first_negative([3, 5, 7, -1, 9, -3]))



def process_until_duplicate(fruits):
    fruitSet = set()
    for fruit in fruits:
        if fruit in fruitSet:
            print(f"Already Processed {fruit}")
            break

        else:
            fruitSet.add(fruit)
            print(f"processed {fruit}")

 
 
if __name__ == "__main__":
    # print_nums()
    # skip_even()
    # Test case
    # print(first_negative([3, 5, 7, -1, 9, -3]))  # -1
    process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])



# Task 3:
 
def censorship_bot(messages:str, banned_words):
    censored_messages = []
    x,y = banned_words
    for message in messages:
        message = message.split()
        if x in message or y in message:
            continue
        
        message = " ".join(message)
        censored_messages.append(message)
    
    return censored_messages

 
messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!",
    "Tumbad is a nice movie"
]
 
banned_words = ["bad", "oops"]

print(censorship_bot(messages, banned_words))
 
 
 
# Expected output
# Approved message: Hello everyone!
# Approved message: Let's keep our chat clean!
# Approved message: Have a nice day!
 