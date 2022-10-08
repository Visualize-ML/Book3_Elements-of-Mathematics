
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

#%%

with st.sidebar:
    
    st.latex('a_k = aq^{k}')
    
    a = st.slider('a',
                  min_value = 1,
                  max_value = 5,
                  step = 1)
    
    n = st.slider('k',
                  min_value = 20,
                  max_value = 50,
                  step = 5)
    
    q = st.slider('q',
                  min_value = -2.0,
                  max_value = 2.0,
                  step = 0.1)

# Generate geometric progression, GP, sequence

GP_sequence = [a*q**i for i in range(n)]
index       = np.arange(1, n + 1, 1)

fig, ax = plt.subplots()

plt.xlabel("Index, $k$") 
plt.ylabel("Term, $a_k$") 
plt.plot(index, GP_sequence, marker = '.',markersize = 6, linestyle = 'None') 
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

st.pyplot(fig)
