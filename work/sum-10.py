count = 0
alist = []

#Asking the user to enter 10 numbers using a while loop
while count < 10:
  num = int(input("Please enter a number: "))
  alist.append(num)
  count = count + 1
  
#Prints the sum of the list of numbers
print(sum(alist))
