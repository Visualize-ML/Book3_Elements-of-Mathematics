
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch20_2

import numpy as np
import matplotlib.pyplot as plt

num_toss = 100
toss = np.random.randint(low = 0, high = 2, size = (num_toss,1))

up = (toss == 1)

iteration = np.arange(1,num_toss + 1)

fig, axs  = plt.subplots(2,1)

axs[0].plot(iteration[up.flatten()],  toss[up],  
         color = 'r', marker = '.',linestyle = 'None')

axs[0].plot(iteration[~up.flatten()], toss[~up], 
         color = 'b', marker = 'x',linestyle = 'None')

axs[0].set_yticks([0,1])

cum_mean = np.cumsum(toss)/iteration

axs[1].plot(iteration, cum_mean)
axs[1].axhline(y = 0.5, color = 'r')
axs[1].set_yticks([0,0.5,1])
