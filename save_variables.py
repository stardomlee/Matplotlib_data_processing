import numpy as np

###############################################
#In Python, range(start, stop + 1, step) can be used like Matlab's start:step:stop command. 
#Unlike Matlab's functionality, however, range only works when start, step, and stop are 
#all integers. If you want a parallel function that works with floating-point values, try 
#the arange command from numpy:
################################################

with open('numbers.txt', 'w') as handle:
    for n in np.arange(1, 5, 0.1):
        handle.write('{}\n'.format(n))
        
#################################################

f = open("test.txt","wb")                                                                                                                                                                           
for i in range(1,50,5):                                                                                                                                                                             
    f.write("%d\n"%i)
f.close()
