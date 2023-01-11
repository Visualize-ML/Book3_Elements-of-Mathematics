
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch17_01

from sympy import lambdify, diff, evalf, sin, exp
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm

f_x = exp(-x**2)

x_array   = np.linspace(-3,3,100)
x_0_array = np.linspace(-2.5,2.5,21)
# f_x.evalf(subs = {x: 0})

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

#%% plot quadratic approx for original fcn

plt.close('all')

colors = plt.cm.rainbow(np.linspace(0,1,len(x_0_array)))

f_x_1_diff = diff(f_x,x)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)

f_x_2_diff = diff(f_x,x,2)
f_x_2_diff_fcn = lambdify(x,f_x_2_diff)

fig, ax = plt.subplots()

ax.plot(x_array, f_x_array, linewidth = 1.5) 
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("$\it{f}(\it{x})$")

for i in np.arange(len(x_0_array)):
    
    color = colors[i,:]
    
    x_0 = x_0_array[i]
    
    y_0 = f_x.evalf(subs = {x: x_0})
    x_t_array = np.linspace(x_0-0.5, x_0+0.5, 50)
    
    b = f_x_1_diff.evalf(subs = {x: x_0})
    
    a = f_x_2_diff.evalf(subs = {x: x_0})
    
    second_order_f = a/2*(x - x_0)**2 + b*(x - x_0) + y_0
    
    second_order_f_fcn = lambdify(x,second_order_f)
    second_order_f_array = second_order_f_fcn(x_t_array)
    
    ax.plot(x_t_array, second_order_f_array, linewidth = 0.25, color = color) 
    ax.plot(x_0,y_0,marker = '.', color = color,
            markersize = 12)

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim((x_array.min(),x_array.max()))

ax.set_xlim(-3,3)
ax.set_ylim(-0.25,1.25)

#%% plot quadratic approx for first-order derivative

f_x_1_diff_new = diff(f_x,x)
print(f_x_1_diff)
f_x_1_diff_fcn_new = lambdify(x,f_x_1_diff_new)
f_x_1_diff_array_new = f_x_1_diff_fcn_new(x_array)

colors = plt.cm.rainbow(np.linspace(0,1,len(x_0_array)))

f_x_1_diff = diff(f_x,x,2)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)

f_x_2_diff = diff(f_x,x,3)
f_x_2_diff_fcn = lambdify(x,f_x_2_diff)


fig, ax = plt.subplots()

ax.plot(x_array, f_x_1_diff_array_new, linewidth = 1.5) 
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("$\it{f}(\it{x})$")

for i in np.arange(len(x_0_array)):
    
    color = colors[i,:]
    
    x_0 = x_0_array[i]
    
    y_0 = f_x_1_diff_new.evalf(subs = {x: x_0})
    x_t_array = np.linspace(x_0-0.5, x_0+0.5, 50)
    
    b = f_x_1_diff.evalf(subs = {x: x_0})
    
    a = f_x_2_diff.evalf(subs = {x: x_0})
    
    second_order_f = a/2*(x - x_0)**2 + b*(x - x_0) + y_0
    
    second_order_f_fcn = lambdify(x,second_order_f)
    second_order_f_array = second_order_f_fcn(x_t_array)
    
    ax.plot(x_t_array, second_order_f_array, linewidth = 0.25, color = color) 
    ax.plot(x_0,y_0,marker = '.', color = color,
            markersize = 12)

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim((x_array.min(),x_array.max()))

ax.set_xlim(-3,3)
ax.set_ylim(-1.25,1.25)
