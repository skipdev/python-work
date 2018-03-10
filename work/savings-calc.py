#Asking the user to enter current amount of savings
savings = float(input("Please enter your current amount of savings: "))

#Asking the user to enter percentage interest rate
rate = int(input("What is your percentage interest rate? "))

#Calculating new amount of savings
newsavings = float(savings + (savings * (rate / 100)))

#Display new amount of savings
print("Your balance after a year will be: " , round(newsavings, 2))