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

tiago = Car("Tiago","v4",4,4)
punch = Car("Punch","v8",4,4)


print(ferrari.name, ferrari.wheels)
print(tiago.name, tiago.wheels)

print(tiago.horn())
