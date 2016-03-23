# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 10:16:52 2015

@author: Keine
"""
import sqlite3

cx = sqlite3.connect("../text2DB/get_data.db")
distxy = [([0.0] * 49) for i in range(49)]
cu = cx.cursor()
for i in range(49):
    for j in range(49):
        if i == j:
            distxy[i-1][j-1] = 0.0
        else:
            print i
            print j
            sql = cu.execute("""select similarity from old_similarity where id1 = ? and id2 = ?""", (i,j))
            if sql.fetchall() == []:
                sim = 0
            else:
                sql = cu.execute("""select similarity from old_similarity where id1 = ? and id2 = ?""", (i,j))
                sim = float(sql.fetchone()[0])
            distxy[i][j] = sim
cx.close();
#print distxy[49-1][48-1]
#from scipy.cluster.hierarchy import linkage, dendrogram

#R = dendrogram(linkage(distxy, method='complete'))

#suptitle('Cluster Dendrogram', fontweight='bold', fontsize=14);

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
data_dist = pdist(distxy) # computing the distance
data_link = linkage(data_dist) # computing the linkage
dendrogram(data_link)
plt.xlabel('User_ID')
plt.ylabel('Similarity ratio')
plt.suptitle('Hierarchy Clustering', fontweight='bold', fontsize=14);

