# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:51:30 2018

@author: Delol
"""

import random
numberofguesses=0
number=random.randint(1,10)
name=raw_input("Hello What is Your Name>")
print(name.strip()+",I am thinking of a number between 1 and 10.Can you guess what it is?")
while numberofguesses<6:
    guess=int(raw_input("take a guess>"))
    numberofguesses=numberofguesses+1
    guessesleft=6-numberofguesses
    if guess<number:
        guessesleft=str(guessesleft)
        print("Your guess is too low! You have "+guessesleft+" guesses left>")
    if guess>number:
        guessesleft=str(guessesleft)
        print("Your guess is too high! You have "+guessesleft+" guesses left>")
    if number==guess:
        break
if guess==number:
    numberofguesses=str(numberofguesses)
    print("player wins and computer lose.You guessed the number in "+numberofguesses+" tries:>")
if guess!=number:
    number=str(number)
    print("player lose and computer wins.And the number I am thinking was "+number+" :> ")

    