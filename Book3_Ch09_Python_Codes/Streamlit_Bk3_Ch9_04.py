
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

#%%

with st.sidebar:
    
    st.latex(r' \left|\frac{x_1}{a}\right|^p + \left|\frac{x_2}{b}\right|^q = 1')
    
    a = st.slider('a',
                  min_value = 1.0,
                  max_value = 3.0,
                  step = 0.1)
    
    b = st.slider('b',
                  min_value = 1.0,
                  max_value = 3.0,
                  step = 0.1)
    
    p = st.slider('p',
                  min_value = 0.2,
                  max_value = 3.0,
                  step = 0.1)

    q = st.slider('q',
                  min_value = 0.2,
                  max_value = 3.0,
                  step = 0.1)
    
#%%

st.latex(r' \left|\frac{x_1}{%.2f}\right|^{%.2f}+ \left|\frac{x_2}{%.2f}\right|^{%.2f} = 1' 
         % (a, p, b, q))

#%%

pp,qq = np.meshgrid(p,q)
pp = pp.flatten()
qq = qq.flatten()

x1 = np.linspace(-2, 2, num=101);
x2 = x1;

xx1, xx2 = np.meshgrid(x1,x2)

fig, ax = plt.subplots(figsize=(12, 12))



if np.isinf(p):
    zz = np.maximum(np.abs(xx1/a),np.abs(xx2/b))
else:
    zz = ((np.abs((xx1/a))**p) + (np.abs((xx2/b))**q))**(1./q)

# plot contour of Lp
ax.contourf(xx1, xx2, zz, 20, cmap='RdYlBu_r')

# plot contour of Lp = 1
ax.contour (xx1, xx2, zz, [1], colors='k', linewidths = 2) 

# decorations

ax.axhline(y=0, color='k', linewidth = 0.25)
ax.axvline(x=0, color='k', linewidth = 0.25)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_aspect('equal', adjustable='box')

st.pyplot(fig)
