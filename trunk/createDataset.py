# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 20:47:58 2014

@author: John
"""
import dexdata as dex
from datetime import datetime
import time
import os
from pprint import pprint
import numpy as np
import gzip, cPickle
import theano.tensor as T
from theano import function
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
    
def readDataset(filename):
    f = open(filename,"r")
    array = []
    for line in f:
        line = line.strip('\xef\xbb\xbf\n')   
        b = line.split(";")
        array.append(b)
    
    for i1, inner_l in enumerate(array):
            array[i1][0] = float(array[i1][0])
            array[i1][1] = float(array[i1][1])
            array[i1][2] = float(array[i1][2])
    return array
    
def buildDataset(array):
    arr_len = len(array) - 2
    savefile = savepath + "dex3Data(built).txt"
    f = open(savefile,'w')
    for i in range(arr_len):
        i1 = i+1
        i2 = i+2
        line = str(array[i][0])+";"+str(array[i1][0])+";"+str(array[i][1])+";"+ str(array[i1][1])+";"+str(array[i][2])+";"+str(array[i1][2])+";"
        if(array[i2][0]>array[i1][0]):
            target = 1
        else:
            target = 0     
        line = line+str(target)+"\n"
        f.write(line)
    f.close()            

def createPklDataset(filename):

    size = 6
    
    f = open(filename,"r")
    X = []
    Y = []
    
    for line in f:
            line = line.strip('\n')  
            b = line.split(';')
            b[0] = float(b[0])
            b[1] = float(b[1])
            b[2] = float(b[2])
            b[3] = float(b[3])
            b[4] = float(b[4])
            b[5] = float(b[5])
            b[6] = int(b[6])
            x_temp = (b[0:6])
            X.append(x_temp)
            Y.append(b[6])
    
    data_file = gzip.open('C:\Python27\Lib\data\dex.pkl.gz','wb')
    #data_file = gzip.open('dex.pkl.gz','wb')
    
    train_set_x = np.ndarray((3000,size), dtype = 'float64')
    #train_set_y = np.ndarray((2000,1), dtype = 'int64')
    
    for a in range(0,3000):
        train_set_x[a] = X[a]
        #train_set_y[a] = Y[a]
    
    train_set_y = np.array(Y[0:3000])
    
    train_set = ((train_set_x),(train_set_y))
    
    
    
    valid_set_x = np.ndarray((100,size), dtype = 'float64')
    #valid_set_y = np.ndarray((600,1), dtype = 'int64')
    
    for a in range(0,100):
        b = a + 3000
        valid_set_x[a] = X[b]
        #valid_set_y[a] = Y[b]
    valid_set_y = np.array(Y[3000:3100])
        
    valid_set = ((valid_set_x),(valid_set_y))
    
    
    
    test_set_x = np.ndarray((820,size), dtype = 'float64')
    #test_set_y = np.ndarray((550,1), dtype = 'int64')
    
    for a in range(0,820):
        b = a + 820
        test_set_x[a] = X[b]
        #test_set_y[a] = Y[b]
    test_set_y = np.array(Y[3100:3920])    
        
    test_set = ((test_set_x),(test_set_y))
    
    dataset = [train_set, valid_set, test_set]
    cPickle.dump(dataset,data_file,-1)
    data_file.close()

    
    
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
    arr = readDataset(savepath + "dex3Data.txt")
#    pprint(arr)
    buildDataset(arr)
    createPklDataset(savepath + "dex3Data(built).txt")