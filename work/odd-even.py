#Asking for a whole number
number = (int(input("Please enter a whole number: ")))

#Is the number even or odd?
evenorodd = number % 2

#Display a message
if evenorodd == 0:
  print("The number is even")
else:
  print("The number is odd")
