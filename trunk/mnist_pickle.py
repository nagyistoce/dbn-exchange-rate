# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 21:06:34 2014

@author: John
"""
from logistic_sgd import LogisticRegression, load_data
from datetime import datetime
import time
import os
from pprint import pprint
import numpy as np
import gzip, cPickle

os.system("cls")
dataset = "C:\Python27\Lib\data\mnist.pkl.gz"

datasets = load_data(dataset)

train_set_x, train_set_y = datasets[0]
valid_set_x, valid_set_y = datasets[1]
test_set_x, test_set_y = datasets[2]

print test_set_y