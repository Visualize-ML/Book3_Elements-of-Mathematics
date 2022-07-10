
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch18_03

from sympy import oo, erf, lambdify
import numpy as np

x_array = np.linspace(-3,3,100)

erf_x_fcn = lambdify(x,erf(x))
y_array = erf_x_fcn(x_array)

fig, ax = plt.subplots()
ax.plot(x_array, y_array, 'b')

ax.axhline(y = erf(oo), color = 'r', linestyle = '-')
ax.axhline(y = erf(-oo), color = 'r', linestyle = '-')
ax.axhline(y = erf(0), color = 'r', linestyle = '-')

ax.set_xlim(x_array.min(), x_array.max())
ax.set_ylim(-1,1)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
ax.set_xlabel('x')
ax.set_ylabel('erf(x)')
ax.grid(linestyle='--', linewidth=0.25, color=[0.75,0.75,0.75])
