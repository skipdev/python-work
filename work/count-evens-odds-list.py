#Asking the user for three numbers
first = float(input("Please enter your first number: "))
second = float(input("Please enter your second number: "))
third = float(input("Please enter your third number: "))

#set the count for odd and even numbers
oddcount = 0
evencount = 0

#put numbers into a list
alist = []
alist.append(first)
alist.append(second)
alist.append(third)

#go through each number in the list
#add one to evencount if the number is even, and vice versa
for x in alist:
  if (x % 2) == 0:
    evencount = evencount + 1
  else:
    oddcount = oddcount + 1

#print the results
print()
if evencount == 2:
  print("There are" , evencount , "even numbers")
  print("There is" , oddcount , "odd number")
else:
  print("There is" , evencount , "even number")
  print("There are" , oddcount , "odd numbers")