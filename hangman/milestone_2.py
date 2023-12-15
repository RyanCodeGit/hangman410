import random as ra

# Creating a short list of words and assigning a variable to pick them at random
word_list = ["Grape", "Pineapple", "Mango", "Strawberry", "Banana"]
word = ra.choice(word_list)

if __name__ == '__main__':
    # Code for users to guess letters
    guess = input("Please input a single letter: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print("Your guess: ", guess)
    if len(guess) == 1 and guess in alphabet:
        print("Good guess!")
    else:
        print("Oops! That input is invalid, please try again.")