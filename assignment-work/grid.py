import functions

#The program should prompt the user to enter a word and choose one of four options.
def run():
  word = str(input("Please enter a word: "))
  print("Please pick an option (1 - 4) from the following:")
  print("1) Under - display the word with a line under it.")
  print("2) Over - display the word with a line over it.")
  print("3) Both - display the word in an underline and overline.")
  print("4) Grid - display the word in a grid that is n x n in size.")
  
  #This is a check to see if the input is valid.
  try:
    option = int(input())
    if option > 4 or option < 1:
      print("That number isn't an option")
      print()
      run()
  except:
    print("That's not a number.")
    print()
    run()
    
  print()
  
  #choosing the function based on the user's choice.
  if option == 1:
    functions.over(word)
  elif option == 2:
    functions.under(word)
  elif option == 3:
    functions.both(word)
  elif option == 4:
    #asking user for grid size
    grid_size = int(input("Please enter the 'n' value for the size of the grid (n x n): "))
    functions.grid(word, grid_size)
  else:
    run()
    
run()