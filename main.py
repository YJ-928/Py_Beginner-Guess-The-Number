'''Number Guessing Game Objectives:-
Include an ASCII art logo.
Allow the player to submit a guess for a number between 1 and 100.
Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
If they got the answer correct, show the actual answer to the player.
Track the number of turns remaining.
If they run out of turns, provide feedback to the player.
Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).'''

import os
import random
from os import path
from art import logo
from numberList import numbers
from time import sleep


def guess_the_number():
    print('\n', logo, "\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    choosen_number = random.choice(numbers)

    if difficulty.lower() == 'easy':
        number_of_guesses = 10

    elif difficulty.lower() == 'hard':
        number_of_guesses = 5

    while number_of_guesses != 0:
        guess = int(input(
            f"You have {number_of_guesses} attempts remaining to guess the number.\nMake a guess: "))
        if guess == int(choosen_number):
            print(f"You got it! The answer was {choosen_number}.")
            break
        elif guess > int(choosen_number):
            print("Too High.\nGuess again.")
        elif guess < int(choosen_number):
            print("Too Low.\nGuess again.")
        number_of_guesses -= 1
        if number_of_guesses == 0:
            print(
                f"You've run out of guesses, you lose.\nThe answer was {choosen_number}.")
            break


# for playing first time by directly running code.
guess_the_number()

if input("Do you want to play again?, Type 'y' for Yes, 'n' for No: ").lower() == 'y':
    os.system('cls')  # clearing the screen of console
    guess_the_number()
