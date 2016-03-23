# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 22:21:19 2014

@author: Keine
"""

import sqlite3
import os

file_path = "../similarity/sim_result.txt"
cx = sqlite3.connect("./get_data.db")
cu = cx.cursor()
with open(file_path, 'r') as in_data:
    for line in in_data.readlines():
        if line.strip() == "":
            #print sim + ' ' + cos + ' ' + name1 + ' ' + name2
            id1 = cu.execute("""select id from user_text where name = ?""", [name1]).fetchone()
            id2 = cu.execute("""select id from user_text where name = ?""", [name2]).fetchone()
            #id1[0] id2[0]
            cu.execute("""insert into user_similarity (id1, id2, similarity, total_cost) values
                          (?,?,?,?)""", (id1[0], id2[0], sim, cos))
            cu.execute("""insert into user_similarity (id1, id2, similarity, total_cost) values
                          (?,?,?,?)""", (id2[0], id1[0], sim, cos))
            print name1 + ' ' + name2
        elif line[:3] == 'tot':
            cos = float(line.split(' ')[2].strip())
        elif line[:3] == 'sim':
            sim = float(line.split(' ')[1].strip())
        else:
            name1 = ((line.split(' ')[0]).split('.')[0]).split('_')[0].strip()
            name2 = ((line.split(' ')[1]).split('.')[0]).split('_')[0].strip()
cx.commit()
cx.close()
