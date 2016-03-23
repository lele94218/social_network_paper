# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 10:01:04 2015

@author: Keine
"""

import sqlite3
import os

file_path = "../similarity/old_sim_result.txt"
cx = sqlite3.connect("./get_data.db")
cu = cx.cursor()
id1 = ''
id2 = ''
sim = 0.0
with open(file_path, 'r') as in_data:
    for line in in_data.readlines():
        if line.strip() == "":
            cu.execute("""insert into old_similarity (id1, id2, similarity) values
                          (?,?,?)""", (id1, id2, sim))
            cu.execute("""insert into old_similarity (id1, id2, similarity) values
                          (?,?,?)""", (id2, id1, sim))
            print id1 + ' ' + id2
        elif '.' in line:
            sim = float(line.strip())
        else:
            id1 = line.split(' ')[0].strip()
            id2 = line.split(' ')[1].strip()
cx.commit()
cx.close()

