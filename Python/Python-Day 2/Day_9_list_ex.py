scrambled_message = "world the save to time no is There"
scrambled_message = scrambled_message.split(" ")
scrambled_message = scrambled_message[::-1]

print(scrambled_message)

unscrambled_message = " ".join(scrambled_message)
print(unscrambled_message)
