
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch15_02

from sympy import latex, lambdify, limit, log, oo
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 

f_x = 1/(1 + 2**(-1/x))

f_x_fcn = lambdify(x,f_x)

# right limit
x_array_right = np.linspace(0.01,4,500)
f_x_array_right = f_x_fcn(x_array_right)
f_x_0_limit_right = limit(f_x,x,0,'+')

# left limit
x_array_left = np.linspace(-4,-0.01,500)
f_x_array_left = f_x_fcn(x_array_left)
f_x_0_limit_left = limit(f_x,x,0,'-')

# visualization

plt.close('all')

fig, ax = plt.subplots()

ax.plot(x_array_right, f_x_array_right, linewidth = 1.5, color = 'b') 
ax.axhline(y = f_x_0_limit_right, color = 'r')

ax.plot(x_array_left, f_x_array_left, linewidth = 1.5, color = 'b') 
ax.axhline(y = f_x_0_limit_left, color = 'r')

ax.axvline(x = 0,   color = 'k')
ax.axhline(y = 0.5, color = 'k')

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array_left.min(),x_array_right.max())

ax.set_xlabel('$\it{x}$',fontname = 'Times New Roman')
ax.set_ylabel('$%s$' % latex(f_x), fontname = 'Times New Roman')
