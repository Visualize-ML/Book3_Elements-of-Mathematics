
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch3_03

import numpy as np
import matplotlib.pyplot as plt
n_start = 6
n_stop  = 50
n_array = np.linspace(n_start,n_stop,n_stop-n_start + 1)

pi_lower_b = np.sin(np.pi/n_array)*n_array
pi_upper_b = np.tan(np.pi/n_array)*n_array

fig, ax = plt.subplots()

plt.axhline(y=np.pi, color='r', linestyle='-')
plt.plot(n_array,pi_lower_b, color = 'b')
plt.plot(n_array,pi_upper_b, color = 'g')
plt.fill_between(n_array, pi_lower_b, pi_upper_b, color = '#DEEAF6')
plt.tight_layout()
plt.xlabel('Number of sides, n')
plt.ylabel('Estimate of $\pi$')
