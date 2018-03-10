#Enter a character representing a marker.
marker = input("Enter a character representing a marker")

#Ask the user to enter a sequence of characters consisting of dashes and 2 markers.
sequence = input("Enter a sequence of characters consisting of dashes and 2 markers e.g. 'X----X' ")

pos = []

#Find marker positions
for x,y in enumerate(sequence):
  if marker==y:
    position = x + 1
    pos.append(position)
    print(x + 1)

print(pos)
print("")

#Count the number of dashes between the two markers.
answer = pos[1] - pos[0]

#Print the total number of characters between the markers.
print("The difference between the two markers is:" , answer - 1)


