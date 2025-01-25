# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string
import random

alph = string.ascii_lowercase
WORDLIST_FILENAME = "words.txt"
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    running = True
    while running:
        if len(random.choice(wordlist)) == 5:
            running = False
            return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    final = ""
    for char in secretWord:
        if char in lettersGuessed:
            final += char
            final += ' '
        else:
            final += '_ '
    return print(final)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    new = []
    final =''
    for char in alph:
        new.append(char)
    for i in lettersGuessed:
        if i in new:
            new.remove(i)
    new.sort()
    for ch in range(len(new)):
        final += new[ch]
    return print(final)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print(f"Hello! Your word contains {len(secretWord)} letters")

    lettersGuessed =''

    runtime =0
    while runtime <= 6:
        letter_guessed = str(input("Please choose a letter: "))
        if len(letter_guessed) != 1:
            print("Please input only one letter")
        elif not letter_guessed.isascii():
            print("Please print only letters")
        else:
            if letter_guessed == lettersGuessed:
                print("You have already tried that")
                print(f"The available letters are {getAvailableLetters(lettersGuessed)}")
            else:
                lettersGuessed += letter_guessed
                getGuessedWord(secretWord, lettersGuessed)
                if letter_guessed in secretWord:
                    if isWordGuessed(secretWord,lettersGuessed):
                        is_running = False
                        return print("Congratulations! You have successfully guessed the word!")
                    print(HANGMANPICS[runtime])
                else:
                    print(HANGMANPICS[runtime])
                    print("Your letter was not found")
                    runtime += 1
    print("Better Luck Next Time!")
    return print(f"Your Word was \033[1;33;40m{secretWord}")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
