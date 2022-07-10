
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch23_2

import numpy as np
import matplotlib.pyplot as plt

def draw_vector(vector,RBG): 
    array = np.array([[0, 0, vector[0], vector[1]]], dtype=object)
    X, Y, U, V = zip(*array)
    plt.quiver(X, Y, U, V,angles='xy', scale_units='xy',scale=1,color = RBG)


x1 = np.arange(-25, 25 + 1, step=1);
x2 = np.arange(-25, 25 + 1, step=1);

XX1,XX2 = np.meshgrid(x1,x2);

X = np.column_stack((XX1.ravel(),XX2.ravel()))

A = np.matrix([[1,1],
               [2,4]]);

Z = X@A.T;

ZZ1 = Z[:,0].reshape((len(x1), len(x2)))
ZZ2 = Z[:,1].reshape((len(x1), len(x2)))

#%% base: e1 and e2

fig, ax = plt.subplots()

plt.plot(XX1,XX2,color = [0.8,0.8,0.8])
plt.plot(XX1.T,XX2.T,color = [0.8,0.8,0.8])

a1 = A[:,0].tolist()
a2 = A[:,1].tolist()
b  =  [3,8]

draw_vector(a1, np.array([0,112,192])/255)
draw_vector(a2, np.array([255,0,0])/255)

draw_vector(b,  np.array([255,125,255])/255)


plt.xlabel('$e_1$')
plt.ylabel('$e_2$')

plt.axis('scaled')
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])

plt.xticks(np.arange(0, 8 + 1, step=2))
plt.yticks(np.arange(0, 8 + 1, step=2))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#%% base: a1 and a2

fig, ax = plt.subplots()

plt.plot(ZZ1,ZZ2,color = [0.8,0.8,0.8])
plt.plot(ZZ1.T,ZZ2.T,color = [0.8,0.8,0.8])

draw_vector(a1, np.array([0,112,192])/255)
draw_vector(a2, np.array([255,0,0])/255)

draw_vector(b,  np.array([255,125,255])/255)

plt.axis('scaled')
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])

plt.xticks(np.arange(0, 8 + 1, step=2))
plt.yticks(np.arange(0, 8 + 1, step=2))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
