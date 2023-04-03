
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch2_10_A

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Repeatability
np.random.seed(7)

# Generate matrix A and B
m = 6
p = 3
n = 4

A = np.random.uniform(-1,1,m*p).reshape(m, p)
B = np.random.uniform(-1,1,p*n).reshape(p, n)

C = A@B

all_max = 1
all_min = -1

#%% matrix multiplication, first perspective

fig, axs = plt.subplots(1, 5, figsize=(12, 3))

plt.sca(axs[0])
ax = sns.heatmap(A,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,m+1), xticklabels=np.arange(1,p+1))
ax.set_aspect("equal")
plt.title('$A$')
plt.yticks(rotation=0) 

plt.sca(axs[1])
plt.title('$@$')
plt.axis('off')

plt.sca(axs[2])
ax = sns.heatmap(B,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,p+1), xticklabels=np.arange(1,n+1))
ax.set_aspect("equal")
plt.title('$B$')
plt.yticks(rotation=0) 

plt.sca(axs[3])
plt.title('$=$')
plt.axis('off')

plt.sca(axs[4])
ax = sns.heatmap(C,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,m+1), xticklabels=np.arange(1,n+1))
ax.set_aspect("equal")
plt.title('$C$')
plt.yticks(rotation=0) 



# Bk_Ch2_10_B

#%% matrix multiplication, second perspective

C1 = A[:,[0]]@B[[0],:]

C2 = A[:,[1]]@B[[1],:]

C3 = A[:,[2]]@B[[2],:]

fig, axs = plt.subplots(1, 7, figsize=(12, 3))

plt.sca(axs[0])
ax = sns.heatmap(C1,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,m+1), xticklabels=np.arange(1,n+1))
ax.set_aspect("equal")
plt.title('$C_1$')
plt.yticks(rotation=0) 

plt.sca(axs[1])
plt.title('$+$')
plt.axis('off')

plt.sca(axs[2])
ax = sns.heatmap(C2,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,m+1), xticklabels=np.arange(1,n+1))
ax.set_aspect("equal")
plt.title('$C_2$')
plt.yticks(rotation=0) 

plt.sca(axs[3])
plt.title('$+$')
plt.axis('off')

plt.sca(axs[4])
ax = sns.heatmap(C3,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,m+1), xticklabels=np.arange(1,n+1))
ax.set_aspect("equal")
plt.title('$C_3$')
plt.yticks(rotation=0) 

plt.sca(axs[5])
plt.title('$=$')
plt.axis('off')

plt.sca(axs[6])
ax = sns.heatmap(C,cmap='RdBu_r',vmax = all_max,vmin = all_min,
                 cbar_kws={"orientation": "horizontal"},
                 yticklabels=np.arange(1,m+1), xticklabels=np.arange(1,n+1))
ax.set_aspect("equal")
plt.title('$C$')
plt.yticks(rotation=0) 