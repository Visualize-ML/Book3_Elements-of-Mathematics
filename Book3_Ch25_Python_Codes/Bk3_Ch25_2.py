
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch25_2

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

T = np.matrix([[0.7, 0.2],
               [0.3, 0.8]])

pi_i = np.matrix([[0.6],
                  [0.4]])

all_max = 1
all_min = 0


pi_array = np.vstack((np.linspace(1,0,11),1 - np.linspace(1,0,11)))
pi_array=np.matrix(pi_array)
num_steps = 12

for ini in np.arange(0,np.shape(pi_array)[1]):
    
    pi = pi_array[:,ini]
    

    fig, axes = plt.subplots(1, num_steps + 1, figsize=(12, 3))
    
    for i in np.arange(0,num_steps + 1):
        
        plt.sca(axes[i])
        ax = sns.heatmap(pi,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                         annot = True,fmt=".3f",cbar=False,
                         xticklabels=False, yticklabels=False)
        ax.set_aspect("equal")
        plt.title('$\pi(' + str(i) + ')$')
        ax.tick_params(left=False, bottom=False)
        
        pi = T@pi
