# print('Hello, 🌏')
# # Task-1: Fahrenheit to celsius

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('The equivalent of ' + str(fahrenheit) + '°F is ' + str(celsius) + '°C')

# # Task-2: Given the birth year should calculate the age.

birth_year = int(input("Enter your birth year: "))
age = 2024-birth_year
print('Your age is ' + str(age))

#Task-3: Area of the circle given radius

radius = int(input('Enter the radius: '))
area =  (22/7)*(radius**2)
print(f'The area of the circle is {area}')

#Task-4: Build a loader

percent = int(input('Enter loader value:'))
loaderValue = percent//10
remainingValue = 10-loaderValue
print(f'[{"="*loaderValue}{" "*(10-loaderValue)}]{percent}%')