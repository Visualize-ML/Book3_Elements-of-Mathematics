
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch7_03

import matplotlib.pyplot as plt
import itertools 
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import seaborn as sns
from matplotlib import cm

# define sample data
X = np.array([[1,6], [4,6], [1,5], [6,0], 
              [3,8], [8,3], [4,1], [3,5], 
              [9, 2], [5, 9], [4, 9], [8, 4]])

# define labels
labels = ['a','b','c','d','e','f','g','h','i','j','k','l']

colors = plt.cm.rainbow(np.linspace(0,1,int(len(X)*len(X)/2)))

fig, ax = plt.subplots()

for i, d in enumerate(itertools.combinations(X, 2)):
    
    plt.plot([d[0][0],d[1][0]],[d[0][1],d[1][1]], color = colors[i,:])

# plot scatter of sample data
plt.scatter(x=X[:, 0], y=X[:, 1], color=np.array([0, 68, 138])/255., alpha=1.0, 
                linewidth = 1, edgecolor=[1,1,1])

for i, (x,y) in enumerate(zip(X[:, 0],X[:, 1])):

    # add labels to the sample data
    label = labels[i] + f"({x},{y})"

    plt.annotate(label, # text
                 (x,y), # point to label
                 textcoords="offset points", 
                 xytext=(0,10), 
                 # distance from text to points (x,y)
                 ha='center') 
                 # horizontal alignment center

ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 11, 1))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_aspect('equal')
plt.show()

#%% compute pairwise distance matrix

Pairwise_d = euclidean_distances(X)

fig, ax = plt.subplots()

h = sns.heatmap(Pairwise_d, cmap="coolwarm",
                square=True, linewidths=.05, annot=True,
                xticklabels = labels, yticklabels = labels)
