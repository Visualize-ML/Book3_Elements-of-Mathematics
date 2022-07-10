
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch11_02

import numpy as np
import matplotlib.pyplot as plt

a_array = np.linspace(1,6,6)
x_array = np.linspace(-2,2,100)

aa, xx = np.meshgrid(a_array,x_array)
ww = aa*xx**2

fig, ax = plt.subplots()

colors = plt.cm.jet(np.linspace(0,1,6))

for i in np.linspace(1,6,6):
    plt.plot(x_array,ww[:,int(i)-1],
             color = colors[int(i)-1],
             label = '$a = {lll:.0f}$'.format(lll = a_array[int(i)-1]))

plt.xlabel('x'); plt.ylabel('f(x)')
plt.legend()
plt.xticks(np.arange(-2, 2.5, step=0.5)); plt.yticks(np.arange(0, 4.5,  step=0.5))
plt.axis('scaled')
ax.set_xlim(-2,2); ax.set_ylim(0,4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
