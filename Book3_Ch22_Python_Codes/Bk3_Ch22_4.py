
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch22_4

import numpy as np
import matplotlib.pyplot as plt

def draw_vector(vector,RBG,label,zdir): 
    array = np.array([[0, 0, 0, vector[0], vector[1], vector[2]]])
    X, Y, Z, U, V, W = zip(*array)
    plt.quiver(X, Y, Z, U, V, W, normalize = False, color = RBG,
               arrow_length_ratio=0.1)

    label = label + ' (%d, %d, %d)' %(vector[0], vector[1], vector[2])

    ax.text(vector[0], vector[1], vector[2], label, zdir,
            verticalalignment='center')

# define one vector
c = np.array([4, 3, 5])
a = np.array([4, 3, 0])
i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])

fig = plt.figure()
ax = fig.gca(projection='3d')

draw_vector(a,np.array([0,0,0])/255, 'a',a)
draw_vector(c,np.array([0,0,0]), 'c',c)

draw_vector(i, np.array([0,112,192])/255,  'i',(1,0,0))
draw_vector(j, np.array([255,0,0])/255,    'j',(0,1,0))
draw_vector(k, np.array([146,208,80])/255, 'k',(0,0,1))

plt.show()
ax.set_proj_type('ortho')

ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(0,5)
ax.spines['left'].set_position('zero')

plt.tight_layout()
ax.set_xlabel('$\it{x}$')
ax.set_ylabel('$\it{y}$')
ax.set_zlabel('$\it{z}$')

ax.view_init(azim=60, elev=20)
# ax.view_init(azim=30, elev=20)
ax.xaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
ax.yaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
ax.zaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
