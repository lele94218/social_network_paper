# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 19:56:28 2014

@author: Keine
"""
import sqlite3

cx = sqlite3.connect("../text2DB/get_data.db")
distxy = [([0.0] * 49) for i in range(49)]
cu = cx.cursor()
for i in range(1, 50):
    for j in range(1, 50):
        if i == j:
            distxy[i-1][j-1] = 0.0
        else:
            sql = cu.execute("""select similarity from user_similarity where id1 = ? and id2 = ?""", (i,j))
            sim = 1.0 - float(sql.fetchone()[0]) - 0.98
            distxy[i-1][j-1] = sim
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