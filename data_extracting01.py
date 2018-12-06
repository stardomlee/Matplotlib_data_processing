import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('angular.txt')
y = np.array(data[:])


b = data[data[:,0]>2,1]
c = data[data[:,0]<5,1]

idx = np.where ((data[:,1]<10) & (data[:,1]>1))
print y[:,2][idx]
print b

