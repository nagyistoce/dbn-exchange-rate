# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 16:46:27 2014

@author: John
"""

import dexdata
import numpy as np
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score, KFold
from sklearn import metrics
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import os
from pprint import pprint

from sklearn.preprocessing import StandardScaler


os.system("cls")
print "Running...."

filename = "C:\JulyData\DEXCHUS.txt"

###############################################################################
# Generate the data

n = 4
X = []
Y = []
xi = []

# Get data
data = dexdata.getDataByDateRange(filename, "2012-01-01", "2014-07-31")
length = len(data)
length = length - n

rev = data[::-1]

# Create target array
for i in reversed(data[n::]):
    Y.append(i[0]) 

# Create 
for j in range(len(Y)):
    xi = []
    for i in (rev[(j+1):(j+n+1)]):
        xi.append(i[1]) 
    X.append(xi)    
    
###############################################################################
# Cross validation
    
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)
    
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.25,random_state=33)
scalerX = StandardScaler().fit(X_train)
scalery = StandardScaler().fit(y_train)
X_train = scalerX.transform(X_train)
y_train = scalery.transform(y_train)
X_test = scalerX.transform(X_test)
y_test = scalery.transform(y_test)
  


  
    
###############################################################################
def train_and_evaluate(clf, X_train, y_train):
    clf.fit(X_train, y_train)
    print "Coefficient of determination on training set:",clf.score(X_train, y_train)
    y_pred = clf.predict(X_train)
    print metrics.accuracy_score(y_train, abs(y_pred))
    for 
    # create a k-fold cross validation iterator of k=5 folds
    cv = KFold(X_train.shape[0], 5, shuffle=True, random_state=33)
    scores = cross_val_score(clf, X_train, y_train, cv=cv)

    print "Average coefficient of determination using 5-fold crossvalidation:", np.mean(scores)
###############################################################################
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.01)
print train_and_evaluate(svr_rbf, X_train, y_train)    
"""
###############################################################################
# Fit regression model
    

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
scores = []
for i in range(10):
    y_rbf = svr_rbf.fit(X_train, y_train)
    y_train_pred = svr_rbf.predict(X_train)
    scores = metrics.accuracy_score(y_train, y_train_pred)
    #scores = cross_validation.cross_val_score(y_rbf, X, Y, cv=5)

print scores
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

"""

