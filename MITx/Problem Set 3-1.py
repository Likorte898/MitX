secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):

#    secretWord: string, the word the user is guessing
#   lettersGuessed: list, what letters have been guessed so far
#  returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

