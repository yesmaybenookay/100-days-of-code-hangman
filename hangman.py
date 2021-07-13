from os import system, name
import string
import random
import hangman_art as ha
import hangman_words as hw


# Sets a life counter to six
abc = list(string.ascii_lowercase)

# Chooses a random word from a word list
chosen_word = list(random.choice(hw.word_list))

# Creates a list to store correct guesses
good_guesses = []

# Creates a list to store all guesses
guessed = []

# Creates a list containing the alphabet
lives = 6

# Variable to store empty space indicator
blank = "_"

# Creates an underscore for each character in chosen_word
for letter in chosen_word:
    good_guesses.append(blank)

# Creates an underscore for each letter of the alphabet in guessed
for letter in abc:
    guessed.append(blank)

# Prints the user interface
def print_ui():
    if name =="nt":
        _ = system("cls")
    # MacOS, Linux, etc.
    else:
        _ = system("clear")

    # ASCII Art "hangman"
    print(f"{ha.logo}")

    # Prints characters the player hasn't guessed in two rows
    print(f"Usable letters:\n{' '.join(abc[:13])}\n{' '.join(abc[13:])}\n")

    # Prints characters the player has guessed in two rows
    print(f"Guessed Letters:\n{' '.join(guessed[:13])}\n{' '.join(guessed[13:])}\n")

    # Prints an ASCII gallows and a body part for each lost life
    print(f"{ha.stages[lives]}")

    # Prints the number of incorrect guesses before game over
    print(f"Lives: {lives}")

    # Prints correct guesses and underscores for unguessed letters 
    print(f"Word: {' '.join(good_guesses)}\n")

    # Testing code: uncomment the next line to print chosen_word
    # print(f"The word is: '{''.join(chosen_word)}'.")


game_over = False
# Prints the user interface before the first guess
print_ui()
while not game_over:
    # Asks player to input a letter
    guess = input("Guess a letter: ").lower()
    # Valid guess
    if guess not in guessed and guess in abc and guess != blank:
        # Guess is a correct one
        if guess in chosen_word:
            # Adds correct guesses to correct position in good_guesses
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    good_guesses[position] = letter
        # Takes a "life"
        else:
            lives -= 1
        # Replaces guessed letters in abc with blank vice versa
        x = 0
        for i in abc:
            if guess == i:
                abc[x] = blank
                guessed[x] = guess
            x += 1
        # Clears screen and prints the user interface
        print_ui()
    # Invalid guesses (length > 1, guessed, not an abc)
    elif len(guess) != 1:
        print("You can only guess one letter at a time. Try again...")
    elif guess in guessed:
        print(f"You already guessed '{guess}'. Try again...")
    else:
        print(f"Your guess ({guess}) cannot be used. Try again...")
    
    # Ends the game if lives is zero or if word is complete
    if lives == 0 or good_guesses == chosen_word:
        if lives == 0:
            print(f"Game over, you lost... The word was: {''.join(chosen_word)}")
        elif chosen_word == good_guesses:
            print("You guessed the word correctly... You won!")
        game_over = True
