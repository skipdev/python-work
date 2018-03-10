#Stan wishes to create a program that asks the user to enter a word and then prints out the word in reverse. For example, if the user enters the word "Happy" then the program should display "yppaH". The program should use an appropriate loop.

alist = []

#Ask user for a word
word = input("Please enter a word")
for x in word:
  alist.append(x)
  
alist.reverse()

print(alist)