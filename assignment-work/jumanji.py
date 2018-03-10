number = 0
#Display the message "How many zones must I cross?"
print("How many zones must I cross?")

#Read in the user’s whole number.
number = int(input())

#Display the message "Crossing zones...". 
print("Crossing zones...")

#Display all the numbers from the user's whole number to 1 in the form "…crossed zone [number]" where [number] is the zone number.
while int(number) > 0:
  print("... crossed zone" , number)
  number = int(number) - 1

#Display the message "Crossed all zones.  Jumanji!"
print("Crossed all zones.  Jumanji!")
