# Elizaveta Latash following examples from Towardsai.net

# Importing necessary libraries
import pandas as pd
import numpy as np
import nltk
import os



# Tokenization
###########################################

import nltk.corpus# sample text for performing tokenization
text = "Going to Costa Rica will be very fun. Adventure time commence! I can't wait to see the emeral toucanet! It will be the best time ever."
from nltk.tokenize import word_tokenize# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
token


# Finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist



# Stemming
###########################################
# Importing Porterstemmer from nltk library
# to get root of words
from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem("waiting")

stm = ["waited", "waiting", "waits"]
for word in stm :
   print(word+ ":" +pst.stem(word))
   
# Importing LancasterStemmer from nltk
# to get root of words
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
stm = ["giving", "given", "given", "gave"]
for word in stm :
 print(word+ ":" +lst.stem(word))
 
 
 
#Lemmatization
###########################################

# Importing Lemmatizer library from nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
 
print(“rocks :”, lemmatizer.lemmatize(“rocks”))
print(“corpora :”, lemmatizer.lemmatize(“corpora”))



# Removing Stop Words
###########################################
# importing stopwords from nltk library
from nltk import word_tokenize
from nltk.corpus import stopwords
a = set(stopwords.words('english'))
text = "My dog is very fluffy and kind. His name is Zoltar."
text1 = word_tokenize(text.lower())
# print(text1)
stopwords = [x for x in text1 if x in a]
# print(stopwords)
stopwords_removed = [x for x in text1 if x not in a]
print(stopwords_removed)
