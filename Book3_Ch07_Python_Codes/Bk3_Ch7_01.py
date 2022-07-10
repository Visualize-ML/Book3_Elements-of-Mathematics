
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch7_01

import matplotlib.pyplot as plt
import numpy as np

x_A = -4
y_A = 6

x_B = 5
y_B = -6

x_M = (x_A + x_B)/2
y_M = (y_A + y_B)/2

fig, ax = plt.subplots()

plt.plot(x_A,y_A, 'x', markersize = 12)

plt.plot(x_B,y_B, 'x', markersize = 12)

x_points = [x_A,x_B,x_M]
y_points = [y_A,y_B,y_M]

plt.plot(x_points,y_points)
plt.plot(x_points,y_points)

labels = ['A', 'B', 'M']

plt.plot(x_points, y_points, 'x')

for label, i, j in zip(labels, x_points, y_points):
   plt.text(i, j+0.5, label + ' ({}, {})'.format(i, j))

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.xticks(np.arange(-8, 8 + 1, step=1))
plt.yticks(np.arange(-8, 8 + 1, step=1))
plt.axis('scaled')

ax.set_xlim(-8,8)
ax.set_ylim(-8,8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
