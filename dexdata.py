# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 12:21:37 2014

@author: John
"""
from datetime import datetime
import time
import os
from pprint import pprint
import csv

os.system("cls")

filename = "C:\JulyData\Data\INTLFXD_csv_2\data\DEXJPUS.csv"
def getData(filename):
    f = open(filename,"r")
    array = []
    readyFlag = False;
    goFlag = False;
    for line in f:
        if "DATE         VALUE" in line:
            readyFlag = True;
        if( goFlag == True):  
            line = line.strip('\n')   
            b = line.split(',')
            b[0] = int(time.mktime(time.strptime(b[0], "%Y-%m-%d")))
            if(b[1] != "."):
                b[1] = float(b[1])
                array.append(b)
        if(readyFlag == True):
            goFlag = True
    #pprint(array)
    return array
    
def getDataAfterDate(filename, date):
    f = open(filename,"r")
    array = []
    readyFlag = False;
    failFlag = False;
    goFlag = False;
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        failFlag = True
    if( failFlag == False ):
            start = int(time.mktime(time.strptime(date, "%Y-%m-%d")))
            for line in f:
                if "DATE         VALUE" in line:
                    readyFlag = True;
                if( goFlag == True): 
                    line = line.strip('\n')   
                    b = line.split()
                    b[0] = int(time.mktime(time.strptime(b[0], "%Y-%m-%d")))
                    if(b[0] >= start):
                        if(b[1] != "."):
                            b[1] = float(b[1])
                            array.append(b)
                if(readyFlag == True):
                    goFlag = True
            return array
    
    
def getDataByDateRange(filename, start, end):
    f = open(filename,"r")
    array = []
    readyFlag = False;
    failFlag = False;
    goFlag = False;
    
    try:
        datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        failFlag = True
    try:
        datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        failFlag = True
        
    if( failFlag == False ):
        end = int(time.mktime(time.strptime(end, "%Y-%m-%d")))
        start = int(time.mktime(time.strptime(start, "%Y-%m-%d")))
        cur_date = 0;
        for line in f:
                if "DATE         VALUE" in line:
                    readyFlag = True;
                if( goFlag == True): 
                    line = line.strip('\n')   
                    b = line.split()
                    cur_date = int(time.mktime(time.strptime(b[0], "%Y-%m-%d")))
                    b[0] = cur_date
                    if(cur_date >= start and cur_date<= end):
                        if(b[1] != "."):
                            b[1] = float(b[1])
                            array.append(b)
                if(readyFlag == True):
                    goFlag = True
    return array

def getCsvData(filename):
    f = open(filename,"r")
    array = dict()
    readyFlag = False;
    goFlag = False;
    for line in f:
        if "DATE,VALUE" in line:
            readyFlag = True;
        if( goFlag == True):  
            line = line.strip('\n')   
            b = line.split(',')
            b[0] = int(time.mktime(time.strptime(b[0], "%Y-%m-%d")))
            if(b[1] != "."):
                b[1] = float(b[1])
                array[b[0]] = (b[1])
        if(readyFlag == True):
            goFlag = True
    #pprint(array)
    return array
   
#pprint(getCsvData(filename))    
#pprint(getDataAfterDate(filename, "2014-01-04"))
#pprint(getDataByDateRange(filename, "2014-01-05", "2014-02-05"))