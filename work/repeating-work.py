#Get the user's name
name = str(input("Please enter your name: "))

#Find the number of characters in the name (x)
x = len(name)

#Use that number to print the name x amount of times
for count in range(x):
  print(name)