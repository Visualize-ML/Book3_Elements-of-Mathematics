
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch7_02

import numpy as np
import matplotlib.pyplot as plt

# point A
x_A = -2
y_A = 3
z_A = 1

# point B

x_B = 3
y_B = -1
z_B = -3

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([x_A, x_B],[y_A, y_B],[z_A, z_B],'x', linestyle = '-')

plt.show()
ax.set_proj_type('ortho')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-4,4)

plt.tight_layout()
ax.set_xlabel('$\it{x}$')
ax.set_ylabel('$\it{y}$')
ax.set_zlabel('$\it{z}$')

ax.view_init(azim=-135, elev=30)
ax.xaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
ax.yaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
ax.zaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
