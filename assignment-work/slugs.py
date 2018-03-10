def IsFusionShot(type1, type2):
  #Finding out if the two slugs are equal
  return bool(type1 == type2)
  
def IsDefectiveShot(type1, type2):
  #Calling the IsFusionShot function
  IsFusionShot(type1, type2)
  #If IsFusionShot returns False, find out if one slug is "Infurnus" and the other is "Aquabeek".
  if IsFusionShot(type1, type2) == False:
    return bool((type1 == "Infurnus" and type2 == "AquaBeek") or (type2 == "Infurnus" and type1 == "AquaBeek"))
  else:
    return True
    
def run():
  #User inputs
  user_slugchoice1 = str(input("Please enter the first type of slug: "))
  user_slugchoice2 = str(input("Please enter the second type of slug: "))
  user_fdchoice = str(input("Please enter either the word 'fusion' or 'defective': "))
  
  #Calling functions depending on the user choice
  if user_fdchoice == "fusion":
    IsFusionShot(user_slugchoice1, user_slugchoice2)
  elif user_fdchoice == "defective:":
    IsDefectiveShot(user_slugchoice1, user_slugchoice2)
  else:
    print("Invalid selection. Please try again.")
    run()
  
run()