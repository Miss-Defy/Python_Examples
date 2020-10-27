# Problem Set 2, hangman.py
# Name: Elizaveta Latash
# Collaborators: None
# Time spent: 1 day

# Hangman Game
#######################################################################
# From the MIT Introduction to Computer Science and Programming in Python Course
# Instructions in double quotes are from the course

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

secret_word=choose_word(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    secret_letters=list(secret_word)
    Length_secret=len(secret_letters)
    Length_guessed=len(letters_guessed)
    
    n=0
    for i in range(1,Length_secret+1):
        if secret_letters[i-1] in letters_guessed:
            n=n+1
    
    if n==Length_secret:
        return True
    else:
        return False

    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''




def get_guessed_word(secret_word, letters_guessed):
    
    secret_letters=list(secret_word)
    Length_secret=len(secret_letters)
    Length_guessed=len(letters_guessed)
    
    Get_guessed=[]
    
    for i in range(1,Length_secret+1):
        if secret_letters[i-1] in letters_guessed:
            Get_guessed.append(secret_letters[i-1])
        else:
            Get_guessed.append('_ ')

    GetGuessed=''.join(Get_guessed)
    
    print(GetGuessed)

    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''



def get_available_letters(letters_guessed):
    Length_guessed=len(letters_guessed)
    All_letters=string.ascii_lowercase
    All_letters_list=list(All_letters)
    
    for i in range(1,Length_guessed+1):
        if letters_guessed[i-1] in All_letters_list:
            All_letters_list.remove(letters_guessed[i-1])


    All_Remaining_Letters= ''.join(All_letters_list)
    
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''


    
    

def hangman(secret_word):
    global Guesses_left
    Vowels=['a','e','i','o','u']
    
    Guess1=input('Enter your guess: ')

    if Guess1 in Guesses:
        print("You already picked that letter. Please try again.")
        Guess1=input('Enter your guess: ')
    else:
        Guesses.append(Guess1)
        Letters_available.remove(Guess1)
        if Guess1 in secret_word:
            print("Good guess!  :O) ")
            if is_word_guessed(secret_word, Guesses):
                Guesses_left=0
                return Guesses_left
            else:
                get_guessed_word(secret_word, Guesses)
                return Guesses_left
        elif Guess1 in Vowels:
            Guesses_left = Guesses_left - 2
            print("Nope :O,   You have ",Guesses_left," guesses left")
            get_guessed_word(secret_word, Guesses)
            return Guesses_left
        else:
            Guesses_left = Guesses_left - 1
            print("Nope   :O, ")
            get_guessed_word(secret_word, Guesses)
            return Guesses_left




    
    
    
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''



#######################################################################




if __name__ == "__main__":
    # pass

    
    secret_word = choose_word(wordlist)
    Length_secret_word=len(secret_word)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", Length_secret_word," letters long.")
    print("-------------")
                  
    All_letters=string.ascii_lowercase
    Letters_available=list(All_letters)
                  
    
    global Guesses_left
    Guesses_left=10
    Guesses=[]
                  
    while Guesses_left > 0:
        print("             ")
        print("-------------")
        print("             ")
        print("You have ", Guesses_left, " guesses left.")
        All_Remaining_Letters= ''.join(Letters_available)
        print("Available letters are: ",All_Remaining_Letters)
        hangman(secret_word)
    
    if is_word_guessed(secret_word, Guesses):
        print("             ")
        print("             ")
        print("             ")
        print("-------------")
        print("---*******---")
        print("---*-----*---")
        print("---*-----*---")
        print("---*----***--")
        print("---*-----*---")
        print("---*---*****-")
        print("---*-----*---")
        print("---*-----*---")
        print("---*----*-*--")
        print("---*----*-*--")
        print("---*---**-**-")
        print("-*****-------")
        print("             ")
        print("             ")
        print("             ")
        print("Congratulations! You just WON the GAME!!! Woot Woot   oo,")
        print("The secret word was ", secret_word)
        print("             ")
        print("             ")
        print("             ")
        print("*-----------*")
        print("-*---------*-")
        print("--*-------*--")
        print("---*-----*---")
        print("----*---*----")
        print("-----*-*-----")
        print("------*------")
        print("-----*-*-----")
        print("----*---*----")
        print("---*-----*---")
        print("--*-------*--")
        print("-*---------*-")
        print("*-----------*")
    else:
        print("             ")
        print("             ")
        print("             ")
        print("-------------")
        print("---*******---")
        print("---*-----*---")
        print("---*-----*---")
        print("---*----***--")
        print("---*-----*---")
        print("---*---*****-")
        print("---*-----*---")
        print("---*-----*---")
        print("---*----*-*--")
        print("---*----*-*--")
        print("---*---**-**-")
        print("-*****-------")
        print("             ")
        print("             ")
        print("             ")
        print("No win this time. Play again and win!   oo,")
        print("The secret word was ", secret_word)
        print("             ")
        print("             ")
        print("             ")
        print("*-----------*")
        print("-*---------*-")
        print("--*-------*--")
        print("---*-----*---")
        print("----*---*----")
        print("-----*-*-----")
        print("------*------")
        print("-----*-*-----")
        print("----*---*----")
        print("---*-----*---")
        print("--*-------*--")
        print("-*---------*-")
        print("*-----------*")

#######################################################################

