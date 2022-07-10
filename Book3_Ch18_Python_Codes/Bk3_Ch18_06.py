
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch18_06

import numpy as np
from scipy.special import factorial

n_array = np.linspace(0,10,11)

expansion = factorial(2*n_array)/2**(4*n_array + 2)/(factorial(n_array))**2/(2*n_array - 1)/(2*n_array + 3)

est_pi = 24*(np.sqrt(3)/32 - np.cumsum(expansion))

fig, ax = plt.subplots()

plt.axhline(y=np.pi, color='r', linestyle='-')
plt.plot(n_array,est_pi, color = 'b', marker = 'x')

plt.tight_layout()
plt.xlabel('n')
plt.ylabel('Estimate of $\pi$')
