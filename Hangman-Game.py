import random as ra


class Hangman:
    """
    This class is designed to allow a user to play hangman against their computer.

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
        self.word = ra.choice(word_list).lower() # Conversion to lower-case for consistency in _check_guess().
        self.word_guessed = ['_' for character in self.word] # Visual representation of the word the user is guessing.
        self.num_letters = len(set(self.word)) # Number of unique letters left in self.word.
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def _check_guess(self, guess):
        """
        This method checks if the user's guess is in the word, then updates the num_letters, word_guessed and num_lives attributes. 

        This method takes the guess from the ask_for_input() method, converts it to lowercase then checks if the guess exists in the word.
        If the guess is in the word, the word_guessed list updates to replace the appropriate underscore with the guessed character, then reduces num_letters by 1.
        If the guess is not in the word, num_lives is reduced by 1.

        Args:
            guess (str) = A single alphabetic character, designed to be passed from the ask_for_input() method.
        """
        guess = guess.lower() # Conversion to lower-case for checking against self.word.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, character in enumerate(self.word): # Adds correctly guessed letter to visual representation.
                if character == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')

    def ask_for_input(self):
        """
        This method asks the user to input a single alphabetic character, then passes that character as the 'guess' argument in the check_guess() method.

        This method defines the 'guess' variable to be used in the check_guess() method with a loop. The user is asked to input a single letter, then uses the loop
        to iteratively check that the guess is a single alphabetic character that has not been guessed yet, only breaking the loop when these conditions are met. 
        """
        while True:
            guess = input('Please input a single letter: ')
            if len(guess) > 1 or guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
                break
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    This function will start a game of hangman using the Hangman class defined in this file.
    
    This function creates an instance of the Hangman class, then loops until the game is over.
    Once the game is over, the function will recur via the rematch section if the user responds "Y".
    The user will be given information showing how many letters remain, which letters they've
    already guessed and their remaining lives before they make each guess.

    Attributes:
        num_lives (int) = The number of lives that will be passed to the Hangman class to start the game with.
        game (Hangman) = An instance of the Hangman class with this function's word_list and num_lives passed as initialising attributes. 
                         See help(Hangman) for more detail on the class.
    
    Args:
        word_list (list) = The list of words you would like to use. A word will be randomly selected from this list.

    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"The word you are guessing has {len(game.word)} letters. Good luck! You have {num_lives} lives")
    while True:
        if game.num_lives == 0:
            print(game.word_guessed)
            print(f"No more lives remaining. The word was {game.word}.")
            break
        elif game.num_letters > 0:
            print("~~~~~~~~~~")  # Included to make the game easier to read while playing.
            print(f"Current letters: {game.word_guessed}")
            print(f"Letters you've guessed: {game.list_of_guesses}")
            print(f"Lives: {game.num_lives}")
            game.ask_for_input()
        else:
            print(game.word_guessed)
            print(f"Congratulations, the word was {game.word}. You win!")
            break
    
    # Code to allow user to play again after game over.
    rematch = str(input("Play again? (Y or N): ")).upper() # Conversion to upper-case to simplify following condition.
    if rematch == "Y":
        play_game(word_list)
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    # Default word list.
    wl = ["Grape", "Pineapple", "Mango", "Strawberry", "Banana"]

    # This line starts the game. If you would like to use a custom word_list, please replace the argument "wl" with a list of words of your choosing.
    play_game(wl)