x = 0
wolfcount = 0

#Display the message "Little Red Riding Hood goes into the woods..."
print("Little Red Riding Hood goes into the woods...")



#Do this 4 times:
while x < 4:
  
  #Display the message "Walking in the woods, who did I see?"
  print("Walking in the woods, who did I see?")
  
  #Read in the user's response.
  who = str(input())
  
  #If the user enters "The Big Bad Wolf" then the program should remember the number of times the wolf was seen
  if who == "The Big Bad Wolf":
    wolfcount = wolfcount + 1
    
  #Repeat the user's response followed by the message "looking at me!"
  print(who , "looking at me!")
  
  print()
  x = x + 1
  
  
  
#Display the message "I saw the wolf" followed by the number of times the wolf was seen and then followed by the message "times".
print("I saw the wolf" , wolfcount , "times")
