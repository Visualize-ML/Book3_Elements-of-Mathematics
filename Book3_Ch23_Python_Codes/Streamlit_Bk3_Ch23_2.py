
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def draw_vector(vector,RBG): 
    array = np.array([[0, 0, vector[0], vector[1]]], dtype=object)
    X, Y, U, V = zip(*array)
    plt.quiver(X, Y, U, V,angles='xy', scale_units='xy',scale=1,color = RBG)


x1 = np.arange(-25, 25 + 1, step=1);
x2 = np.arange(-25, 25 + 1, step=1);

XX1,XX2 = np.meshgrid(x1,x2);

X = np.column_stack((XX1.ravel(),XX2.ravel()))


with st.sidebar:
    
    st.latex(r'''
             A = \begin{bmatrix}
    a & b\\
    c & d
    \end{bmatrix}''')
    
    a = st.slider('a',-2.0, 2.0, step = 0.1, value = 1.0)
    b = st.slider('b',-2.0, 2.0, step = 0.1, value = 0.0)  
    c = st.slider('c',-2.0, 2.0, step = 0.1, value = 0.0)  
    d = st.slider('d',-2.0, 2.0, step = 0.1, value = 1.0) 

theta = np.pi/6
A = np.array([[a, b], 
              [c, d]], dtype=float)

Z = X@A.T;

ZZ1 = Z[:,0].reshape((len(x1), len(x2)))
ZZ2 = Z[:,1].reshape((len(x1), len(x2)))

#%% base: e1 and e2



fig_1, ax = plt.subplots()

plt.plot(XX1,XX2,color = [0.8,0.8,0.8])
plt.plot(XX1.T,XX2.T,color = [0.8,0.8,0.8])

plt.axis('scaled')
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])

plt.xticks(np.arange(0, 8 + 1, step=2))
plt.yticks(np.arange(0, 8 + 1, step=2))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#%% base: a1 and a2

fig_2, ax = plt.subplots()

plt.plot(ZZ1,ZZ2,color = [0.8,0.8,0.8])
plt.plot(ZZ1.T,ZZ2.T,color = [0.8,0.8,0.8])

plt.axis('scaled')
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])

plt.xticks(np.arange(0, 8 + 1, step=2))
plt.yticks(np.arange(0, 8 + 1, step=2))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#%% two columns 

col1, col2 = st.columns(2)

with col1:
    
    st.pyplot(fig_1)
    
    
with col2:
    
    st.pyplot(fig_2)