import numpy as np

with open('numbers.txt', 'w') as handle:
    for n in np.arange(1, 5, 0.1):
        handle.write('{}\n'.format(n))
-----------------------------------------------------

f = open("test.txt","wb")                                                                                                                                                                           
for i in range(1,50,5):                                                                                                                                                                             
    f.write("%d\n"%i)
f.close()
