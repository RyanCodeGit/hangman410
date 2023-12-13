import random as ra

# Creating a short list of words and assigning a variable to pick them at random
word_list = ["Grape", "Pineapple", "Mango", "Strawberry", "Banana"]
word = ra.choice(word_list)

# Code for users to guess letters
guess = input("Please input a single letter: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
if len(guess) == 1 and guess in alphabet:
    print("Your guess: ", guess)
    print("Good guess!")
else:
    print("Your guess: ", guess)
    print("Oops! That input is invalid, please try again.")