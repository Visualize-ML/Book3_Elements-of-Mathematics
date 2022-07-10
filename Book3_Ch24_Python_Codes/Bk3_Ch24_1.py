
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch24_1

from sympy.abc import a
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

# generate data

num_chickens = np.array([32, 110, 71, 79, 45, 20, 56, 55, 87, 68, 87, 63, 31, 88])
num_rabbits  = np.array([22, 53, 39, 40, 25, 15, 34, 34, 52 , 41, 43, 33, 24, 52])
# scatter plot

fig, ax = plt.subplots()

plt.scatter(num_chickens, num_rabbits)

fig_decor(ax)

#%% generate f(a), sum of squared errors (SSE), symbolic

from sympy import *

y_pred = a*num_chickens

f_a_SSE = np.sum((num_rabbits - y_pred)**2)

f_a_SSE = simplify(f_a_SSE)

print(f_a_SSE)

#%% plot f(a) versus a

a_array = np.linspace(0,1,51)

f_a_SSE_fcn = lambdify(a, f_a_SSE)

SSE_array = f_a_SSE_fcn(a_array)

# first-order differential
df_da_SSE = diff(f_a_SSE, a)
print(df_da_SSE)

# solution of a
a_star_only = solve(df_da_SSE, a)

print(a_star_only)

a_star_only = a_star_only[0].evalf()

SSE_min = f_a_SSE_fcn(a_star_only)

fig, ax = plt.subplots()

plt.plot(a_array, SSE_array)
plt.axvline(x=a_star_only, linestyle = '--')
plt.plot(a_star_only, SSE_min, 'rx', markersize = 16)

plt.xlabel('a, slope')
plt.ylabel('f(a), sum of squared errors, SSE')
ax.set_xlim([a_array.min(), a_array.max()])
ax.set_ylim([0, SSE_array.max()])

ax.grid(linestyle=':', linewidth='0.5', color=[0.8, 0.8, 0.8])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#%% y = ax model

def plot_square(x,y1,y2):
    
    if y2 > y1:
        temp = y2;
        y2 = y1;
        y1 = temp;

    d = y1 - y2;
    
    plt.fill(np.vstack((x, x + d, x + d, x)), 
             np.vstack((y2, y2, y1, y1)),
             facecolor='b', edgecolor='none',
             alpha = 0.3)

x_array = np.linspace(0,150,10)[:, None]

y_pred = a_star_only*x_array

fig, ax = plt.subplots()

plt.plot(x_array, y_pred, color = 'r')
plt.scatter(num_chickens, num_rabbits)

num_rabbits_predicted = a_star_only*num_chickens

plt.plot(np.vstack((num_chickens,num_chickens)),
         np.vstack((num_rabbits, num_rabbits_predicted)),
         color = np.array([255,182,0])/255)

for i in range(0,len(num_rabbits_predicted)):
    plot_square(num_chickens[i],num_rabbits[i],num_rabbits_predicted[i]); 
        
fig_decor(ax)

