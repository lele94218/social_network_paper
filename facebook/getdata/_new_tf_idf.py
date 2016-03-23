from __future__ import division
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

path = 'F:\\paper\\myPython\\py2.7\\final_raw'

bloblist = []
file_name = []
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        with open(file_path, 'r') as in_data:
            string = ''
            for line in in_data.readlines():
                string = string + line.decode('utf-8')
            bloblist.append(tb(string))
            file_name.append(file)
#with open('F:\\paper\\myPython\\py2.7\\' + 'result.txt', 'w') as out:
for i, blob in enumerate(bloblist):    
    with open('F:\\paper\\myPython\\py2.7\\key_words\\' + file_name[i], 'w') as out:
        print("Top words in document " + file_name[i])
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:200]:
            out.write(word.encode('utf-8') + ' ')
        out.write('\n\n')
        out.close()
