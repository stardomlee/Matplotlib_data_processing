import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Results/')
#plot_name = "sample"

if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
    
# this is just for testing.
plt.plot([1,2,3,4])
plt.ylabel('some numbers')

plt.savefig(results_dir + 'plot_name.eps', dpi=300)
