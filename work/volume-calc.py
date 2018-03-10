import math 

shape = ""

def calculate():
  global shape
  #Asking the user for which shape they would like to calculate the volume of.
  shape = str(input("Please enter a shape (cylinder or cone): "))
  if shape != "cylinder" and shape != "cone":
    print("That was not an option")
    calculate()
    
calculate()

#Ask the user to enter a radius.
radius = float(input("Please enter the radius of your shape: "))

#Ask the user to enter a height.
height = float(input("Please enter the height of your shape: "))

#Work out the volume of the user's shape.
if shape == "cylinder":
  volume = math.pi * (radius ** 2) * height
elif shape == "cone":
  volume = (math.pi * (radius ** 2) * height) / 3
  
#Prints the shape volume
print(volume)
  