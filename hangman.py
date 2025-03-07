# import libraries
import random

# Constants
MAX_GUESSES = 6

# Global Variables
secret_word = ''
letters_guessed = []

# TODO: Create a function for generating a secret word
def get_word():
    words = ["apple", "orange", "python", "happy", "birthday", "random", "life", "string", "list"]
    word = random.choice(words)

    return word

# TODO: Create a function for guessing letters
def check_word_guessed():
    global secret_word
    global letters_guessed
    guessed_word = []
    mistakes_made = 0

    print("You have %d guesses left." % (MAX_GUESSES - mistakes_made))
    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("-")
    print("".join(guessed_word))

def player_guessed_word():
    global secret_word, letters_guessed

    for letter in secret_word:
        if not (letter in letters_guessed):
            word_guessed = False
            break
        else:
            word_guessed = True

# TODO WARM-UP: Find the code in Hangman that checks if a letter
# is found in the word and updates a variable that says if the word
# is correct. Refactor this code into a function that returns the
# variable instead.
# BONUS TODO: See if you can update the conditional logic to something
# more simplified!

def play_hangman():
    global secret_word
    global letters_guessed
    global word_guessed
    
    play_game = True
    word_guessed = False

    while play_game:
        # Get user input
        guess = input("Enter a letter: ").lower()
        while guess in letters_guessed:
            print("You have already guessed letter %s." % guess)
            guess = input("Enter a different letter: ").lower()

        # Check if letter is in word
        letters_guessed.append(guess)

        if guess in secret_word:
            print("There is a %s" % guess)
            # for letter in secret_word:
            #     if not (letter in letters_guessed):
            #         word_guessed = False
            #         break
            #     else:
            #         word_guessed = True
            
            if word_guessed:
                print(secret_word)
                print("You won!")
                play_game = False
        else:
            mistakes_made += 1
            print("There is no %s" % guess)
            if mistakes_made == MAX_GUESSES:
                print("Game over")
                play_game = False

play_hangman()
        