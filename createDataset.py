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
from random import shuffle


filepath = "C:\\JulyData\\Data\\INTLFXD_csv_2\\data\\"
savepath = "C:\\Python27\\Lib\\site-packages\\xy\\Projects\\Data\\"
file1 = filepath + "DEXJPUS.csv"
file2 = filepath + "DEXUSUK.csv"
file3 = filepath + "DEXUSEU.csv"
file4 = "C:\\JulyData\\Commodities\\GOLD.csv"
file5 = "C:\\JulyData\\Commodities\\LIBOR.csv"
file6 = "C:\\JulyData\\Commodities\\OIL.csv"

def runTests():
#    a = { 'b':1, 'c':2, 'e':4, 'a':1}
#    b = { 'b':2, 'd':3, 'e':1, 'a':1}
#    c = { 'b':3, 'c':1, 'j':1, 'e':2, 'a':1}
#    d = { 'b':2, 'd':3, 'k':1, 'a':1}
#    
#    data = [a, b, c, d]
#    k = (a.keys())
#
##    ck = getCommonKeys(k, b)
##    print getCommonKeys(ck, c)
#    print getCommonKeys(data)

    fileTime = "C:\\Python27\\Lib\\site-packages\\xy\\Projects\\Data\\data_days.csv"
    USEU = normalizeSet(dex.getCsvData(file3))
    time = dex.getTimeData(fileTime)
        
        



        
def createDataset():
    JPUS = normalizeSet(dex.getCsvData(file1))
    USUK = normalizeSet(dex.getCsvData(file2))
    USEU = normalizeSet(dex.getCsvData(file3))
    GOLD = normalizeSet(dex.getCsvData(file4))
    LIBOR = normalizeSet(dex.getCsvData(file5))
    OIL = normalizeSet(dex.getCsvData(file6))
    
    data = [USEU, JPUS, USUK, GOLD, LIBOR, OIL]
    
    #common_table_keys = JPUS.viewkeys() & USUK.viewkeys() & USEU.viewkeys()
   
    common_table_keys = getCommonKeys(data)
    #print common_table_keys
    savefile = savepath + "dex3Data.txt"
    f = open(savefile,'w')
    for item1 in common_table_keys:
         
        line = str(JPUS[item1])+";"+ str(USUK[item1])+";"+        str(USEU[item1])+";"+            str(GOLD[item1])+";"+            str(LIBOR[item1])+";"+            str(OIL[item1])+";"+ "\n"
        f.write(line)
    f.close()
    #pprint(common_table_keys)
    
def readDataset(filename, features):
    f = open(filename,"r")
    array = []
    for line in f:
        line = line.strip('\xef\xbb\xbf\n')   
        b = line.split(";")
        array.append(b)
    
    for i1, inner_l in enumerate(array):
        for j in range(features):
            array[i1][j] = float(array[i1][j])
    return array
    
def buildDataset(array, features):
    arr_len = len(array) - 2
    savefile = savepath + "dex3Data(built).txt"
    f = open(savefile,'w')
    for i in range(arr_len):
        i1 = i+1
        i2 = i+2
        line = "";
        for j in range(features):
            if( line == ""):
                line = str(array[i][j])+";"+str(array[i1][j])
            else:
                line = line +";" +str(array[i][j])+";"+str(array[i1][j])
#        line = str(array[i][0])+";"+str(array[i1][0])+";"+str(array[i][1])+";"+ str(array[i1][1])+";"+str(array[i][2])+";"+str(array[i1][2])+";"
        if(array[i2][0]>array[i1][0]):
            target = 1
        else:
            target = 0     
        line = line+";"+str(target)+"\n"
        f.write(line)
    f.close()            

def createPklDataset(filename, features):

    size = features * 2
    set_size = 10
    
    f = open(filename,"r")
    X = []
    Y = []
    
    for line in f:
            line = line.strip('\n')  
            b = line.split(';')
            for a in range(size):
                b[a] = float(b[a])
            b[size] = int(b[size]) 
            x_temp = (b[0:10])
            X.append(x_temp)
            Y.append(b[size])
    
    data_file = gzip.open('C:\Python27\Lib\data\dex.pkl.gz','wb')
    #data_file = gzip.open('dex.pkl.gz','wb')
    
    # shuffles the data for cross validation
    shuffle(X)

    perc = [80, 10, 10]
    l_size = roundValue(len(X))
    train_size = roundValue(int(perc[0]*0.01*l_size))
    valid_size = roundValue(int(perc[1]*0.01*l_size))
    test_size = l_size - (train_size + valid_size)
    

    train_start = 0
    train_end = int(train_size)
    valid_start = int(train_size)
    valid_end = int(train_size + valid_size)
    test_start = int(train_size + valid_size)
    test_end = int(l_size)
    
#### Checking results    
#    print perc[2]*0.01*l_size
#    print l_size ,train_size, valid_size, test_size
#    print train_start ,":", train_end, "==> ", train_end - train_start
#    print valid_start , ":" , valid_end, "==> ", valid_end - valid_start
#    print test_start , ":" , test_end, "==> ", test_end - test_start
    
    
#### Train set
    train_set_x = np.ndarray((train_size,set_size), dtype = 'float64') 
    for a in range(0,train_end):
        train_set_x[a] = X[a]
        #train_set_y[a] = Y[a]    
    train_set_y = np.array(Y[train_start:train_end])    
    train_set = ((train_set_x),(train_set_y))
    
    
#### Valid set    
    valid_set_x = np.ndarray((valid_size,set_size), dtype = 'float64')   
    for a in range(0,valid_size):
        b = a + train_size
        valid_set_x[a] = X[b]
        #valid_set_y[a] = Y[b]
    valid_set_y = np.array(Y[valid_start:valid_end])
        
    valid_set = ((valid_set_x),(valid_set_y))
    
    
#### Test set    
    test_set_x = np.ndarray((test_size,set_size), dtype = 'float64')   
    for a in range(0,test_size):
        b = a + train_size + valid_size
        test_set_x[a] = X[b]
        #test_set_y[a] = Y[b]
    test_set_y = np.array(Y[test_start:test_end])    
        
    test_set = ((test_set_x),(test_set_y))
    
    
    
    
    
    dataset = [train_set, valid_set, test_set]
    cPickle.dump(dataset,data_file,-1)
    data_file.close()
    print "Dataset creation complete"
    
    
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

# needs a list of dictionaries
def getCommonKeys(data):
    first_dic = data[0]
    commonkeys = (first_dic.keys())
    for dic in data:
        keys = dic.keys()
        new_list = []
        for element in keys:
            if element in commonkeys:
                new_list.append(element)
        commonkeys = new_list
    return commonkeys

def roundValue(num):
    return abs(num/10)*10


if __name__ == '__main__':
    os.system("cls")

    runTests()
    
#    createDataset()
#    features = 6
#    arr = readDataset(savepath + "dex3Data.txt", 6)
#    buildDataset(arr, 6)
#    createPklDataset(savepath + "dex3Data(built).txt", 6)