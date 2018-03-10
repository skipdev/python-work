def jedi():
  #Display the message "Have you fear in your heart?"
  print("Have you fear in your heart?")
  
  #Read in the user’s string.
  response = input(str())
  
  #The program will then decide if the user can be a Jedi or not, based on their response.
  if response.lower() == "yes":
    print("Fear is the path to the dark side. You cannot be a Jedi apprentice.")
  elif response.lower() == "no":
    print("The force is strong in you. You may be a Jedi apprentice.")
  else:
    print("You need to decide... yes or no?")
    jedi()
    
jedi()