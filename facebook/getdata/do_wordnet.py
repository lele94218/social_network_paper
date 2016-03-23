from __future__ import division
import re
import os
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn
from munkres import Munkres, print_matrix

#transfer tags
def get_wordnet_pos(pos_tag):
    if pos_tag.startswith('J'):
        return wn.ADJ
    elif pos_tag.startswith('V'):
        return wn.VERB
    elif pos_tag.startswith('N'):
        return wn.NOUN
    elif pos_tag.startswith('R'):
        return wn.ADV
    else:
        return ''

#Tokenize text
path = 'F:\\paper\\myPython\\py2.7\\key_words\\'
#path = 'F:\\paper\\myPython\\py2.7\\test\\a\\'
map = {}
out = open('F:\\paper\\myPython\\py2.7\\similarity\\sim_result.txt', 'w')
for subdir, dirs, files in os.walk(path):
    count = len(files) - 1
    for each in files:
        map[each] = 0
    for file1 in files:
        for file2 in files:
            if (file1 == file2 or map[file1] >= count or map[file2] >= count):
                continue
            print file1 + ' ' + file2
            out.write(file1 + ' ' + file2 + '\n')
            tokenizer = RegexpTokenizer(r'\w+')
            word1 = tokenizer.tokenize(file(path + file1).read().decode('utf-8'))
            word2 = tokenizer.tokenize(file(path + file2).read().decode('utf-8'))
            map[file1] = map[file1] + 1
            map[file2] = map[file2] + 1
            #tag1 = nltk.pos_tag(word1)
            #tag2 = nltk.pos_tag(word2)
            n_word1 = []
            n_word2 = []
            for i, word in enumerate(word1):
                ll = wn.synsets(word)
                if ll == []:
                    continue
                else:
                    n_word1.append(wn.synsets(word)[0])
            for i, word in enumerate(word2):
                ll = wn.synsets(word)
                if ll == []:
                    continue
                else:                    
                    n_word2.append(wn.synsets(word)[0])
            row = len(n_word1)
            col = len(n_word2)
            print '%d %d ' %(row, col)
            matrix_r = [([0] * col) for i in range(row)]
            for i, word1 in enumerate(n_word1):
                for j, word2 in enumerate(n_word2):
                    if word1.path_similarity(word2) == None:
                        matrix_r[i][j] = 0.0
                    else:
                        matrix_r[i][j] = word1.path_similarity(word2)
            print 'ok1'
            #with open('F:\\paper\\myPython\\py2.7\\similarity\\test0.txt', 'w') as write:
            #    for i in range(len(matrix_r)):
            #        for j in range(len(matrix_r[i])):
            #            write.write('%lf ' %(matrix_r[i][j]))
            #        write.write('\n')
            #print 'finish'
            
#Kuhn Munkras Algorithm solves the assignment problem of words to words
#Algorithm complexity is O(m^2*n)
            m = Munkres()
            indexes = m.compute(matrix_r)
            print 'ok2'
            total = 0.0
            for row, column in indexes:
                value = matrix_r[row][column]
                total += value
                #print '(%d, %d) -> %lf' % (row, column, value)
            print 'total cost: %lf' % total
            print 'similarity: %f' % float(2.0 * total / (row + col))
            out.write('total cost: %lf' % total + '\n')
            out.write('similarity: %f' % float(2.0 * total / (row + col)) + '\n\n')
            
            
        




