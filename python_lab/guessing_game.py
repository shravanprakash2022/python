import random
import os
#from os import system

number = random.randint(1, 100)

guess = None
while guess != number:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")

