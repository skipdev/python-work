#six functions
import math
x = 0
y = 0
z = 0


def Validate():
  if x + y > z or x + z > y or y + z > x:
    print("The triangle is valid")
  else:
    print("The triangle is not valid")
    
    
def Identify():
  if x + y > z or x + z > y or y + z > x:
    if x == y and y == z:
      print("The triangle is an equilateral.")
    elif x != y and y != z and x != z:
      print("The trangle is a scalene.")
    else:
      print("The triangle is an isosceles.")
  else:
    print("Not a triangle.")
    
    
def CalculatePerimiter():
  perimiter = x + y + z
  print(perimiter)
  
def CalculateArea():
  perimiter = x + y + z
  half_perimiter = perimiter / 2 
  area = math.sqrt(half_perimiter(half_perimiter - x)(half_perimiter - y)(half_perimiter - z))
  print(area)
  
def Draw():
  count = 0
  p = x + y + z
  count2 = p
  while count < p:
    for i in range(count2):
      print("*")
      count = count + 1
      count2 = count2 - 1
  
def Run():
  
  x = float(input("Please enter the first side of the triangle: "))
  y = float(input("Please enter the second side of the triangle: "))
  z = float(input("Please enter the third side of the triangle: "))
  
  print("1. Validate")
  print("2. Identify")
  print("3. CalculatePerimiter")
  print("4. CalculateArea")
  print("5. Draw")
  user_choice = int(input("Please enter a number to carry out the appropriate action: "))
  
  if user_choice == 1:
    Validate()
  elif user_choice == 2:
    Identify()
  elif user_choice == 3:
    CalculatePerimiter()
  elif user_choice == 4:
    CalculateArea()
  elif user_choice == 5:
    Draw()
  else:
    Run()
    
  
  
Run()