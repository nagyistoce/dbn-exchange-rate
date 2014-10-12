
from datetime import datetime
import time
import os
from pprint import pprint
import numpy as np
import gzip, cPickle
import theano.tensor as T
from theano import function


os.system("cls")

filename = "completeData.txt"
size =4

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
        b[6] = float(b[6])
        b[7] = float(b[7])
        b[8] = float(b[8])
        b[9] = float(b[9])
        b[10] = float(b[10])
        b[11] = float(b[11])
        b[12] = float(b[12])
        b[13] = float(b[13])
        b[14] = float(b[14])
        b[15] = float(b[15])
        b[17] = int(b[17])
        x_temp = (b[0], b[1], b[2], b[3])
        X.append(x_temp)
        Y.append(b[17])


data_file = gzip.open('..\..\..\data\dex.pkl.gz','wb')
#data_file = gzip.open('dex.pkl.gz','wb')

train_set_x = np.ndarray((2000,size), dtype = 'float64')
#train_set_y = np.ndarray((2000,1), dtype = 'int64')

for a in range(0,2000):
    train_set_x[a] = X[a]
    #train_set_y[a] = Y[a]

train_set_y = np.array(Y[0:2000])

train_set = ((train_set_x),(train_set_y))



valid_set_x = np.ndarray((600,size), dtype = 'float64')
#valid_set_y = np.ndarray((600,1), dtype = 'int64')

for a in range(0,600):
    b = a + 2000
    valid_set_x[a] = X[b]
    #valid_set_y[a] = Y[b]
valid_set_y = np.array(Y[2000:2600])
    
valid_set = ((valid_set_x),(valid_set_y))



test_set_x = np.ndarray((550,size), dtype = 'float64')
#test_set_y = np.ndarray((550,1), dtype = 'int64')

for a in range(0,550):
    b = a + 550
    test_set_x[a] = X[b]
    #test_set_y[a] = Y[b]
test_set_y = np.array(Y[2600:3150])    
    
test_set = ((test_set_x),(test_set_y))

dataset = [train_set, valid_set, test_set]
cPickle.dump(dataset,data_file,-1)
data_file.close()


print "finished!"