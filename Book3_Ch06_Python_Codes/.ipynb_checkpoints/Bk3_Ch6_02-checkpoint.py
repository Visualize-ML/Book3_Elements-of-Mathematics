
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch6_02

import math
import numpy as np
import matplotlib.pyplot as plt

num = 33
x = np.linspace(-4,4,num)
y = np.linspace(-4,4,num)
xx,yy = np.meshgrid(x,y);

plt.close('all')

zz1 = xx + yy;
zz2 = 2*xx - yy;

fig = plt.figure()
ax = fig.gca(projection='3d')

CS = ax.contour(xx,yy, zz1 - zz2, levels = [0],
           colors = '#339933')
ax.cla()  

ax.plot_wireframe(xx, yy, zz1, color = '#BDD6EE') 
# , rstride=10, cstride=10
ax.plot_wireframe(xx, yy, zz2, color = '#ECCCC0') 

# plot the intersection line

for i in range(0,len(CS.allsegs[0])):

    contour_points_x_y = CS.allsegs[0][i]
    
    contour_points_z = (contour_points_x_y[:,0] + 
                        contour_points_x_y[:,1])

    ax.plot3D(contour_points_x_y[:,0],
              contour_points_x_y[:,1], 
              contour_points_z,
              color = 'k',
              linewidth = 4)

ax.set_proj_type('ortho')

ax.set_xlim(xx.min(),xx.max())
ax.set_ylim(yy.min(),yy.max())

plt.tight_layout()
ax.set_xlabel('$\it{x}$')
ax.set_ylabel('$\it{y}$')
ax.set_zlabel('$\it{z}$')

ax.view_init(azim=-135, elev=30)
ax.grid(False)
