
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


# Bk3_Ch12_02

import matplotlib.pyplot as plt

def plot_curve(x_array, y_array, 
               x_array_new, y_array_new):

    fig, ax = plt.subplots()
    
    plt.plot(x_array, y_array, color = '#0070C0',
             label = 'Original')
    
    ax.fill_between(x_array,
                    y_array, 
                    edgecolor = 'none', 
                    facecolor = '#0070C0',
                    alpha = 0.2)

    plt.plot(x_array_new, y_array_new, color = 'r',
             label = 'Transformed')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(y=0, color='k', linestyle='-')
    plt.axvline(x=0, color='k', linestyle='-')
    plt.xticks(np.arange(-4, 4+1, step=1))
    plt.yticks(np.arange(-4, 4+1, step=1))
    plt.axis('scaled')
    
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.legend()
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
    
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

import numpy as np
from sympy.abc import x
from sympy import exp, lambdify

x_array = np.arange(-4,4+0.01, step = 0.01)
f_x = 2*exp(- (x-1)**2);

f_x_fcn = lambdify([x],f_x)

f_x_array = f_x_fcn(x_array) # original function

#%% vertical shift

for c in [2,-3]:
    
    f_x_array_new = f_x_array + c
    
    plot_curve(x_array, f_x_array, 
               x_array, f_x_array_new)


#%% horizontal shift

for c in [3,-1]:

    f_x_new = 2*exp(- ((x+c)-1)**2);
    f_x_new_fcn = lambdify([x],f_x_new)
    
    f_x_array_new = f_x_new_fcn(x_array)
    
    plot_curve(x_array, f_x_array, 
               x_array, f_x_array_new)

#%% vertical scaling

for c in [1/2,2]:
    
    f_x_array_new = c*f_x_array
    
    plot_curve(x_array, f_x_array, 
               x_array, f_x_array_new)

#%% horizontal scaling 

for c in [1/2,2]:

    f_x_new = 2*exp(- (c*x-1)**2);
    f_x_new_fcn = lambdify([x],f_x_new)
    
    f_x_array_new = f_x_new_fcn(x_array)
    
    plot_curve(x_array, f_x_array, 
               x_array, f_x_array_new)
    
#%% reflection about x-axis

f_x_array_new = -f_x_array

plot_curve(x_array, f_x_array, 
           x_array, f_x_array_new)

#%% reflection about y-axis

f_x_new = 2*exp(- (-x-1)**2);
f_x_new_fcn = lambdify([x],f_x_new)

f_x_array_new = f_x_new_fcn(x_array)

plot_curve(x_array, f_x_array, 
           x_array, f_x_array_new)
