
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch14_06

import numpy as np
import matplotlib.pyplot as plt

n_array = np.arange(1, 100 + 1, 1)

a_n_array = (-1)**(n_array + 1)/(2*n_array - 1)

a_n_cumsum = np.cumsum(a_n_array)

pi_appx = 4*a_n_cumsum

fig, ax = plt.subplots(figsize=(20, 8))

plt.xlabel("Index, k") 
plt.ylabel("Approx pi") 
plt.stem(n_array, pi_appx) 
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
plt.axhline(y=np.pi, color='r', linestyle='-')

plt.xlim(n_array.min(),n_array.max())
plt.ylim(2.5,4.1)


plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
