#Stan wishes to create a program that displays a grid of (ASCII) faces. The program should first read in the number of rows and columns specified by the user and then produce a grid of ASCII faces with the specified number of rows and columns.

face = ":)"


#Get number of rows
rows = int(input("What is the number of rows? "))

#Get number of columns
columns = int(input("What is the number of columns? "))

#Create the ascii grid
for x in range(rows):
  for y in range(columns):
    print(face, end="")
  print()