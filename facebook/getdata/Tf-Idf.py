import nltk
import string
import os

from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *

def get_tokens():
   with open('F:\\paper\\myPython\\py2.7\\text_data\\obama_msg.txt', 'r') as shakes:
    text = shakes.read()
    lowers = text.lower()

    #Punctuation Removal

    no_punctuation = lowers.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


def stem_tokens(tokens, stemmer):
    stemmed = []
    for each in tokens:
        stemmed.append(stemmer.stem(each))
    return stemmed

tokens = get_tokens()

#Stop Word Removal

filtered = [w.decode('utf-8') for w in tokens if not w in stopwords.words('english')]



#Stemming

stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)

count = Counter(filtered)
print count.most_common(100)
