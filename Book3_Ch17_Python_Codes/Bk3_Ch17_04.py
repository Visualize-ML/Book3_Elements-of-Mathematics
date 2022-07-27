
###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch17_04.py

import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x
from sympy import latex, lambdify, diff, sin, log, exp


def num_diff(f,a,method,dx):

    # f: function handle
    # a: expansion point
    # method: 'forward', 'backward', and 'central'
    # dx: step size

    if method == 'central':
        return (f(a + dx) - f(a - dx))/(2*dx)
    elif method == 'forward':
        return (f(a + dx) - f(a))/dx
    elif method == 'backward':
        return (f(a) - f(a - dx))/dx
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")

f_x = exp(-x**2)
x_array = np.linspace(-3,3,100)
a_array = np.linspace(-2.5,2.5,11)

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

f_x_1_diff = diff(f_x,x)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)
f_x_1_diff_array = f_x_1_diff_fcn(x_array)

#%% visualization

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(2, 1, 1)

ax.plot(x_array, f_x_array, '#0070C0', linewidth = 1.5) 
ax.set_ylim(np.floor(f_x_array.min()),
            np.ceil(f_x_array.max()))

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim((x_array.min(),x_array.max()))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax = fig.add_subplot(2, 1, 2)

ax.plot(x_array, f_x_1_diff_array, '#0070C0', linewidth = 1.5) 

ax.set_xlabel('x')
ax.set_ylabel('f\'(x)')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlim((x_array.min(),x_array.max()))

#%% numerical methods

dx = 0.2

diff_central  = num_diff(f_x_fcn,a_array,'central', dx)
diff_forward  = num_diff(f_x_fcn,a_array,'forward', dx)
diff_backward = num_diff(f_x_fcn,a_array,'backward',dx)

fig, ax = plt.subplots()

ax.plot(x_array, f_x_1_diff_array, '#0070C0', linewidth = 1.5) 

ax.plot(a_array, diff_central, marker = '.', 
        markersize = 12, linestyle = 'none',
        label = 'central') 

ax.plot(a_array, diff_forward, marker = '>', 
        markersize = 12, linestyle = 'none',
        label = 'forward') 

ax.plot(a_array, diff_backward, marker = '<', 
        markersize = 12, linestyle = 'none',
        label = 'backward') 

ax.set_xlabel('x')
ax.set_ylabel('f\'(x)')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlim((x_array.min(),x_array.max()))
plt.axhline(y=0, color='k', linestyle='--', linewidth = 0.25)
plt.legend()

#%% varying step size

dx_array = np.linspace(0.01,0.2,20)

a = 1

diff_central  = num_diff(f_x_fcn,a,'central', dx_array)
diff_forward  = num_diff(f_x_fcn,a,'forward', dx_array)
diff_backward = num_diff(f_x_fcn,a,'backward',dx_array)

f_x_1_diff_a = f_x_1_diff_fcn(a)

fig, ax = plt.subplots()

ax.plot(dx_array, diff_central, linewidth = 1.5, 
        marker = '.',label = 'central')
 
ax.plot(dx_array, diff_forward, linewidth = 1.5, 
        marker = '>',label = 'forward')
 
ax.plot(dx_array, diff_backward, linewidth = 1.5, 
        marker = '<',label = 'backward') 

plt.axhline(y=f_x_1_diff_a, color='k', linestyle='--', 
            linewidth = 0.25,label = 'analytical')

ax.set_xlim((dx_array.min(),dx_array.max()))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.legend()
ax.set_xlabel('\u0394x')
ax.set_ylabel('f\'(x)')
