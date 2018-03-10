#Prompt the user to identify if they are a mutant.

mutant = str(input("Are you a mutant? "))


#If the user’s response is 'Yes' then the message "Your application to Xavier's School for Gifted Youngsters has been accepted" should be displayed. 

if mutant == "yes" or mutant == "Yes":
  print("Your application to Xavier's School for Gifted Youngsters has been accepted.")
else:
  print("Your application was not successful on this occasion")
