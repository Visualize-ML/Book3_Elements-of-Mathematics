
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sympy.abc import x
from sympy import exp, lambdify, latex


#%%

with st.sidebar:
    
    st.latex(r'f(x) = a \exp(- (b(x - c))^2) + d')
    
    a = st.slider('a',
                  min_value = -2.0,
                  max_value = 2.0,
                  step = 0.1)
    
    b = st.slider('b',
                  min_value = -2.0,
                  max_value = 2.0,
                  step = 0.1)
    
    c = st.slider('c',
                  min_value = -2.0,
                  max_value = 2.0,
                  step = 0.1)
    
    d = st.slider('d',
                  min_value = -2.0,
                  max_value = 2.0,
                  step = 0.1)
    
#%%

x_array = np.arange(-4,4+0.01, step = 0.01)
f_x = a*exp(-(b*(x-c))**2) + d

st.latex('f(x) = ' + latex(f_x))

f_x_fcn = lambdify([x],f_x)

f_x_array = f_x_fcn(x_array) # original function

#%%

fig, ax = plt.subplots()

plt.plot(x_array, f_x_array, color = '#0070C0')

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.xticks(np.arange(-4, 4+1, step=1))
plt.yticks(np.arange(-4, 4+1, step=1))
plt.axis('scaled')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.legend()
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

st.pyplot(fig)

