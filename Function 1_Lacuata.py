def isWordGuessed(secretWord, lettersGuessed):
   
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True