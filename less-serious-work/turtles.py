def CalculateAgeTotal(master,leo,donny,ralph,mikey):
  AgeTotal =  master + leo + donny + ralph + mikey
  print(AgeTotal)
  
def CalculateAvgAgeDifference(master,leo,donny,ralph,mikey):
  AgeDifference = (master + leo + donny + ralph + mikey) / 4
  print(AgeDifference)
  
def run():
  master = int(input("Please enter the age for Master Splinter: "))
  leo = int(input("Please enter the age for Leo: "))
  donny = int(input("Please enter the age for Donny: "))
  ralph = int(input("Please enter the age for Ralph: "))
  mikey = int(input("Please enter the age for Mikey: "))
  
  question = str(input("Would you like to see the total age, or the average age difference? Please either input 'total' or 'difference': "))
  if question == "total":
    CalculateAgeTotal(master,leo,donny,ralph,mikey)
  elif question == "difference":
    CalculateAvgAgeDifference(master,leo,donny,ralph,mikey)
    
run()