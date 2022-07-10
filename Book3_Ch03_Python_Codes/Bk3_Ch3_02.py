
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch3_02

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle
import numpy as np

for num_vertices in [6,8,10,12,14,16]:
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    hexagon_inner = RegularPolygon((0,0), numVertices=num_vertices, 
                                   radius=1, alpha=0.2, edgecolor='k')
    ax.add_patch(hexagon_inner)
    
    hexagon_outer = RegularPolygon((0,0), numVertices=num_vertices, 
                                   radius=1/np.cos(np.pi/num_vertices), 
                                   alpha=0.2, edgecolor='k')
    ax.add_patch(hexagon_outer)
    
    circle = Circle((0,0), radius=1, facecolor = 'none', edgecolor='k')
    ax.add_patch(circle)
    
    plt.axis('off')
    
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.show()
