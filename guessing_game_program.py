# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 15:05:39 2025

@author: 91912
"""

import random

random_number = random.randint(1, 20)
guess_count = 1
max_guesses = 5

print("Guess a number between 1 and 20:")

while guess_count <= max_guesses:
    print("Attempt", guess_count, ": ", end="")
    guess = int(input())

    if guess < 1 or guess > 20:
        print("Invalid input! Enter a number between 1 and 20.")
        continue

    if guess < random_number:
        print("Too Low! Try again.")
    elif guess > random_number:
        print("Too High! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break

    guess_count += 1

if guess_count > max_guesses:
    print("Game Over! The correct number was", random_number)
