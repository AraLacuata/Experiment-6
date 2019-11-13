import string
letters = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    remaining = []
    for l in letters:
        if l not in lettersGuessed:
            remaining.append(l)
    return ''.join(remaining)