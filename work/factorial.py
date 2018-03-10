#Stan wishes to create a program that can work out the factorial of a number specified by the user.

#Get a number from the user
num = int(input("Please enter a number: "))

#Create a loop that prints each number, -1 each time
factorial = 1

for x in range(1, num + 1):
  factorial = x * factorial
  
print(factorial)
  