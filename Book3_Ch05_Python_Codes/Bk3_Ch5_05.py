
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch5_05

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,100)

# parametric equation of unit circle
x1 = np.cos(t)
x2 = np.sin(t)

fig, ax = plt.subplots()
# plot the circle
plt.plot(x1,x2)

plt.show()
ax.set_xlabel('$x_1$'); ax.set_ylabel('$x_2$')
ax.set_xticks(np.arange(-2, 2 + 1, step=1))
ax.set_yticks(np.arange(-2, 2 + 1, step=1))
ax.axis('scaled')
ax.grid(linestyle='--', linewidth=0.25, color=[0.7,0.7,0.7])
ax.set_xbound(lower = -2, upper = 2); ax.set_ybound(lower = -2, upper = 2)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
