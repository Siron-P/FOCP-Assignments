'''15. Write a program to create a number guessing game for the user. The program should ask
the user to input a number.'''

import random

def guess():
    num = random.randrange(1,50)

    attempt = 5

    print("--------------------------------------------------------")
    print("----------Welcome to the Number Guessing Game-----------")
    print("--------------------------------------------------------")
    print("I have selected number from 1 to 50. You have to guess that number within 5 attempts.")

    for attempt in range(1,attempt+1):
        guess=int(input("Enter your guess : "))

        if guess<num:
            print("Too low!")

        elif guess>num:
            print("Too High!")
        else:
            print("\nCORRECT NUMBER!\n")
            break
        

    else:
        print("\nGAME OVER!\n")

guess()    
    