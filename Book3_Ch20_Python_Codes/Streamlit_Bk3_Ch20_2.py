
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

with st.sidebar:
    num_toss = st.slider('Number of toss:',
              min_value = 50,
              max_value = 200,
              step = 1)
    
    rnd_seed = st.slider('Random seed number', 
                  min_value = 0, 
                  max_value = 100, 
                  step = 1)
    
np.random.seed(rnd_seed)

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

st.pyplot(fig)