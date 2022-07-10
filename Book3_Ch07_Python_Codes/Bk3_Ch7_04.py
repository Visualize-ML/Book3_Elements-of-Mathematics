
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch7_04

import matplotlib.pyplot as plt
import numpy as np

def dist(a, b, c, x_A, y_A):
    
    dist_AH = np.abs(a*x_A + b*y_A + c)/np.sqrt(a**2 + b**2)
    
    x_H = (b*(b*x_A - a*y_A) - a*c)/(a**2 + b**2)
    y_H = (a*(-b*x_A + a*y_A) - b*c)/(a**2 + b**2)
    return x_H, y_H, dist_AH

x_A = -4
y_A = 6

a = 1
b = -2
c = -4

x_array = np.linspace(-8,8,10)
y_array = -a/b*x_array - c/b

x_H, y_H, dist_AH = dist(a, b, c, x_A, y_A)

fig, ax = plt.subplots()

plt.plot(x_array, y_array)

plt.plot(x_A,y_A, 'x', markersize = 12)

plt.plot(x_H,y_H, 'x', markersize = 12)

x_points = [x_A,x_H]
y_points = [y_A,y_H]

plt.plot(x_points,y_points)

labels = ['A', 'H']

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
