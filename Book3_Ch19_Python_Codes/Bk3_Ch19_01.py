
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch19_01

import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
from sympy import lambdify, diff, exp
from sympy.abc import x

f_x = -2*x*exp(-x**2)
obj_f = lambdify(x,f_x)
# objective function

# def obj_f(x):
#     return -4*x*np.exp(-x**2)

result = optimize.minimize_scalar(obj_f)

print('=== Success ===')
print(result.success)

x_min = result.x

x_array = np.linspace(-2,2,100)
y_array = obj_f(x_array)

fig, ax = plt.subplots()

plt.plot(x_array,y_array, color = 'b')
# plot the optimal solution
plt.plot(x_min,obj_f(x_min), color = 'r', marker = 'x',
         markersize = 12)

plt.xlabel('x'); plt.ylabel('f(x)')
plt.xticks(np.linspace(-2, 2, 5)); plt.yticks(np.linspace(-2, 2, 5))
plt.axis('scaled'); ax.set_xlim(-2,2); ax.set_ylim(-2,2)
ax.spines['top'].set_visible(False); ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False); ax.spines['right'].set_visible(False)
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

#%% plot the first-order derivative

f_x_1_diff = diff(f_x,x)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)
f_x_1_diff_array = f_x_1_diff_fcn(x_array)

fig, ax = plt.subplots()

plt.plot(x_array,f_x_1_diff_array, color = 'b')
# plot the optimal solution
plt.plot(x_min,f_x_1_diff_fcn(x_min), color = 'r', marker = 'x',
         markersize = 12)

plt.xlabel('x'); plt.ylabel('f\'(x)')
plt.xticks(np.linspace(-2, 2, 5)); plt.yticks(np.linspace(-2, 2, 5))
plt.axis('scaled'); ax.set_xlim(-2,2); ax.set_ylim(-2,2)
ax.spines['top'].set_visible(False); ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False); ax.spines['right'].set_visible(False)
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
