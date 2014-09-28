# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 21:22:53 2014

@author: John
"""
import os
from pprint import pprint

os.system("cls")


f = open("C:\Users\John\.spyder2\JulyData\JulyData2.txt","r")
array = []
for line in f:
    line = line.strip('\xef\xbb\xbf\n')   
    b = line.split(";")
    array.append(b)

for i1, inner_l in enumerate(array):
        array[i1][0] = int(array[i1][0])
        array[i1][1] = float(array[i1][1])
        array[i1][2] = float(array[i1][2])
        array[i1][3] = float(array[i1][3])


pprint(array)

