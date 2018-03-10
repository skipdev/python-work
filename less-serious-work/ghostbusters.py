def WhoToCall(TroubleMaker):
  if TroubleMaker == "fire":
    x = "A fire fighter"
  elif TroubleMaker == "burglar":
    x = "A police officer"
  elif TroubleMaker == "ghost":
    x = "GHOSTBUSTERS!"
  else:
    x = "nobody"
  print("Who you gonna call?", x)
  
WhoToCall("ghost")
  