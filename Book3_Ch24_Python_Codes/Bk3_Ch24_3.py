
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch24_3

import numpy as np
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

# scatter plot

fig, ax = plt.subplots()

plt.scatter(num_chickens, num_rabbits)

fig_decor(ax)

#%% proportional function, y = ax

x_array = np.linspace(0,150,10)[:, None]

x = num_chickens[:, None]
y = num_rabbits[:, None]

a_star_only = np.linalg.inv(x.T@x)@x.T@y

y_pred = a_star_only*x_array

fig, ax = plt.subplots()

plt.plot(x_array, y_pred, color = 'r')
plt.scatter(num_chickens, num_rabbits)

fig_decor(ax)

#%% linear function, y = ax + b

X = np.hstack((np.ones_like(x),x))

sol = np.linalg.inv(X.T@X)@X.T@y

a_star_ = sol[0]
b_star_ = sol[1]


a_star, b_star = np.polyfit(num_chickens, num_rabbits, 1)
y_pred = a_star*x_array + b_star

fig, ax = plt.subplots()

plt.plot(x_array, y_pred, color = 'r')
plt.scatter(num_chickens, num_rabbits)

fig_decor(ax)
