
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch17_03

import numpy as np
from sympy import lambdify, diff, exp, latex, simplify
from sympy.abc import x, y
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm


num = 301; # number of mesh grids
x_array = np.linspace(-1.5,1.5,num)
y_array = np.linspace(-1.5,1.5,num)

# global mesh
xx,yy = np.meshgrid(x_array,y_array)

num_stride = 10

plt.close('all')

f_xy = exp(-x**2 - y**2) 
f_xy_fcn = lambdify([x,y],f_xy)
f_xy_zz = f_xy_fcn(xx,yy)

# expansion point
x_a = -0.1
y_b = -0.2

# local mesh
x_a_array = np.linspace(x_a - 0.5,x_a + 0.5,101)
y_b_array = np.linspace(y_b - 0.5,y_b + 0.5,101)

xx_local,yy_local = np.meshgrid(x_a_array,y_b_array)

f_xy_zz_local = f_xy_fcn(xx_local,yy_local)


# expansion point
f_ab = f_xy_fcn(x_a,y_b) 


#%% constant approximation

f_ab = f_xy_fcn(x_a,y_b)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=num_stride, cstride=num_stride,
                  linewidth = 0.25)

approx_zero_order = f_ab + xx_local*0 

ax.plot_wireframe(xx_local,yy_local, approx_zero_order,
                  color = [1,0,0],
                  rstride=num_stride, cstride=num_stride,
                  linewidth = 0.25)

ax.plot(x_a,y_b,f_ab, marker = 'x', color = 'r',
        markersize = 12)

ax.set_proj_type('ortho')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1,x_2)$')

ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_zlim(f_xy_zz.min(), 1.5)

ax.view_init(azim=-145, elev=30)
# ax.view_init(azim=-90, elev=0)

plt.tight_layout()
ax.grid(False)
plt.show()

#%% first order approximation

df_dx = f_xy.diff(x)
df_dx_fcn = lambdify([x,y],df_dx)
df_dx_a_b = df_dx_fcn(x_a,y_b)

df_dy = f_xy.diff(y)
df_dy_fcn = lambdify([x,y],df_dy)
df_dy_a_b = df_dy_fcn(x_a,y_b)

approx_first_order = approx_zero_order + df_dx_a_b*(xx_local - x_a) + df_dy_a_b*(yy_local - y_b)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=num_stride, cstride=num_stride,
                  linewidth = 0.25)

ax.plot_wireframe(xx_local, yy_local, approx_first_order,
                  color = [1,0,0],
                  rstride=num_stride, cstride=num_stride,
                  linewidth = 0.25)

ax.plot(x_a,y_b,f_ab, marker = 'x', color = 'r',
        markersize = 12)

ax.set_proj_type('ortho')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1,x_2)$')

ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_zlim(f_xy_zz.min(), 1.5)

ax.view_init(azim=-145, elev=30)
# ax.view_init(azim=-90, elev=0)

plt.tight_layout()
ax.grid(False)
plt.show()

#%% second order approximation

d2f_dxdx = f_xy.diff(x,2)
d2f_dxdx_fcn = lambdify([x,y],d2f_dxdx)
d2f_dxdx_a_b = d2f_dxdx_fcn(x_a,y_b)

d2f_dxdy = f_xy.diff(x,y)
d2f_dxdy_fcn = lambdify([x,y],d2f_dxdy)
d2f_dxdy_a_b = d2f_dxdy_fcn(x_a,y_b)

d2f_dydy = f_xy.diff(y,2)
d2f_dydy_fcn = lambdify([x,y],d2f_dydy)
d2f_dydy_a_b = d2f_dydy_fcn(x_a,y_b)

approx_second_order = approx_first_order + (d2f_dxdx_a_b*(xx_local - x_a)**2
                                            + 2*d2f_dxdy_a_b*(xx_local - x_a)*(yy_local - y_b)
                                            + d2f_dydy_a_b*(yy_local - y_b)**2)/2

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=num_stride, cstride=num_stride,
                  linewidth = 0.25)

ax.plot_wireframe(xx_local,yy_local, approx_second_order,
                  color = [1,0,0],
                  rstride=num_stride, cstride=num_stride,
                  linewidth = 0.25)

ax.plot(x_a,y_b,f_ab, marker = 'x', color = 'r',
        markersize = 12)

ax.set_proj_type('ortho')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1,x_2)$')

ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_zlim(f_xy_zz.min(), 1.5)

ax.view_init(azim=-145, elev=30)
# ax.view_init(azim=-90, elev=0)

plt.tight_layout()
ax.grid(False)
plt.show()
