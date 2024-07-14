
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch5_03

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x_array = np.arange(0, 30 + 1, step=1)
y_line_1 = 35 - x_array
y_line_2 = (94 - 2*x_array)/4

fig, ax = plt.subplots()

plt.plot(x_array, y_line_1, color = '#0070C0')
plt.plot(x_array, y_line_2, color = 'g')

# solution of linear equations
plt.plot(23,12,marker = 'x', markersize = 12)
plt.axvline(x=23, color='r', linestyle='--')
plt.axhline(y=12, color='r', linestyle='--')

plt.xlabel('$x_1$ (number of chickens)')
plt.ylabel('$x_2$ (number of rabbits)')
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.xticks(np.arange(0, 30 + 1, step=5))
plt.yticks(np.arange(0, 30 + 1, step=5))
plt.axis('scaled')
plt.minorticks_on()
ax.grid(which='minor', linestyle=':', 
        linewidth='0.5', color=[0.8, 0.8, 0.8])
ax.set_xlim(0,30); ax.set_ylim(0,30)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
