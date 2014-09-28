import numpy as np  
from scipy.interpolate import Rbf  
import matplotlib.pyplot as plt 
  
#Reading data from file and adding them to lists
f = open("C:\JulyData\JulyData2.txt","r")
array = []
x = [] #China - US Exchange rate
y = [] #Japan - US Exchange rate
z = [] #US - Euro Exchange rate
date = [] # timestamp for daily exchange rate

for line in f:
    line = line.strip('\xef\xbb\xbf\n')   
    b = line.split(";")
    array.append(b)

for i1, inner_l in enumerate(array):
        date.append(i1)
        x.append(float(array[i1][1]))
        y.append(float(array[i1][2]))
        z.append(float(array[i1][3]))
  
#Creating the figure  
fig = plt.figure(1)
plt.clf()


#Creating the output grid (100x100, in the example)  
ti = np.linspace(0, 22.0, 22)  
 
#Subplot for China - US
plt.subplot(311)
plt.title("China - US") 
plt.plot(date, x, "bo") 
#Creating the interpolation function and populating the output matrix value  
for kind in ['multiquadric', 'inverse', 'gaussian', 'linear', 
             'cubic', 'quintic', 'thin_plate']:
    rbf = Rbf(date, x, function=kind)  
    XI = rbf(ti)   
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.plot(ti, XI, label=kind) 

#Subplot for Japan - US
plt.subplot(312)
plt.title("Japan - US")  
plt.plot(date, y, "bo")  
#Creating the interpolation function and populating the output matrix value  
for kind in ['multiquadric', 'inverse', 'gaussian', 'linear', 
             'cubic', 'quintic', 'thin_plate']:
    rbf = Rbf(date, y, function=kind)  
    YI = rbf(ti)   
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.plot(ti, YI, label=kind)

#Subplot for US - Euro
plt.subplot(313)
plt.title("US - Euro")   
plt.plot(date, z, "bo")   
#Creating the interpolation function and populating the output matrix value  
for kind in ['multiquadric', 'inverse', 'gaussian', 'linear', 
             'cubic', 'quintic', 'thin_plate']:
    rbf = Rbf(date, z, function=kind)  
    ZI = rbf(ti)   
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.plot(ti, ZI, label=kind) 


plt.legend(bbox_to_anchor=(1.05, 1.05), loc='right', borderaxespad=0)
