import string
alph = string.ascii_lowercase

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
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
    return final
print(getAvailableLetters(lettersGuessed))