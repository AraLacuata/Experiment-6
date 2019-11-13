guesses = []
def getGuessedWord(secretWord, lettersGuessed):   
   for l in secretWord:
        if l in lettersGuessed:
            guesses.append(l)
        else:
            guesses.append('_')
   return ' '.join(guesses)