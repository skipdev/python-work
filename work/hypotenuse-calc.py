import math

#Asking the user for triangle side 1
a = float(input("Please enter the length of side a: "))

#Asking the user for triangle side 2
b = float(input("Please enter the length of side b: "))

#Calculating hypotenuse
c= float(math.sqrt((a * a) + (b * b)))

#Display the result rounded to the nearest whole number
print("The hypotenuse is" , round(c, 0))