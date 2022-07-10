
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch15_04

from sympy import latex, lambdify, diff, sin
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 

# function
f_x = x**2 - 2

x_array = np.linspace(-2,2,100)

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

# first order derivative

f_x_1_diff = diff(f_x,x)
print(f_x_1_diff)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)
f_x_1_diff_array = f_x_1_diff_fcn(x_array)

# second order derivative

f_x_2_diff = diff(f_x,x,2)
print(f_x_2_diff)
f_x_2_diff_fcn = lambdify(x,f_x_2_diff)
f_x_2_diff_array = f_x_2_diff_fcn(x_array)
f_x_2_diff_array = f_x_2_diff_array + x_array*0

#%% plot first-, second-order derivatives as functions

fig, ax = plt.subplots(3,1)

# original function

ax[0].plot(x_array, f_x_array, linewidth = 1.5) 
ax[0].hlines(y=0, xmin = x_array.min(), xmax = x_array.max(), 
             color='r', linestyle='--')
ax[0].vlines(x=0, ymin = f_x_array.min(), ymax = f_x_array.max(), 
             color='r', linestyle='--')
ax[0].set_title('$f(x) = %s$' % latex(f_x))
ax[0].set_ylabel('$f(x)$')
ax[0].set_xlim((x_array.min(),x_array.max()))
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].set_xticklabels([])
ax[0].grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

# first-order derivative

ax[1].plot(x_array, f_x_1_diff_array, linewidth = 1.5) 
ax[1].hlines(y=0, xmin = x_array.min(), xmax = x_array.max(), 
             color='r', linestyle='--')
ax[1].vlines(x=0, 
             ymin = f_x_1_diff_array.min(), 
             ymax = f_x_1_diff_array.max(), 
             color='r', linestyle='--')

ax[1].set_xlabel("$\it{x}$")
ax[1].set_title('$f\'(x) = %s$' % latex(f_x_1_diff))
ax[1].set_ylabel('$f\'(x)$')
ax[1].grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax[1].set_xlim((x_array.min(),x_array.max()))
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)

# second-order derivative

ax[2].plot(x_array, f_x_2_diff_array, linewidth = 1.5) 
ax[2].hlines(y=0, xmin = x_array.min(), xmax = x_array.max(), 
             color='r', linestyle='--')
ax[2].vlines(x=0, 
             ymin = f_x_2_diff_array.min(), 
             ymax = f_x_2_diff_array.max(), 
             color='r', linestyle='--')

ax[2].set_xlabel("$\it{x}$")
ax[2].set_title('$f^{(2)}(x) = %s$' % latex(f_x_2_diff))
ax[2].set_ylabel('$f\'(x)$')
ax[2].grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax[2].set_xlim((x_array.min(),x_array.max()))
ax[2].spines['right'].set_visible(False)
ax[2].spines['top'].set_visible(False)
