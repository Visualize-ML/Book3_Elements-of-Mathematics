
###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

Bk3_Ch18_08.py

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from sympy.abc import x, y
from sympy import *

plt.close('all')

f_xy = exp(- x**2 - y**2);

f_xy_fcn = lambdify([x,y],f_xy)

a = -2; b = 1
c = -1; d = 2

x_array_fine = np.linspace(a,b,300)
y_array_fine = np.linspace(c,d,300)

xx_fine,yy_fine = np.meshgrid(x_array_fine,y_array_fine)

zz_fine = f_xy_fcn(xx_fine, yy_fine)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(xx_fine,yy_fine, zz_fine,
                  color = '#0070C0',
                  rstride=10, cstride=10,
                  linewidth = 0.25)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = f(x,y)')

ax.set_xlim((a,b))
ax.set_ylim((c,d))
ax.set_zlim((0,zz_fine.max()))
ax.grid(False)
ax.view_init(azim=-135, elev=30)
ax.set_proj_type('ortho')
plt.show()

#%%

num_array = [5,10,15,20]

for num in num_array:
    
    x_array = np.linspace(a,b - (b - a)/num,num)
    y_array = np.linspace(c,d - (d - c)/num,num)
    
    xx,yy = np.meshgrid(x_array,y_array)
    
    xx_array = xx.ravel()
    yy_array = yy.ravel()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    zz_array = np.zeros_like(yy_array)
    
    dx = np.ones_like(yy_array)/num*(b - a)
    dy = np.ones_like(yy_array)/num*(d - c)
    
    dz = f_xy_fcn(xx_array, yy_array)
    
    ax.bar3d(xx_array, yy_array, zz_array, dx, dy, dz, shade=False,
              color = '#DEEAF6',
              edgecolor = '#B2B2B2')
    
    # ax.scatter(xx_array, yy_array, dz, c=dz, cmap='RdYlBu_r',marker = '.')
    
    # ax.plot_wireframe(xx_fine,yy_fine, zz_fine,
    #                   color = '#0070C0',
    #                   rstride=10, cstride=10,
    #                   linewidth = 0.25)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z = f(x,y)')
    
    ax.set_xlim((a,b))
    ax.set_ylim((c,d))
    ax.set_zlim((0,zz_fine.max()))
    ax.grid(False)
    ax.view_init(azim=-135, elev=30)
    ax.set_proj_type('ortho')
    plt.show()

    estimated_volume = dz.sum()*(b - a)/num*(d - c)/num
    ax.set_title('Estimated volume = %0.3f'%estimated_volume)
    
volume = integrate(f_xy, (y, c, d), (x, a, b))
volume = volume.evalf()
print('==== Volume ====')
print(volume)
