# stock1 = 'vanilla'
# stock2 = 'lime'
# stock3 = 'chocolate'

# # favFlavour = input('Enter your favourite flavour:')
# if(favFlavour == stock1):
#   print('Yes we do have it')
# elif(favFlavour == stock2):
#   print('Yes we do have it')
# elif(favFlavour == stock3):
#   print('Yes we do have it')
# else:
#   print('No, we ran out of stock')

# After the 🔑

# message = "    🚨🔍📱🔑secret_code✌️"

# code = "SECRET_CODE✌️"

message = "    🚨🔍📱🔑******secret_code✌️((((("
code = "SECRET_CODE✌️"

message = message[message.find('🔑')+1:]
message = message.upper()
message = message.strip('*').strip('(')
print(message)
if(message==code):
  print('You are an hacker')
else:
  print('Try Again')
