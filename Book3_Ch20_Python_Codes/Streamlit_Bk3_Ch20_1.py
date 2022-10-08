
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

from matplotlib import pyplot as plt
import numpy as np
from sympy.abc import x
from sympy import Poly
import seaborn as sns
import streamlit as st

#%%

with st.sidebar:
    n = st.slider('Number of steps:',
              min_value = 2,
              max_value = 20,
              step = 1)
    
    p = st.slider('Probability, p', 
                  min_value = 0.1, 
                  max_value = 0.9, 
                  step = 0.1)




#%% probability histogram

from scipy.stats import binom

x = np.arange(0, n + 1)

p_x= binom.pmf(x, n, p)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5), gridspec_kw={'width_ratios': [3, 1]})

for i in np.arange(n):
    
    Nodes_y = np.linspace(-i,i,i+1)
    
    B_y = np.concatenate((Nodes_y+1, Nodes_y-1))
    B_x = np.zeros_like(B_y) + i + 1
    B = np.stack((B_x,B_y))
    
    A_y = np.concatenate((Nodes_y, Nodes_y))
    A_x = np.zeros_like(A_y) + i
    
    x_AB = np.stack((A_x,B_x))
    
    y_AB = np.stack((A_y,B_y))

    ax1.plot(x_AB, y_AB, 'o-', color = '#92D050',
             markerfacecolor = '#0099FF',
             markeredgecolor = None)

locations = np.linspace(B_y.min(),B_y.max(),n+1)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

ax1.set_xlim(0,n)
ax1.set_ylim(B_y.min() - 1,B_y.max() + 1)

ax2.barh(locations, p_x, align='center')

for i,(x,y) in enumerate(zip(locations.tolist(), p_x.tolist())):
    ax2.text(y + p_x.max()*0.1, x, "{:.4f}".format(y))

ax2.set_ylim(B_y.min() - 1,B_y.max() + 1)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

st.pyplot(fig)

