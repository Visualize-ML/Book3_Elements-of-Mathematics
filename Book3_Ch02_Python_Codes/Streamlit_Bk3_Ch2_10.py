
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import numpy as np
import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt

#%%

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

#%%
with st.sidebar:
    
    st.latex(r'C_{m\times n} = A_{m\times p} B_{p\times n}')
    
    rows_A = st.slider('Number of rows in A:',
                    min_value = 1,
                    max_value = 9,
                    value = 5,
                    step = 1)
    
    cols_A = st.slider('Number of columns in A:',
                    min_value = 1,
                    max_value = 9,
                    value = 5,
                    step = 1)
    
    rows_B = st.slider('Number of rows in B:',
                    min_value = 1,
                    max_value = 9,
                    value = 5,
                    step = 1)
    
    cols_B = st.slider('Number of columns in B:',
                    min_value = 1,
                    max_value = 9,
                    value = 5,
                    step = 1)

#%% generate A and B using random integer generator

A = np.random.randint(10, size=(rows_A, cols_A))
B = np.random.randint(10, size=(rows_B, cols_B))

st.latex(r'A_{m\times p} = ' + bmatrix(A))
st.latex(r'B_{p\times n} = ' + bmatrix(B))

#%%

try:
    
    C = A@B
    st.latex('C = AB = ' + bmatrix(C))
    
    
    fig, axs = plt.subplots(1, 5, figsize=(12, 3))
    
    plt.sca(axs[0])
    ax = sns.heatmap(A,cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=np.arange(1,rows_A+1), 
                     xticklabels=np.arange(1,cols_A+1))
    
    ax.set_aspect("equal")
    plt.title('$A$')
    plt.yticks(rotation=0) 
    
    plt.sca(axs[1])
    plt.title('$@$')
    plt.axis('off')
    
    plt.sca(axs[2])
    ax = sns.heatmap(B,cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=np.arange(1,rows_B+1), 
                     xticklabels=np.arange(1,cols_B+1))
    
    ax.set_aspect("equal")
    plt.title('$B$')
    plt.yticks(rotation=0) 
    
    plt.sca(axs[3])
    plt.title('$=$')
    plt.axis('off')
    
    plt.sca(axs[4])
    ax = sns.heatmap(C,cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=np.arange(1,rows_A+1), 
                     xticklabels=np.arange(1,cols_B+1))
    
    ax.set_aspect("equal")
    plt.title('$C$')
    plt.yticks(rotation=0) 
    
    st.pyplot(fig)
    
except:
    st.write('The number of columns of the first matrix, must equal the number of rows of the second matrix.')
