
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch25_1

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# transition matrix
T = np.matrix([[0.7, 0.2],
               [0.3, 0.8]])

# pi(i), state vector
pi_i = np.matrix([[0.6],
                  [0.4]])

#%% pi(i) >>> pi(i + 1): pi(i + 1) = T@pi(i)

pi_i_1 = T@pi_i

fig, axes = plt.subplots(1, 5, figsize=(12, 3))

all_max = 1
all_min = 0

plt.sca(axes[0])
ax = sns.heatmap(T,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$T$')
plt.yticks(rotation=0) 

plt.sca(axes[1])
plt.title('$@$')
plt.axis('off')

plt.sca(axes[2])
ax = sns.heatmap(pi_i,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$\pi_{i}$')
plt.yticks(rotation=0) 

plt.sca(axes[3])
plt.title('$=$')
plt.axis('off')

plt.sca(axes[4])
ax = sns.heatmap(pi_i_1,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$\pi_{i+1}$')
plt.yticks(rotation=0) 

#%% pi(i) >>> pi(i + 2): pi(i + 2) = T^2@pi(i)

pi_i_2 = T@T@pi_i

fig, axes = plt.subplots(1, 7, figsize=(12, 3))

plt.sca(axes[0])
ax = sns.heatmap(T,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$T$')
plt.yticks(rotation=0) 

plt.sca(axes[1])
plt.title('$@$')
plt.axis('off')

plt.sca(axes[2])
ax = sns.heatmap(T,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$T$')
plt.yticks(rotation=0) 

plt.sca(axes[3])
plt.title('$@$')
plt.axis('off')

plt.sca(axes[4])
ax = sns.heatmap(pi_i,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$\pi_{i}$')
plt.yticks(rotation=0) 

plt.sca(axes[5])
plt.title('$=$')
plt.axis('off')

plt.sca(axes[6])
ax = sns.heatmap(pi_i_2,cmap='RdYlBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 annot = True,fmt=".3f")
ax.set_aspect("equal")
plt.title('$\pi_{i+2}$')
plt.yticks(rotation=0) 
