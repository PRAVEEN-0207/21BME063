import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.read().split()
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    return all(letter in lettersGuessed for letter in secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    return ''.join([letter if letter in lettersGuessed else '_ ' for letter in secretWord])

def getAvailableLetters(lettersGuessed):
    import string
    return ''.join([letter for letter in string.ascii_lowercase if letter not in lettersGuessed])

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")

    mistakeMade = 0
    lettersGuessed = []

    while 8 - mistakeMade > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        else:
            print("You have", 8 - mistakeMade, "guesses left.")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter: ").lower()

            if guess in lettersGuessed:
                print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
            elif guess in secretWord:
                lettersGuessed.append(guess)
                print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")

    if 8 - mistakeMade <= 0:
        print("Sorry, you ran out of guesses. The word was:", secretWord)

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
