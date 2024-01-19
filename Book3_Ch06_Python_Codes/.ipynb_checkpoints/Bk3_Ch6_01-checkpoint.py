
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch6_01

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_surf(xx,yy,zz,caption):

    norm_plt = plt.Normalize(zz.min(), zz.max())
    colors = cm.RdYlBu_r(norm_plt(zz))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(xx,yy,zz,
                           facecolors=colors, shade=False)
    surf.set_facecolor((0,0,0,0))

    plt.show()
    ax.set_proj_type('ortho')
    
    if xx.min() == xx.max():
        ax.set_xlim(xx.min() - 4,xx.min() + 4)
    else:
        ax.set_xlim(xx.min(),xx.max())
    
    if yy.min() == yy.max():
        ax.set_ylim(yy.min() - 4,yy.min() + 4)
    else:
        ax.set_ylim(yy.min(),yy.max())
        
    if zz.min() == zz.max():
        ax.set_zlim(zz.min() - 4,zz.min() + 4)
    else:
        ax.set_zlim(zz.min(),zz.max())

    plt.tight_layout()
    ax.set_xlabel('$\it{x}$')
    ax.set_ylabel('$\it{y}$')
    ax.set_zlabel('$\it{z}$')
    ax.set_title(caption)
    ax.view_init(azim=-135, elev=30)
    ax.xaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
    ax.yaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
    ax.zaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})

num = 33
x = np.linspace(-4,4,num)
y = np.linspace(-4,4,num)
xx,yy = np.meshgrid(x,y);

plt.close('all')

#%% z - 2 = 0
zz = 2 + xx*0;
caption = '$z - 2 = 0$';
plot_surf (xx,yy,zz,caption)

#%% y - z = 0
zz = yy;
caption = '$z - y = 0$';
plot_surf (xx,yy,zz,caption)

#%% x - z = 0
zz = xx;
caption = '$x - z = 0$';
plot_surf (xx,yy,zz,caption)

#%% x + y - z = 0
zz = xx + yy;
caption = '$x + y - z = 0$';
plot_surf (xx,yy,zz,caption)

#%% vertical mesh plot

x = np.linspace(-4,4,num)
z = np.linspace(-4,4,num)
xx,zz = np.meshgrid(x,z);

#%% y - 2 = 0
yy = 2 - xx*0
caption = '$y - 2 = 0$';
plot_surf (xx,yy,zz,caption)

#%% x + y - 2 = 0
yy = 2 - xx
caption = '$x + y - 2 = 0$';
plot_surf (xx,yy,zz,caption)

#%% x + 2 = 0
y = np.linspace(-4,4,num)
z = np.linspace(-4,4,num)
yy,zz = np.meshgrid(y,z);

xx = -2 - yy*0
caption = '$x + 2 = 0$';
plot_surf (xx,yy,zz,caption)
