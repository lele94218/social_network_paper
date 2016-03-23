import nltk
import string
import os

from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *

def get_tokens(file):
   with open(file, 'r') as shakes:
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


def doit(dirs, name):
    tokens = get_tokens(dirs + name)
    #Stop Word Removal
    filtered = [w.decode('utf-8') for w in tokens if not w in stopwords.words('english')]
    #Stemming
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    out = open('F:\\paper\\myPython\\py2.7\\final_raw' + os.path.sep + name, 'w')
    for each in filtered:
        points = '\'\"'
        each = each.strip(points)
        out.write(each.encode('utf-8') + ' ')
    #count = Counter(filtered)
    #print count.most_common(100)
    out.close()

read_path = 'F:\\paper\\myPython\\py2.7\\raw_data\\'
for subdir, dirs, files in os.walk(read_path):
    for file in files:
        print file
        doit(subdir + os.path.sep, file)
    
