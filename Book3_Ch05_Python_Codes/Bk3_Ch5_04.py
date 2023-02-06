
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch5_04

import numpy as np
import matplotlib.pyplot as plt

def plot_polar(theta, r):

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    # set radial axis limit
    ax.set_rmax(20)
    # set radial axis ticks
    ax.set_rticks([5, 10, 15, 20])  
    # position radial labels
    ax.set_rlabel_position(-45)  
    ax.set_thetagrids(np.arange(0.0, 360.0, 45.0)); 
    plt.show()
    
#%% circle
theta = np.linspace(0, 6*np.pi, 1000)

r = 10 + theta*0
plot_polar(theta, r)

#%% Archimedes' spiral
r = 1*theta
plot_polar(theta, r)

#%% Rose
r = 10*np.cos(6*theta) + 10
plot_polar(theta, r)

