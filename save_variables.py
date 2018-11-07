import numpy as np

with open('numbers.txt', 'w') as handle:
    for n in np.arange(1, 5, 0.1):
        handle.write('{}\n'.format(n))
