import random as ra
from milestone_2 import word_list as wl

class Hangman:
    """
    This class is designed to allow a user to play hangman against their computer. \n

    Attributes:
        self.word (str) = A word, randomly chosen from self.word_list.
        self.word_guessed (list) = A list containing underscores(_) to represent each letter of the chosen word.
        self.num_letters (int) = The number of unique letters in the word.
        self.num_lives (int) = The number of lives the user has remaining, default value 5.
        self.word_list (list) = A list of words, passed as an argument in the constructor.
        self.list_of_guesses (list) = An empty list that populates with characters the user has already guessed.
    Args:
        word_list (list) = A list of words for the class to pick from for the user to guess.
        num_lives (int) = The number of lives the user has before the game ends. Defaults to 5.

    """
    def __init__(self, word_list, num_lives=5):
        """
        See help(Hangman) for explanations of the attributes defined here.
        """
        self.word = ra.choice(word_list).lower()
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        This method checks if the user's guess is in the word, then updates the num_letters, word_guessed and num_lives attributes. \n

        This method takes the guess from the ask_for_input() method, converts it to lowercase then checks if the guess exists in the word.
        If the guess is in the word, the word_guessed list updates to replace the appropriate underscore with the guessed character, then reduces num_letters by 1.
        If the guess is not in the word, num_lives is reduced by 1. \n

        Args:
            guess (str) = A single alphabetic character, designed to be passed from the ask_for_input() method.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, character in enumerate(self.word):
                if character == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        """
        This method asks the user to input a single alphabetic character, then passes that character as the 'guess' argument in the check_guess() method. \n

        This method defines the 'guess' variable to be used in the check_guess() method with a loop. The user is asked to input a single letter, then uses the loop
        to iteratively check that the guess is a single alphabetic character that has not been guessed yet, only breaking the loop when these conditions are met. 
        """
        while True:
            guess = input('Please input a single letter: ')
            if len(guess) > 1 and guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break