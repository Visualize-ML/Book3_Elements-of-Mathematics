# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:19:50 2022

@author: james
"""

# Bk3_Ch24_4

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def fig_decor(ax):
    
    plt.xlabel('$x$ (number of chickens)')
    plt.ylabel('$y$ (number of rabbits)')
    
    plt.axis('scaled')
    ax.set_xlim([0, 120])
    ax.set_ylim([0, 80])
    
    plt.xticks(np.arange(0, 120 + 1, step=10))
    plt.yticks(np.arange(0, 80 + 1,  step=10))
    plt.minorticks_on()
    ax.grid(which='minor', linestyle=':', 
            linewidth='0.5', color=[0.8, 0.8, 0.8])
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

num_chickens = np.array([32, 110, 71, 79, 45, 20, 56, 55, 87, 68, 87, 63, 31, 88])
num_rabbits  = np.array([22, 53, 39, 40, 25, 15, 34, 34, 52, 41, 43, 33, 24, 52])

sigma_X = num_chickens.std(ddof = 1)
sigma_Y = num_rabbits.std(ddof = 1)
rho_XY = np.corrcoef(num_chickens, num_rabbits)[1][0]
mean_X = num_chickens.mean()
mean_Y = num_rabbits.mean()

a = rho_XY*sigma_Y/sigma_X
b = -a*mean_X + mean_Y

print('=== Slope, a ===')
print(a)
print('=== Intercept, b ===')
print(b)

x_array = np.linspace(0,120,20)
fig, ax = plt.subplots()
sns.regplot(x=num_chickens, y=num_rabbits, ax = ax,  truncate=False,
            line_kws={"color": "red"});

plt.plot(mean_X,mean_Y, marker = 'x', markerfacecolor = 'r',
         markersize = 12)
fig_decor(ax)

#%% use sklearn

from sklearn.linear_model import LinearRegression

x = num_chickens.reshape((-1, 1))
y = num_rabbits

model = LinearRegression().fit(x, y)
print('Slope, a:', model.coef_)
print('Intercept, b:', model.intercept_)
