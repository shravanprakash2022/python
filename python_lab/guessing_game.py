import ranges
import random
import os
#from os import system

number = random.randint(1, 100)

guess = None
while guess != number:
    
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Hurray !!!  You got it!")
        os.system('sleep 3')
        os.system('clear')


