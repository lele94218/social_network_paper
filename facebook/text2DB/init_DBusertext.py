# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 22:06:15 2014

@author: Keine
"""

import sqlite3
import os

cx = sqlite3.connect("./get_data.db")
cu = cx.cursor()

path = 'F:\\paper\\myPython\\py2.7\\key_words'
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        with open(file_path, 'r') as in_data:
            string = ""
            for line in in_data.readlines():
                string = string + line.decode('utf-8')
            _file = file.split('.')
            name = _file[0].split('_')[0]
            print name
            cu.execute("""insert into user_text(name, key_words) values
                          (?,?)""", (name, string))


cx.commit()
cx.close()