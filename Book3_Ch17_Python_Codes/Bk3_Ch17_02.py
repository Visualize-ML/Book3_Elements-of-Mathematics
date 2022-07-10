
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch17_02

from sympy import latex, lambdify, diff, sin, log, exp, series
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm

f_x = exp(x)
x_array = np.linspace(-2,2,100)
x_0 = 0 # expansion point

# f_x = sin(x) 
# x_array = np.linspace(-10,10,100)
# x_0 = np.pi/6 # expansion

# f_x = log(x + 1) # ln(y + 1) = r
# x_array = np.linspace(-0.8,2,100)

y_0 = f_x.evalf(subs = {x: x_0})

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

# Visualization

plt.close('all')

fig, ax = plt.subplots()

ax.plot(x_array, f_x_array, 'k', linewidth = 1.5) 
ax.plot(x_0, y_0, 'xr', markersize = 12) 
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("$\it{f}(\it{x})$")

highest_order = 5
order_array = np.arange(0,highest_order + 1)

colors = plt.cm.rainbow(np.linspace(0,1,len(order_array)))

i = 0

for order in order_array:

    f_series = f_x.series(x,x_0,order + 1).removeO()
    # order + 1 = number of terms
    
    f_series_fcn = lambdify(x,f_series)
    f_series_array = f_series_fcn(x_array)

    ax.plot(x_array, x_array*0 + f_series_array, linewidth = 0.5,
            color = colors[i,:],
            label = 'Order = %0.0f'%order) 

    i += 1

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array.min(),x_array.max())
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# ax.set_ylim(x_array.min(),x_array.max())
# ax.set_aspect('equal', 'box')
plt.legend()

#%% Error

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1)

ax.plot(x_array, f_x_array, 'k', linewidth = 1.5) 
ax.plot(x_0, y_0, 'xr', markersize = 12) 
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("$\it{f}(\it{x})$")

highest_order = 2

f_series = f_x.series(x,x_0,highest_order + 1).removeO()
# order + 1 = number of terms

f_series_fcn = lambdify(x,f_series)
f_series_array = f_series_fcn(x_array)
f_series_array = x_array*0 + f_series_array

ax.plot(x_array, f_series_array, linewidth = 1.5,
        color = 'b') 

ax.fill_between(x_array, 
                f_x_array, 
                x_array*0 + f_series_array,
                color = '#DEEAF6')

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array.min(),x_array.max())

ax.set_ylim(np.floor(f_x_array.min()),
            np.ceil(f_x_array.max()))
# ax.set_aspect('equal', 'box')
# plt.legend()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax = fig.add_subplot(1, 2, 2)

error = f_x_array - f_series_array
ax.plot(x_array, error, 'r', linewidth = 1.5) 
ax.fill_between(x_array, 
                error, 
                color = '#DEEAF6')
plt.axhline(y=0, color='k', linestyle='--', linewidth = 0.25)
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("Error")

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array.min(),x_array.max())
ax.set_ylim(np.floor(error.min()),np.ceil(error.max()))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
