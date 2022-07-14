
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import streamlit as st

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

st.header('Chapter 9, Dive into Conic Sections | Book 3')

#%% sidebar inputs

with st.sidebar:
    
    m = st.slider('Define m: ', 1.0, 2.0, value = 1.5, step = 0.1)
    st.write('m is ' + str(m))
    
    n = st.slider('Define n: ', 1.0, 2.0, value = 1.5, step = 0.1)
    st.write('n is ' + str(n))

    rho = st.slider('Define rho: ', -1.0, 1.0, value = 0.0, step = 0.05)
    st.write('rho is ' + str(rho))
    
#%% main
    
x = np.linspace(-4,4,num = 201)
y = np.linspace(-4,4,num = 201)
# m = 1
# n = 1.5

xx,yy = np.meshgrid(x,y);

# rho_array = np.linspace(-0.95,0,num = 20)

fig, ax = plt.subplots(figsize=(8, 8))

# Create a Rectangle patch
rect = patches.Rectangle((-m, -n), 2*m, 2*n, 
                         linewidth = 0.25, edgecolor='k',
                         linestyle = '--',
                         facecolor = 'none')

# Add the patch to the Axes
ax.add_patch(rect)

# colors = plt.cm.RdYlBu(np.linspace(0,1,len(rho_array)))

# for i in range(0,len(rho_array)):
    
#     rho = rho_array[i]
    
ellipse = ((xx/m)**2 - 2*rho*(xx/m)*(yy/n) + (yy/n)**2)/(1 - rho**2);

# color_code = colors[i,:].tolist()

plt.contour(xx,yy,ellipse,levels = [1], colors = ['b'])

plt.plot(m,rho*n, 'x', color = 'r', markersize = 12)
plt.plot(rho*m,n, 'x', color = 'r', markersize = 12)
plt.plot(-m,-rho*n, 'x', color = 'r', markersize = 12)
plt.plot(-rho*m,-n, 'x', color = 'r', markersize = 12)

plt.axvline(x = 0, color = 'k', linestyle = '-')
plt.axhline(y = 0, color = 'k', linestyle = '-')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# display fig in UI
st.pyplot(fig)











