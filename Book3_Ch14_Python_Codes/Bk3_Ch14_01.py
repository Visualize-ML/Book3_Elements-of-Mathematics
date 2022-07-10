
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch14_01

import numpy as np
from matplotlib import pyplot as plt

# Calculate sum of arithmetic progression sequence

def sum_AP(a, n, d):
    sum_ = (n * (a + a + (n - 1) * d)) / 2
    return sum_

a = 1    # initial term
n = 100  # number of terms
d = 1    # common difference

# Generate arithmetic progression, AP, sequence

AP_sequence = np.arange(a, a + n*d, d)
index       = np.arange(1, n + 1, 1)
print("AP sequence")
print(AP_sequence)

sum_result = sum_AP(a, n, d)
sum_result_2 = np.sum(AP_sequence)
print("Sum of AP sequence = " , sum_result)

fig, ax = plt.subplots(figsize=(20, 8))

plt.xlabel("Index, k") 
plt.ylabel("Term, $a_k$") 
plt.stem(index, AP_sequence) 
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.xlim(index.min(),index.max())
plt.ylim(0,AP_sequence.max() + 1)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

#%% cumulative sum

cumsum_AP = np.cumsum(AP_sequence)

fig, ax = plt.subplots(figsize=(20, 8))

plt.xlabel("Index, k") 
plt.ylabel("Cumulative sum, $S_k$") 
plt.stem(index, cumsum_AP) 
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.xlim(index.min(),index.max())
plt.ylim(0,cumsum_AP.max() + 1)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
