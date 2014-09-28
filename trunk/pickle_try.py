# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 22:16:27 2014


@author: John
"""
from datetime import datetime
import time
import os
from pprint import pprint
import numpy as np
import gzip, cPickle
import theano.tensor as T
from theano import function


os.system("cls")

filename = "C:\Users\John\Documents\MATLAB\completeData.txt"


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
        X.append(b[:16])
        Y.append(b[17])

Len = len(X);
X = np.asmatrix(X)
Y = np.asarray(Y)

sizes = [0.8, 0.1, 0.1]
arr_index = int(sizes[0]*Len)
arr_index2_start = arr_index + 1
arr_index2_end = arr_index + int(sizes[1]*Len)
arr_index3_start = arr_index2_start + 1

"""
train_set_x = np.array(X[:arr_index])
train_set_y = np.array(Y[:arr_index])

val_set_x = np.array(X[arr_index2_start:arr_index2_end])
val_set_y = np.array(Y[arr_index2_start:arr_index2_end])

test_set_x = np.array(X[arr_index3_start:])
test_set_y = np.array(X[arr_index3_start:])

train_set = train_set_x, train_set_y
val_set = val_set_x, val_set_y
test_set = test_set_x, test_set_y
"""
x = T.dmatrix('x')
z = x
t_mat = function([x],z)

y = T.dvector('y')
k = y
t_vec = function([y],k)

train_set_x = t_mat(X[:arr_index].T)
train_set_y = t_vec(Y[:arr_index])
val_set_x = t_mat(X[arr_index2_start:arr_index2_end].T)
val_set_y = t_vec(Y[arr_index2_start:arr_index2_end])
test_set_x = t_mat(X[arr_index3_start:].T)
test_set_y = t_vec(Y[arr_index3_start:])

train_set = train_set_x, train_set_y
val_set = val_set_x, val_set_y
test_set = test_set_x, test_set_y

dataset = [train_set, val_set, test_set]

f = gzip.open('dex.pkl.gz','wb')
cPickle.dump(dataset, f, protocol=2)
f.close()

pprint(train_set_x.shape)

print('Finished\n')

#print(dataset)