import random
import string

WORDLIST_FILENAME = "words.txt"

####################################################
with open("words.txt") as f:
    words = f.read().split()

###########################################################
secret_word = random.choice(words)
letters_guessed = set()
wrong_guesses = set()
max_guess = 10

########################################################
def is_word_guessed(secret_word,letters_guessed):
    for x in secret_word:
        if x == letters_guessed:
            return True
        else:
            return False

is_word_guessed(secret_word,letters_guessed)
##############################################################"
def get_available_letters(letters_guessed):
    letters_guessed = string.ascii_lowercase
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    print(letters_guessed)
get_available_letters(letters_guessed)

##################################################################
def get_guessed_word(secret_word,letters_guessed):
    def guesses_remaining():
        return max_guess - len(wrong_guesses)

    def has_won():
        return all(letter in letters_guessed for letter in secret_word)

    def has_lost():
        return guesses_remaining() == 0

    while not has_won() and not has_lost():
        print("".join(letter if letter in letters_guessed else " _ " for letter in secret_word))
        print("{} guesses_remaining".format(guesses_remaining()))
        letter = str(input("Enter a letter : "))
        if letter in secret_word:
            letters_guessed.add(letter)
        else:
            wrong_guesses.add(letter)
    print("Game over . The word was {}".format(secret_word))
    if not (letter.isalpha()):
        print("ops!that is not a valid letter")

    letters_guessed = string.ascii_lowercase
    count = 0
    limit = 3

    if letter not in letters_guessed and count < limit:
        print("can only input an alphabet.you have {} warning".count)
        count += 1
    elif letter not in letters_guessed and count == limit:
        print("stop")


 




get_guessed_word(secret_word,letters_guessed)

#############################################################
