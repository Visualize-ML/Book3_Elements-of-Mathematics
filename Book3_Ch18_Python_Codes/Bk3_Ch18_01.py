
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch18_01

import numpy as np
from sympy import *
from matplotlib import pyplot as plt 

x = Symbol('x')

f_x = x**2 + 1/2
# f_x = x**2 - 1/2

f_x_fcn = lambdify([x],f_x)

integral_f_x = integrate(f_x, x)
integral_f_x_fcn = lambdify([x],integral_f_x)

a = 0 # lower bound
b = 1 # upper bound

num = 201; # number of mesh grids
x_array     = np.linspace(-0.2,1.2,num)
x_a_b_array = np.linspace(a,b,num)

y_array     = f_x_fcn(x_array)
y_a_b_array = f_x_fcn(x_a_b_array)

fig, ax = plt.subplots()
ax.plot(x_array, y_array, 'b')
ax.axvline(x = a, color = 'r', linestyle = '-')
ax.axvline(x = b, color = 'r', linestyle = '-')
ax.axhline(y = 0, color = 'k', linestyle = '-')

ax.fill_between(x_a_b_array,
                y_a_b_array, 
                edgecolor = 'none', 
                facecolor = '#DBEEF3')

ax.set_xlim(-0.2, 1.2)
# ax.set_ylim(np.floor(y_array.min()), 
#             np.ceil(y_array.max()))
ax.set_ylim(-1,2)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

integral_a_b = integral_f_x_fcn(b) - integral_f_x_fcn(a)

integral_a_b_v2 = integrate(f_x, (x, a, b))
integral_a_b_v2 = float(integral_a_b_v2)

ax.set_title(r'$\int_a^b  f(x) = %0.4f$'%integral_a_b)
