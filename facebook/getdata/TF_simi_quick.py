# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:33:10 2015

@author: Keine
"""

import nltk
import sqlite3
import math
import os

cx = sqlite3.connect("F:\\paper\\myPython\\py2.7\\text2DB\\get_data.db")
cu = cx.cursor()

path = 'F:\\paper\\myPython\\py2.7\\final_raw'
all_words = []
file_name = []
file_num = 49

ix = 0
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        with open(file_path, 'r') as in_data:
            in_data_tmp = in_data
            text = in_data_tmp.read().decode('utf-8')
            tokens = nltk.word_tokenize(text)
            all_words.append(tokens)            


vis = [([0] * file_num) for i in range(file_num)]
out = open('F:\\paper\\myPython\\py2.7\\similarity\\old_sim_result.txt', 'w')
for i in range(file_num):
    for j in range(file_num):
        vis[i][j] = 1
        if i == j or vis[j][i] == 1:
            continue
        res = 0.0
        for each in all_words[i]:
           #print each.encode('utf-8')
            sql1 = cu.execute("""select TF from message_TF where user_id = ? and word = ?""", (i+1, each))
            tf1 = cu.fetchone()[0]
            sql1 = cu.execute("""select TF from message_TF where user_id = ? and word = ?""", (j+1, each))
            if sql1.fetchall() != []:
                sql1 = cu.execute("""select TF from message_TF where user_id = ? and word = ?""", (j+1, each))
                tf2 = cu.fetchone()[0]
                res += (tf1 - tf2) ** 2
            else:
                res += tf1 ** 2
        res = res ** 0.5
        out.write('%d %d' % (i, j) + '\n')
        out.write('%lf' %res + '\n\n')
        
        print '%d %d' % (i, j) + '\n'
        print '%lf' % res + '\n\n'
        
        

cx.commit()
cx.close()


        
        

        
    
    
