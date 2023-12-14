# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## A Learning Experience
This is an implementation of the Hangman game in which you will be able to play hangman against your computer.

I will be testing my current knowledge of basic Python and Object Oriented Programming to create the game.

## What I've Learned
1. While completing the code in milestone_2.py, I implemented my own code to check if a variable is in the alphabet:
``` python
# Code for users to guess letters
guess = input("Please input a single letter: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("Your guess: ", guess)
if len(guess) == 1 and guess in alphabet:
    print("Good guess!")
else:
    print("Oops! That input is invalid, please try again.")
```
I've since learned that I could've used the string method `.isalpha()` to accomplish the same thing, oops. This is the method of checking used in milestone_3.py and later files.