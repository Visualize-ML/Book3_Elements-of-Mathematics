
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch6_05

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,8*np.pi, 200)

# parametric equation of spiral
x1 = np.cos(t)
x2 = np.sin(t)
x3 = t

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, x2, x3)

plt.show()
ax.set_proj_type('ortho')

ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.set_zlim(0,t.max())

plt.tight_layout()
ax.set_xlabel('$\it{x_1}$')
ax.set_ylabel('$\it{x_2}$')
ax.set_zlabel('$\it{x_3}$')

ax.view_init(azim=-135, elev=30)
ax.xaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
ax.yaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
ax.zaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
