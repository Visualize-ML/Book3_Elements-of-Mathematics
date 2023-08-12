
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch5_02

import numpy as np
import matplotlib.pyplot as plt

def fig_decor(ax):

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    ax.hlines(y=0, xmin=-8, xmax=8, color='k')
    ax.vlines(x=0, ymin=-8, ymax=8, color='k')
    
    ax.set_xticks(np.arange(-8, 8 + 1, step=1))
    ax.set_yticks(np.arange(-8, 8 + 1, step=1))
    
    ax.axis('scaled')
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

    ax.set_xbound(lower = -8, upper = 8)
    ax.set_ybound(lower = -8, upper = 8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

x_array = np.linspace(-8,8)
y_array = np.linspace(-8,8)

# orthogonal
fig, ax = plt.subplots()

y1 = 0.5*x_array + 2
y2 = -2*x_array - 1

ax.plot(x_array, y1)
ax.plot(x_array, y2)
fig_decor(ax)

# parallel
fig, ax = plt.subplots()

y1 = 0.5*x_array + 2
y2 = 0.5*x_array - 4

ax.plot(x_array, y1)
ax.plot(x_array, y2)
fig_decor(ax)

# horizontal
fig, ax = plt.subplots()

y1 = 0*x_array + 2
y2 = 0*x_array - 4

ax.plot(x_array, y1)
# axhline
ax.plot(x_array, y2)
fig_decor(ax)

# vertical
fig, ax = plt.subplots()

x1 = 0*y_array + 2
x2 = 0*y_array - 4

ax.plot(x1, y_array)
# axvline
ax.plot(x2, y_array)
fig_decor(ax)
