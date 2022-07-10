
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch14_04

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def heatmap_sum(data,i_array,j_array,title):
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    
    ax = sns.heatmap(data,cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=i_array, xticklabels=j_array,
                     ax = ax)
    ax.set_xlabel('Index, $j$')
    ax.set_ylabel('Index, $i$')
    
    ax.set_aspect("equal")
    plt.title(title)
    plt.yticks(rotation=0) 

# Repeatability
np.random.seed(0)

m = 12 # j = 1 ~ n
n = 8  # i = 1 ~ m

j_array = np.arange(1,m + 1)
i_array = np.arange(1,n + 1)

jj, ii = np.meshgrid(j_array,i_array)

a_ij = np.random.normal(loc=0.0, scale=1.0, size=(n, m))

#%% heatmap of a_i_j

title = '$a_{i,j}$'
heatmap_sum(a_ij,i_array,j_array,title)

#%% partial summation of a_ij over i

# sum_over_i = a_ij.sum(axis = 0).reshape((1,-1))

all_1 = np.ones((8, 1))
sum_over_i = all_1.T@a_ij
# sum over row dimension

title = '$\sum_{i=1}^{n} a_{i,j}$'
heatmap_sum(sum_over_i,i_array,j_array,title)

#%% partial summation of a_ij over j

# sum_over_j = a_ij.sum(axis = 1).reshape((-1,1))

all_1 = np.ones((12, 1))
sum_over_j = a_ij@all_1
# sum over column dimension

title = '$\sum_{j=1}^{m} a_{i,j}$'
heatmap_sum(sum_over_j,i_array,j_array,title)
