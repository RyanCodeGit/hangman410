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
        self.word = ra.choice(word_list).lower()
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word))
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
    
    This function creates an instance of the Hangman class, then loops until the user is finished playing. The user will be told how many letters are in the word they are guessing,
    then shown a representation of the word with non-guessed letters hidden by underscores, a list of letters they have already guessed and the amount of lives they have remaining.
    As long as there are letters left in the word, the user will be asked to input guesses for the remaining letters. Once there are no letters or lives remaining, the game is over.
    When the game is over, the user will be asked if they would like to play again. If they input "y", this function will be called again. If they input anything else, the loop breaks.

    Attributes:
        num_lives (int) = The number of lives that will be passed to the Hangman class to start the game with. If you would like more or less lives, change the value.
        game (Hangman) = An instance of class Hangman that passes the word_list argument of this function and the num_lives attribute as arguments for the instance. 
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
            print("~~~~~~~~~~")
            print(f"Current letters: {game.word_guessed}")
            print(f"Letters you've guessed: {game.list_of_guesses}")
            print(f"Lives: {game.num_lives}")
            game.ask_for_input()
        else:
            print(game.word_guessed)
            print(f"Congratulations, the word was {game.word}. You win!")
            break
    rematch = str(input("Play again? (Y or N): ")).upper()
    if rematch == "Y":
        play_game(word_list)
    else:
        print("Thank you for playing!")

# Help files. Un-comment these lines and comment out the play_game(wl) call below if you would like to view help documentation.
# help(play_game)
# help(Hangman)

# Default word list
wl = ["Grape", "Pineapple", "Mango", "Strawberry", "Banana"]

# This line starts the game. If you would like to use a custom word_list, please replace the argument "wl" with a list of words of your choosing.
play_game(wl)