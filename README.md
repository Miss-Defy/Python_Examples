# Python_Examples


Example Python projects are in the Python_Examples repository.

###############################################

#

Permutations.py - Permutes a word of your choice and shows you all of the permutations. This is a problem from the MIT Introduction to Computer Science and Programming in Python Course I did for fun.

#

Caesar_Cipher.py - A caesar cipher shifts all of the letters of a message by a specified shift. This program allows you to choose if you want to encrypt or decrypt your message. For encryption, you choose the shift you want and your message is encoded and shown to you. For decryption, the shift used for encryption is determined by going through all possible shifts and matching resulting words to a word bank. This is a problem from the MIT Introduction to Computer Science and Programming in Python Course I did for fun.

#

Hangman.py - Lets you play hangman! You need to have the words.txt file in the same directory for it to work. It gives you six guesses initially. Is you guess a letter in the word you retain all guesses. If you guess a consonant incorrectly, you lose one guess. If you guess a vowel incorrectly (aeiou), you lose two guesses. This is a problem from the MIT Introduction to Computer Science and Programming in Python Course I did for fun.

words.txt - words for the Hangman game. Must be in the same directory for Hangman.py to work.

#

Optimization_s1_s2_q_Partial_Data.py is an optimization script that was used for validation of the optimization routine in Excel used in my dissertation project. This script is titled, "Partial_Data" because this particular upload to github provides a sample of the experimental data to serve as an example. The script finds parameter values s1, s2, and q by matching the amplitude (A), period (P) and normalized center of mass (ZCOM) in our inverted pendulum model to experimental values from cats walking on split-belt treadmills in different speed conditions. 

We optimize using the following pdf function:

pdf ~ exp(-1.2)*( (A-A(s1,s2,q))^2/(deltaA)^2 + (P-P(s1,s2,q))^2/(deltaP)^2 + (Zcom-Zcom(s1,s2,q))^2/(deltaZcom)^2 )

where delta is the standard error of A, P, and Zcom respectively.

When A=A(s1,s2,q) , P=P(s1,s2,q), and ZCOM=ZCOM(s1,s2,q), then the inside of the function is about equal to zero and the pdf is about equal to 1.

The script accesses values for A, P, and ZCOM for a speed condition from an Excel sheet called Variable_Values_Partial_Data.xlsx. The control condition is shown as an example in the Excel file and is called "S_0404." In the control condition left and right belts of the split-belt treadmill are equal. In other conditions (not shown in Excel sheet), the right belt was faster than the left belt. It is possible to vary the speed of left and right belts individually in a split-belt treadmill. 
