
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def draw_vector(vector,RBG, ax): 

    ax.quiver(0, 0, vector[0], vector[1],
               angles='xy', 
               scale_units='xy',
               scale=1,
               color = RBG)

T = np.matrix([[0.7, 0.2],
               [0.3, 0.8]])


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
                    max_value = 20,
                    step = 1)
    
    pi_0 = np.array([[p],
                     [1-p]])
    
    st.latex('T = ' + bmatrix(T))
    st.latex('\pi (0) = ' + bmatrix(pi_0))
    
    st.latex('\pi(k + 1) = T \pi(k)')
    
    
all_max = 1
all_min = 0

x1 = np.linspace(-1.1, 1.1, num=201)
x2 = x1
xx1, xx2 = np.meshgrid(x1,x2)
zz = ((np.abs((xx1))**2) + (np.abs((xx2))**2))**(1./2)

pi = pi_0

colors = plt.cm.rainbow(np.linspace(0,1,num_steps + 1))

fig, ax = plt.subplots(figsize=(10, 10))

# plot a reference line
plt.plot(x1,1-x1,color = 'k',
         linestyle = '--')

# plot a unit circle as reference
plt.contour(xx1, xx2, zz, levels = [1], 
            colors='k', linestyles = ['--'])
    
for i in np.arange(0,num_steps + 1):
    
    # plot normalized vector
    draw_vector(pi/np.linalg.norm(pi), colors[i], ax)
    
    # plot original vector
    draw_vector(pi, colors[i], ax)
    pi = T@pi
    # update pi
    
    
ax.tick_params(left=False, bottom=False)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
# plt.axis('off')
ax.axvline(x = 0, color = 'k')
ax.axhline(y = 0, color = 'k')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(color = [0.8,0.8,0.8])
plt.xticks(np.linspace(-1,1,21))
plt.yticks(np.linspace(-1,1,21))

st.pyplot(fig=fig)
