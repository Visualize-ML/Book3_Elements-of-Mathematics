
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch6_04

import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, np.pi, 30)
v = np.linspace(0, 2 * np.pi, 30)


x = np.outer(np.sin(u), np.sin(v))
y = np.outer(np.sin(u), np.cos(v))
z = np.outer(np.cos(u), np.ones_like(v))


fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.set_aspect('equal')

ax.plot_wireframe(x, y, z)
ax.set_xlabel('$\it{x_1}$')
ax.set_ylabel('$\it{x_2}$')
ax.set_zlabel('$\it{x_3}$')
ax.view_init(azim=-125, elev=30)
