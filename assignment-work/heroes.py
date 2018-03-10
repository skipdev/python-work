count = 1

#Display the message "How many heroes must we gather?". 
print("How many heroes must we gather?")

#Read in the user’s whole number.
number_of_heroes = int(input())

#Display the message "Gathering heroes…"
print("Gathering heroes...")

#Display all the numbers from 1 to the user's whole number in the form "…found hero [number]" 
while count < (number_of_heroes + 1):
  print("...found hero" , count )
  count = count + 1

#Display the message "All the heroes have been gathered"
print("...all the heroes have been gathered")