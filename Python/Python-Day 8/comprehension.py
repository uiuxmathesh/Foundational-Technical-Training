# from pprint import pprint as print
# words = ["This", "is", "cool", "mangoes", "oranges", "apple"]
# # len_words = {len(word) for word in words}


# # print(len_words)

# # Task 2
# classes = {
#     "Class A": [
#         {"name": "Alice", "grades": [82, 90, 88]},
#         {"name": "Bob", "grades": [78, 81, 86]},
#         {"name": "Charlie", "grades": [85, 85, 87]},
#         {"name": "Alex", "grades": [85, 90, 87]},
#     ],
#     "Class B": [
#         {"name": "Dave", "grades": [92, 93, 88]},
#         {"name": "Eve", "grades": [76, 88, 91]},
#         {"name": "Frank", "grades": [88, 90, 92]},
#     ],
# }
 
# result = {}
# output = {}
# for class_name,students in classes.items(): 
    
#     guys_result = {}
#     for student in students:
#         value  = round(sum(student['grades'])/len(student['grades']),2)
#         key = student['name']
#         guys_result[key] = value
    
#     output[class_name] = guys_result
#     avg_marks = [value for value in guys_result.values()]
#     result[class_name] = round(sum(avg_marks)/len(avg_marks),2)

# print(result)
# print(result)


# for class_name,students in classes.items():

#     # print(student.items() for student in students)
#     guys_result = { key[0][1]: sum(values[1][1]) for key,values in (student.items() for student in students) }



        






#     # for student in section:
#     #     name = student.get('name')
#     #     grades = student.get('grades')
#     #     print(name)
#     #     print(grades)

# # Task 1: Find average of each student
# # output = {
# #     "Class A": {"Alice": 90.50, "Bob": 84.50, "Charlie": 90.00},
# #     "Class B": {"Dave": 92.50, "Eve": 86.50, "Frank": 950},
# # }


marks = [50, 40, 20, 90]

if 40 < all(marks):
    print('Yes they will get a grade')
    
else:
    print('No they will not get a grade')
 