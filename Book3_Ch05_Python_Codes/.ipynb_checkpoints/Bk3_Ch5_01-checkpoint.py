
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch5_01

import matplotlib.pyplot as plt
import numpy as np

x = [4,  0, -5, -4,  6, 0]
y = [2, -2,  7, -6, -5, 0]

labels = ['A', 'B', 'C', 'D', 'E', 'O']

fig, ax = plt.subplots()

plt.plot(x, y, 'x')

for label, i, j in zip(labels, x, y):
   plt.text(i, j+0.5, label + ' ({}, {})'.format(i, j))

plt.xlabel('x'); plt.ylabel('y')
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.xticks(np.arange(-8, 8 + 1, step=1))
plt.yticks(np.arange(-8, 8 + 1, step=1))
plt.axis('scaled')

ax.set_xlim(-8,8); ax.set_ylim(-8,8)
ax.spines['top'].set_visible(False); ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False); ax.spines['right'].set_visible(False)

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
