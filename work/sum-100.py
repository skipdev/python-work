#Stan wishes to create a program that prints out the sum of the first 100 numbers. When the program is executed it should display the message "The sum of the first 100 numbers is" followed by the answer. Your program should use an appropriate loop.
answer = 0

for count in range(1, 101, 1):
  answer = answer + count
  
print(answer)
  