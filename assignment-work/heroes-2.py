#isLeagueUnited takes two parameters each of which represents a hero. The function should return True if the two heroes are "Superman" and "Wonder Woman" otherwise it should return False.

def isLeagueUnited(hero1, hero2):
  print(bool((hero1.lower() == "superman" and hero2.lower() == "wonder woman") or (hero1.lower() == "wonder woman" and hero2.lower() == "superman")))
  return bool((hero1.lower() == "superman" and hero2.lower() == "wonder woman") or (hero1.lower() == "wonder woman" and hero2.lower() == "superman"))

#decidePlan takes two parameters each of which represents a hero. A different message is displayed depending on whether or not the isLeagueUnited function returns True or False. 

def decidePlan(hero1, hero2):
  if isLeagueUnited(hero1, hero2) == True:
    print("Time to save the world!")
    return("Time to save the world!")
  else:
    print("We must unite the league!")
    return("We must unite the league!")
  

#The third function should be named run and should take 0 parameters.
def run():
  
#Prompt the user to enter name of the first hero, the second hero, and either the word "league" or "plan".
  hero1_name = str(input("What is the name of the first hero? "))
  hero2_name = str(input("What is the name of the second hero? "))
  key_word = str(input("Please type either the word 'league' or 'plan': "))
  
#If the user enters "league", the result of isLeaugeUnited should be displayed.
#If the user types in "plan", the result of decidePlan should be displayed.
#If the user types something else then "Invalid command. Please try again" should be displayed.
  if key_word.lower() == "league":
    isLeagueUnited(hero1_name, hero2_name)
  elif key_word.lower() == "plan":
    decidePlan(hero1_name, hero2_name)
  else:
    print("Invalid command. Please try again.")
    print()
    run()


#Calling the run function
run()