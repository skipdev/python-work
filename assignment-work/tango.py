#Display the message "Learn the steps of the 5 sequence tango."
print("Learn the steps of the 5 sequence tango.")

#defining the function
def tango():
  #Display the message "What step do you wish to learn?".
  print("What step do you wish to learn?")
  
  #Read in the user's response.
  step_number = int(input())
  
  
  #If the user's response is between 1 and 5, the appropriate step is displayed.
  #After every step, the user is asked whether they want to learn another step or not. (I just added this in because I had spare time)
  #If the user's response is anything else other than 1 - 5, then "Terminate the sequence." should be displayed.
  
  again = "Would you like to learn another step? (yes/no): "
  
  if step_number == 1:
    print("Leader takes a step back.")
    print()
    answer = input(again)
    if answer == "yes":
      tango()
  elif step_number == 2:
    print("Side step towards centre of the floor.")
    print()
    answer = input(again)
    if answer == "yes":
      tango()
  elif step_number == 3:
    print("Leader steps outside of follower.")
    print()
    answer = input(again)
    if answer == "yes":
      tango()
  elif step_number == 4:
    print("Preparation of the cross with the forward step.")
    print()
    answer = input(again)
    if answer == "yes":
      tango()
  elif step_number == 5:
    print("Leader closes his feet, follower completes cross step.")
    print()
    answer = input(again)
    if answer == "yes":
      tango()
  else:
    print("Terminate the sequence.")

tango()