# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 21:49:05 2014

@author: Keine
"""

import sqlite3
cx = sqlite3.connect("./get_data.db")
cu = cx.cursor()

#create user_text
cu.execute("""create table user_text(
              id    integer primary key autoincrement unique not null,
              name  text not null,
              key_words text not null              
              )""")
              
#create user_similarity
cu.execute("""create table user_similarity(
              id1           integer not null,
              id2           integer not null,
              similarity    real    not null,
              total_cost    real    not null,
              foreign key (id1) references user_text(id),
              foreign key (id2) references user_text(id)              
              )""")

cx.commit()
cx.close()