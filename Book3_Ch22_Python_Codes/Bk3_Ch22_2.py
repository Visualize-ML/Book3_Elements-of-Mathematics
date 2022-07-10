
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch22_2

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

# define two vectors

a = np.array([4,1])
b = np.array([1,3])

# addition of a and b

fig, ax = plt.subplots()

draw_vector(a, np.array([0,112,192])/255, 'a')
draw_vector(b, np.array([255,0,0])/255, 'b')
draw_vector(a + b,np.array([146,208,80])/255, 'a + b')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.axis('scaled')
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.show()

# subtraction, a - b
fig, ax = plt.subplots()

draw_vector(a, np.array([0,112,192])/255, 'a')
draw_vector(b, np.array([255,0,0])/255, 'b')
draw_vector(a - b,np.array([146,208,80])/255, 'a - b')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.axis('scaled')
ax.set_xlim([0, 5])
ax.set_ylim([-2, 3])
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.show()

a = np.array([2,2])

# scalar multiplication
fig, ax = plt.subplots()

draw_vector(2*a, np.array([146,208,80])/255, '2*a')
draw_vector(a, np.array([0,112,192])/255, 'a')
draw_vector(0.5*a, np.array([255,0,0])/255, '0.5*a')


plt.xlabel('$x$')
plt.ylabel('$y$')

plt.axis('scaled')
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.show()
