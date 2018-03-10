x = 0

#Prompt the user to enter a whole number representing the total number of friends.
friends = int(input("How many friends do you have now? "))

#Display the message "Displaying friends...". 
print("Displaying friends...")

#Display ":-)" (smiley face as text) for each friend so that the number of smiley faces displayed is equivalent to the user’s whole number
while x < friends:
  print(":-)")
  x = x + 1