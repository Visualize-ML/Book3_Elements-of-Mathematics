
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch6_03

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# define three visualization tools
# ========================
# 3D contour plot of zz
# ========================

def plot_3D_f_xy(xx,yy,zz):
    fig = plt.figure(figsize = (8,8))
    ax = fig.gca(projection='3d')
    
    ax.plot_wireframe(xx,yy, zz,
                    color = [0.75,0.75,0.75],
                    cmap='RdYlBu_r',
                    rstride=20, cstride=20,
                    linewidth = 0.25)
    
    l_max = max(np.max(zz),-np.min(zz))
    levels = np.linspace(-l_max,l_max,21)
    ax.contour(xx, yy, zz, levels = levels, cmap = 'RdYlBu_r')
    
    # plot decision boundary
    ax.contour(xx, yy, zz, levels = [0], 
                colors=['k'])
    
    ax.set_proj_type('ortho')
    
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    
    plt.tight_layout()
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('f($x_1$,$x_2$)')
    ax.view_init(azim=-120, elev=30)
    ax.grid(False)

# ========================
# Wireframe plot of mask
# ========================

def plot_3D_mask(xx,yy,mask):
    fig = plt.figure(figsize = (8,8))
    ax = fig.gca(projection='3d')
    
    ax.plot_wireframe(xx,yy, mask,
                    cmap='RdYlBu_r',
                    rstride=20, cstride=20,
                    linewidth = 0.25)
    
    ax.set_proj_type('ortho')
    
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    ax.set_zlim(0,1.2)
    
    plt.tight_layout()
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('[0,1]')
    ax.set_zticks([0,1])
    ax.view_init(azim=-120, elev=30)
    ax.grid(False)

# ========================
# 2D contour plot
# ========================

def plot_2D_contour(xx,yy,zz,mask):
    
    # Create color maps
    rgb = [[255, 238, 255],  # red
           [219, 238, 244]]  # blue
    rgb = np.array(rgb)/255.
    
    cmap_light = ListedColormap(rgb)
    
    fig, ax = plt.subplots(figsize = (8,8))
    l_max = max(np.max(zz),-np.min(zz))
    levels = np.linspace(-l_max,l_max,21)
    plt.contourf(xx, yy, mask, cmap=cmap_light)
    plt.contour(xx, yy, zz, levels = levels, cmap = 'RdYlBu_r')
    
    # plot decision boundary
    plt.contour(xx, yy, zz, levels = [0], 
                colors=['k'])
    
    # Figure decorations
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
    # plt.axis('equal')
    plt.show()
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')

#%%

num = 500
x = np.linspace(-4,4,num)
y = np.linspace(-4,4,num)
xx,yy = np.meshgrid(x,y);

plt.close('all')

#%% x1 + 1 > 0
zz = -xx - 1
# satisfy the inequality: 1
# otherwise: 0
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% -1 < x1 < 2
zz = np.abs(xx - 0.5) - 1.5
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% x2 < 0 or x2 > 2
zz = -np.abs(yy - 1) + 1
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% x1 - x2 + 1 < 0
zz = xx - yy + 1
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% x1 > 2*x2
zz = - xx + 2*yy
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% |x1 + x2| < 1
zz = np.abs(xx + yy) - 1
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% |x1| + |x2| < 2
zz = np.abs(xx) + np.abs(yy) - 2
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)

#%% x1**2 + x2**2 < 4
zz = xx**2 + yy**2 - 4
mask_less_than_0 = (zz < 0) + 0

plot_3D_f_xy(xx,yy,zz)
plot_3D_mask(xx,yy,mask_less_than_0)
plot_2D_contour(xx,yy,zz,mask_less_than_0)
