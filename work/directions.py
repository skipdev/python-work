#Ask user for a key and move in that direction
def question():
  key = str(input("Please enter a key to move in that direction or type STOP to stop moving. W/A/S/D: "))
  if key == "W":
    print("Moving up")
    question()
  elif key == "S":
    print("Moving down")
    question()
  elif key == "A":
    print("Moving left")
    question()
  elif key == "D":
    print("Moving right")
    question()
  elif key == "STOP":
    print("No longer moving!")
  else:
    print("That's not a direction!")
    question()
    
question()
  