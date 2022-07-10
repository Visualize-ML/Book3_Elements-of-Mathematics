
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch10_02_A

import numpy as np
from sympy import lambdify, diff, exp, latex, simplify
from sympy.abc import x, y
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm

num = 301; # number of mesh grids
x_array = np.linspace(-3,3,num)
y_array = np.linspace(-3,3,num)
xx,yy = np.meshgrid(x_array,y_array)

plt.close('all')
# f_xy = x*exp(- x**2 - y**2);
f_xy =  3*(1-x)**2*exp(-(x**2) - (y+1)**2)\
    - 10*(x/5 - x**3 - y**5)*exp(-x**2-y**2)\
    - 1/3*exp(-(x+1)**2 - y**2) 

f_xy_fcn = lambdify([x,y],f_xy)
f_xy_zz = f_xy_fcn(xx,yy)

#%% visualize the surface

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=5, cstride=5,
                  linewidth = 0.25)

ax.set_proj_type('ortho')
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
ax.set_xlim(xx.min(), xx.max()); ax.set_ylim(yy.min(), yy.max())
ax.view_init(azim=-135, elev=30)
plt.tight_layout()
ax.grid(False)
plt.show()

# Bk3_Ch10_02_B

#%% evaluate f(x1,x2) with x2 = c

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=5, cstride=0,
                  linewidth = 0.25)

# x2 = b

colors = plt.cm.rainbow(np.linspace(0,1,7))

i = 0

for b in [-3,-2,-1,0,1,2,3]:
    f_xy_b = f_xy.subs(y, b)
    
    print('==========')
    print('x_2 = %0.0f'%b)
    print('f(x1,x2 = %0.0f) = %s)'%(b,str(simplify(f_xy_b))))
    print('==========')
    
    f_xy_b_fcn = lambdify([x],f_xy_b)
    f_xy_b_zz = f_xy_b_fcn(x_array)

    ax.plot(x_array,x_array*0 + b,f_xy_b_zz, 
            color = colors[i,:],
            label = '$x_2$ = %0.0f'%b)
    i = i + 1

plt.legend()
ax.set_proj_type('ortho')
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.view_init(azim=-135, elev=30)
plt.tight_layout()
ax.grid(False)
plt.show()

#%% surface projected along Y to X-Z plane

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz, 
                  rstride=5, cstride=0,
                  color = [0.5,0.5,0.5],
                  linewidth = 0.25)

ax.contour(xx,yy, f_xy_zz, 
           levels = 60, zdir='y', \
            offset= yy.max(), cmap='rainbow')

ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
ax.set_proj_type('ortho')

ax.view_init(azim=-135, elev=30)
ax.grid(False)
ax.set_xlim(xx.min(), xx.max()); ax.set_ylim(yy.min(), yy.max())
# ax.set_zlim(0, 0.7)
plt.tight_layout()

plt.show()

# project down-sampled surface

down_step = 2;
y_array_downsample = y_array[0::down_step]

fig, ax = plt.subplots()

colors = plt.cm.rainbow(np.linspace(0,1,len(y_array_downsample)))

for i in np.linspace(1,len(y_array_downsample),len(y_array_downsample)):
    plt.plot(x_array,f_xy_zz[(int(i)-1)*down_step,:],
             color = colors[int(i)-1])

plt.axhline(y=0, color='k', linestyle='-')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xlabel('$x_1$')
plt.ylabel('$f(x_1,x_2 = b)$')
ax.set_xlim(xx.min(), xx.max())

# Bk3_Ch10_02_C

#%% evaluate f(x1,x2) with x1 = a

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=0, cstride=5,
                  linewidth = 0.25)

# x1 = a

colors = plt.cm.rainbow(np.linspace(0,1,7))

i = 0

for a in [-3,-2,-1,0,1,2,3]:
    f_x_a_y = f_xy.subs(x, a)
    
    print('==========')
    print('x_1 = %0.0f'%a)
    print('f(x1 = %0.0f,x2) = %s)'%(a,str(simplify(f_x_a_y))))
    print('==========')
    
    f_x_a_y_fcn = lambdify([y],f_x_a_y)
    f_x_a_y_zz = f_x_a_y_fcn(y_array)

    ax.plot(y_array*0 + a,y_array,f_x_a_y_zz, 
            color = colors[i,:],
            label = '$x_1$ = %0.0f'%a)
    i = i + 1


plt.legend()
ax.set_proj_type('ortho')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')

ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())

ax.view_init(azim=-135, elev=30)
plt.tight_layout()
ax.grid(False)
plt.show()


#%% surface projected along X to Y-Z plane

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz, 
                  rstride=0, cstride=5,
                  color = [0.5,0.5,0.5],
                  linewidth = 0.25)

ax.contour(xx,yy, f_xy_zz, 
           levels = 60, zdir='x', \
            offset= xx.max(), cmap='rainbow')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')

ax.set_proj_type('ortho')
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])
ax.view_init(azim=-135, elev=30)
ax.grid(False)
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
# ax.set_zlim(0, 0.7)
plt.tight_layout()

plt.show()

# project down-sampled surface

down_step = 2;
x_array_downsample = x_array[0::down_step]

fig, ax = plt.subplots()

colors = plt.cm.rainbow(np.linspace(0,1,len(x_array_downsample)))

for i in np.linspace(1,len(x_array_downsample),len(x_array_downsample)):
    plt.plot(y_array,f_xy_zz[:,(int(i)-1)*down_step],
             color = colors[int(i)-1])
plt.axhline(y=0, color='k', linestyle='-')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xlabel('$x_2$')
plt.ylabel('$f(x_1 = a,x_2)$')

ax.set_xlim(xx.min(), xx.max())


# Bk3_Ch10_02_D

#%% surface projected along Z to X-Y plane, contour

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_surface(xx,yy, f_xy_zz,
                cmap=cm.RdYlBu_r,
                rstride=5, cstride=5,
                linewidth = 0.25,
                edgecolors = [0.5,0.5,0.5])

ax.set_proj_type('ortho')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.view_init(azim=-135, elev=30)
plt.tight_layout()
ax.grid(False)
plt.show()

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  linewidth = 0.25)

colorbar = ax.contour(xx,yy, f_xy_zz,20,
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

fig, ax = plt.subplots()

colorbar = ax.contour(xx,yy, f_xy_zz, 20, cmap='RdYlBu_r')
fig.colorbar(colorbar, ax=ax)

ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.gca().set_aspect('equal', adjustable='box')

plt.show()

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz, 
                  rstride=5, cstride=5,
                  color = [0.5,0.5,0.5],
                  linewidth = 0.25)

colorbar = ax.contourf(xx,yy, f_xy_zz, 
           levels = 20, zdir='z', \
            offset= 0, cmap='RdYlBu_r')

fig.colorbar(colorbar, ax=ax)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
ax.set_proj_type('ortho')
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])
ax.view_init(azim=-135, elev=30)
ax.grid(False)
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
# ax.set_zlim(0, 0.7)
plt.tight_layout()

plt.show()


fig, ax = plt.subplots()

colorbar = ax.contourf(xx,yy, f_xy_zz, 20, cmap='RdYlBu_r')
fig.colorbar(colorbar, ax=ax)

ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
