from __future__ import division
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:01:24 2015

@author: Keine
"""
import nltk
import sqlite3
import math
import os
from textblob import TextBlob as tb
 
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)
 
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)
 
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
 
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
    
    
file_num = 49

cx = sqlite3.connect("F:\\paper\\myPython\\py2.7\\text2DB\\get_data.db")
cu = cx.cursor()

# count words
scores_m = [({}) for i in range(file_num)]

path = 'F:\\paper\\myPython\\py2.7\\final_raw'
all_words = {}
bloblist = []
file_name = []
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        with open(file_path, 'r') as in_data:
            in_data_tmp = in_data
            text = in_data_tmp.read()
            tokens = nltk.word_tokenize(text)
            for each in tokens:
                all_words[each] = 1
            print len(all_words)

for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        with open(file_path, 'r') as in_data:
            string = ''
            for line in in_data.readlines():
                string = string + line.decode('utf-8')
            bloblist.append(tb(string))
            file_name.append(file)
print len(all_words)
for i, blob in enumerate(bloblist):    
    print("TF-IDFs in document " + file_name[i])
    #scores_m[i] = {word: tfidf(word, blob, bloblist) for word in blob.words}
    for word in blob.words:
        cu.execute("""insert into message_TF(user_id, word, TF) values
                          (?, ?, ?)""", (i+1, word, tfidf(word, blob, bloblist)))


cx.commit()
cx.close()

