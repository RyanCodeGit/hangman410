# Word absolutely defined for testing purposes
word = "apple"

# Loop to confirm that the guessed input is a single alphabetic character
while True:
    guess = input("Please input a single letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Checking if guessed letter appears in the chosen word
if guess in word:
    print(f'Good guess! {guess} is in the word.')
else:
    print(f'Sorry, {guess} is not in the word. Try again.')

# Functions to encapsulate above code
def check_guess(guess):
    """
This function converts the passed argument to lowercase then checks if it exists in a pre-defined 'word' variable. \n

The function is not designed for use on its own, it is designed to be called in the ask_for_input function,
and the input generated from that function passed as the argument for the 'guess' parameter. \n

Args:
    guess (str): A single alphabetic character, ideally passed from the ask_for_input function.
    """
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    """
This function asks the user for input then calls check_guess to confirm that the input is a single alphabetic character. \n

The function runs a loop that asks the user to input a string as the 'guess' variable, which repeats infinitely until 'guess' is confirmed to be a single alphabetic character. 
When the 'guess' is a single alphabetic character, the loop will break and the function will call check_guess(guess)
to check whether the 'guess' variable is contained in a pre-defined 'word' variable.
    """
    while True:
        guess = input("Please input a single letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

