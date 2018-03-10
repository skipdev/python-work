#Display the message "Welcome to the Planet of the Apes…". 
print("Welcome to the Planet of the Apes...")

#Set counters to see how many humans and apes were encountered
ape_count = 0
human_count = 0

#Do the following 7 times using a loop: 
x = 0
while x < 7:

  
  #Display the message "…be ye human or be ye ape?"and read in the user's response.
  print("...be ye human or be ye ape?")
  species = str(input())
  
  #If the user's response is "Human" then add 1 to a total representing the number of times a human was encountered. Display the message "I did not start this war. But I will finish it."
  if species == "human":
    human_count = human_count + 1
    print("I did not start this war. But I will finish it.")
       
  #If the user’s response is "Ape" then add 1 to a total representing the number of times an ape was encountered and display the message "Apes together strong!" 
  elif species == "ape":
    ape_count = ape_count + 1
    print("Apes together strong!")
    
  #If the user’s response is anything else then the program should display the message "This is not your fight." 
  else:
    print("This is not your fight.")
    
  print()
  x = x + 1
    
    
#At the end the program should display the total number of times Caesar encountered humans and apes.:
print("Total humans encountered: ", human_count)
print("Total apes encountered: ", ape_count)