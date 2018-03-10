import random

def game():
    target = int(random.randint(1, 2000))
    num = 0
    while target != num:
        num = int(input("Pick a number. "))
        if num > target:
            print("My number is lower than yours.")
        elif num < target:
            print("My number is higher than yours.")
        else:
            print("You got it!")

    final = input("Thanks for playing! Would you like to play again? Y/N ")
    if final == "Y" and "yes" and "ye" and "y" and "yeah":
        game()
    else:
        print("ok bye")


name = input("What is your name? ")
print("Hey," , name, "... I'm gonna play a little game with you.")
print("I've chosen a number from 1 to 2000. Now you have to try and figure it out! :)")
game()