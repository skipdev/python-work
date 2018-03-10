#Declare a variable representing health with a value of 100.
health = 100

#Display the message "Your health is 100%. Escape is in progress...". 
print("Your health is 100%. Escape is in progress...")
    
#Do the following 5 times using a loop: 
x = 0
while x < 5:
  #Display the message "…Oh dear, who is that?" and read user response
  print("...Oh dear, who is that?")
  response = str(input())
  
  #If the user's response is "Smiler's Bot" then subtract 20 from the value of health and display the message "Time to jam out of here!"
  if response.lower() == "smiler's bot":
    health = health - 20
    print("Time to jam out of here!")
    print()
    
  #If the user’s response is "Hacker" then add 20 to to the value of health and display the message "Yay! Better follow this one!" 
  elif response.lower() == "hacker":
    health = health + 20
    print("Yay! Better follow this one!")
    print()
    
  #If the user’s response is anything else then display the message "Phew, just another emoji!"
  else:
    print("Phew, just another emoji!")
    print()
    
  x = x + 1

    
#At the end, the program should display the message "Escaped! Health is [value]" where [value] is the value of health:
print("Escaped! Health is" , str(health) + "%.")