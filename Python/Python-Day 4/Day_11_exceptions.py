# Compile-time error (Syntax error)
# def math_divide(n1, n2):
#     try:
#         result = n1 / n2
#         return result

#     # Generic message
#     except:
#         return "Oops. 🤭 An Error happened"


# Errors
# 1. try
# 2. except
# 3. else
# # 4. finally
# def math_divide(n1, n2):
#     try:
#         result = n1 / n2

#     # Specific message
#     except ZeroDivisionError:
#         return "You cannot divide by zero! 💀"
#     else:
#         # When no error
#         print("Division was successful ✅")
#     finally:
#         # No matter
#         print("Operation done 😊✌️")

#     return result


# # Runtime error
# print(math_divide(10, 5))
# print(math_divide(10, 0))  # Execution stops
# print(math_divide(15, 3))

# # Handle error

# from datetime import datetime

# print(datetime.now().weekday())
# print(datetime.now().day)


# # # Calculate age & Handle errors
# # birth_year = input("Please provide your birth year: ")
# # age = 2024 - int(birth_year)
# # # print(f"Your age is {age}")
# # print(f"Your age is {2024 - int(birth_year)}")


# birth_year = input("Please provide your birth year: ")
# date = datetime.now().year
# print(date)


# def calc_age(birth_year):
#     currYear = datetime.now().year
#     try:
#         age = currYear - birth_year
#     except TypeError:
#         return f"Oops! Doesn't seems to be valid year"
#     else:
#         print(f"Here is your age! {age}")
#     finally:
#         return f"Some random final thing here"


# # Compile-time error (Syntax error)
# # def math_divide(n1, n2):
# #     try:
# #         result = n1 / n2
# #         return result

# #     # Generic message
# #     except:
# #         return "Oops. 🤭 An Error happened"


# # Errors
# # 1. try
# # 2. except
# # 3. else
# # 4. finally
# def divide_eggs(n1, n2):
#     try:
#         if n1 < 0:
#             raise ValueError("Eggs cannot be negative 🤭")
#         if n2 < 0:
#             raise ValueError("People cannot be negative 🤭")

#         # Code is shield 🛡️
#         result = n1 / n2

#     # Specific message
#     except ZeroDivisionError:
#         return "You cannot divide by zero! 💀"
#     except ValueError as e:
#         return f"Invalid number: {e}"
#     else:
#         # When no error
#         print("Division was successful ✅")
#     finally:
#         # No matter
#         print("Operation done 😊✌️")

#     return result


# # Runtime error
# print(divide_eggs(10, -5))
# print(divide_eggs(-10, 5))
# print(divide_eggs(10, 5))
# print(divide_eggs(10, 0))  # Execution stops
# print(divide_eggs(15, 3))

# # Handle error

# from datetime import datetime

# print(datetime.now().weekday())
# print(datetime.now().day)

from datetime import datetime
# Calculate age & Handle errors
def calculate_age():
    birth_year = input("Please provide your birth year: ")
    try:
        birth_year = int(birth_year)
        if birth_year > datetime.now().year:
            raise Exception(" Strictly, no one from future ⚠️")
        if birth_year < 0:
            raise Exception(" You are existing even before the Big Bang 😲")
        age = datetime.now().year - birth_year
        print(f'Your age is {age}')

    except ValueError:
        print(f"Invalid Argument: Year cannot be a String ❌")
    except Exception as e:
        print(f"Invalid Argument: {e}")
    finally:   
        return f"Operation Done 🫡"

print(calculate_age())