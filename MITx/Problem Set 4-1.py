import ps4a
from ps4a import SCRABBLE_LETTER_VALUES


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    word = word.lower()
    score = 0
    if len(word) == n:
        for char in word:
            score += SCRABBLE_LETTER_VALUES.get(char)
        return score*n
    elif word == '':
        return 0
    else:
        for char in word:
            score += SCRABBLE_LETTER_VALUES.get(char)
        return score * len(word)

print(getWordScore('qi', 7))
