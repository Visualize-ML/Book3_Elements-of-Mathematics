
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import numpy as np
import streamlit as st
import plotly.express as px


def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

T = np.matrix([[0.7, 0.2],
               [0.3, 0.8]])

with st.sidebar:
    
    
    p = st.slider('Ratio of chickens: ',
              min_value = 0.0, 
              max_value = 1.0,
              step = 0.05)
    
    num_steps = st.slider('Number of nights: ', 
                    min_value = 10,
                    max_value = 30,
                    step = 1)
    
    pi_0 = np.array([[p],
                     [1-p]])
    
    st.latex('T = ' + bmatrix(T))
    st.latex('\pi (0) = ' + bmatrix(pi_0))
    
    st.latex('\pi(k + 1) = T \pi(k)')

pi_array = pi_0
pi_idx   = pi_0

for idx in np.arange(0,num_steps):
    
    pi_idx = T@pi_idx
    
    pi_array = np.column_stack((pi_array, pi_idx))
    
#%%

fig = px.imshow(pi_array, text_auto=True,
                color_continuous_scale = 'RdYlBu_r')

fig.update_layout(
    autosize=False,
    width=1000,
    height=500,
    coloraxis_showscale=False)

st.plotly_chart(fig)



#%%
