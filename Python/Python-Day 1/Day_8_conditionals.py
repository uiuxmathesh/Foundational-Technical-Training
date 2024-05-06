name1,name2 = input(f'What is first guy\'s name? '),input(f'What is second guy\'s name? ')
height1,height2 = int(input(f'What is {name1}\'s height?  ')),int(input(f'what is {name2}\'s height? '))
if height1 > height2:
  print(f'{name1} is taller than {name2}')
else:
  print(f'{name2} is taller than {name1}')