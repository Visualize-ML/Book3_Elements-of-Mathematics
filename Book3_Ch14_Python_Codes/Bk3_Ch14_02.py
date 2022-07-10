
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch14_02

import numpy as np
from matplotlib import pyplot as plt

a = 1    # initial term
n = 50   # number of terms
q = -1.1 # common ratio, q = 1.1, 1, 0.9, -0.9, -1, -1.1

# Generate geometric progression, GP, sequence

GP_sequence = [a*q**i for i in range(n)]
index       = np.arange(1, n + 1, 1)

fig, ax = plt.subplots()

plt.xlabel("Index, $k$") 
plt.ylabel("Term, $a_k$") 
plt.plot(index, GP_sequence, marker = '.',markersize = 6, linestyle = 'None') 
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
