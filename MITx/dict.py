import string
word = 'adD'
word = word.lower()

alph = string.ascii_lowercase
dict = {}
score = 0
for i in range(26):
    dict.update({alph[i]: i +1})
for i in range(len(word)):
    score += dict.get(word[i]) * i
    print(word[i])
    print(score)


