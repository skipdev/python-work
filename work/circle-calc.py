import math

radius = float(input("Please enter the circle radius: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("The area is:" , round(area, 2))
print("The circumference is:" , round(circumference, 2))