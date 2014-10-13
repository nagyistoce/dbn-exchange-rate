# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 20:47:58 2014

@author: John
"""
import dexdata as dex
from pprint import pprint

filepath = "C:\\JulyData\\Data\\INTLFXD_csv_2\\data\\"
savepath = "C:\\Python27\\Lib\\site-packages\\xy\\Projects\\Data\\"
file1 = filepath + "DEXJPUS.csv"
file2 = filepath + "DEXUSUK.csv"
file3 = filepath + "DEXUSEU.csv"

def createDataset():
    JPUS = dex.getCsvData(file1)
    USUK = dex.getCsvData(file2)
    USEU = dex.getCsvData(file3)
    
    JPUS = normalizeSet(JPUS)
    USUK = normalizeSet(USUK)
    USEU = normalizeSet(USEU)
    
    common_table_keys = JPUS.viewkeys() & USUK.viewkeys() & USEU.viewkeys()
#    print common_table_keys
    savefile = savepath + "dex3Data.txt"
    f = open(savefile,'w')
    for item1 in common_table_keys:
        line = str(JPUS[item1])+";"+str(USUK[item1])+";"+str(USEU[item1])+"\n"
        f.write(line)
    f.close()
    #pprint(common_table_keys)
    
    
    
    
def normalizeSet(set):
    max = 0
    for key, value in set.items():
        if(max < value):
            max = value
    d = dict()
    for key, value in set.items():
        d[key] = value / max
    return d
    
def common_keys(a,b):
    return set(a).intersection(set(b))


if __name__ == '__main__':
    createDataset()