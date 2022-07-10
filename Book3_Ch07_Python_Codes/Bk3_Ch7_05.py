
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch7_05

import numpy as np
from sympy import lambdify, sqrt
from sympy.abc import x, y
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm


O = [0, 0]

num = 301; # number of mesh grids
x_array = np.linspace(-8,8,num)
y_array = np.linspace(-8,8,num)

xx,yy = np.meshgrid(x_array,y_array)

dist_OP = sqrt((x - O[0])**2 + (y - O[1])**2)

dist_OP_fcn = lambdify([x,y],dist_OP)

dist_OP_zz = dist_OP_fcn(xx,yy)

#%% mesh plot

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, dist_OP_zz,
                  color = [0.5,0.5,0.5],
                  rstride=10, cstride=10,
                  linewidth = 0.25)

colorbar = ax.contour(xx,yy, dist_OP_zz,
                      levels = np.arange(0,11 + 1),
                      cmap = 'RdYlBu_r')

fig.colorbar(colorbar, ax=ax)

ax.set_proj_type('ortho')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
plt.tight_layout()
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())

ax.view_init(azim=-135, elev=30)

ax.grid(False)
plt.show()

#%% contour plot

fig, ax = plt.subplots()

plt.plot(O[0],O[1], color = 'k',
         marker = 'x', markersize = 12)

colorbar = ax.contour(xx,yy, dist_OP_zz, 
                      levels = np.arange(0,11 + 1), 
                      cmap='RdYlBu_r')

fig.colorbar(colorbar, ax=ax)

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.xticks(np.arange(-10, 10, step=2))
plt.yticks(np.arange(-10, 10, step=2))
plt.axis('scaled')

ax.set_xlim(x_array.min(),x_array.max())
ax.set_ylim(y_array.min(),y_array.max())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.grid(linestyle='--', linewidth=0.25, color=[0.8,0.8,0.8])
