
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#%%

with st.sidebar:
    
    st.latex('y = ax + b')
    
    a = st.slider('Slope, a:',
              min_value = -4.0,
              max_value = 4.0,
              step = 0.1)
    
    b = st.slider('Intercept, b:',
              min_value = -4.0,
              max_value = 4.0,
              step = 0.1)


#%%
st.latex("y = %.2f x + %.2f" % (a, b))
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x_array = np.arange(-10, 10 + 1, step=1)
y_array = a*x_array + b

fig, ax = plt.subplots()

plt.plot(x_array, y_array)


plt.xlabel('$x_1$')
plt.ylabel('$x_2$ ')
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.xticks(np.arange(-10, 10 + 1, step=2))
plt.yticks(np.arange(-10, 10 + 1, step=2))
plt.axis('scaled')
plt.minorticks_on()
ax.grid(which='major', linestyle=':', 
        linewidth='0.5', color=[0.8, 0.8, 0.8])
ax.set_xlim(-10,10); 
ax.set_ylim(-10,10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

st.pyplot(fig)