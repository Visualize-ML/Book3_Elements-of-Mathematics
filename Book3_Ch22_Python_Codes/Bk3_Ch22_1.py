
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch22_1

import numpy as np
import matplotlib.pyplot as plt

# draw vectors starting from origin

def draw_vector(vector,RBG,label): 
    array = np.array([[0, 0, vector[0], vector[1]]])
    X, Y, U, V = zip(*array)
    plt.quiver(X, Y, U, V,angles='xy', scale_units='xy',scale=1,color = RBG)
    
    # add labels to the sample data
    
    label = label + f" ({vector[0]},{vector[1]})"

    plt.annotate(label, # text
                 (vector[0],vector[1]), # point to label
                 textcoords="offset points", 
                 xytext=(0,10), 
                 # distance from text to points (x,y)
                 ha='center') 
                 # horizontal alignment center

# define one vector
a = np.array([4,3])
i = np.array([1,0])
j = np.array([0,1])

fig, ax = plt.subplots()

draw_vector(4*i, np.array([0,112,192])/255, '4i')
draw_vector(3*j, np.array([255,0,0])/255, '3j')

draw_vector(i, np.array([0,112,192])/255, 'i')
draw_vector(j, np.array([255,0,0])/255, 'j')

draw_vector(a,np.array([146,208,80])/255, 'a')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.axis('scaled')
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.show()
