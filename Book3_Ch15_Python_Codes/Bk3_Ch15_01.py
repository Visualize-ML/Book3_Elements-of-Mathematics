
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch15_01

from sympy import latex, lambdify, limit, log, oo
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 

f_x = (1 + 1/x)**x

x_array = np.linspace(0.1,1000,1000)

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

f_x_oo_limit = limit(f_x,x,oo)

# visualization

plt.close('all')

fig, ax = plt.subplots()

ax.plot(x_array, f_x_array, linewidth = 1.5) 
ax.axhline(y = f_x_oo_limit, color = 'r')

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array.min(),x_array.max())
plt.xscale("log")
ax.set_xlabel('$\it{x}$',fontname = 'Times New Roman')
ax.set_ylabel('$%s$' % latex(f_x), fontname = 'Times New Roman')

plt.grid(True, which="both", ls="-")
