#Stan wishes to create a program that presents the user with two options; "[1] Identify" or "[2] Quit". If the user enters 1 then the program should ask the user to enter a number. The program should then display a message to indicate if the number entered by the user is even or odd. The program should then present the two options to the user again. This sequence should be repeated until the user types 2 (i.e. quits) when presented with the options.

def ask():
  option = (input("Would you like to '[1] Identify' or '[2] Quit'? "))
  if option == "1":
    even_odd()
  elif option == "2":
    print()
  else:
    ask()
    
    
def even_odd():
  number = int(input("Please enter a number: "))
  evenorodd = number % 2
  if evenorodd == 0:
    print("The number is even")
    print()
  else:
    print("The number is odd")
    print()
  ask()
  
ask()
  