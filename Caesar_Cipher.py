# Problem Set 4B
# Name: <Elizaveta Latash>
# Collaborators: None
# Time Spent: 2 days

import string
import numpy as np

##############################################################################################

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

##############################################################################################

WORDLIST_FILENAME = 'words.txt'

##############################################################################################
# ENCRYPT MESSAGE
##############################################################################################



class Message(object):
    def __init__(self, text):
        
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
        '''
        Initializes a Message object text (string): the message's text a Message object has two attributes:self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

    def get_message_text(self):
        return self.message_text
        '''
        Used to safely access self.message_text outside of the classReturns: self.message_text
        '''

    def get_valid_words(self):
        return self.valid_words[:]
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        Returns: a COPY of self.valid_words
        '''
    

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowercase_keys = list(string.ascii_lowercase)
        lowercase_values = list(string.ascii_lowercase)
        lowercase_values_shifted = lowercase_values[shift:] + lowercase_values[:shift]

        uppercase_keys = list(string.ascii_uppercase)
        uppercase_values = list(string.ascii_uppercase)
        uppercase_values_shifted = uppercase_values[shift:] + uppercase_values[:shift]
    
        All_keys = lowercase_keys + uppercase_keys
        All_values = lowercase_values_shifted + uppercase_values_shifted
    
        self.shift_dict = dict(zip(All_keys, All_values))
    
        return self.shift_dict
    

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)





##############################################################################################
# DECRYPT MESSAGE
##############################################################################################



class CiphertextMessage(Message):
    def __init__(self, text):
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass #delete this line and replace with your code here
    
    def get_message_text(self):
        return self.message_text
    
    def get_valid_words(self):
        return self.valid_words[:]

    def build_shift_dict(self, shift):

        lowercase_keys = list(string.ascii_lowercase)
        lowercase_values = list(string.ascii_lowercase)
        lowercase_values_shifted = lowercase_values[shift:] + lowercase_values[:shift]
        
        uppercase_keys = list(string.ascii_uppercase)
        uppercase_values = list(string.ascii_uppercase)
        uppercase_values_shifted = uppercase_values[shift:] + uppercase_values[:shift]
        
        All_keys = lowercase_keys + uppercase_keys
        All_values = lowercase_values_shifted + uppercase_values_shifted
        
        self.shift_dict = dict(zip(All_keys, All_values))
        
        return self.shift_dict
    
    
    def apply_shift(self, shift):
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)
    
    
    def decrypt_message(self):
        
        Number_words_in_message=len(CiphertextMessage.get_message_text(self).split())
        
        Words_Found_Per_Shift=np.zeros((1,26))
        
        for i in range(0,26):
            Try_Shift=CiphertextMessage.apply_shift(self,i)
            Try_Shift_Words=Try_Shift.split()
            n=0
            for j in range(0,Number_words_in_message):
                if is_word(CiphertextMessage.get_valid_words(self), Try_Shift_Words[j]):
                    n=n+1
            Words_Found_Per_Shift[0,i]=n
        
        
        Max_word_found_per_shift=np.amax(Words_Found_Per_Shift)
        for i in range(0,26):
            if Words_Found_Per_Shift[0,i]==Max_word_found_per_shift:
                Best_shift_found=i
            
        Output_message=CiphertextMessage.apply_shift(self,Best_shift_found)
        
        return Output_message
        
        
        
        
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''



if __name__ == '__main__':
    
    Yes_options = ('Yes','yes','YES')
    All_options = ('Yes','yes','No','no','NO')
    
    print('This is a Caesar Cipher. You can either encrypt or decrypt a message with the Caesar Cipher.')
    print('  ')
    print('A Caesar Cipher shifts each letter of a message by a chosen shift. A shift of two turns an "A" into a "C".')
    print('  ')
    print('If you choose to encrypt your message, you should choose the shift you want.')
    print('  ')
    print('Please choose if you would like to encrypt or decrypt your message. Please answer yes or no.')
    print('  ')
    
    Encrypt_YN= input('Would you like to encrypt? (yes or no)  ')
    
    if Encrypt_YN not in All_options:
        print('You did not answer yes or no. Please say yes if you would like to encrypt your message and no if you do not.')
        Encrypt_YN= input('Would you like to encrypt? (yes or no)  ')

    Encrypt_do=0
    if Encrypt_YN in Yes_options:
        Encrypt_do=1

    if Encrypt_do == 1:
        print('  ')
        Chosen_shift = input('Please enter your shit (Must be an integer between 1 and 26):   ')
        Chosen__shift=int(Chosen_shift)
        print('  ')
        print('Please choose your message.')
        Chosen_message=input('Enter your message:   ')
        print('  ')
        print('Awesome! Here is your encrypted messsage:')
        Encrypt__Message = Message(Chosen_message)
        Encrypted__message=Message.apply_shift(Encrypt__Message, Chosen__shift)
        print('  ')
        print('************************************************************')
        print('  ')
        print('Encrypted_message: ' , Encrypted__message)
        print('  ')
        print('************************************************************')

    

    if Encrypt_do ==0:
        Decrypt_YN= input('Would you like to decrypt? (yes or no)  ')
        
        if Decrypt_YN not in All_options:
            print('You did not answer yes or no. Please say yes if you would like to decrypt your message and no if you do not.')
            Decrypt_YN= input('Would you like to decrypt? (yes or no)  ')

        Decrypt_do=0
        if Decrypt_YN in Yes_options:
            Decrypt_do=1

    
        if Decrypt_do == 1:
            print('  ')
            print('Please choose your message.')
            Chosen_message=input('Enter your message:   ')
            print('  ')
            print('Awesome! Here is your decrypted messsage:')
            Decrypt__Message = CiphertextMessage(Chosen_message)
            Decrypted__message = CiphertextMessage.decrypt_message(Decrypt__Message)
            print('  ')
            print('************************************************************')
            print('  ')
            print('   Decrypted_message: ' , Decrypted__message)
            print('  ')
            print('************************************************************')


#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 

