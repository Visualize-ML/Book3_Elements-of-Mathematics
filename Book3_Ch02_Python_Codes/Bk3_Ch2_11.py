
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch2_11

import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
import seaborn as sns

# Repeatability
np.random.seed(0)
# Generate matrix A
n = 4
A = np.random.uniform(-1.5,1.5,n*n).reshape(n, n)

all_max = 1.5
all_min = -1.5

# matrix inverse
A_inverse = inv(A)

fig, axs = plt.subplots(1, 5, figsize=(12, 3))

plt.sca(axs[0])
ax = sns.heatmap(A,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,n+1), xticklabels=np.arange(1,n+1),
                 annot = True,fmt=".2f")
ax.set_aspect("equal")
plt.title('$A$')
plt.yticks(rotation=0) 

plt.sca(axs[1])
plt.title('$@$')
plt.axis('off')

plt.sca(axs[2])
ax = sns.heatmap(A_inverse,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,n+1), xticklabels=np.arange(1,n+1),
                 annot = True,fmt=".2f")
ax.set_aspect("equal")
plt.title('$A^{-1}$')
plt.yticks(rotation=0) 

plt.sca(axs[3])
plt.title('$=$')
plt.axis('off')

plt.sca(axs[4])
ax = sns.heatmap(A@A_inverse,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,n+1), xticklabels=np.arange(1,n+1),
                 annot = True,fmt=".2f")
ax.set_aspect("equal")
plt.title('$I$')
plt.yticks(rotation=0) 

