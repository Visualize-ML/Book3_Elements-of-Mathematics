
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch15_03

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # Colormaps
from sympy import latex, lambdify

def plot_secant(x0, y0, x1, y1, color):
    
    k = (y1 - y0)/(x1 - x0)
    
    x = np.linspace(-1,4,100)
    
    secant_y_x = k*(x - x0) + y0
    
    plt.plot(x, secant_y_x, color = color,
             linewidth = 0.25)

delta_Xs = np.linspace(0.1, 1, 10)

from sympy.abc import x

f_x = x**2

x_array = np.linspace(-1,4,100)

f_x_fcn = lambdify(x,f_x)
y_array = f_x_fcn(x_array)

x0 = 1
y0 = f_x_fcn(x0)

fig, ax = plt.subplots(figsize = (8,8))

plt.plot(x_array, y_array, color = '#00448A',
         linewidth = 1.25)
plt.plot(x0, y0, color = '#92D050', marker = 'x', markersize = 12)

colors = plt.cm.RdYlBu_r(np.linspace(0,1,len(delta_Xs)))

for i in np.linspace(1,len(delta_Xs),len(delta_Xs)):
    
    x1 = x0 + delta_Xs[int(i)-1]
    y1 = f_x_fcn(x1)
    plt.plot(x1, y1, color = '#00448A', 
             marker = 'x', markersize = 12)
    
    plot_secant(x0, y0, x1, y1, colors[int(i)-1])

plt.xlabel('X')
plt.ylabel('$y = f(x)$')
ax.set_title('$f(x) = %s$' % latex(f_x))
ax.set_xlim(0, 2)
ax.set_ylim(-1, 4)

fig, ax = plt.subplots()

plt.plot(x0, y0, color = '#92D050', marker = 'x', markersize = 12)

colors = plt.cm.RdYlBu_r(np.linspace(0,1,len(delta_Xs)))

for i in np.linspace(1,len(delta_Xs),len(delta_Xs)):
    
    x1 = x0 + delta_Xs[int(i)-1]
    y1 = f_x_fcn(x1)
    
    k = (y1 - y0)/(x1 - x0)
    
    plt.plot(delta_Xs[int(i)-1], k, color = colors[int(i)-1],
             marker = 'x', markersize = 12)

plt.xlabel('$\Delta$X')
plt.ylabel('$k$')
ax.set_xlim(0, 1)
ax.set_ylim(2, 3)
