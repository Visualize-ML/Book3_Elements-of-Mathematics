
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch11_03

import math
import numpy as np
from matplotlib import pyplot as plt 

x = np.linspace(-2,2,100);

def plot_curve(x, y):
    
    fig, ax = plt.subplots()

    plt.xlabel("$\it{x}$") 
    plt.ylabel("$\it{f}(\it{x})$") 
    plt.plot(x, y, linewidth = 1.5) 
    plt.axhline(y=0, color='k', linewidth = 1.5)
    plt.axvline(x=0, color='k', linewidth = 1.5)
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
    plt.axis('equal')
    plt.xticks(np.arange(-2, 2.5, step=0.5))
    plt.yticks(np.arange(y.min(), y.max() + 0.5, step=0.5))
    ax.set_xlim(x.min(),x.max())
    ax.set_ylim(y.min(),y.max())
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.axis('square')

#%% plot linear, quadratic, and cubic functions

plt.close('all')

# linear function
y = x + 1;
plot_curve(x, y)

# linear function
y = -x + 1;
plot_curve(x, y)

# quadratic function, parabola opens upwards
# y = np.power(x,2) - 2;
y = x**2 - 2;
plot_curve(x, y)

# quadratic function, parabola opens downwards
# y = -np.power(x,2) + 2;
y = -x**2 + 2;
plot_curve(x, y)

# cubic function
# y = np.power(x,3) - x;
y = x**3 - x;
plot_curve(x, y)

# cubic function
# y = -np.power(x,3) + x;
y = -x**3 + x;
plot_curve(x, y)
