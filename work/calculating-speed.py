#Asking for distance walked in km
distance = float(input("Please enter the distance you have walked (in kilometers): "))

#Asking for the time taken in hrs
time = float(input("Please enter the time you took to walk this distance (in hours): "))

#Calculate speed in metres per minute
distanceinmetres = distance / 1000
timeinminutes = time / 60
speed = distanceinmetres / timeinminutes

#Diplay the result to 1dp in ASCII box
print("####################################################################")
print("#                                                                  #")
print("#         You walked at a speed of" , round(speed, 2) , "metres per minute          #")
print("#                                                                  #")
print("####################################################################")