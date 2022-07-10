
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch11_01

import numpy as np
import matplotlib.pyplot as plt

w_array = np.array([1/5,1/4,1/3,1/2,1,2,3,4,5])
x_array = np.linspace(-2,2,100)

ww, xx = np.meshgrid(w_array,x_array)

b = 0 # y intercept
ff = ww*xx + b

fig, ax = plt.subplots()

colors = plt.cm.jet(np.linspace(0,1,len(w_array)))

for i in np.linspace(1,len(w_array),len(w_array)):
    plt.plot(x_array,ff[:,int(i)-1],
             color = colors[int(i)-1],
             label = '$w_1 = {lll:.2f}$'.format(lll = w_array[int(i)-1]))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.xticks(np.arange(-2, 2.5, step=0.5))
plt.yticks(np.arange(-2, 2.5,  step=0.5))
plt.axis('scaled')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
