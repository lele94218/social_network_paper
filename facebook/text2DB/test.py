# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 10:21:43 2015

@author: Keine
"""
file_num = 49
vis = [([0] * file_num) for i in range(file_num)]
out = open('F:\\paper\\myPython\\py2.7\\similarity\\old_sim_result.txt', 'w')
for i in range(file_num):
    for j in range(file_num):
        vis[i][j] = 1
        if i == j or vis[j][i] == 1:
            continue
        print '%d %d\n' %(i,j)
