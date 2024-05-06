# Given a number n make a pascal triangle with  ✨ 

n = int(input())

i = 1
while i <= n:
    print("✨" * i)
    i += 1

for i in range(1,n+1):
    print('✨'*i)

player_stats = [10,20,30]

for i in range(len(player_stats)):
    player_stats[i] *=2

print(player_stats)

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
 
 
# Output
# [4, 8, 11, 15, 10, 4]
 

# Task 4.1 - for loop
name_length = []
for hero in avengers:
   name_length.append(len(hero))

print(name_length)


# Task 4.2 - List comprehension
name_length2 = [len(hero)  for  hero in avengers]

print(name_length2)

# Task 5.1 - Storing the hero names with more than 10 character using typical for loop
big_names = [ ]
for hero in avengers:
   if(len(hero)>10):
       big_names.append(hero.upper())

print(big_names)

# Task 5.2- Storing the hero names with more than 10 character using list comprehension
big_names2 = [hero for  hero in avengers if len(hero)>10]

print(big_names2)