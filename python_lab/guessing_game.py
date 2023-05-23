<<<<<<< HEAD
import ranges
import random
import os
#from os import system

number = random.randint(1, 100)

guess = None
while guess != number:
    
    guess = int(input("Guess the number between 1 and 100: "))
=======
import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess the number between 1 and 10: "))
>>>>>>> 85157dd (New Go lang Folder)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
<<<<<<< HEAD
        print("Hurray !!!  You got it!")
        os.system('sleep 3')
        os.system('clear')

=======
        print("You got it!")
>>>>>>> 85157dd (New Go lang Folder)

