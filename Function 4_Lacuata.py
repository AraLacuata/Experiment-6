#Function 1 (Is Word Guessed)
def isWordGuessed(secretWord, lettersGuessed):
   
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True

#Function 2 (Get Guessed Word)
guesses = []
def getGuessedWord(secretWord, lettersGuessed):   
   for l in secretWord:
        if l in lettersGuessed:
            guesses.append(l)
        else:
            guesses.append('_')
   return ' '.join(guesses)

#Function 3 (Get Available Letters)
import string
letters = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    remaining = []
    for l in letters:
        if l not in lettersGuessed:
            remaining.append(l)
    return ''.join(remaining)

#Function 4 (Hangaroo)
def Hangaroo(secretWord):

    print('Welcome to Hangaroo!')
    print('The word is', len(secretWord), "letters long.")
    mistakes = 0
    lettersGuessed = []

    while 5 - mistakes > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:           
            print('\nCongratulations, you won!')
            break
        
        else:    	
        	print('\nYou have', 5 - mistakes, 'guesses left.')
        	print('Available letters:',getAvailableLetters(lettersGuessed))
        	guesses = str(input('Guess a letter: ')).lower()
        	if guesses in secretWord and guesses not in lettersGuessed:
        		lettersGuessed.append(guesses)
        		print('Good guess: \n', getGuessedWord(secretWord, lettersGuessed))
        	elif guesses in lettersGuessed:
        		print("You've already guessed that letter: \n", getGuessedWord(secretWord, lettersGuessed))
        	elif guesses not in secretWord:
        		print("That letter is not in the word: \n", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guesses)
        		mistakes += 1
                
        if 5 - mistakes == 0:       	
        	print('\nGame Over. You ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue

        