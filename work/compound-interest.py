#Get the principal amount
P = float(input("Please enter the principal amount (£) "))

#Get the interest rate
r = float(input("Please enter the interest rate(decimal) "))

#Get the number of times interest in compounded per years
n = int(input("How many times is the interest compounded per year? "))

#Get the number of years the money is invested for
t = int(input("How many years are you borrowing/investing the money for? "))

#Work out the answer
A = P * (1 + (r / n)) ** (n * t)

#Print the answer rounded to 2 dp
print("The amount will be £", round(A, 2))