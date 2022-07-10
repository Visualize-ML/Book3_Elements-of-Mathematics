
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch25_3

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def draw_vector(vector,RBG, ax): 

    ax.quiver(0, 0, vector[0], vector[1],
               angles='xy', 
               scale_units='xy',
               scale=1,
               color = RBG)

T = np.matrix([[0.7, 0.2],
               [0.3, 0.8]])

all_max = 1
all_min = 0

x1 = np.linspace(-1.1, 1.1, num=201)
x2 = x1
xx1, xx2 = np.meshgrid(x1,x2)
zz = ((np.abs((xx1))**2) + (np.abs((xx2))**2))**(1./2)

pi_array = np.vstack((np.linspace(1,0,11),1 - np.linspace(1,0,11)))
pi_array=np.matrix(pi_array)
num_steps = 12

colors = plt.cm.rainbow(np.linspace(0,1,num_steps + 1))

for ini in np.arange(0,np.shape(pi_array)[1]):
    
    pi = pi_array[:,ini]
    

    fig, ax = plt.subplots(figsize=(10, 10))
    
    # plot a reference line
    plt.plot(x1,1-x1,color = 'k',
             linestyle = '--')
    
    # plot a unit circle as reference
    plt.contour(xx1, xx2, zz, levels = [1], 
                colors='k', linestyles = ['--'])
        
    for i in np.arange(0,num_steps + 1):
        
        # plot normalized vector
        draw_vector(pi/np.linalg.norm(pi), colors[i], ax)
        
        # plot original vector
        draw_vector(pi, colors[i], ax)

        ax.tick_params(left=False, bottom=False)
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        # plt.axis('off')
        ax.axvline(x = 0, color = 'k')
        ax.axhline(y = 0, color = 'k')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.grid(color = [0.8,0.8,0.8])
        plt.xticks(np.linspace(-1,1,21))
        plt.yticks(np.linspace(-1,1,21))

        pi = T@pi
        # update pi
